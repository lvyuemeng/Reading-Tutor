# Typst Handling Rules

## Purpose

Rules for reading, parsing, and explaining Typst markup files.

## When To Use

- User provides a `.typ` file path
- User wants to understand Typst syntax
- User wants to convert Typst to notes

## Instructions

### Basic Typst Processing

1. **Read the file** using file reading tool
2. **Parse markup**: Identify headings, content blocks, functions
3. **Explain syntax**: Translate Typst markup to plain language
4. **Describe output**: How this structured document will render
5. **Generate notes**: Use Note mode to summarize structure

### Key Typst Elements

| Syntax | Meaning | Example |
|--------|---------|---------|
| `= Heading` | Heading level 1 | `= Introduction` |
| `== Heading` | Heading level 2 | `== Background` |
| `[...]` | Content block | `[This is text]` |
| `#function()` | Function call | `#heading("Title")` |
| `#let x = ...` | Variable assignment | `#let title = "Book"` |
| `=>` | Rule/definition | `#figure(=> {...})` |
| `*text*` | Italic | `*emphasis*` |
| `**text**` | Bold | `**strong**` |
| `` `code` `` | Code/raw | `` `let x = 1` `` |
| `$...$` | Math inline | `$x^2 + y^2 = r^2$` |
| `$...$` | Math block | `$ F = ma $` |

### Document Structure

Identify:

- **Metadata**: `#set document(title: "...", author: "...")`
- **Page setup**: `#set page(...)`
- **Text styling**: `#set text(...)`
- **Headings**: Hierarchy levels
- **Figures**: Images, tables, code blocks
- **Bibliography**: `#bibliography("refs.bib")`

### Custom Functions

Parse and explain user-defined functions:

```typst
#let important(body) = text(red, weight: "bold", body)
```

Explain: Creates a function that makes text red and bold.

### Code Blocks

```typst
#{
  let x = 1
  let y = 2
}
```

Explain: Typst code block for scripting/logic.

## Output Format

For Note mode:

```markdown
## Document Structure
- Type: [document/setter type]
- Title: [from metadata]

## Key Elements
- Headings: [list with levels]
- Custom functions: [list with purpose]
- Content blocks: [count]

## Syntax Explained
| Typst | Meaning |
|-------|---------|
| `= X` | Heading 1 |
| `[X]` | Content block |
...

## Render Description
[How the document will appear when compiled]
```

## Semantic Explanation

Don't just translate—explain the **meaning**:

| Instead of... | Say... |
|---------------|--------|
| "Hash heading" | "Heading marker (creates section)" |
| "Number sign equals" | "Level 1 heading" |
| "Square brackets" | "Content block (groups text)" |

## Anti-Patterns

- **Don't compare to LaTeX unnecessarily** — Explain Typst on its own terms
- **Don't skip custom functions** — They're core to Typst
- **Don't ignore code blocks** — They're significant in Typst
QJ|
SN|
### Output Format Rules

**Notes should be appended as comments/code, NOT as page settings.**

1. **For .typ file output**:
- Append notes inside `// ===== NOTES =====` comment block at end
- Or append to location specified by user (e.g., "add after heading X")
- Use `//` for comments explaining equations
- Do NOT generate #set document, #set page, page settings

2. **Equation handling**:
```typst
// ===== NOTES =====
// Key equations from this section:
// E = m c^2  // Einstein's mass-energy equivalence
// F = m a    // Newton's second law
// End of notes
```

3. **For appending**:
- **No location specified**: Append to end of file
- **Location specified**: Insert after specified heading or comment
- **User provides path**: Use absolute/relative path as given

4. **Workspace separation**:
- PDF may be in different location than output file
- Use provided paths exactly as given
- If path doesn't exist, create new file with notes only
## Validation Checklist

- [ ] File read successfully
- [ ] All headings identified with levels
- [ ] Content blocks recognized
- [ ] Custom functions explained
- [ ] Math syntax identified
- [ ] Code blocks handled
- [ ] Semantic meaning conveyed
- [ ] Note mode output structured
