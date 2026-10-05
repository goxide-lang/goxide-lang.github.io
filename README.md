# Goxide 网站与浏览器 Playground

[正式站点](https://goxide-lang.github.io/) · [RFC 特性目录](https://goxide-lang.github.io/#catalog)

此仓库只发布审计后的静态资源。Pages 使用 `deploy/goxide-site-ae61ec6` 分支根目录；部署分支名不是当前编译器版本。

当前编译器：`f1474551cb7f18c5610880b91b54e7367a2a6a2e`，Go 1.27.1。语言名 **Goxide**，命令 `goxide`，源码 `.gox`，环境变量 `GOXIDE_*`。旧 `.hgo`、`HGO_*`、旧 directive 与旧生成 marker 输入会明确拒绝；应迁移并重新生成产物，不混用旧 ABI。

配套 ABI：enum metadata **8**、reference **3**、use **2**、sum **2**。公开依赖路径不变，固定 std `ce5bccb4ff9c7fb96b7f192a3a263051590d9288`（`v0.0.0-20261004173304-ce5bccb4ff9c`），serde `a1b791e96d660c6be620e110c566a9a171631b7e`。不使用 std main 的旧 ABI 或本机 replace。[构建清单](examples.json)记录真实解析版本/checksum、ABI、编译器/网站提交、源与export data摘要、WASM SHA-256和实际示例输出。

26 个主题覆盖 RFC 0001–0026 及相关研究；状态仅指注明的实现范围。10 个单文件例子由 CLI 实际转译/运行，并与 WASM 逐字节对照；10 个目录拒绝例核对诊断，另有8个适配检查及旧 directive 拒绝检查。CLI、Worker `goxideCompile`、WASM、export data与新std同批重建。

工程快照展示TOML/锁、feature/target、普通Go与go.work向新目录迁入、渐进`.gox`/features、统一版本与selected构建，以及显式物化本地路径后复制根锁拆出。脚本仍须明确授权，迁入不授权；浏览器不执行这些多文件工程。

**Goxide没有长期vendor模式。** 原生vendor仅是Go迁移输入：保留供应字节/权限及逻辑module身份，物化到`local-modules/`普通模块，以显式本地replace使用。`goxide-import.json`记录原始政策、摘要、来源和映射。迁入后可正常编辑本地源码，旧vendor构建和独立vendor拆出方案已取消；旧vendor TOML/锁字段要求重新迁入。

默认local核心与只读来源候选已支持；交互式一次来源选择、显式remote切换及远端差异/修改确认仍在下一阶段。未比对远端时差异为unknown，不从module路径猜Git URL。`--offline`仅声称已核验的本地材料/缓存路径，不探测或补包，也不等于用户脚本网络沙箱。迁入分析限定当前平台/工具配置；外部本地依赖仍须显式安排路径。统一host resolver、细粒度lock update、publish/registry仍未实现。RFC0024新use路径仍属提案。

浏览器只转译单文件与白名单包，不运行生成Go，不上传源码，不解析任意模块或执行脚本。输入≤32KiB，Worker转译10秒超时，可中断恢复。无需后端执行服务、账号或数据库。清单no-store读取，app/style绑定网站版本，Worker/WASM绑定编译器版本；执行前核验WASM SHA-256，混版/损坏内容拒绝。公开WASM可下载和分析，不保证逆向保密。

公开内容仅为审核摘要、刻意示例和静态资源，不含私有RFC全文、编译器源码历史、凭据或本机路径。许可见[GO-LICENSE.txt](GO-LICENSE.txt)。`.nojekyll`关闭Jekyll；GitHub Pages不应用`_headers`，不承诺自托管服务器的同等CSP响应头。

本地预览：在资源目录运行 `python3 -m http.server 8080 --bind 127.0.0.1`，打开 http://127.0.0.1:8080 。
