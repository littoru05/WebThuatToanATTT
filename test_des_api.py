import requests

response = requests.post('http://127.0.0.1:5000/api/des/encrypt-detailed', 
    json={'plaintext': 'Hello!!!', 'key': 'mysecrets'})

if response.status_code == 200:
    data = response.json()
    print('✅ DES API Response Status: 200')
    print(f'Total steps: {len(data["steps"])}')
    print('\n--- First step (Init) ---')
    step0 = data['steps'][0]
    print(f'Name: {step0.get("name")}')
    print(f'Type: {step0.get("type")}')
    print(f'Has input: {"input" in step0}')
    print(f'Has output: {"output" in step0}')
    print(f'Has explanation: {"explanation" in step0}')
    if 'input' in step0 and step0['input']:
        print(f'Input shape: {len(step0["input"])}x{len(step0["input"][0]) if step0["input"][0] else 0}')
else:
    print(f'❌ API Error: Status {response.status_code}')
    print(response.text)
