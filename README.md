# Goxide 网站与浏览器 Playground

本仓库托管 [Goxide 网站源码](https://github.com/goxide-lang/goxide/tree/main/website)生成的静态产物：语言介绍、快速开始、使用参考、设计文档与浏览器 Playground。

- [快速开始](https://goxide-lang.github.io/learn/)：同一个订单项目，从纯 Go、混合接入到完整 Gox 项目和 feature 配置；源码包含清单与锁文件，并提供完整 ZIP 下载。
- [使用参考](https://goxide-lang.github.io/docs/)：项目、包管理、CLI 与互操作指南。
- [设计文档](https://goxide-lang.github.io/design/)：词法与文法、各阶段输入输出与翻译语义、前端和 enum 规范、完整 RFC；从仓库 Markdown 生成。
- [Playground](https://goxide-lang.github.io/playground.html)：浏览器使用 WASM 将 `.gox` 转成 Go，不执行生成的 Go。

## 编译器与产物

网站和编译器由干净检出 [`6a80c52`](https://github.com/goxide-lang/goxide/commit/6a80c526216b4d24597089bbebed6e15a3331974) 构建。完整构建身份、依赖、项目源码与生成结果记录在 [examples.json](examples.json) 中；`compilerSource.kind=worktree`、`dirty=false`。

| 内容 | 标识 |
| --- | --- |
| 编译器源码 SHA-256 | `edcbd910796749b2e7e5a42a5b6ccf1362a5d234855a2d032cb3cd6aa8d52f25` |
| `compiler.wasm` SHA-256 | `e5aa870af6d75eec2640e9a7f205fdb2ac1b387cfcbebd66445976f0cfd7c734` |
| 构建工具链 | Go 1.27.1 |
| 浏览器编译目标 | darwin/arm64，与内嵌 Go 导出数据一致 |
| 编译管线 | `parser → expand → resolve → check → lower` |

快速开始项目在构建时真实生成、运行和测试。浏览器允许一个用户包内最多 16 个文件、总计 32 KiB；固定随附依赖只读。每次转译限时 10 秒，并支持中断后恢复。完整项目使用 CLI 快照与下载包；浏览器不解析任意模块或执行构建脚本。

## 预览与托管

```sh
python3 -m http.server 8080 --bind 127.0.0.1
```

打开 [本地网站](http://127.0.0.1:8080)。GitHub Pages 沿用 `deploy/goxide-site-ae61ec6` 分支根目录发布，`main` 同步保存相同产物；`.nojekyll` 关闭 Jekyll 处理。页面不需要账户、数据库或外部编译服务。

Go runtime 许可见 [GO-LICENSE.txt](GO-LICENSE.txt)，其他前端许可见 [THIRD-PARTY-LICENSES.txt](THIRD-PARTY-LICENSES.txt)。`_headers` 供支持该格式的静态托管平台使用，GitHub Pages 不读取它。

语言与工具链能力以 [当前状态表](https://github.com/goxide-lang/goxide/blob/main/docs/mvp-gap-audit.md)为准。
