# Atlas Text Translator

A lightweight Python script that translates an English text file into multiple languages. Provide one `.txt` file inside `input/` and the script will create one translated file per language inside `output/`.

## Project structure

```bash
your_project/
├── main.py
├── input/
│   └── your_phrases.txt     # one phrase per line, English
└── output/                  # created automatically
```

## Requirements

- Python 3.10+
- `deep-translator` library

The project uses [uv](https://github.com/astral-sh/uv) to manage dependencies, but you can install them with `pip` as well.

## Running

1. Place exactly one `.txt` file with your English phrases inside `input/`.
2. From the project root, run:

```
uv run python main.py
```

The first run will install dependencies and start the script. Each translated file will be named `Atlas_<Language>.txt` and saved in `output/`.

## Customizing Languages

Open `main.py` and edit the `languages` dictionary:

```python
languages = {
    'German': 'de',
    'Portugues': 'pt',
    'French': 'fr',
}
```

The key is the name that will appear in the output filename; the value is the ISO 639‑1 language code used for translation. Add or remove entries as needed.

## Example

With the default settings and an input file containing:

```
Hello
How are you?
```

the script will produce:

```
output/Atlas_German.txt
output/Atlas_Portugues.txt
output/Atlas_French.txt
```

Each file contains the translated lines in the respective language.

---

This tool is intended for small batches of phrases. It uses the public Google Translate service through `deep-translator`, so be mindful of usage limits.
