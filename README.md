# AI-Powered Multi-language Translator

This project is a text-based AI-powered multi-language translator using the transformers library. It supports translation between English, German, and Spanish using pre-trained MarianMT models.

## Features

- Translate text between English, German, and Spanish.
- Handle input in different cases (lowercase, uppercase, title case).
- Support for common language abbreviations (e.g., eng, ger, spa).

## Requirements

- Python 3.6 or later
- transformers library
- torch library

## Installation

1. Clone the repository:
    sh
    git clone https://github.com/your-username/ai-multi-language-translator.git
    cd ai-multi-language-translator
    

2. Install the required libraries:
    sh
    pip install transformers torch
    

## Usage

Run the main script to start the interactive translation tool:
sh
python main.py


### Example Workflow

1. *Starting the Program*: Run python main.py to start the translator.
2. *Enter Source Language*: Input the source language (English, German, Spanish) or its abbreviation (eng, ger, spa).
3. *Enter Target Language*: Input the target language (English, German, Spanish) or its abbreviation (eng, ger, spa).
4. *Enter Text for Translation*: Input the text you want to translate. The translation will be displayed with the proper case.

### Sample Session

plaintext
Welcome to the AI-powered Multi-language Translator!

Enter source language (English|German|Spanish) or 'exit': eng
Enter target language (English|German|Spanish) or 'exit': ger
Enter a sentence to translate, 'change' to change languages, or 'exit': hello
Source language (English): hello
Translated language (German): hallo
Enter a sentence to translate, 'change' to change languages, or 'exit': exit


## Code Overview

### main.py

The main script contains the following key functions:

- load_model_and_tokenizer(model_name): Loads and caches the MarianMT model and tokenizer.
- match_case(original, translated): Matches the case of the translated text to the original input text.
- translate_sentence(sentence, from_lang, to_lang): Translates the given sentence from the source language to the target language.
- get_full_language_name(abbreviation_or_name): Converts language abbreviations to full language names.
- main(): The main function to handle user interaction and translation workflow.

### Error Handling

- The program checks for valid language inputs and provides feedback for unsupported language pairs.
- The translation function handles unknown words by leveraging the AI model's contextual understanding and subword tokenization.

## Contributing

Feel free to submit issues, fork the repository, and send pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
