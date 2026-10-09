# Goxide 官网与浏览器 Playground

[正式站点](https://goxide-lang.github.io/) · [特性目录](https://goxide-lang.github.io/#catalog) · [完整构建清单](examples.json)

源码来自已合并 main `cf56a52c22acff7a1ab353f86515745b542d6abd`，编译器生产 pin `03251a7cb31cee22a41c37af1df1ff0b90aba6d3`。构建逐文件核对生产源码与该 pin 相同；两种提交身份分别记录。工具链为 Go 1.27.1 linux/amd64。

Pages 延用 `deploy/goxide-site-ae61ec6` 分支根目录；分支名不是版本号。此次仅同步已合并内容，未合入设计 PR #16 或自动发布 PR #18，未修改凭据、权限或 Pages source。

公开依赖锁定 std `v0.0.0-20261009104839-c02a09d8c417`（`c02a09d8c417b35dc7e432fc484172fab6db6182`）、serde `v0.0.0-20261009021520-f342a31e20d0`（`f342a31e20d0be3a4c02b5c750fb609dc25a7dc3`），没有本机 replace。std main 的合并提交不同于构建选择的精确模块版本；不擅自升级锁。ABI：enum metadata 9、reference 3、use 3、sum 3、protocol 1、typeinfo 1。旧生成物需重新生成。

本批包含 std 运行支持迁移、显式 `use` / `::` 路径、由实际 serde owner 解析的限定派生、enum 原槽 `ref` / `ref mut` 与基本自动 match 借用，以及静态协议、关联函数和受约束泛型调用的 carrier 支持。13 个单文件示例和一个五文件示例由真实 CLI 转译并执行，WASM 与同版 CLI 对照。浏览器展示完整生成 Go/helper，以及固定依赖的真实源码、许可证、导出身份和根配置摘要。

浏览器只编辑同一用户包的 1–16 个 `.gox` 文件，总 UTF-8 输入不超过 32 KiB，不运行生成 Go、任意下载模块或执行构建脚本。CLI 与 WASM 共用 `goxide.roots.toml` 声明的依赖根。跨模块 `.goxide.protocols.json` sidecar 恢复属于 CLI 范围，浏览器不加载任意外部协议产物。

当前仅为 pre-MVP 已验收切片，**不宣称 MVP 完成**。原槽引用可留存，不新增生命周期、逃逸/冲突或替换失效 borrow 检查；路径只读不等于全局不可变，写引用不保证独占。静态协议不包含完整 trait、关联类型、动态 trait 对象、泛型协议/impl 或完整泛型系统；现有业务 serde API 未迁写为该通用协议片，也未因此实现新的业务 serde API。Value/PATCH/YAML、定制 field adapters 等未交付能力仍按特性目录限定。

公开首页的旧总览仍有一处过宽的“.gox 用户泛型定义尚未交付”表述；当前已实现的限定范围应以静态协议卡片及 `static_protocol` / 五文件真实例子为准。此处保留合并主线的原始页面字节，不用发布目录临时改写来冒充源提交；该文案需在主线后续修正。

WASM SHA-256：`62f490f513a15194949e41bb5fb07557fcc674a670b73903439aa7746a61b983`。页面与 Worker 按提交加载资源，执行前验证 WASM 和依赖根身份。公开内容包括刻意示例、审阅摘要、固定随附依赖源码和许可；WASM 可下载和分析。未复制完整编译器仓库、RFC 原文、Git 历史或凭据。

`.nojekyll` 保持静态发布；GitHub Pages 不应用 `_headers`，不承诺自托管服务器的同等 CSP 响应头。本地预览：`python3 -m http.server 8080 --bind 127.0.0.1`。
