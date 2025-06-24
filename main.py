import os
import glob
from deep_translator import GoogleTranslator


def main():
    # Determine script’s directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(base_dir, 'input')
    output_dir = os.path.join(base_dir, 'output')

    # Verify input directory
    if not os.path.isdir(input_dir):
        print(f"ERROR: Input directory not found: {input_dir}")
        return

    # Find .txt files in input; require exactly one
    txt_files = glob.glob(os.path.join(input_dir, '*.txt'))
    if not txt_files:
        print(f"ERROR: No .txt files found in {input_dir}")
        return
    if len(txt_files) > 1:
        print("ERROR: Multiple .txt files found in input directory:")
        for path in txt_files:
            print("  ", path)
        print("Please leave only one .txt file in 'input/' and rerun.")
        return

    input_file = txt_files[0]

    # Create output directory if needed
    os.makedirs(output_dir, exist_ok=True)

    # Read non-empty lines from the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]

    # Language targets: key → output file suffix, value → ISO code
    languages = {
        'German': 'de',
        'Portugues': 'pt',
        'French': 'fr'
    }

    # Perform translations and write outputs
    for lang_name, lang_code in languages.items():
        translator = GoogleTranslator(source='en', target=lang_code)
        translations = []
        for text in lines:
            try:
                translated = translator.translate(text)
            except Exception as e:
                # On failure, keep original text
                print(
                    f'Warning: failed to translate "{text}" to {lang_name}: {e}')
                translated = text
            translations.append(translated)

        output_path = os.path.join(output_dir, f'Atlas_{lang_name}.txt')
        with open(output_path, 'w', encoding='utf-8') as out_f:
            out_f.write('\n'.join(translations))

        print(f"✔ Generated: {output_path}")


if __name__ == '__main__':
    main()
