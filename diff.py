#!/usr/bin/env python3

import argparse
import re
import subprocess
import tempfile
from pathlib import Path

CSS = """
<style>
body {
    font-family: sans-serif;
    line-height: 1.5;
}

ins,
ins * {
    background: #d4f8d4;
    text-decoration: none;
}

del,
del * {
    background: #ffd6d6;
    text-decoration: line-through;
}
</style>

"""

parser = argparse.ArgumentParser(
    description="Erzeugt einen HTML-Diff zweier Markdown-Dateien."
)

parser.add_argument("old", help="Pfad zur alten Markdown-Datei")
parser.add_argument("new", help="Pfad zur neuen Markdown-Datei")
parser.add_argument("-o", "--output", default="diff.html", help="Ausgabedatei")

args = parser.parse_args()

FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


def read_markdown(path):
    text = Path(path).read_text(encoding="utf-8")
    match = FRONTMATTER.match(text)
    if not match:
        return text

    body = text[match.end() :]
    title = re.search(r"^title:\s*(.+?)\s*$", match.group(1), re.MULTILINE)
    if not title:
        return body

    heading = title.group(1).strip("\"'")
    return f"# {heading}\n\n{body}"


with tempfile.TemporaryDirectory() as tmp:
    tmp = Path(tmp)

    old_html = tmp / "old.html"
    new_html = tmp / "new.html"

    subprocess.run(
        [
            "pandoc",
            "-f",
            "commonmark",
            "-o",
            str(old_html),
        ],
        input=read_markdown(args.old),
        text=True,
        encoding="utf-8",
        check=True,
    )

    subprocess.run(
        [
            "pandoc",
            "-f",
            "commonmark",
            "-o",
            str(new_html),
        ],
        input=read_markdown(args.new),
        text=True,
        encoding="utf-8",
        check=True,
    )

    result = subprocess.run(
        [
            "wdiff",
            "-w",
            "<ins>",
            "-x",
            "</ins>",
            "-y",
            "<del>",
            "-z",
            "</del>",
            str(new_html),
            str(old_html),
        ],
        capture_output=True,
        text=True,
    )

    html = CSS + result.stdout

    Path(args.output).write_text(html, encoding="utf-8")

print(f"Diff erfolgreich erstellt: {args.output}")
