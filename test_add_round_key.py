import requests

response = requests.post('http://127.0.0.1:5000/api/aes/encrypt-detailed', 
    json={'plaintext': 'Hello!!!!!!!!!!', 'key': 'mysecretpassword'})

data = response.json()

# Find an AddRoundKey step
for i, step in enumerate(data['steps']):
    if step.get('type') == 'add_round_key':
        print(f'AddRoundKey step at index {i}:')
        print(f'  Name: {step.get("name")}')
        print(f'  Round: {step.get("round")}')
        print(f'  Has key: {"key" in step}')
        if 'key' in step and step['key']:
            print(f'  Key shape: {len(step["key"])}x{len(step["key"][0])}')
            print(f'  First row key: {step["key"][0][:2]}')
        if 'input' in step:
            print(f'  Input shape: {len(step["input"])}x{len(step["input"][0])}')
        if 'output' in step:
            print(f'  Output shape: {len(step["output"])}x{len(step["output"][0])}')
        break
