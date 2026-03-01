#!/usr/bin/env python3
"""
PDF Reader for Reading Tutor Skill
Extracts text from PDF files with page number support.
Usage:
    python pdf_reader.py <pdf_path> [pages] [options]
    uv run pdf_reader.py <pdf_path> [pages] [options]

Examples:
    python pdf_reader.py paper.pdf                    # Extract all pages
    uv run pdf_reader.py paper.pdf 
    python pdf_reader.py paper.pdf --page 5           # Extract page 5
    python pdf_reader.py paper.pdf --pages 1-10       # Extract pages 1-10
    python pdf_reader.py paper.pdf --pages 3,7,12     # Extract specific pages

Installation:
    pip install pypdf
"""

import argparse
import sys
import os
from pathlib import Path
from typing import List, Optional, Union

try:
    import pypdf
except ImportError:
    print("Error: pypdf not installed. Run: pip install pypdf", file=sys.stderr)
    sys.exit(1)


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
    parts = pages_str.split(",")

    for part in parts:
        part = part.strip()
        if not part:
            continue

        if "-" in part:
            try:
                start, end = part.split("-", 1)
                start = int(start.strip())
                end = int(end.strip())

                if start > end:
                    print(f"Warning: Invalid range {part}, skipping", file=sys.stderr)
                    continue

                pages.extend(range(start, end + 1))
            except ValueError:
                print(f"Warning: Invalid range format '{part}', skipping", file=sys.stderr)
        else:
            try:
                pages.append(int(part))
            except ValueError:
                print(f"Warning: Invalid page number '{part}', skipping", file=sys.stderr)

    # Convert to 0-indexed and validate
    result = []
    for p in pages:
        if p < 1 or p > max_pages:
            print(f"Warning: Page {p} out of range (1-{max_pages}), skipping", file=sys.stderr)
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
    pdf_path = Path(pdf_path).resolve()

    if not pdf_path.exists():
        print(f"Error: File not found: {pdf_path}", file=sys.stderr)
        sys.exit(1)

    if not pdf_path.is_file():
        print(f"Error: Path is not a file: {pdf_path}", file=sys.stderr)
        sys.exit(1)

    try:
        reader = pypdf.PdfReader(str(pdf_path))
    except Exception as e:
        print(f"Error reading PDF: {e}", file=sys.stderr)
        sys.exit(1)

    total_pages = len(reader.pages)

    if verbose:
        print(f"PDF: {pdf_path.name}", file=sys.stderr)
        print(f"Total pages: {total_pages}", file=sys.stderr)

    # Determine which pages to extract
    if pages is None:
        page_indices = list(range(total_pages))
        if verbose:
            print("Extracting: all pages", file=sys.stderr)
    elif isinstance(pages, int):
        if pages < 1 or pages > total_pages:
            print(f"Error: Page {pages} out of range (1-{total_pages})", file=sys.stderr)
            sys.exit(1)
        page_indices = [pages - 1]
        if verbose:
            print(f"Extracting: page {pages}", file=sys.stderr)
    else:
        page_indices = parse_page_range(pages, total_pages)
        if not page_indices:
            print("Error: No valid pages specified", file=sys.stderr)
            sys.exit(1)
        if verbose:
            print(f"Extracting: pages {[p + 1 for p in page_indices]}", file=sys.stderr)

    # Extract text from selected pages
    extracted_parts = []
    total_chars = 0

    for i, page_idx in enumerate(page_indices):
        try:
            page = reader.pages[page_idx]
            text = page.extract_text() or ""  # Handle None return

            if text.strip():  # Only add separator if there's actual text
                if len(page_indices) > 1:
                    # Add page separator for multi-page extraction
                    extracted_parts.append(f"\n\n--- Page {page_idx + 1} ---\n\n")
                extracted_parts.append(text)

            if verbose:
                chars = len(text)
                total_chars += chars
                print(f"  Page {page_idx + 1}: {chars} characters", file=sys.stderr)

        except Exception as e:
            print(f"Warning: Error extracting page {page_idx + 1}: {e}", file=sys.stderr)
            continue

    full_text = "".join(extracted_parts)

    # Save to file if requested
    if output_file:
        output_path = Path(output_file).resolve()
        try:
            # Create parent directories if they don't exist
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(full_text, encoding="utf-8")
            if verbose:
                print(f"Saved to: {output_path}", file=sys.stderr)
        except Exception as e:
            print(f"Error saving to file: {e}", file=sys.stderr)
            sys.exit(1)

    return full_text


def main():
    parser = argparse.ArgumentParser(
        description="Extract text from PDF files with page support.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )

    parser.add_argument("pdf_path", help="Path to PDF file")

    # Make page and pages mutually exclusive
    page_group = parser.add_mutually_exclusive_group()

    page_group.add_argument(
        "-p", "--page", 
        help="Single page number (1-indexed)", 
        type=int, 
        metavar="N"
    )

    page_group.add_argument(
        "-r", "--pages",
        help='Page range: "1-10" or "1,3,5" or "1-3,5,7"',
        metavar="RANGE",
    )

    parser.add_argument(
        "-o", "--output",
        help="Output file path (default: print to stdout)",
        metavar="FILE",
    )

    parser.add_argument(
        "-v", "--verbose", 
        help="Verbose output", 
        action="store_true"
    )

    parser.add_argument(
        "--version", 
        action="version", 
        version="PDF Reader 1.0"
    )

    args = parser.parse_args()

    # Determine page specification
    if args.page:
        pages = args.page
    elif args.pages:
        pages = args.pages
    else:
        pages = None

    try:
        # Extract text
        text = extract_text_from_pdf(
            args.pdf_path, pages=pages, output_file=args.output, verbose=args.verbose
        )

        # Print to stdout if no output file
        if not args.output:
            if text:
                print(text, end="")
            else:
                print("No text extracted from PDF", file=sys.stderr)
                sys.exit(1)

        # Print summary
        if not args.verbose and text:
            lines = text.count("\n") + 1
            chars = len(text)
            print(f"\n[Extracted: {chars} chars, {lines} lines]", file=sys.stderr)

    except KeyboardInterrupt:
        print("\nInterrupted by user", file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()