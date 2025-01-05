import argparse
import os
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def create_client():
    """
    Create OpenAI client based on configuration
    """
    api_key = os.getenv("OPENAI_API_KEY")
    base_url = os.getenv("OPENAI_BASE_URL")
    
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable is not set")
    
    if not base_url:
        # Default OpenAI endpoint
        return OpenAI(api_key=api_key)
    
    # Custom endpoint (e.g., Azure, Deepseek, etc.)
    return OpenAI(
        api_key=api_key,
        base_url=base_url
    )

# Initialize OpenAI client
try:
    client = create_client()
except Exception as e:
    print(f"Error initializing OpenAI client: {str(e)}")
    exit(1)

def translate_text(text, source_lang, target_lang):
    """
    Translate text using OpenAI API while preserving Markdown formatting
    """
    system_prompt = f"""You are a professional translator. Translate the following Markdown text from {source_lang} to {target_lang}.
    Important rules:
    1. Preserve ALL Markdown syntax and formatting exactly as is
    2. Keep all code blocks, URLs, and special characters unchanged
    3. Only translate the actual content text
    4. Maintain the same line breaks and paragraph structure
    5. Do not translate content within code blocks (surrounded by ``` or `)
    """
    
    try:
        response = client.chat.completions.create(
            model=os.getenv("MODEL"),
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error during translation: {str(e)}")
        return None

def process_file(input_file, source_lang, target_langs):
    """
    Process the input Markdown file and create translated versions
    """
    # Read input file
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading input file: {str(e)}")
        return

    # Get the base filename and directory
    input_path = Path(input_file)
    base_name = input_path.stem
    file_dir = input_path.parent

    # Process each target language
    for target_lang in target_langs:
        # Translate content
        translated_content = translate_text(content, source_lang, target_lang)
        if translated_content is None:
            print(f"Failed to translate to {target_lang}")
            continue

        # Create output filename
        output_file = file_dir / f"{base_name}_{target_lang}.md"
        
        # Write translated content
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(translated_content)
            print(f"Successfully created {output_file}")
        except Exception as e:
            print(f"Error writing output file for {target_lang}: {str(e)}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Translate Markdown files while preserving formatting')
    parser.add_argument('input_file', help='Input Markdown file to translate')
    parser.add_argument('--source', required=True, help='Source language code (e.g., CN, EN, JP)')
    parser.add_argument('--target', required=True, help='Comma-separated list of target language codes')

    # Parse arguments
    args = parser.parse_args()

    # Split target languages and remove any whitespace
    target_langs = [lang.strip() for lang in args.target.split(',')]

    # Check if input file exists
    if not os.path.exists(args.input_file):
        print(f"Error: Input file '{args.input_file}' does not exist")
        return

    # Process the file
    process_file(args.input_file, args.source, target_langs)

if __name__ == "__main__":
    main()