from googletrans import Translator

translator = Translator()

# Get input
text = input("Enter text to translate: ")
target_lang = input("Enter target language code (e.g. hi, fr, es): ")

# Translate
translated = translator.translate(text, dest=target_lang)

print("\nTranslated Text:")
print(translated.text)
