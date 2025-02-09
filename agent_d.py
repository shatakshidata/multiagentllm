
from openai import OpenAI
import yaml

# Load config
with open("config/config.yaml", "r") as file:
    config = yaml.safe_load(file)

client = OpenAI(api_key=config["openai"]["api_key"], base_url=config["openai"]["base_url"])

def generate_insights(df, scenario):
    """ Uses LLM to extract insights from the data. """
    prompt = f"Summarize key insights for {scenario}. Here’s the data sample:\n{df.head().to_string(index=False)}"
    response = client.chat.completions.create(
        model=config["openai"]["model"],
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
    )
    return response.choices[0].message.content
