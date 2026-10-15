#!/usr/bin/env python3
"""Convert Markdown files to separate A4 PDFs using Pandoc and XeLaTeX."""

import argparse
from pathlib import Path
import shutil
import sys
import tempfile

import pypandoc


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path, help="Markdown files to convert")
    parser.add_argument(
        "--output-dir", type=Path, default=Path("pdf"), help="Output directory (default: pdf)"
    )
    args = parser.parse_args()

    destinations = set()
    for source in args.files:
        if not source.is_file() or source.suffix.lower() not in {".md", ".markdown"}:
            parser.error(f"Not a Markdown file: {source}")
        destination = args.output_dir / f"{source.stem}.pdf"
        if destination.resolve() in destinations:
            parser.error(f"Multiple inputs would produce the same PDF: {destination}")
        destinations.add(destination.resolve())

    if not shutil.which("xelatex"):
        parser.error("XeLaTeX is missing. Install a TeX distribution such as MacTeX.")

    try:
        pypandoc.get_pandoc_path()
        args.output_dir.mkdir(parents=True, exist_ok=True)
        for source in args.files:
            destination = args.output_dir / f"{source.stem}.pdf"
            # Keep an existing PDF intact if conversion fails.
            with tempfile.TemporaryDirectory(dir=args.output_dir) as temporary:
                output = Path(temporary) / "document.pdf"
                pypandoc.convert_file(
                    str(source.resolve()),
                    to="pdf",
                    format="markdown+tex_math_single_backslash",
                    outputfile=str(output),
                    extra_args=[
                        "--standalone",
                        "--pdf-engine=xelatex",
                        f"--resource-path={source.resolve().parent}",
                        "-V", "papersize=a4",
                        "-V", "geometry:margin=20mm",
                        "-V", "fontsize=11pt",
                        "-V", "linestretch=1.12",
                        "-V", "lang=de-DE",
                        "-V", "colorlinks=false",
                    ],
                )
                output.replace(destination)
            print(f"Created {destination}")
    except (OSError, RuntimeError) as error:
        print(f"PDF generation failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
