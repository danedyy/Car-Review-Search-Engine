import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

# Load the API key from an environment variable
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Configure the generative AI with the API key
genai.configure(api_key=GOOGLE_API_KEY)

version = 'models/gemini-1.5-flash'
model = genai.GenerativeModel(version)
model_info = genai.get_model(version)

def check_prompt_length(prompt):
    if len(prompt.split()) > model_info.input_token_limit:
        print(f'Prompt length is greater than the input token limit of {model_info.input_token_limit}')
        exit()

initial_prompt = "I will provide you with a list of different cars and their respective descriptions about a certain feature. With the list of cars there will be a query that was inserted by a user, which targets cars with certain perks related with the features' descriptions provided. Your task is to strictly return a ranking list of these cars based on the relevance of the description of the cars according to the user's query. The list should have this format: 1: 'name of the car', 2: 'name of the car'."

def re_rank_cars(query):
    prompt = initial_prompt + query
    check_prompt_length(prompt)
    response = model.generate_content(prompt)
    return response.text
