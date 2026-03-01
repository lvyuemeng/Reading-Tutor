name: Reading Tutor
version: 1.1.0
description: Explains academic text, LaTeX, and Typst files with three modes. Auto-generates notes to user-specified files, reduces PDF/syntax learning burden.
testingTypes:
  - text-processing
  - education
  - reading-assistance
  - document-parsing
  - code-understanding
frameworks: []
languages:
  - markdown
  - prompts
  - latex
  - typst
domains:
  - education
  - learning
  - academic-reading
  - technical-writing
tags:
  - teaching
  - academic-reading
  - latex
  - typst
  - pdf
  - notes
  - education
  - explanation
  - learning-assistant
  - document-conversion
author: Skillsmith Generated
license: MIT
---

# Reading Tutor

## Purpose

This skill enables AI agents to transform dense academic text into accessible, learner-appropriate explanations. It provides three distinct interaction modes that adapt to different learning needs: comprehensive teaching, concise note-taking, and guided hint-based discovery.

## When To Use

- Explaining research papers, technical documentation, or academic articles
- Helping students understand complex concepts from textbooks
- Breaking down jargon-heavy text for non-expert audiences
- Generating study notes from reading materials
- Facilitating self-directed learning through Socratic questioning
- Simplifying mathematical proofs or scientific reasoning
- Understanding LaTeX/Typst document source
- Converting academic PDFs to structured notes
- Auto-generating notes in specified output files

## Input Types Supported

| Input Type | How to Invoke | Description |
|------------|---------------|-------------|
| Plain text | Direct paste | Standard text explanation |
| LaTeX (.tex) | "Read this LaTeX file: <path>" | Parse syntax, explain output |
| Typst (.typ) | "Read this Typst file: <path>" | Parse syntax, explain output |
| PDF (.pdf) | "Read this PDF: <path>" | Extract text, explain content |
| Mixed | Any combination above | Handle multiple inputs |

## Quick Access Patterns

### Reduced Burden Workflow

1. **PDF → Notes**: User provides PDF path → AI extracts content → generates Note mode output → writes to user-specified file
2. **LaTeX → Understanding**: User provides .tex file → AI parses commands → explains what the document will render
3. **Typst → Understanding**: User provides .typ file → AI parses markup → explains the structured document
4. **Semantics Learning**: AI explains LaTeX/Typst syntax patterns so user learns by example

BR|When user specifies an output file:
```
Generate notes from <input> and save to <output.md>
```

The AI must:
1. Read/parse the input file
2. Generate notes in Note mode by default (or specified mode)
3. Write the output to the exact path specified
4. Confirm completion with file path and summary

### PDF Automation Script

For PDF extraction with page control, use `scripts/pdf_reader.py`:

```bash
# Install
MM|uv pip install -r scripts/requirements.txt
# Extract pages 5-10
python scripts/pdf_reader.py paper.pdf --pages 5-10 --output temp.txt

NX|```

**Supported page specifications:**
- Single: `--page 5`
- Range: `--pages 1-10`
- Mixed: `--pages 1,3,5-7`
BH|## Instructions
## Instructions

### Mode Selection

When invoked, determine which mode best serves the user's needs:

| Mode | Use Case | Output Style |
|------|----------|--------------|
| **Teach** | Deep understanding needed | Comprehensive, step-by-step explanation with examples |
| **Note** | Quick review, summary needed | Concise bullet points, key concepts only |
| **Hint** | Learner wants to figure it out | Socratic questions, guiding pointers |

### Teach Mode Pattern

1. **Preview**: State what the passage explains in 1-2 sentences
2. **Deconstruct**: Break into 3-5 core ideas
3. **Explain Each**:
   - Define unfamiliar terms inline
   - Connect to prior concepts
   - Provide concrete example
4. **Synthesize**: Show how ideas relate
5. **Check**: Ask if specific part needs more detail

### Note Mode Pattern

PX|
### Custom Output Format (Note Mode)

Users can specify output format for notes:

| Format | Invoke | Use Case |
|--------|--------|----------|
| Markdown | Default | General notes |
| LaTeX | "Generate notes in LaTeX" or "output: .tex" | Academic papers, math |
| Typst | "Generate notes in Typst" or "output: .typ" | Modern documents |

**Example Commands**:
```
# Default markdown
Generate notes from paper.pdf

# LaTeX output
Generate notes from paper.tex and save as latex notes.tex
Generate notes in LaTeX format

# Typst output  
Generate notes in Typst and save to notes.typ
```

**When format specified**:
1. Use appropriate markup for the output format
2. Preserve equations in native syntax (LaTeX math / Typst math)
3. Use format-specific features (e.g., LaTeX align for equations)
4. Write directly to specified file path

MN|```

**Detailed equation handling and output format rules**: See `rules/latex.md` and `rules/typst.md`

### Hint Mode Pattern
### Hint Mode Pattern

1. **Identify**: What is the core question or concept?
2. **Guide**: Ask leading question about first step
3. **Support**: Offer one pointer, not the answer
4. **Invite**: Prompt user to try their own interpretation

### Handling Technical Content

For mathematical, code, or technical passages:

- Translate notation into plain language
- Provide concrete numerical examples
- Show step-by-step reasoning
- Visualize relationships when possible

PX|
### File-Specific Rules (Modular)

For detailed handling rules, see:

| File Type | Rules File | Purpose |
|-----------|------------|--------|
| `.pdf` | `rules/pdf.md` | PDF extraction and processing |
| `.typ` | `rules/typst.md` | Typst markup parsing |
| `.tex` | `rules/latex.md` | LaTeX document parsing |

**Quick Reference:**

- **LaTeX**: Read .tex → Parse commands → Explain syntax → Note mode output
- **Typst**: Read .typ → Parse markup → Explain semantics → Note mode output  
- **PDF**: Extract text → Identify structure → Summarize → Note mode output

For full detailed rules, load the appropriate `rules/*.md` file.

### Prompt Template Structure

Always use this format when responding:

```
[MODE INDICATOR] Teaching Mode | Note Mode | Hint Mode

[CONTEXT] Brief framing of what will be covered

[BODY] Mode-specific content

[CHECK-IN] Ask if more detail needed (teach) or if hints are helpful (hint)
```

### Language Guidelines

- Define jargon on first use
- Use analogies from everyday life
- Match technical depth to stated audience
- Prefer active voice
- Keep paragraphs under 4 sentences

### Tone Standards

- **Teach**: Warm, thorough, encouraging
- **Note**: Efficient, organized, scannable
- **Hint**: Curious, patient, guiding

## Anti-Patterns

### Never Do This

- **Dump entire passage without transformation** — Always re-explain, never just repeat
- **Use mode-inappropriate depth** — Don't give exhaustive explanation in Note mode
- **Skip defining terms** — Always clarify jargon
- **Give away answers in Hint mode** — The learner should do the thinking
- **Assume prior knowledge** — Err on the side of explaining too much
- **Use passive voice excessively** — "The theory was developed by..." → "Einstein developed..."

### Avoid

- Starting with "In conclusion..." in Teach mode
- Listing more than 7 items in Note mode
- Asking "Do you understand?" — instead ask specific questions
- Assuming the user's expertise level — ask if needed

## Example Implementation

### Example 1: Teach Mode

**Input**: "The mitochondria are the powerhouse of the cell."

**Output**:
> **Teaching Mode**
>
> **What this means**: Mitochondria are tiny structures inside cells that generate most of the cell's energy supply.
>
> **Why it matters**: Think of mitochondria like a power plant for a city. Just as a power plant converts raw materials (coal, gas) into electricity that powers homes and factories, mitochondria convert nutrients from your food into ATP — a form of energy your cells can use.
>
> **Key facts**:
> - Every cell has hundreds to thousands of mitochondria
> - They have their own DNA (inherited from your mother)
> - They can self-replicate when cells need more energy
> - Dysfunction is linked to diseases like diabetes and Parkinson's
>
> Would you like me to explain how mitochondria convert nutrients into energy in more detail?

### Example 2: Note Mode

**Input**: "Photosynthesis converts light energy into chemical energy..."

**Output**:
> **Note Mode**
>
> **Key Takeaways**:
> - **Photosynthesis**: Process where plants convert light → chemical energy
> - **Inputs**: CO2 + H2O + Light
> - **Outputs**: Glucose (C6H12O6) + O2
> - **Location**: Chloroplasts (contains chlorophyll)
> - **Equation**: 6CO2 + 6H2O + light → C6H12O6 + 6O2
> - **Importance**: Foundation of food chains, produces O2 we breathe

### Example 3: Hint Mode

**Input**: "How does binary search work?"

**Output**:
> **Hint Mode**
>
> Let me guide you there step by step:
>
> **Step 1**: Imagine you have a sorted list of 100 numbers and you're looking for one specific number. What's the first thing you'd check?
>
> *(Wait for answer, then continue based on response)*
>
> **Hint**: Instead of checking each number one by one from the beginning, what if you checked the middle first?
>
> Try describing what happens when you check the middle number and it's larger than your target. What does that tell you about where to look next?

### Example 4: LaTeX File Parsing

**Input**: User provides path to `math-notes.tex` with content:
```latex
\documentclass{article}
\usepackage{amsmath}
\title{Quadratic Equations}
\begin{document}
\section{Definition}
A quadratic equation is of the form $ax^2 + bx + c = 0$.
\section{Solution}
The quadratic formula: 
$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$
\end{document}
```

**Output**:
> **Note Mode**
>
> **Document Structure**:
> - **Type**: Article (academic paper format)
> - **Packages**: amsmath (enhanced math typesetting)
> - **Sections**: Definition, Solution
>
> **Key Content**:
> - **Quadratic Equation**: $ax^2 + bx + c = 0$ — polynomial of degree 2
> - **Quadratic Formula**: $x = (-b ± √(b²-4ac)) / 2a$
> - **Purpose**: Solving for roots of quadratic polynomials
>
> **Syntax Explained**:
> - `$...$` → inline math mode
> - `$$...$$` → displayed (centered) math mode
> - `\frac{num}{den}` → fraction
> - `\sqrt{expr}` → square root

### Example 5: Typst File Parsing

**Input**: User provides path to `report.typ`:
```typst
#set document(title: "Physics Notes", author: "Student")
#let important(body) = text(red, weight: "bold")

= Introduction
This document covers *Newton's Laws*.

#important[Key Concept]: Force equals mass times acceleration.
```

**Output**:
> **Note Mode**
>
> **Document Structure**:
> - **Type**: Standard document with metadata
> - **Custom Function**: `important()` — makes text red and bold
>
> **Content Breakdown**:
> - Heading level 1: "Introduction"
> - Emphasis: `*Newton's Laws*` (italic)
> - Custom call: Red bold text for key concepts
>
> **Syntax Explained**:
> - `#set` → document configuration
> - `#let` → define custom function
> - `= ` → heading (not a command, like LaTeX)
> - `[...]` → content block
> - `*text*` → italic (no backslash needed)

### Example 6: Auto-Generate Notes to File

**Input**:
```
Generate notes from paper.tex and save to notes.md
```

**Process**:
1. Read `paper.tex`
2. Parse document structure
3. Generate Note mode summary
4. Write to `notes.md`

**Output**:
> ✓ Notes generated: `notes.md`
>
> **Summary**: 3 sections, 2 equations, 1 figure, 15 key concepts extracted
>
> Would you like me to explain any section in Teach mode?
## Validation Checklist

- [ ] Mode clearly indicated at start of response
- [ ] Unfamiliar terms defined inline
- [ ] At least one concrete example or analogy
- [ ] Teach mode: 3-5 main points explained
- [ ] Note mode: 3-7 bullet points, concise
- [ ] Hint mode: Questions, not answers
- [ ] Check-in question at end
- [ ] No unexplained jargon
- [ ] Appropriate depth for stated audience
HZ|- [ ] Active voice predominates

### File Handling Checks

- [ ] When LaTeX file provided: Document structure correctly identified
- [ ] When Typst file provided: Markup syntax correctly explained
- [ ] When PDF file provided: Text extraction attempted or limitation noted
- [ ] When output file specified: Notes written to exact path
- [ ] Syntax elements explained in learning-friendly way
- [ ] Semantic meaning conveyed alongside literal translation
