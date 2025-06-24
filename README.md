# Atlas Text Translator

**Atlas Text Translator** is a minimal Python utility that reads an English `.txt` file (one phrase per line) from an `input/` folder and generates translated `.txt` files—one per target language—in an `output/` folder. You can add or remove languages simply by editing a single dictionary in the script.

## 📂 Project Structure

your_project/
├── main.py
├── input/ # Put exactly ONE .txt file here (English phrases)
│ └── phrases.txt
└── output/ # Translated files will appear here
├── Atlas_German.txt
├── Atlas_Portugues.txt
└── Atlas_French.txt


## ⚙️ Requirements

- Python 3.6+
- **deep-translator** library

Install via UV:

```bash
uv run main.py 
# Dependencies will be automatically installed.

🚀 How It Works
Input
Place a single .txt file with English phrases (one per line) into input/.

Run
From your project root, execute:

bash
Copiar
Editar
uv run python main.py
The script will:

Detect the one .txt file in input/

Read each non-empty line

Translate into every language defined in the languages dict

Write one Atlas_<Language>.txt file per target language into output/

Output
Check output/ for your translated files.

✅ Adding or Removing Languages
Open main.py and locate the languages dictionary:

python
Copiar
Editar
languages = {
    'German': 'de',
    'Portugues': 'pt',
    'French': 'fr'
}
Add a language: add an entry 'YourLangName': 'xx', where xx is the ISO 639-1 code.

Remove a language: delete its entry.

Example—adding Spanish and Italian:

python
Copiar
Editar
languages = {
    'German': 'de',
    'Portugues': 'pt',
    'French': 'fr',
    'Spanish': 'es',
    'Italian': 'it'
}
Save and rerun main.py. New Atlas_Spanish.txt and Atlas_Italian.txt will appear in output/.

