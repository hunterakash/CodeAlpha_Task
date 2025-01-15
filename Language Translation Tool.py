pip install requests


import requests

def display_languages():
    """
    Display a predefined list of languages and their codes for translation.
    """
    print("\nAvailable Languages:")
    languages = {
        'en': 'English',
        'es': 'Spanish',
        'fr': 'French',
        'de': 'German',
        'zh-Hans': 'Chinese (Simplified)',
        'ja': 'Japanese',
        'ko': 'Korean',
    }
    for code, name in languages.items():
        print(f"{code}: {name}")
    print()

def translate_text(text, src_lang, dest_lang, subscription_key, endpoint):
    """
    Translate text using Microsoft Translator API.

    Args:
        text (str): The text to translate.
        src_lang (str): Source language code.
        dest_lang (str): Target language code.
        subscription_key (str): Azure Translator subscription key.
        endpoint (str): Translator API endpoint URL.

    Returns:
        str: Translated text.
    """
    path = '/translate'
    url = endpoint + path
    params = {
        'api-version': '3.0',
        'from': src_lang,
        'to': dest_lang,
    }
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-Type': 'application/json',
    }
    body = [{'text': text}]

    try:
        response = requests.post(url, params=params, headers=headers, json=body)
        response.raise_for_status()
        result = response.json()
        return result[0]['translations'][0]['text']
    except Exception as e:
        return f"Error: {e}"

def main():
    """
    Main function for the language translation tool.
    """
    # Replace these with your actual Azure Translator subscription key and endpoint.
    subscription_key = "YOUR_SUBSCRIPTION_KEY"
    endpoint = "https://api.cognitive.microsofttranslator.com"

    print("Welcome to the Language Translation Tool!")

    while True:
        print("\nMenu:")
        print("1. View available languages")
        print("2. Translate text")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            display_languages()
        elif choice == '2':
            text = input("\nEnter the text to translate: ").strip()
            src_lang = input("Enter the source language code (or type 'auto' to detect): ").strip()
            dest_lang = input("Enter the target language code: ").strip()

            translated_text = translate_text(text, src_lang, dest_lang, subscription_key, endpoint)
            print(f"\nTranslated Text: {translated_text}\n")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



INPUT:
    Enter the text to translate: Hello, how are you?
    Enter the source language code (or type 'auto' to detect): en
    Enter the target language code: es



OUTPUT:
    Translated Text: Hola, ¿cómo estás?
