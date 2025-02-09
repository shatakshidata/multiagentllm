import os
import yaml
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv()
import time

openai.api_base = "https://llm.dsrs.illinois.edu/v1"
openai.api_key = os.getenv("OPENAI_API_KEY")
# Initialize the client for chat completions
client = openai.ChatCompletion  
OPENAI_MODEL = "gpt-3.5-turbo"  # or your model

def time_it(func):
    """Decorator to measure execution time of a function."""
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executed in {end - start:.4f} seconds")
        return result
    return wrapper

def log_info(message):
    print(f"INFO: {message}")

def log_error(message):
    print(f"ERROR: {message}")
