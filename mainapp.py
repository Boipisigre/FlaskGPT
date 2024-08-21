import os

from openai import OpenAI
from dotenv import load_dotenv
from flask import Flask
from flask import Response
from flask import render_template
from flask import request

load_dotenv()

app = Flask(__name__)

client = OpenAI( api_key = os.getenv("API_KEY"), )


# print(openai.api_key)

@app.route('/')
def home():
    return  render_template('index.html')

@app.route('/prompt', methods=['POST'])
def prompt():
    messages = request.json['messages']
    conversation = build_conversation_dict(messages=messages)

    return Response(event_stream(conversation), mimetype='text/event-stream')


def event_stream(conversation: list[dict]) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversation,
        stream=True
    )

    for line in response:
        text = line.choices[0].delta.content
        if text:
            yield text

def build_conversation_dict(messages: list) -> list[dict]:
    return [
        {"role": "user" if i % 2 == 0 else "assistant", "content": message}
        for i, message in enumerate(messages)
    ]

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
