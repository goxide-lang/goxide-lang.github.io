# Goxide 网站与浏览器 Playground

此仓库仅托管静态构建产物。网站源码来自 goxide main `38b6e4203d7daf8d622fe10cf57064a84d48ff0d`（PR #27 → #28）；编译器固定 `690cd5178dc11a0089a41e9320ed1275778383e1`，Go 1.27.1。来源、依赖、工具链与 WASM 摘要见 [examples.json](examples.json)，前端文件摘要见 [frontend-assets.json](frontend-assets.json)。

当前 GitHub Pages 发布源为 `deploy/goxide-site-ae61ec6` 分支根目录，`.nojekyll` 关闭 Jekyll；此发布不改变 Pages 配置。

Preact + Vite + Monaco 提供多页导航和同包多文件编辑；浏览器在本机 Worker WASM 中只转译，不运行生成 Go、不上传源码、不解析任意项目依赖或执行构建脚本。最多16个源码文件、总UTF-8 32KiB。Go 基础着色与词汇补全不是完整语义语言服务。

[feature/bin 完整工程](project-features.zip) 与 [lib/双 bin/example 完整工程](project-targets.zip) 含新 schema 的 goxide.toml、goxide.lock、全部源码和复现说明。首次本机构建可能下载固定 Go 支持依赖，offline 运行需要已有缓存。这两个下载包不代表所有只读 CLI 快照都已转为完整可独立运行项目。

本地可运行 `python3 -m http.server 8080 --bind 127.0.0.1`；页面入口为 `/`、`rfc.html`、`playground.html`、`local.html`，未知文件返回404。

静态产物审计不包含私有仓库、历史、凭据或本机调试路径。Go runtime 许可见 [GO-LICENSE.txt](GO-LICENSE.txt)，前端依赖许可见 [THIRD-PARTY-LICENSES.txt](THIRD-PARTY-LICENSES.txt)。`_headers` 不会由 GitHub Pages 应用，不保证平台返回其中的 CSP 响应头。
