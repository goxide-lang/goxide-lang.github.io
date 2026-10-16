# Goxide 网站与浏览器 Playground

本仓库托管 [Goxide 网站源码](https://github.com/goxide-lang/goxide/tree/main/website)生成的静态产物：特性与示例目录、只读 CLI 项目快照，以及单包多文件的浏览器转译 Playground。浏览器使用 WASM 将 `.gox` 转成 Go，不执行生成的 Go。

## 编译器与产物

当前产物由编译器干净检出 [`0df22b6`](https://github.com/goxide-lang/goxide/commit/0df22b6f81d387c697934309f4230e3074944ff8) 重建，包含新前端、原生 Go 生成和统一 feature/target/env 配置。完整构建身份、依赖、示例源码与生成结果记录在 [examples.json](examples.json) 中；`compilerSource.kind=worktree`、`dirty=false`。

| 内容 | 标识 |
| --- | --- |
| 编译器源码 SHA-256 | `edcbd910796749b2e7e5a42a5b6ccf1362a5d234855a2d032cb3cd6aa8d52f25` |
| `compiler.wasm` SHA-256 | `e5aa870af6d75eec2640e9a7f205fdb2ac1b387cfcbebd66445976f0cfd7c734` |
| 构建工具链 | Go 1.27.1 |
| 浏览器编译目标 | darwin/arm64，与内嵌 Go 导出数据一致 |
| 编译管线 | `parser → expand → resolve → check → lower` |

示例的源码、生成 Go、依赖版本和包集合均在 `examples.json` 中。浏览器允许一个用户包内最多 16 个文件、总计 32 KiB；固定随附依赖只读。每次转译限时 10 秒，并支持中断后恢复。CLI 多包示例来自构建时快照；浏览器不解析任意模块或执行构建脚本。

## 预览与托管

```sh
python3 -m http.server 8080 --bind 127.0.0.1
```

打开 [本地网站](http://127.0.0.1:8080)。GitHub Pages 沿用 `deploy/goxide-site-ae61ec6` 分支根目录发布，`main` 同步保存相同产物；`.nojekyll` 关闭 Jekyll 处理。页面不需要账户、数据库或外部编译服务。

Go runtime 许可见 [GO-LICENSE.txt](GO-LICENSE.txt)，其他前端许可见 [THIRD-PARTY-LICENSES.txt](THIRD-PARTY-LICENSES.txt)。`_headers` 供支持该格式的静态托管平台使用，GitHub Pages 不读取它。

语言与工具链能力以 [当前状态表](https://github.com/goxide-lang/goxide/blob/main/docs/mvp-gap-audit.md)为准；已有 Go 项目的使用方式见 [gen 用户指南](https://github.com/goxide-lang/goxide/blob/main/docs/using-goxide-gen.md)。网站上的指南页面待从同一份 Markdown 生成。
