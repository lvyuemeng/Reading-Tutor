# Reading Tutor

An AI skill for explaining academic text, LaTeX, and Typst documents with three interaction modes.

## Features

- **Teach Mode**: Comprehensive, step-by-step explanations with examples
- **Note Mode**: Concise bullet-point summaries
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

### Use with AI Agent

1. Load the skill (SKILL.md) into your AI agent
2. Provide input: text, file path, or PDF
3. Specify mode (teach/note/hint) if desired
4. Optionally specify output file

### Example Commands

WT|
# Generate notes in LaTeX format
Generate notes from paper.tex and save as notes.tex
Generate notes in LaTeX

# Generate notes in Typst format
Generate notes in Typst and save to notes.typ
```

## Project Structure

```
tutor/
├── SKILL.md           # Main skill definition
├── LICENSE            # MIT License
├── README.md          # This file
├── rules/
│   ├── pdf.md        # PDF handling rules
│   ├── typst.md      # Typst handling rules
│   └── latex.md      # LaTeX handling rules
└── scripts/
    ├── pdf_reader.py # PDF extraction script
    ├── requirements.txt
    └── README.md     # Script usage guide
```

## PDF Script Usage

```bash
# Extract all pages
python scripts/pdf_reader.py paper.pdf

# Extract single page
python scripts/pdf_reader.py paper.pdf --page 5

# Extract page range
python scripts/pdf_reader.py paper.pdf --pages 1-10

# Save to file
python scripts/pdf_reader.py paper.pdf --output notes.txt
```

## License

MIT License - see [LICENSE](./LICENSE) file
