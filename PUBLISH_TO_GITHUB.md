# 🚀 发布到 GitHub 指南

## 📋 发布步骤

### 步骤 1：在 GitHub 创建仓库

1. 访问 [GitHub](https://github.com)
2. 点击右上角 **+** → **New repository**
3. 填写仓库信息：
   - **Repository name**: `overseas-assessment`
   - **Description**: `企业出海战略智能评估专家 - Claude Code Skill`
   - **Visibility**: ✅ Public（公开）或 ⚪ Private（私有）
   - ⚠️ **不要**勾选 "Add a README file"（我们已经有了）
4. 点击 **Create repository**

### 步骤 2：推送代码到 GitHub

创建仓库后，GitHub 会显示推送命令。执行以下命令：

```bash
cd "C:\Users\shiya\Desktop\prj\高力\overseas-assessment-skill"

# 添加远程仓库（替换 YOUR_USERNAME 为你的 GitHub 用户名）
git remote add origin https://github.com/YOUR_USERNAME/overseas-assessment.git

# 推送代码
git push -u origin master
```

### 步骤 3：配置仓库（可选但推荐）

#### 3.1 添加 Topics 标签
在仓库页面点击 ⚙️ Settings → 按顺序添加：
- `claude-code`
- `skill`
- `overseas-assessment`
- `business-intelligence`
- `chinese-companies`
- `internationalization`

#### 3.2 设置仓库描述
在 Settings → General → Description：
```
企业出海战略智能评估专家 - 为 Claude Code 提供中国企业出海可行性评估能力
```

#### 3.3 启用功能（推荐）
- ✅ Issues：用于反馈和问题追踪
- ✅ Discussions：用于讨论和交流
- ✅ Wiki：用于补充文档
- ✅ Actions：如果需要自动化测试

### 步骤 4：创建 Release（推荐）

1. 在仓库页面点击 **Releases** → **Create a new release**
2. 填写信息：
   - **Tag**: `v1.0.0`
   - **Title**: `overseas-assessment v1.0.0`
   - **Description**:
     ```markdown
     ## 🎉 首次发布

     ### ✨ 特性
     - 三层智能检索架构（WebSearch → Jina Reader → 浏览器自动化）
     - 五大维度评分体系（产品技术、资金储备、团队基因、市场契合、合规环境）
     - 站点经验系统（天眼查、企查查、招聘平台等）
     - Token 效率优化（节省约 40%）

     ### 📦 安装
     下载 `overseas-assessment.skill` 文件到 `~/.config/claude/skills/` 目录即可

     ### 📖 使用
     在 Claude Code 中输入：
     ```
     评估[企业名称]的出海可行性
     ```
     ```
`

## 🎯 发布后检查清单

- [ ] 仓库已公开（如果希望他人可见）
- [ ] README.md 显示正常
- [ ] Topics 标签已添加
- [ ] License 已设置（MIT）
- [ ] Release v1.0.0 已创建
- [ ] 下载的 .skill 文件可以正常使用

## 📢 推广建议

发布后，可以通过以下方式推广：

1. **分享到社区**
   - Claude Code Discord/Slack 社区
   - Reddit r/Claude
   - 中文 AI 社区

2. **写博客/文章**
   - 介绍 skill 的功能和使用方法
   - 分享评估报告示例

3. **社交媒体**
   - Twitter/X、微博等平台分享
   - 使用相关标签：#ClaudeCode #AI #出海评估

## 🐛 遇到问题？

### Git 认证问题
如果推送时提示认证错误，请：
1. 安装 [GitHub CLI](https://cli.github.com/)
2. 运行 `gh auth login`
3. 使用 `git remote set-url origin git@github.com:YOUR_USERNAME/overseas-assessment.git`

### 中文文件名显示问题
这是 Windows Git 的已知问题，不影响实际使用。如需修复：
```bash
git config --global core.quotepath false
```

---

**祝你发布顺利！🎉**
