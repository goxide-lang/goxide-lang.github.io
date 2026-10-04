# goxide 网站与浏览器 Playground

正式站点：https://goxide-lang.github.io/ · [RFC 特性目录](https://goxide-lang.github.io/#catalog)

此仓库只发布审计后的静态网站产物，GitHub Pages 使用 `deploy/goxide-site-ae61ec6` 分支根目录。分支名是部署路径，不能当作当前编译器版本。

当前编译器：`27d2e2740c5ee7dc3e3766bd7b5f0eec6bb852b8`，Go 1.27.1，metadata schema 7。[examples.json](examples.json) 记录实际编译器/网站提交、源码和 export data 摘要、WASM SHA-256、公开依赖版本/checksum、真实 hgo/Go/stdout。

26 个主题覆盖 RFC 0001–0026 及相关研究，状态针对限定能力；提案不代表已实现。当前已包含公开 std/sum 与 serde、明确上下文下的普通 Option/Result 省参、有限生成代码可读性改进。RFC 0024 的新 use 路径仍是提案；next 暂无公共 API。

10 个单文件示例经 CLI 实际转译/运行，并与浏览器 WASM 逐字节对照；10 个目录拒绝例核对诊断。CLI 区展示 format 2 goxide.toml/goxide.lock、target 内真实生成 Go，以及 import-go 只读 plan→新目录迁入→offline/locked 运行的实证。迁入保留原工程，不自动升级旧格式，支持受限原生 module vendor 迁入，并实测冷 module cache 下 offline/locked 运行、vendor 字节变化拒绝；单模块vendor模式与增强依赖图混用未支持；独立go.work迁入模式支持workspace vendor及渐进增强。新增 CLI 长短选项、run 参数透传与旧 Go 风格选项拒绝快照。RFC 0026 作者 workspace 核心现为部分实现：显式 workspace=true 继承、全 workspace 统一版本与根唯一 schema 3 锁、仅所选图合并 feature/构建、成员与 bin/example 选择、复制根锁拆出。新增两个真实 CLI 快照展示版本/feature区别和 Git 分支移动后仍复用原 pin；这些多文件工程不能在浏览器运行。go.work/workspace vendor 已支持只读plan→新目录迁入，保留work/member原生政策并物化显式成员边；迁入后可渐进使用.hgo/features及明确授权scripts，schema4非vendor根锁经显式物化可复制拆出。新增两组真实快照验证上述流程、vendor修改字节/权限与冷modulecache。workspace vendor独立拆出仍未支持，须确认转换协议；统一host resolver、细粒度lock update与publish/registry尚未实现。迁入分析限定当时平台/工具/C配置，迁入本身不授予脚本权限。复制锁不复制 path 源码，继承须先物化；快照中的归一化锁仅展示。

浏览器仅转译单文件与白名单包，不运行生成 Go，不解析多模块项目或执行脚本。UTF-8 输入 ≤32 KiB；Worker 转译 10 秒超时，支持中断恢复。无需后端执行服务、账户或数据库。

公开依赖固定提交：std `3f2204770fd3b09cf9f5a1d9228464b7f7c1bdcd`；serde `a1b791e96d660c6be620e110c566a9a171631b7e`。生成 Go 使用共享类型别名和必要的具体载荷 validator，不复制通用 sum 实现；不承诺旧 schema 6 或 v1 ABI 兼容。

清单以 no-store 读取；app/style URL 绑定网站版本，Worker/WASM URL 绑定编译器版本。执行前验证 WASM SHA-256，混版/损坏内容会被拒绝。WASM 可下载和分析，这不是逆向保密保证。

公开内容只有审核摘要、刻意示例和静态资源，不含私有 RFC 全文、实现证据索引、编译器源码历史、凭据或本机路径。Go runtime 许可见 [GO-LICENSE.txt](GO-LICENSE.txt)。`.nojekyll` 关闭 Jekyll；GitHub Pages 不应用 `_headers`，不承诺自托管服务器的同等 CSP 响应头。

本地预览：在资源目录运行 `python3 -m http.server 8080 --bind 127.0.0.1`，打开 http://127.0.0.1:8080 。
