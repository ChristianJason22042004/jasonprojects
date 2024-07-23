from transformers import MarianMTModel, MarianTokenizer

# Dictionary to map language pairs to their corresponding model names
model_names = {
    ('English', 'German'): 'Helsinki-NLP/opus-mt-en-de',
    ('German', 'English'): 'Helsinki-NLP/opus-mt-de-en',
    ('English', 'Spanish'): 'Helsinki-NLP/opus-mt-en-es',
    ('Spanish', 'English'): 'Helsinki-NLP/opus-mt-es-en'
}

# Dictionary to map abbreviations to full language names
abbreviation_map = {
    'eng': 'English',
    'ger': 'German',
    'spa': 'Spanish'
}

# Dictionaries to store loaded models and tokenizers
models, tokenizers = {}, {}

def load_model_and_tokenizer(model_name):
    # Load the model and tokenizer if not already loaded
    if model_name not in models:
        tokenizer = MarianTokenizer.from_pretrained(model_name)
        model = MarianMTModel.from_pretrained(model_name)
        models[model_name], tokenizers[model_name] = model, tokenizer

    return models[model_name], tokenizers[model_name]

def translate_sentence(sentence, from_lang, to_lang):
    # Get the model name for the given language pair
    model_name = model_names.get((from_lang, to_lang))

    if not model_name:
        return "Unsupported language pair."

    # Load the model and tokenizer
    model, tokenizer = load_model_and_tokenizer(model_name)

    # Tokenize the input sentence
    inputs = tokenizer(sentence, return_tensors="pt")

    # Generate the translation
    translated = model.generate(**inputs)

    # Decode and return the translated sentence
    return tokenizer.batch_decode(translated, skip_special_tokens=True)[0]

def get_full_language_name(abbreviation_or_name):
    # Convert abbreviations to full language names
    return abbreviation_map.get(abbreviation_or_name.lower(), abbreviation_or_name.title())

def main():
    print("\033[1;34mWelcome to the AI-powered Multi-language Translator!\033[0m")

    while True:
        # Get source language from user and format it
        from_lang = input("Enter source language (English|German|Spanish) or 'exit': ").strip()
        from_lang = get_full_language_name(from_lang)

        if from_lang.lower() == 'exit':
            break  # Exit the loop and end the program

        if from_lang not in ['English', 'German', 'Spanish']:
            print("Invalid source language.")
            continue

        # Get target language from user and format it
        to_lang = input("Enter target language (English|German|Spanish) or 'exit': ").strip()
        to_lang = get_full_language_name(to_lang)

        if to_lang.lower() == 'exit':
            break  # Exit the loop and end the program

        if to_lang not in ['English', 'German', 'Spanish'] or from_lang == to_lang:
            print("Invalid target language.")
            continue

        while True:
            # Get sentence to translate from user
            sentence = input("Enter a sentence to translate, 'change' to change languages, or 'exit': ").strip()

            if sentence.lower() == 'change':
                break  # Break the inner loop to change languages

            if sentence.lower() == 'exit':
                return  # Exit the function and end the program

            # Translate the sentence
            translated = translate_sentence(sentence, from_lang, to_lang)

            # Print the source and translated sentences with colors
            print(f"\033[1;32mSource language ({from_lang}):\033[0m {sentence}")
            print(f"\033[1;31mTranslated language ({to_lang}):\033[0m {translated}")

if __name__ == "__main__":
    main()