[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

[简体中文](docs/README_CN.md) | [日语](docs/README_JP.md)

# AI-markdown-translator
Translate the markdown into various languages and create new markdown files for each.

## Features
- Preserves all Markdown formatting and structure during translation
- Supports multiple target languages in a single run
- Uses OpenAI's GPT-3.5-turbo model for high-quality translations
- Maintains code blocks, URLs, and special characters unchanged
- Creates separate output files for each target language

## Prerequisites
- Python 3.6 or higher
- OpenAI API key or any large language model that supports the OpenAI interface

## Installation

1. Clone the repository:
```bash
git clone https://github.com/imhuiye/AI-markdown-translator.git
cd AI-markdown-translator
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root directory with your OpenAI API credentials:
```
OPENAI_API_KEY=your_api_key_here
OPENAI_BASE_URL=https://api.openai.com/v1
MODEL=gpt-3.5-turbo
```

## Usage

The basic command syntax is:
```bash
python translator.py <input_file> --source <source_lang> --target <target_langs>
```

Parameters:
- `input_file`: Path to the Markdown file you want to translate
- `--source`: Source language code (e.g., CN for Chinese, EN for English)
- `--target`: Comma-separated list of target language codes (e.g., EN,JP,KR)

Example:
```bash
python translator.py README.md --source CN --target EN,JP
```

This will create:
- `README_EN.md` (English translation)
- `README_JP.md` (Japanese translation)

## Language Codes
Common language codes:
- EN: English
- CN: Chinese
- JP: Japanese
- KR: Korean
- FR: French
- DE: German
- ES: Spanish

## Notes
- The translation preserves all Markdown syntax, including headers, lists, code blocks, links, and formatting
- Content within code blocks (surrounded by ``` or `) will not be translated
- Make sure your OpenAI API key has sufficient credits for the translation

## Error Handling
The script includes error handling for:
- Invalid file paths
- API errors
- File reading/writing issues
- Invalid language codes

If you encounter any issues, check the error message in the console output for more details.
