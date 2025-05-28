import os
import base64
from google import genai
from google.genai import types
from IPython.display import display

GEMINI_API_KEY = 'REPLACE_THIS_WITH_YOUR GEMINI_API_KEY'
os.environ['GEMINI_API_KEY'] = GEMINI_API_KEY

def generate(user_input):
    client = genai.Client(
        api_key=os.environ.get('GEMINI_API_KEY'),
    )

    model = 'gemma-3-1b-it'
    contents = [
        types.Content(
            role='user',
            parts=[
                types.Part.from_text(text=user_input),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type='text/plain',
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config
    ):
        print(chunk.text, end='')
    print()

if __name__ == '__main__':
    print('Connection to Gemini API established. Type "break" to disconnect.')
    print()
    while True:
        user_input = input('User: ')
        if user_input.lower() == 'break':
            print()
            print('Disconnected from Gemini API.')
            break
        print('Gemini: ', end='')
        generate(user_input)
