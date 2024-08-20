
import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

client = OpenAI( api_key = os.getenv("API_KEY"), )


response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "Vous êtes un assistant expert."},
    {"role": "user", "content": "Qu'est ce qu'un LLM?"}
  ],
stream=True,
)

for chunk in response:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
