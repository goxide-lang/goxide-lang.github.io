# Goxide 网站与浏览器 Playground

本仓库托管 [Goxide 网站源码](https://github.com/goxide-lang/goxide/tree/main/website)生成的静态产物：特性与示例目录、只读 CLI 项目快照，以及单包多文件的浏览器转译 Playground。浏览器使用 WASM 将 `.gox` 转成 Go，不执行生成的 Go。

## 编译器与产物

本地待发布快照的编译器源码与 [P7 提交 `1a70654255e0388c5c2a775367ae7a1491d7a04a`](https://github.com/goxide-lang/goxide/commit/1a70654255e0388c5c2a775367ae7a1491d7a04a)一致。产物创建时的原始身份保留在 [examples.json](examples.json)：基准提交 `bd90e606dcfa220b4054fe41c56bdc63a5687355`、`kind=worktree`、`dirty=true`。这份快照不包含后续的 CLI `gen` 改动。下文引用的站点文件（包括 `examples.json` 和 `compiler.wasm`）将随该快照发布。

| 内容 | 标识 |
| --- | --- |
| 编译器源码 SHA-256 | `05db6dc5c35745b056df570b16b28057447d92e7e827345047494faf546b463a` |
| `compiler.wasm` SHA-256 | `2bb850d33f628a82b147833adaef141b2736f2414a8e175b8e2d27e95901f578` |
| 构建工具链 | Go 1.27.1 |
| 编译管线 | `parser → expand → resolve → check → lower` |

示例的源码、生成 Go、依赖版本和包集合均在 `examples.json` 中。浏览器允许一个用户包内最多 16 个文件、总计 32 KiB；固定随附依赖只读。每次转译限时 10 秒，并支持中断后恢复。CLI 多包示例来自构建时快照；浏览器不解析任意模块或执行构建脚本。

## 预览与托管

```sh
python3 -m http.server 8080 --bind 127.0.0.1
```

打开 [本地网站](http://127.0.0.1:8080)。GitHub Pages 从 `main` 分支根目录发布；`.nojekyll` 关闭 Jekyll 处理。页面不需要账户、数据库或外部编译服务。

Go runtime 许可见 [GO-LICENSE.txt](GO-LICENSE.txt)，其他前端许可见 [THIRD-PARTY-LICENSES.txt](THIRD-PARTY-LICENSES.txt)。`_headers` 供支持该格式的静态托管平台使用，GitHub Pages 不读取它。

语言与工具链能力以 [当前状态表](https://github.com/goxide-lang/goxide/blob/main/docs/mvp-gap-audit.md)为准；已有 Go 项目的使用方式见 [gen 用户指南](https://github.com/goxide-lang/goxide/blob/main/docs/using-goxide-gen.md)。网站上的指南页面待从同一份 Markdown 生成。
