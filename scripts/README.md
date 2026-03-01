# PDF Reader Script Usage Guide

## Quick Install

### Install uv (Choose Your OS)

**macOS / Linux**
```bash
# Using curl (recommended)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or via pip
pip install uv
```

**Windows (PowerShell)**
```powershell
# Using winget (recommended)
winget install astral-sh.uv

# Or via pip
pip install uv
```

**Verify**
```bash
uv --version
```

**Install dependencies (with virtual environment)**
```bash
cd scripts
uv venv
uv pip install pypdf
# Or: uv pip install -r requirements.txt
```
## Basic Usage

```bash
# Extract all pages (using uv run)
uv run pdf_reader.py paper.pdf

# If the script is in a different directory
uv run /path/to/pdf_reader.py /path/to/paper.pdf

# Using uv with arguments
uv run pdf_reader.py paper.pdf --page 5

# On Windows (PowerShell)
uv run .\pdf_reader.py .\paper.pdf

# Extract single page
uv run pdf_reader.py paper.pdf --page 5

# Extract page range
uv run pdf_reader.py paper.pdf --pages 1-10

# Extract specific pages
uv run pdf_reader.py paper.pdf --pages 1,3,5,7

# Extract mixed range
uv run pdf_reader.py paper.pdf --pages 1-3,5,8-10

# Save to file
uv run pdf_reader.py paper.pdf --output extracted_text.txt

# Verbose mode
uv run pdf_reader.py paper.pdf --pages 1-5 --verbose

# Help
uv run pdf_reader.py --help
```

## Using with Reading Tutor Skill

### From AI Agent

When using the Reading Tutor skill with PDF files:

1. **Direct the AI**: "Read pages 3-7 from paper.pdf and generate notes"
2. **The AI will**: Use this script internally to extract text → generate notes

### Example Workflow

```
User: "Generate notes from paper.pdf, pages 5-10, save to notes.md"

AI Action:
1. Run: python scripts/pdf_reader.py paper.pdf --pages 5-10 --output temp.txt
2. Read extracted text from temp.txt
3. Apply Note mode processing
4. Write to notes.md
```

## Page Numbering

- **1-indexed**: Page 1 = first page of PDF
- **Range format**: "start-end" inclusive
- **Multiple**: Use commas to separate

## Output Format

The script extracts plain text. Headers, footers, and complex formatting may not be perfectly preserved. The AI will organize the extracted content when generating notes.

## Troubleshooting

| Error | Solution |
|-------|----------|
| "pypdf not installed" | Run `uv pip install pypdf` |

## Programmatic Usage

```python
from pdf_reader import extract_text_from_pdf

# In Python code
text = extract_text_from_pdf(
    'paper.pdf',
    pages='1-10',  # or None for all, or 5 for single page
    output_file='output.txt',
    verbose=True
)
```
