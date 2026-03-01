# Reading Tutor

An AI skill for explaining academic text, LaTeX, and Typst documents with three interaction modes.

## Features

- **Teach Mode**: Comprehensive, step-by-step explanations with examples
- **Note Mode**: Concise bullet-point summaries and writer of latex/typst.
- **Hint Mode**: Socratic questioning for guided discovery

## Supported Input Types

| Type | Extension | Description |
|------|-----------|-------------|
| Plain text | - | Direct paste for explanation |
| LaTeX | .tex | Parse commands, explain syntax |
| Typst | .typ | Parse markup, explain semantics |
| PDF | .pdf | Extract text, generate notes |

## Quick Start

### Install Dependencies

```bash
# Install uv (if not installed)
# macOS/Linux: curl -LsSf https://astral.sh/uv/install.sh | sh
# Windows: winget install astral-sh.uv

# Install PDF extraction dependency
cd scripts
uv pip install -r requirements.txt
```

### Install Skill

```bash
npx skills add lvyuemeng/Reading-Tutor
bunx skills add lvyuemeng/Reading-Tutor
```

Or clone the repo:

```bash
git clone https://github.com/lvyuemeng/Reading-Tutor.git
```

Into the path of skill of agent tool you expected.

### Use with AI Agent

1. Load the skill (SKILL.md) into your AI agent
2. Provide input: text, file path, or PDF
3. Specify mode (teach/note/hint) if desired
4. Optionally specify output file

## License

MIT License - see [LICENSE](./LICENSE) file
