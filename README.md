# Goxide 网站与浏览器 Playground

[正式站点](https://goxide-lang.github.io/) · [RFC 特性目录](https://goxide-lang.github.io/#catalog)

此仓库只发布审计后的静态资源。Pages 使用 `deploy/goxide-site-ae61ec6` 分支根目录；部署分支名不是当前编译器版本。

网站源码来自已合并 main `3bbc06531849409bb9a35e391899f6bae4be6e1d`，编译器生产 pin 为 `e68bfe6ed83de432e2c2ee79936bda4150cc78ca`（构建逐文件核对与该 main 的生产源码相同）。工具链：Go 1.27.1 linux/amd64。不包含未合并功能 PR。

配套 ABI：enum metadata **8**、reference **3**、use **2**、sum **2**。公开依赖固定 std `ce5bccb4ff9c7fb96b7f192a3a263051590d9288`（`v0.0.0-20261004173304-ce5bccb4ff9c`）与 serde `a1b791e96d660c6be620e110c566a9a171631b7e`（`v0.0.0-20261004120911-a1b791e96d66`），无本机 replace。[构建清单](examples.json)记录版本/checksum、源与 export data 摘要、WASM SHA-256 和实际示例输出。

包含别名精简、显式 std 校验、宏/Eq 来源修复，以及同包多文件 Playground。十一组单文件示例和一个三文件示例均由真实 CLI 转译、执行并断言输出；浏览器通过 Worker 内的同版 Go WASM 转译。完整生成 Go（含 helper）按文件查看，固定随附依赖源码只读并标明真实来源。

浏览器只编辑一个用户包内的 `.gox` 文件，最多 16 个文件、合计 32 KiB；不运行生成 Go、不上传源码、不解析任意模块或执行脚本。Worker 转译 10 秒超时，可中断恢复。工程快照仅展示构建时验证的 CLI 能力；不代表浏览器支持完整工程、跨包模块恢复或任意依赖解析。

清单以 no-store 读取，app/style 绑定网站版本，Worker/WASM 绑定编译器版本；执行前校验 WASM SHA-256，混版或损坏资源拒绝。此批 WASM SHA-256：`7c9062eab6f9b4a62efae0f3754551b43a91a631fd0b25dc6103a5086738d204`。

公开内容包含审阅摘要、刻意示例、静态资源，以及构建清单中固定随附依赖的源码和许可。公开 WASM 可下载和分析。未发布完整编译器仓库、RFC 原文、Git 历史、凭据或本机路径。Go 许可见 [GO-LICENSE.txt](GO-LICENSE.txt)；其他许可随依赖来源展示。

`.nojekyll` 关闭 Jekyll；GitHub Pages 不应用 `_headers`，不承诺自托管服务器的同等 CSP 响应头。无需后端执行服务、账号或数据库。

本地预览：在资源目录运行 `python3 -m http.server 8080 --bind 127.0.0.1`。
