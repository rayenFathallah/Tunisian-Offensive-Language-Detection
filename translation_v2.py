from deep_translator import GoogleTranslator
import re

# Step 1: Define the transliteration mapping
latin_to_arabic_map = {
    "ch": "ش",
    "gh": "غ",
    "kh": "خ",
    "dh": "ذ",
    "th": "ث",
    "9": "ق",
    "8": "غ",
    "7": "ح",
    "ta": "ط",
    "5": "خ",
    "4": "ظ",
    "3": "ع",
    "2": "ء",
    "a": "ا",
    "b": "ب",
    "t": "ت",
    "j": "ج",
    "h": "ه",
    "d": "د",
    "r": "ر",
    "z": "ز",
    "s": "س",
    "f": "ف",
    "q": "ق",
    "k": "ك",
    "l": "ل",
    "m": "م",
    "n": "ن","w":"و",
    "ou": "و","o": "و",
    "y": "ي",
    "aa":"ع",
    "i": "ي",
    # Optional: Tunisian-specific pronunciation of "e"
}

# Step 2: Function to transliterate text with complex rules
def transliterate_to_arabic(text):
    """
    Transliterates Tunisian Arabizi to Arabic script with advanced processing.
    Args:
        text (str): Input text in Latin characters.
    Returns:
        str: Transliterated text in Arabic script.
    """
    # Handle specific complex patterns first
    text = re.sub(r"bch", "باش", text)  # Example: bch -> باش
    text = re.sub(r"m3", "مع", text)    # Example: m3 -> مع
    text = re.sub(r"3ala", "على", text) # Example: 3ala -> على
    text = re.sub(r"fiha", "فيها", text) # Example: fiha -> فيها

    # Sort keys by length to handle multi-character mappings first (e.g., "ch" before "c")
    sorted_map = sorted(latin_to_arabic_map.items(), key=lambda x: -len(x[0]))

    for latin, arabic in sorted_map:
        text = re.sub(re.escape(latin), arabic, text)

    # Remove any remaining Latin characters
    text = re.sub(r"[a-zA-Z0-9]", "", text)

    # Normalize spacing and punctuation
    text = re.sub(r"\s+", " ", text).strip()  # Remove extra spaces
    text = re.sub(r"\s*([\.,!?؛])\s*", r"\1", text)  # Normalize punctuation spacing

    return text
def remove_emojis(text):
    emoji_pattern = re.compile(
        "[\U0001F600-\U0001F64F"
        "\U0001F300-\U0001F5FF"
        "\U0001F680-\U0001F6FF"
        "\U0001F700-\U0001F77F"
        "\U0001F780-\U0001F7FF"
        "\U0001F800-\U0001F8FF"
        "\U0001F900-\U0001F9FF"
        "\U0001FA00-\U0001FA6F"
        "\U0001FA70-\U0001FAFF"
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
        "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

# Step 3: Define the translation function and combine approaches
def translate_and_convert_to_arabic(text):
    """
    Translates French text to Arabic and converts non-Arabic characters to Arabic using transliteration if necessary.
    Args:
        text (str): Input text in French.
    Returns:
        str: Translated text in Arabic.
    """
    text=text.lower()
    try:
        text = remove_emojis(text)
        # Step 3.1: Translate using GoogleTranslator
        translator = GoogleTranslator(source='fr', target='ar')
        arabic_translation = translator.translate(text)

        # Step 3.2: Check if the translation contains any non-Arabic characters
        if any(c not in "اأببتثجحخدذرزسشصضطظعغفقكلمنهوىي" for c in arabic_translation):
            # If there are non-Arabic characters, apply transliteration
            arabic_translation = transliterate_to_arabic(arabic_translation)

        return arabic_translation
    except Exception as e:
        return f"Error in translation: {e}"

