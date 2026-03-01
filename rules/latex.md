# LaTeX Handling Rules

## Purpose

Rules for reading, parsing, and explaining LaTeX document source files.

## When To Use

- User provides a `.tex` file path
- User wants to understand LaTeX syntax
- User wants to convert LaTeX to notes

## Instructions

### Basic LaTeX Processing

1. **Read the file** using file reading tool
2. **Parse structure**: Identify documentclass, packages, sections, equations, figures
3. **Explain syntax**: Translate LaTeX commands to plain language
4. **Describe output**: What will this document look like when compiled?
5. **Generate notes**: Use Note mode to summarize document structure

### Document Structure

Identify the hierarchical components:

```latex
\documentclass{article}     % Document type
\usepackage{amsmath}         % Packages
\title{My Title}           % Metadata
\author{Author Name}

\begin{document}
\maketitle
\section{Introduction}    % Level 1
\subsection{Background}  % Level 2
\subsection{Methods}      % Level 2
\section{Results}
\subsection{Data}
\section{Conclusion}
\end{document}
```

### Key LaTeX Elements

| Command | Meaning | Example |
|---------|---------|---------|
| `\documentclass` | Document type | `{article}`, `{report}`, `{book}`, `{beamer}` |
| `\usepackage` | Load package | `{amsmath}`, `{graphicx}` |
| `\section` | Level 1 heading | `\section{Intro}` |
| `\subsection` | Level 2 heading | `\subsection{Methods}` |
| `\begin{center}` | Center environment | `\begin{center}...\end{center}` |
| `\begin{figure}` | Figure environment | `\begin{figure}...\end{figure}` |
| `\begin{table}` | Table environment | `\begin{table}...\end{table}` |
| `\begin{equation}` | Numbered equation | `\begin{equation}...\end{equation}` |
| `\begin{align}` | Aligned equations | `\begin{align}...\end{align}` |

### Mathematical Notation

| Syntax | Meaning |
|--------|---------|
| `$...$` | Inline math mode |
| `$$...$$` | Display math mode (deprecated, use `\[...\]`) |
| `\[...\]` | Display math mode |
| `\frac{num}{den}` | Fraction |
| `\sqrt{x}` | Square root |
| `\sqrt[n]{x}` | nth root |
| `^{exp}` | Superscript |
| `_{sub}` | Subscript |
| `\sum` | Summation |
| `\int` | Integral |
| `\lim` | Limit |
| `\alpha`, `\beta` | Greek letters |
| `\partial` | Partial derivative |

### Cross-References

| Command | Purpose |
|---------|---------|
| `\label{name}` | Create a reference point |
| `\ref{name}` | Reference (section/equation number) |
| `\pageref{name}` | Reference page number |
| `\cite{key}` | Bibliography citation |
| `\bibliography{file}` | Bibliography source |

### Environments

Common environments to identify:

- **Lists**: `itemize`, `enumerate`, `description`
- **Floats**: `figure`, `table`
- **Math**: `equation`, `align`, `gather`, `multline`
- **Text**: `verbatim`, `quote`, `abstract`

## Output Format

For Note mode:

```markdown
## Document Overview
- Type: [article/report/book/beamer]
- Packages: [list]
- Sections: [count]

## Structure
1. Section: [title]
   - Subsection: [title]
2. ...

## Key Content
- Equations: [list with descriptions]
- Figures: [list with captions]
- Tables: [list]

## Syntax Reference
| LaTeX | Output |
|-------|--------|
| `\section{X}` | Level 1 heading |
| `$x^2$` | Math: x² |
...
```

## Semantic Explanation

Explain commands by **what they do**, not just translation:

| Instead of... | Say... |
|---------------|--------|
| "Backslash section" | "Creates a numbered section heading" |
| "Dollar sign math" | "Switches to math typesetting mode" |
| "Begin figure" | "Starts a floating figure environment" |

## Anti-Patterns

- **Don't explain every command** — Focus on meaningful ones
- **Don't skip packages** — They modify core behavior
- **Don't ignore math** — It's LaTeX's strength
- **Don't treat \ as escape** — It's a command prefix
QR|
QK|
### Output Format Rules

**Notes should be appended as comments/code, NOT as page settings.**

1. **For .tex file output**:
- Append notes inside `% ===== NOTES =====` comment block at end
- Or append to location specified by user (e.g., "add to section X")
- Use `%` for comments explaining equations
- Do NOT generate \documentclass, \begin{document}, page settings

2. **Equation handling**:
```latex
% ===== NOTES =====
% Key equations from this section:
% E = mc^2  % Einstein's mass-energy equivalence
% F = ma    % Newton's second law
% End of notes
```

3. **For appending**:
- **No location specified**: Append to end of file
- **Location specified**: Insert at specified section or comment marker
- **User provides path**: Use absolute/relative path as given

4. **Workspace separation**:
- PDF may be in different location than output file
- Use provided paths exactly as given
- If path doesn't exist, create new file with notes only
## Validation Checklist

- [ ] File read successfully
- [ ] Document class identified
- [ ] Packages listed and explained
- [ ] Section hierarchy mapped
- [ ] Equations identified and explained
- [ ] Environments recognized
- [ ] Cross-references noted
- [ ] Semantic meaning conveyed
- [ ] Note mode output structured
