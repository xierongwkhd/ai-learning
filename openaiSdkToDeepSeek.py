# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
        {"role": "assistant", "content": "Hello! How can I assist you today?"},
        {"role": "user", "content": "what is your name?"},
        {"role": "assistant", "content": "I'm an AI assistant created by DeepSeek! You can think of me as DeepSeek Assistant. I don't have a personal name, but you can call me whatever you like. How can I help you today?"},
        {"role": "user", "content": "can you speak?"}
    ],
    stream=False
)

print(response.choices[0].message.content)