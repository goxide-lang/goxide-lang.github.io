# Goxide 网站与浏览器 Playground

本仓库托管 [Goxide 网站源码](https://github.com/goxide-lang/goxide/tree/22b8fb2452fba79c30ee429fe16f517a1e4a87ef/website)生成的静态产物：语言介绍、快速开始、使用参考、设计文档与浏览器 Playground。

- [安装当前编译器](https://goxide-lang.github.io/docs/?page=install)：使用 Go 1.27.3 从本页对应的源码提交构建；正式构建脚本会写入过程宏 SDK 身份。运行时的 Go 工具链也须为 1.27.3，包括补丁号。
- [快速开始](https://goxide-lang.github.io/learn/)：从纯 Go、混合接入到完整 Goxide 项目、feature 配置和用户过程宏，共五个阶段；提供包含清单、锁文件与测试的完整 ZIP 下载。
- [使用参考](https://goxide-lang.github.io/docs/)：项目、包管理、CLI 与互操作指南，以及过程宏、syntax 语法工具的完整教程和 SDK API 参考。
- [设计文档](https://goxide-lang.github.io/design/)：词法与文法、各阶段输入输出与转译语义、前端和 enum 规范、完整 RFC；从仓库 Markdown 生成。
- [Playground](https://goxide-lang.github.io/playground.html)：浏览器使用 WASM 将 `.gox` 转成 Go，并执行随附的过程宏展开；不执行生成的 Go。

## 编译器与产物

编译器绑定干净提交 [`92b0a0c`](https://github.com/goxide-lang/goxide/commit/92b0a0c42d904b338afee48c04c6d1293427708c)，网站源码提交为 [`22b8fb2`](https://github.com/goxide-lang/goxide/commit/22b8fb2452fba79c30ee429fe16f517a1e4a87ef)。完整构建身份、公开库版本、项目源码与生成结果记录在 [examples.json](examples.json) 中；`compilerSource.kind=commit`、`dirty=false`。

| 内容 | 标识 |
| --- | --- |
| 编译器源码 SHA-256 | `dc1485e6f18c2ceff104d465df56ceb332935d49f97d49e3a801d13485c02816` |
| `compiler.wasm` SHA-256 | `d44217bdc2f8919b84e5d0b2c147e0f9970c250a7844c9c889728b343d40540e` |
| 构建工具链 | Go 1.27.3 |
| 浏览器编译目标 | darwin/arm64，与内嵌 Go 导出数据一致 |
| 编译管线 | `parser → expand → resolve → check → lower` |

示例和快速开始项目在构建时真实生成、运行和测试，并检查重复生成一致。浏览器允许一个用户包内最多 16 个文件、总计 32 KiB；固定随附依赖只读。正式 std/serde 协议随用户编辑按需实例化，三类用户过程宏提供可运行示例、完整只读实现和项目下载。IDE 工作区内提供图标工具栏、独立源码与生成文件树、四种布局和可定位诊断；手机默认收起文件树，保留新建入口。每次转译限时 70 秒，并支持中断后恢复。完整项目与自定义宏源码构建使用 CLI；浏览器不解析任意模块或执行构建脚本。

## 预览与托管

```sh
python3 -m http.server 8080 --bind 127.0.0.1
```

打开 [本地网站](http://127.0.0.1:8080)。GitHub Pages 沿用 `deploy/goxide-site-ae61ec6` 分支根目录发布，`main` 同步保存相同产物；`.nojekyll` 关闭 Jekyll 处理。页面不需要账户、数据库或外部编译服务。

Go runtime 许可见 [GO-LICENSE.txt](GO-LICENSE.txt)，其他前端许可见 [THIRD-PARTY-LICENSES.txt](THIRD-PARTY-LICENSES.txt)。`_headers` 供支持该格式的静态托管平台使用，GitHub Pages 不读取它。

语言与工具链能力以 [当前状态表](https://github.com/goxide-lang/goxide/blob/92b0a0c42d904b338afee48c04c6d1293427708c/docs/mvp-gap-audit.md)为准。
