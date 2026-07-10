# Official documents for Animexx e. V

All official documents for the Animexx e. V. can be found here.

## Local project setup

### Dependencies

- Docker (Desktop)
- Visual Studio Code with Dev Containers extension.

**Open the project with a [dev container](https://code.visualstudio.com/docs/devcontainers/containers).**

## Local preview

To create a local preview, run the following command:

```sh
zensical serve
```

**It is important to activate the environment for the terminal before running the command.**

## Export Diff as Document

Use the `diff.py` script to generate an HTML document highlighting the differences between two Markdown files. The script first converts both files to HTML using `pandoc` and then compares them with `wdiff`. Additions are highlighted in green, while deletions are highlighted in red.

### Prerequisites

The following tools must be installed and available in your `PATH`:

- [pandoc](https://pandoc.org)
- `wdiff`

### Usage

```bash
python diff.py ./OLD.md ./NEW.md
```

The generated HTML file can be opened in any web browser and printed or exported as a PDF.
