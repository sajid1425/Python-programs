import openai
import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyCMhU8chE2IPYU5tuz8hMv_cRzJEoYTgj4"
OPENAI_API_KEY = "AIzaSyDbGcmB8sfMhXP3tU6WjLlyrb-s3gcb7po" 

# Initialize OpenAI API
openai.api_key = OPENAI_API_KEY
# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

def get_openai_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error with OpenAI API: {e}"

def get_gemini_response(prompt):
    try:
        model = genai.GenerativeModel(
            model_name='gemini-1.5-pro',
            tools='code_execution'
        )
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error with Gemini API: {e}"


current_model = "OpenAI"
print("Welcome to the terminal-based chatbot!")
print("You can switch between OpenAI and Gemini by typing 'switch'. Type 'quit' to exit.")
    
while True:
    user_input = input(f"({current_model}) You: ")
    if user_input.lower() == "quit":
            print("Goodbye!")
            break
    elif user_input.lower() == "switch":
            current_model = "Gemini" if current_model == "OpenAI" else "OpenAI"
            print(f"Switched to {current_model}.")
            continue
    if current_model == "OpenAI":
            response = get_openai_response(user_input)
    else:
            response = get_gemini_response(user_input)
        
    print(f"{current_model} Bot: {response}")