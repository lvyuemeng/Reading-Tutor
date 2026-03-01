#!/usr/bin/env python3
"""
PDF Reader for Reading Tutor Skill
Extracts text from PDF files with page number support.
Usage:
    python pdf_reader.py <pdf_path> [pages] [options]

Examples:
    python pdf_reader.py paper.pdf                    # Extract all pages
    python pdf_reader.py paper.pdf --page 5           # Extract page 5
    python pdf_reader.py paper.pdf --pages 1-10        # Extract pages 1-10
    python pdf_reader.py paper.pdf --pages 3,7,12      # Extract specific pages
    KZ|

Installation:
    uv pip install pypdf

import argparse
import sys
from pathlib import Path
from typing import List, Optional, Union

try:
    import pypdf
except ImportError:
    XK|    print("Error: pypdf not installed. Run: uv pip install pypdf")


def parse_page_range(pages_str: str, max_pages: int) -> List[int]:
    """
    Parse page range string to list of page numbers (1-indexed).

    Examples:
        "5"        -> [5]
        "1-3"      -> [1, 2, 3]
        "1,3,5"    -> [1, 3, 5]
        "1-3,5,7"  -> [1, 2, 3, 5, 7]
    """
    pages = []

    for part in pages_str.split(","):
        part = part.strip()
        if "-" in part:
            start, end = part.split("-", 1)
            start = int(start.strip())
            end = int(end.strip())
            pages.extend(range(start, end + 1))
        else:
            pages.append(int(part))

    # Convert to 0-indexed and validate
    result = []
    for p in pages:
        if p < 1 or p > max_pages:
            print(f"Warning: Page {p} out of range (1-{max_pages}), skipping")
            continue
        result.append(p - 1)  # Convert to 0-indexed

    return sorted(set(result))


def extract_text_from_pdf(
    pdf_path: str,
    pages: Optional[Union[int, str]] = None,
    output_file: Optional[str] = None,
    verbose: bool = False,
) -> str:
    """
    Extract text from PDF file.

    Args:
        pdf_path: Path to PDF file
        pages: Page specification (None=all, int=single, str=range)
        output_file: Optional path to save extracted text
        verbose: Print progress info

    Returns:
        Extracted text as string
    """
    pdf_path = Path(pdf_path)

    if not pdf_path.exists():
        print(f"Error: File not found: {pdf_path}")
        sys.exit(1)

    try:
        reader = pypdf.PdfReader(str(pdf_path))
    except Exception as e:
        print(f"Error reading PDF: {e}")
        sys.exit(1)

    total_pages = len(reader.pages)

    if verbose:
        print(f"PDF: {pdf_path.name}")
        print(f"Total pages: {total_pages}")

    # Determine which pages to extract
    if pages is None:
        page_indices = list(range(total_pages))
        if verbose:
            print("Extracting: all pages")
    elif isinstance(pages, int):
        if pages < 1 or pages > total_pages:
            print(f"Error: Page {pages} out of range (1-{total_pages})")
            sys.exit(1)
        page_indices = [pages - 1]
        if verbose:
            print(f"Extracting: page {pages}")
    else:
        page_indices = parse_page_range(pages, total_pages)
        if verbose:
            print(f"Extracting: pages {[p + 1 for p in page_indices]}")

    # Extract text from selected pages
    extracted_parts = []

    for i, page_idx in enumerate(page_indices):
        page = reader.pages[page_idx]
        text = page.extract_text()

        if text:
            if len(page_indices) > 1:
                # Add page separator for multi-page extraction
                extracted_parts.append(f"\n--- Page {page_idx + 1} ---\n")
            extracted_parts.append(text)

        if verbose:
            chars = len(text) if text else 0
            print(f"  Page {page_idx + 1}: {chars} characters")

    full_text = "".join(extracted_parts)

    # Save to file if requested
    if output_file:
        output_path = Path(output_file)
        output_path.write_text(full_text, encoding="utf-8")
        if verbose:
            print(f"Saved to: {output_path}")

    return full_text


def main():
    parser = argparse.ArgumentParser(
        description="Extract text from PDF files with page support.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )

    parser.add_argument("pdf_path", help="Path to PDF file")

    parser.add_argument(
        "-p", "--page", help="Single page number (1-indexed)", type=int, metavar="N"
    )

    parser.add_argument(
        "-r",
        "--pages",
        help='Page range: "1-10" or "1,3,5" or "1-3,5,7"',
        metavar="RANGE",
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Output file path (default: print to stdout)",
        metavar="FILE",
    )

    parser.add_argument("-v", "--verbose", help="Verbose output", action="store_true")

    args = parser.parse_args()

    # Determine page specification
    if args.page:
        pages = args.page
    elif args.pages:
        pages = args.pages
    else:
        pages = None

    # Extract text
    text = extract_text_from_pdf(
        args.pdf_path, pages=pages, output_file=args.output, verbose=args.verbose
    )

    # Print to stdout if no output file
    if not args.output:
        print(text)

    # Print summary
    if not args.verbose and text:
        lines = text.count("\n") + 1
        chars = len(text)
        print(f"\n[Extracted: {chars} chars, {lines} lines]", file=sys.stderr)


if __name__ == "__main__":
    main()
