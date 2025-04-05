import google.generativeai as genai

# Replace with your valid API key
genai.configure(api_key= "GOOGLE_API_KEY")

models = genai.list_models()

for model in models:
    print(f"Name: {model.name}")
    print(f"Supports generate_content: {model.supports_generation}")
    print("-" * 50)
