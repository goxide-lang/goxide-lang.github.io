#!/usr/bin/env python3
"""Verify a website artifact, publish both branches, and wait for Pages."""

import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request

SITE = Path(__file__).resolve().parents[2]
SOURCE = SITE.parent / 'source'
ARTIFACT = Path(os.environ['WEBSITE_ARTIFACT'])
SOURCE_SHA = os.environ['WEBSITE_SOURCE_SHA']
SOURCE_REPO = 'goxide-lang/goxide'
TARGET_REPO = 'goxide-lang/goxide-lang.github.io'
PAGES_BRANCH = 'deploy/goxide-site-ae61ec6'
STATIC_FILES = {
    'index.html', 'rfc.html', 'playground.html', 'local.html', '404.html',
    'worker.js', 'proc-macro-worker.js', 'proc-macro-wasi.js', '_headers',
    '.nojekyll', 'compiler.wasm', 'wasm_exec.js', 'examples.json',
    'frontend-assets.json', 'GO-LICENSE.txt', 'THIRD-PARTY-LICENSES.txt',
    'learn/index.html', 'docs/index.html', 'design/index.html',
    'project-reexports.zip', 'tutorial-go.zip', 'tutorial-mixed.zip',
    'tutorial-gox.zip', 'tutorial-features.zip', 'tutorial-procedural.zip',
}


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def run(*args, **kwargs):
    return subprocess.check_output(args, text=True, **kwargs).strip()


def git(*args):
    return run('git', *args, cwd=SITE)


def api(path, method='GET'):
    return json.loads(run('gh', 'api', '--method', method, f'repos/{TARGET_REPO}/{path}'))


def manifest():
    data = json.loads((ARTIFACT / 'examples.json').read_text())
    compiler = data['compilerSource']
    require(data['websiteCommit'] == SOURCE_SHA, 'Artifact website commit differs from the resolved source')
    require(compiler['kind'] == 'commit' and compiler['dirty'] is False,
            'Artifact must use a clean pinned compiler')
    require(re.fullmatch(r'[0-9a-f]{40}', compiler['commit']) and
            data['commit'] == data['catalogCompilerCommit'] == compiler['commit'],
            'Artifact compiler commits differ')
    require(re.fullmatch(r'[0-9a-f]{64}', compiler['digest']) and compiler['digest'] == data['compilerDigest'],
            'Artifact compiler source digests differ')
    require(hashlib.sha256((ARTIFACT / 'compiler.wasm').read_bytes()).hexdigest() == data['wasmSha256'],
            'Artifact compiler WASM digest differs')
    return data


def verify():
    manifest()
    require(run('git', 'rev-parse', 'HEAD', cwd=SOURCE) == SOURCE_SHA, 'Audit source commit differs')
    require(not any(path.is_symlink() for path in ARTIFACT.rglob('*')), 'Artifact contains a symlink')
    destination = SOURCE / 'website/dist'
    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(ARTIFACT, destination)
    # Execute the selected source's audit before exposing the publishing token.
    subprocess.run([sys.executable, '-B', str(SOURCE / 'website/hosting/audit.py')], check=True)
    print(f'Verified website artifact for {SOURCE_SHA}')


def previous_static_files():
    old_manifest = json.loads((SITE / 'examples.json').read_text())
    frontend = json.loads((SITE / 'frontend-assets.json').read_text())['assets']
    require(all(re.fullmatch(r'assets/[A-Za-z0-9_.-]+\.(?:js|css|ttf)', name) for name in frontend),
            'Previous frontend manifest has an invalid path')
    macros = {item['path'] for item in old_manifest['macroBundle']['artifacts']}
    require(all(re.fullmatch(r'proc-macros/[0-9a-f]{64}\.wasm', name) for name in macros),
            'Previous macro manifest has an invalid path')
    return STATIC_FILES | set(frontend) | macros


def readme(data):
    compiler = data['compilerSource']['commit']
    target = data['exportTarget']
    return f'''# Goxide 网站与浏览器 Playground

本仓库保存 [Goxide 网站源码](https://github.com/{SOURCE_REPO}/tree/{SOURCE_SHA}/website)生成的静态产物。

- [安装当前编译器](https://goxide-lang.github.io/docs/?page=install)
- [快速开始](https://goxide-lang.github.io/learn/)
- [使用参考](https://goxide-lang.github.io/docs/)
- [serde 与 JSON](https://goxide-lang.github.io/docs/?page=serde-overview)：struct、enum、Option、字段标记和字符串编解码。
- [设计文档](https://goxide-lang.github.io/design/)
- [Playground](https://goxide-lang.github.io/playground.html)：浏览器转译 Goxide 并执行随附的过程宏，不执行生成的 Go。

## 编译器与产物

网站源码提交为 [`{SOURCE_SHA[:7]}`](https://github.com/{SOURCE_REPO}/commit/{SOURCE_SHA})，编译器绑定干净提交 [`{compiler[:7]}`](https://github.com/{SOURCE_REPO}/commit/{compiler})。完整构建身份和公开库版本记录在 [examples.json](examples.json) 中。

| 内容 | 标识 |
| --- | --- |
| 编译器源码 SHA-256 | `{data['compilerDigest']}` |
| `compiler.wasm` SHA-256 | `{data['wasmSha256']}` |
| Go 导出数据 SHA-256 | `{data['exportsDigest']}` |
| 构建工具链 | `{data['toolchain']}` |
| 浏览器编译目标 | `{target['GOOS']}/{target['GOARCH']}`，与内嵌 Go 导出数据一致 |
| 编译管线 | `{data['pipeline']}` |

## 自动部署与托管

本仓库的 [Publish website workflow](https://github.com/{TARGET_REPO}/actions/workflows/publish.yml)读取指定公开源码，固定到完整提交后构建、审计并发布。构建与发布使用独立 job，只有发布 job 获得写权限；推送与 Pages API 使用本仓库的短期 `GITHUB_TOKEN`，无需跨仓库密钥或个人 token。

GitHub Pages 从 `{PAGES_BRANCH}` 分支根目录发布，`main` 原子同步相同产物；`.nojekyll` 关闭 Jekyll 处理。workflow 显式请求 Pages build，并等待本次提交部署完成。网站门禁覆盖构建、HTTP race/vet 和静态产物审计；浏览器 QA 与源码仓库全树检查需查看各自结果。

本地预览：`python3 -m http.server 8080 --bind 127.0.0.1`。

Go runtime 许可见 [GO-LICENSE.txt](GO-LICENSE.txt)，其他前端许可见 [THIRD-PARTY-LICENSES.txt](THIRD-PARTY-LICENSES.txt)。`_headers` 供支持该格式的托管平台使用，GitHub Pages 不读取它。

语言与工具链能力以[当前状态表](https://github.com/{SOURCE_REPO}/blob/{compiler}/docs/mvp-gap-audit.md)为准。
'''


def wait_for_pages(commit):
    api('pages/builds', method='POST')
    deadline = time.monotonic() + 600
    previous = None
    while time.monotonic() < deadline:
        build = api('pages/builds/latest')
        state = (build.get('commit'), build['status'])
        if state != previous:
            print('Pages build:', *state, flush=True)
            previous = state
        if state[0] == commit:
            if state[1] == 'built':
                break
            require(state[1] != 'errored', 'Pages build failed: ' + str(build.get('error')))
        time.sleep(10)
    else:
        raise SystemExit('Timed out waiting for Pages to build the published commit')
    deadline = time.monotonic() + 120
    while time.monotonic() < deadline:
        try:
            request = urllib.request.Request(
                'https://goxide-lang.github.io/examples.json?deployment=' + commit,
                headers={'Cache-Control': 'no-cache'})
            with urllib.request.urlopen(request, timeout=20) as response:
                if json.load(response).get('websiteCommit') == SOURCE_SHA:
                    return
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
            pass
        time.sleep(5)
    raise SystemExit('Pages built the commit but the public manifest has not updated')


def publish():
    require(os.environ.get('GITHUB_REPOSITORY') == TARGET_REPO and os.environ.get('GITHUB_REF') == 'refs/heads/main',
            'Publish workflow must run from the deployment repository main branch')
    data = manifest()
    pages = api('pages')
    require(pages.get('build_type') == 'legacy' and pages['source'] == {'branch': PAGES_BRANCH, 'path': '/'},
            'GitHub Pages publishing source changed')
    run('gh', 'auth', 'setup-git', '--hostname', 'github.com')
    git('remote', 'set-url', 'origin', 'https://github.com/' + TARGET_REPO + '.git')
    git('fetch', 'origin', 'refs/heads/main:refs/remotes/origin/main',
        f'refs/heads/{PAGES_BRANCH}:refs/remotes/origin/{PAGES_BRANCH}')
    start = git('rev-parse', 'HEAD')
    require(start == git('rev-parse', 'refs/remotes/origin/main'), 'Remote main changed after checkout')
    subprocess.run(['git', 'merge-base', '--is-ancestor', 'refs/remotes/origin/' + PAGES_BRANCH, start],
                   cwd=SITE, check=True)
    old_files = previous_static_files()
    tracked = set(git('ls-files', '-z').split('\0'))
    new_files = {path.relative_to(ARTIFACT).as_posix() for path in ARTIFACT.rglob('*') if path.is_file()}
    require(not (new_files & (tracked - old_files)), 'Artifact would overwrite a non-generated repository file')
    for name in old_files & tracked:
        (SITE / name).unlink()
    for name in new_files:
        destination = SITE / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ARTIFACT / name, destination)
    (SITE / 'README.md').write_text(readme(data))
    git('add', '--all')
    if git('diff', '--cached', '--name-only'):
        git('-c', 'user.name=github-actions[bot]', '-c', 'user.email=41898282+github-actions[bot]@users.noreply.github.com',
            'commit', '-m', 'Publish website from ' + SOURCE_SHA)
    git('push', '--atomic', 'origin', 'HEAD:refs/heads/main', 'HEAD:refs/heads/' + PAGES_BRANCH)
    commit = git('rev-parse', 'HEAD')
    refs = git('ls-remote', '--heads', 'origin', 'main', PAGES_BRANCH).splitlines()
    require(len(refs) == 2 and all(line.split()[0] == commit for line in refs),
            'Remote deployment branches differ from the published commit')
    wait_for_pages(commit)
    with open(os.environ['GITHUB_STEP_SUMMARY'], 'a') as output:
        print(f'Published source `{SOURCE_SHA}` at deployment commit `{commit}`. '
              '[Open serde documentation](https://goxide-lang.github.io/docs/?page=serde-overview).', file=output)


if __name__ == '__main__':
    require(re.fullmatch(r'[0-9a-f]{40}', SOURCE_SHA), 'Expected a complete source commit SHA')
    require(len(sys.argv) == 2 and sys.argv[1] in {'verify', 'publish'}, 'Expected verify or publish')
    {'verify': verify, 'publish': publish}[sys.argv[1]]()
