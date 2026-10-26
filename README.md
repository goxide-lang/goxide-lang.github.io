# Goxide 网站与浏览器 Playground

本仓库保存 [Goxide 网站源码](https://github.com/goxide-lang/goxide/tree/cdf69aca80fe55569cd9b0c27ab0400390f0c20f/website)生成的静态产物。

- [安装当前编译器](https://goxide-lang.github.io/docs/?page=install)
- [快速开始](https://goxide-lang.github.io/learn/)
- [使用参考](https://goxide-lang.github.io/docs/)
- [serde 与 JSON](https://goxide-lang.github.io/docs/?page=serde-overview)：struct、enum、Option、字段标记和字符串编解码。
- [设计文档](https://goxide-lang.github.io/design/)
- [Playground](https://goxide-lang.github.io/playground.html)：浏览器转译 Goxide 并执行随附的过程宏，不执行生成的 Go。

## 编译器与产物

网站源码提交为 [`cdf69ac`](https://github.com/goxide-lang/goxide/commit/cdf69aca80fe55569cd9b0c27ab0400390f0c20f)，编译器绑定干净提交 [`8112e7c`](https://github.com/goxide-lang/goxide/commit/8112e7ccf71218d7d117d5be44b4180437cb8b09)。完整构建身份和公开库版本记录在 [examples.json](examples.json) 中。

| 内容 | 标识 |
| --- | --- |
| 编译器源码 SHA-256 | `ad9cc553ba37a08ac7ba04130e59a6719c49c6945f65bdf7ce98de7992f668c3` |
| `compiler.wasm` SHA-256 | `3343e2f0f86a225fa4ff2a647f5e60715e764053bcd9535f52275bf3a2e40c7d` |
| Go 导出数据 SHA-256 | `45e8cd7d3c4626d15500c4d2d539d4c0e7d56be87b205d5dfb8781701675b89c` |
| 构建工具链 | `go version go1.27.3 linux/amd64` |
| 浏览器编译目标 | `linux/amd64`，与内嵌 Go 导出数据一致 |
| 编译管线 | `parser-expand-resolve-check-lower` |

## 自动部署与托管

本仓库的 [Publish website workflow](https://github.com/goxide-lang/goxide-lang.github.io/actions/workflows/publish.yml)读取指定公开源码，固定到完整提交后构建、审计并发布。构建与发布使用独立 job，只有发布 job 获得写权限；推送与 Pages API 使用本仓库的短期 `GITHUB_TOKEN`，无需跨仓库密钥或个人 token。

GitHub Pages 从 `deploy/goxide-site-ae61ec6` 分支根目录发布，`main` 原子同步相同产物；`.nojekyll` 关闭 Jekyll 处理。workflow 显式请求 Pages build，并等待本次提交部署完成。网站门禁覆盖构建、HTTP race/vet 和静态产物审计；浏览器 QA 与源码仓库全树检查需查看各自结果。

本地预览：`python3 -m http.server 8080 --bind 127.0.0.1`。

Go runtime 许可见 [GO-LICENSE.txt](GO-LICENSE.txt)，其他前端许可见 [THIRD-PARTY-LICENSES.txt](THIRD-PARTY-LICENSES.txt)。`_headers` 供支持该格式的托管平台使用，GitHub Pages 不读取它。

语言与工具链能力以[当前状态表](https://github.com/goxide-lang/goxide/blob/8112e7ccf71218d7d117d5be44b4180437cb8b09/docs/mvp-gap-audit.md)为准。
