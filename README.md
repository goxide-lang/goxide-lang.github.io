# goxide 网站与浏览器 Playground

此仓库只托管静态网站产物。编译器版本：`ae61ec628b55e0fc66ce96d47261c0a6809c0280`，Go 1.27.1。包集合、源码摘要和真实生成示例记录在 [examples.json](examples.json)。页面文案适配公开访问；WASM 和示例保持该版本构建结果。

此独立发布分支用于审阅静态资源，尚未启用或更新 GitHub Pages。`.nojekyll` 用于关闭 Jekyll 处理。无需服务器端执行、账户、数据库或外部编译服务。

本地可运行 `python3 -m http.server 8080 --bind 127.0.0.1`，打开 http://127.0.0.1:8080 。

浏览器只转译单文件和清单内随附包，不运行生成 Go、解析任意模块或执行构建脚本。源码限制 32 KiB；Worker 单次转译 10 秒，支持中断恢复。CLI 多包示例是构建时生成的只读快照，不是浏览器多包功能，也不是完整项目源码。

WASM 为可下载、可分析的浏览器编译器产物；未包含完整私有源码仓库、RFC、历史、凭据或本机调试路径。Go runtime 许可见 [GO-LICENSE.txt](GO-LICENSE.txt)。`_headers` 是静态资产中的托管配置，GitHub Pages 不使用它，不保证提供其中的 CSP 响应头。
