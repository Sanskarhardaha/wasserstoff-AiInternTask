import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

async def query_ai(seed, guess, persona):
    prompt = f"As a {persona} game host, does '{guess}' beat '{seed}'? Answer Yes or No only."
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=10,
            temperature=0.7
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return "No"