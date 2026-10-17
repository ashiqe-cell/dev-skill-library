# Distribution plan

The library is public on GitHub. The fastest way to reach users is to make each skill easy to try, then maintain it and collect real feedback.

## 1. Reach multiple coding agents

Use the `skills` CLI to install a named package from this repository:

```bash
npx skills add ashiqe-cell/dev-skill-library --skill web-vuln-auditor -g
```

The CLI supports many coding agents. The `skills.sh` directory and CLI search help people discover community packages. Keep the skill's folder layout, `SKILL.md`, package README, license, and examples clean so the CLI can identify the package. See [Vercel's skills documentation](https://vercel.com/docs/agent-resources/skills) and [skills.sh](https://skills.sh).

## 2. Codex and ChatGPT directory

For a public listing in the shared ChatGPT and Codex plugin directory, package the skill as a skills-only plugin and submit the ZIP in the OpenAI plugin portal. The submission requires a verified developer identity, package metadata, automated skill scans, and review. A GitHub repo alone does not create a directory listing. Follow the [OpenAI submission guide](https://developers.openai.com/plugins/deploy/submission) and [plugin package guide](https://developers.openai.com/plugins/build/plugins).

## 3. Claude marketplace

For one-click installation from Claude's public directory, package the skill as a Claude plugin and submit it through the [Claude plugin portal](https://claude.com/marketplace/plugins). A public GitHub marketplace can also be added directly by Claude Code users. Claude's review is separate from OpenAI's, so plan for two package submissions if you pursue both directories.

## 4. Help developers find and trust it

- Keep one clear, copyable install command near the top of the README.
- Show a short demo with a realistic input, what the skill checks, and the resulting report.
- Keep releases focused, tested, and explained in the changelog.
- Ask early users for specific feedback and turn common issues into improvements.
- Share it where the intended users already gather, such as security engineering communities, developer forums, and relevant open-source discussions. Follow each community's self-promotion rules.
- Invite maintainers and users to file issues and contribute fixes. Do not buy stars or use automated engagement.

Distribution improves reach, but no listing or campaign guarantees installs or GitHub stars. Useful behavior, a low-friction install, and ongoing maintenance are what earn trust.
