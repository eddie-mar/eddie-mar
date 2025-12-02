import json
import time
import os

import requests
from openai import OpenAI
from dotenv import load_dotenv

import utils

load_dotenv()
open_ai_key = os.getenv('OPENAI_API_KEY')
model = os.getenv('AI_MODEL')

client = OpenAI(api_key=open_ai_key)


TOOLS = [
    {
        'type': 'function',
        'function': {
            'name': 'get_weather',
            'description': 'Return current temperature for a city',
            'parameters': {
                'type': 'object',
                'properties': {'city': {'type': 'string'}},
                'required': ['city']
            }
        }
    },
    {
        'type': 'function',
        'function': {
            'name': 'run_math',
            'description': 'Calculate a simple math expression of only two variables and a basic operator (+, -, /, *)',
            'parameters': {
                'type': 'object',
                'properties': {'expression': {'type': 'string'}},
                'required': ['expression']
            }
        }
    }
]


def safe_execute_tool(name: str, args: dict, max_retries=2):
    try:
        tool = utils.ToolFactory().get(name)
    except Exception as e:
        raise Exception(f'Error: {e}')
    
    attempt = 0
    while True:
        try:
            return tool.execute(args)
        except requests.RequestException as e:
            attempt += 1
            if attempt > max_retries:
                raise Exception(f'Error: {e}')
            time.sleep(0.5 * attempt)
        except Exception as e:
            raise Exception(f'Error: {e}')
        
def run_agent_once(user_input: str):
    messages = [
        {'role': 'system', 'content': 'You are an assistant with access to tools.'},
        {'role': 'user', 'content': user_input}
    ]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=TOOLS
    )
    tool_calls = response.get('tool_calls') or []

    if not tool_calls:
        return response['choices'][0]['message']['content']
    
    call = tool_calls[0]
    call_id = call['id']
    func_name = call['function']['name']
    args = json.loads(call['function']['arguments'])

    try:
        result = safe_execute_tool(func_name, args)
    except Exception as e:
        messages.append({
            'role': 'tool',
            'tool_call_id': call_id,
            'content': json.dumps({'error': str(e)})
        })
        follow_up = client.chat.completions.create(
            model=model,
            messages=messages,
            tools=TOOLS
        )
        return follow_up['choices'][0]['message']['content']

    messages.append({
        'role': 'tool',
        'tool_call_id': call_id,
        'content': json.dumps(result)
    })
    final = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=TOOLS
    )
    return final['choices'][0]['message']['content']


if __name__ == '__main__':
    question = input('User input: ')
    answer = run_agent_once(question)

    print(answer)
