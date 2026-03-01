# PDF Handling Rules

## Purpose

Rules for reading, parsing, and generating notes from PDF files.

## When To Use

- User provides a `.pdf` file path
- User requests extraction from specific pages
- User wants to convert PDF content to notes

## Instructions

### Basic PDF Processing

1. **Read the PDF file** using PDF reading capability
2. **Extract text content**: Pull all text from the document
3. **Identify structure**: Detect headings, paragraphs, equations, figures, tables
4. **Generate summary**: Use Note mode to create concise extraction
5. **Explain complex content**: Use Teach mode for difficult passages

### Page-Specific Extraction

When user specifies page numbers:

- **Single page**: `page 5` → Extract only page 5 content
- **Page range**: `pages 5-10` → Extract pages 5 through 10
- **Multiple pages**: `pages 3, 7, 12` → Extract specific pages
- **All pages**: No specification → Extract entire document

### Structured Output

Extract and organize:

| Element | How to Handle |
|---------|---------------|
| Headings | Identify hierarchy (H1, H2, H3) |
| Paragraphs | Preserve flow, note section context |
| Equations | Copy as-is, note equation numbers |
| Figures | Note figure captions, describe visual |
| Tables | Extract structure, note headers |
| References | List citation keys |

## Key Elements to Identify

- **Title page**: Author, title, date, institution
- **Abstract**: Summary of paper
- **Introduction**: Problem statement, motivation
- **Methods**: Approach, methodology
- **Results**: Findings, data
- **Discussion**: Interpretation, implications
- **Conclusion**: Summary, future work
- **References**: Bibliography

## Limitations

If PDF text extraction is unavailable:

1. Explain the limitation clearly
2. Offer alternative: user copies text manually
3. Still provide value: explain what you'd do with extracted text

## Output Format

For Note mode extraction:

```markdown
## Document Overview
- Title: [title]
- Pages: [N]
- Sections: [count]

## Key Sections
1. [Section name] - [brief description]
2. ...

## Important Content
- [Key finding 1]
- [Key finding 2]
...

## Equations/Formulas
- [Equation 1]: [description]
- [Equation 2]: [description]
```

## Anti-Patterns

SN|
### Workspace Separation

**PDF and output file may be in different locations.**

1. **Path handling**:
- PDF path: Use exactly as provided by user (may be absolute or relative)
- Output path: Use exactly as provided by user
- Do NOT assume PDF and notes are in same directory

2. **When user says**:
- "Read paper.pdf and save to notes.md" → Use paths as given
- "Read /path/to/paper.pdf and save to ./notes/notes.md" → Create ./notes/ if needed

3. **AI must**:
- Use provided PDF path for extraction (may need to use scripts/pdf_reader.py)
- Use provided output path for writing notes
- Handle cases where PDF is in different workspace/directory

4. **Absolute vs Relative**:
- Absolute path: Use as-is
- Relative path: Resolve from current working directory
- Create directories if they don't exist (for output file)

## Validation Checklist

- [ ] PDF file opened successfully
- [ ] Text extracted (or limitation noted)
- [ ] Document structure identified
- [ ] Key sections summarized
- [ ] Mode-appropriate output (Note/Teach/Hint)
