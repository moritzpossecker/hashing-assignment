import re

def get_word_list(file_path: str, encoding='utf-8') -> list[str]:
    with open(file_path, 'r', encoding=encoding) as f:
        text = f.read()

    # Sonder- und Satzzeichen mit regulärem Ausdruck entfernen (nur Buchstaben und Zahlen behalten)
    text = re.sub(r'[^a-zA-ZäöüÄÖÜß0-9\s]', '', text)

    # In einzelne Wörter aufteilen
    words = text.split()

    return words
