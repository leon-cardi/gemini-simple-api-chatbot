import os
import base64
from google import genai
from google.genai import types
from IPython.display import display

GEMINI_API_KEY = 'REPLACE_THIS_WITH_YOUR GEMINI_API_KEY'
os.environ['GEMINI_API_KEY'] = GEMINI_API_KEY

def generate_with_context(user_input, chat_history):
    client = genai.Client(
        api_key=os.environ.get('GEMINI_API_KEY'),
    )

    model = 'gemma-3-1b-it'
    
    chat_history.append(types.Content(
        role='user',
        parts=[types.Part.from_text(text=user_input)],
    ))
    
    generate_content_config = types.GenerateContentConfig(
        response_mime_type='text/plain',
    )

    full_response = ""
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=chat_history,
        config=generate_content_config
    ):

        if chunk.text is not None:
            full_response += chunk.text
            print(chunk.text, end='')
    print()
    
    if full_response: 
        chat_history.append(types.Content(
            role='model',
            parts=[types.Part.from_text(text=full_response)],
        ))
    
    return chat_history

if __name__ == '__main__':
    print('Connection to Gemini API established. Type "logout" to disconnect.')
    print()
    
    chat_history = []
    
    while True:
        user_input = input('User: ')
        if user_input.lower() == 'logout':
            print()
            print('Disconnected from Gemini API.')
            break
        print('Gemini: ', end='')
        
        chat_history = generate_with_context(user_input, chat_history)
