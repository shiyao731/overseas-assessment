# 🌍 overseas-assessment

> 企业出海战略智能评估专家 - Claude Code Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Skill Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/yourusername/overseas-assessment)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Compatible-green.svg)](https://claude.ai/claude-code)

## 📖 简介

**overseas-assessment** 是一个为 Claude Code 设计的企业出海可行性评估技能。基于用户提供的企业名称，自动进行全网深度调研，生成包含五大维度评分、风险分析和战略建议的专业评估报告。

### ✨ 核心特性

- 🤖 **三层智能检索架构**：WebSearch → Jina Reader → 浏览器自动化
- 🎯 **目标导向研究流程**：以研究目标为核心，而非固定步骤
- 📚 **站点经验系统**：针对中文商业平台优化的访问模式
- 📊 **五大维度评分**：产品技术、资金储备、团队基因、市场契合、合规环境
- 💰 **Token 效率优化**：使用 Jina Reader 节省约 40% tokens
- 🔄 **并行研究能力**：支持多代理并行研究复杂企业

## 🚀 快速开始

### 安装

```bash
# 克隆仓库
git clone https://github.com/yourusername/overseas-assessment.git

# 复制 skill 文件到 Claude Code skills 目录
cp overseas-assessment.skill ~/.config/claude/skills/
```

或手动安装：
1. 下载 `overseas-assessment.skill` 文件
2. 复制到 `~/.config/claude/skills/` 目录
3. 重启 Claude Code

### 使用方法

在 Claude Code 中直接输入：

```
评估招商银行的出海可行性
```

或

```
分析比亚迪的出海战略
```

## 📊 评估维度

| 维度 | 权重 | 评估要点 |
|------|------|----------|
| **产品与技术竞争力** | 20分 | 技术壁垒、专利数量、产品独特性 |
| **资金与供应链储备** | 20分 | 融资规模、现金流、跨国履约能力 |
| **团队与国际化基因** | 20分 | 创始人背景、海外经验、本地化能力 |
| **目标市场契合度** | 20分 | 海外需求匹配度、产品本地化难度 |
| **合规与宏观环境** | 20分 | 政策壁垒、地缘风险、监管环境 |

**总分**：100分

**出海评级标准**：
- 🟢 80-100分：出海条件成熟
- 🟡 60-79分：具备出海潜力
- 🟠 40-59分：出海风险较高
- 🔴 0-39分：暂不具备条件

## 📁 项目结构

```
overseas-assessment/
├── SKILL.md                    # 主技能文件
├── INTEGRATION_NOTES.md         # 整合说明文档
├── README.md                    # 本文件
├── LICENSE                      # MIT 许可证
└── references/
    ├── 中国企业出海全景分析报告.md
    └── site-patterns/
        ├── tianyancha.md        # 天眼查访问指南
        ├── qcc.md               # 企查查访问指南
        ├── company-sites.md     # 公司官网访问指南
        ├── job-platforms.md     # 招聘平台访问指南
        └── news-sources.md      # 新闻媒体检索指南
```

## 🔧 技术架构

### 三层检索架构

```
┌─────────────────────────────────────────────────────────────┐
│                    三层检索架构                               │
├─────────────────────────────────────────────────────────────┤
│  第一层：WebSearch (Duckduckgo/Bing/Brave)                   │
│  • 用途：一般性搜索、发现信息源                               │
├─────────────────────────────────────────────────────────────┤
│  第二层：Jina Reader (jina.ai/http://)                       │
│  • 用途：已知 URL 的高效内容提取                              │
│  • 优势：Token 效率高、处理动态页面                           │
├─────────────────────────────────────────────────────────────┤
│  第三层：浏览器自动化 (CDP/Playwright)                        │
│  • 用途：处理反爬虫网站、需要登录的内容                       │
└─────────────────────────────────────────────────────────────┘
```

### 研究目标体系

```
研究目标体系
├── 目标1：构建企业完整画像
├── 目标2：评估出海基础能力
├── 目标3：分析目标市场环境
└── 目标4：识别风险与机遇
```

## 📝 输出示例

评估报告包含以下章节：

1. **核心判定与综合评分** - 总分、评级、战略判定
2. **五大核心维度表现** - 各维度得分与数据支撑
3. **深度出海全景分析**
   - 企业出海的战略逻辑框架
   - 区域布局战略建议
   - 出海成功要素匹配度
   - 风险识别与应对
   - 未来趋势与建议
4. **总结** - 核心发现、关键建议、风险提示

## 🤝 贡献指南

欢迎贡献！请遵循以下步骤：

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

### 贡献方向

- 🌍 添加更多站点经验模式
- 📊 优化评分算法
- 🤖 集成更多数据源
- 📝 改进报告模板
- 🐛 修复 Bug

## 📄 许可证

本项目采用 [MIT 许可证](LICENSE) - 详见 LICENSE 文件

## 🙏 致谢

- [web-access](https://github.com/eze-is/web-access) - 提供三层检索架构灵感
- Claude Code 团队 - 提供 Skills 框架
- 所有贡献者

## 📧 联系方式

- Issues: [GitHub Issues](https://github.com/yourusername/overseas-assessment/issues)
- Discussions: [GitHub Discussions](https://github.com/yourusername/overseas-assessment/discussions)

## 🌟 Star History

如果这个项目对你有帮助，请给一个 Star ⭐️

---

**Made with ❤️ by Chinese AI Community**
