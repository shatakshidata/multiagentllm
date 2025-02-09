import openai
import pandas as pd
from utils import OPENAI_MODEL, time_it, log_info, log_error

@time_it
def generate_synthetic_data(scenario, num_rows):
    """Generates structured synthetic data using OpenAI."""
    prompt = f"Generate {num_rows} rows of structured data for: {scenario}. Output as CSV."
    try:
        response = openai.ChatCompletion.create(
            model=OPENAI_MODEL,
            messages=[{"role": "system", "content": prompt}],
        )

        if response and response.choices:
            ai_response = response.choices[0].message.get("content", "")
            print("\n🔍 OpenAI Response:\n", ai_response)  # Debug output

            # Convert AI response to DataFrame
            from io import StringIO
            df = pd.read_csv(StringIO(ai_response))
            log_info(f"Synthetic data generated for {scenario}.")
            return df
        else:
            log_error("No response from OpenAI.")
            return None

    except Exception as e:
        log_error(f"Data generation failed: {e}")
        return None
