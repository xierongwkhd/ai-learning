import os
import requests

DEEPSEEK_API_KEY = os.environ.get('DEEPSEEK_API_KEY')
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {DEEPSEEK_API_KEY}'
}
url = 'https://api.deepseek.com/chat/completions'
data = {
'model': 'deepseek-chat',
'messages': [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hello! How can I assist you today?"},
    {"role": "user", "content": "what is your name?"},
    {"role": "assistant", "content": "I'm an AI assistant created by DeepSeek! You can think of me as DeepSeek Assistant. I don't have a personal name, but you can call me whatever you like. How can I help you today?"},
    {"role": "user", "content": "can you speak?"}
],
'stream': False
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()
    print(result['choices'][0]['message']['content'])
else:
    print("请求失败，错误码：", response.status_code)