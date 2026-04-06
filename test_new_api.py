import requests
import json

response = requests.post('http://127.0.0.1:5000/api/aes/encrypt-detailed', 
    json={'plaintext': 'Hello!!!!!!!!!!', 'key': 'mysecretpassword'})

if response.status_code == 200:
    data = response.json()
    print('✅ API Response Status: 200')
    print(f'Total steps: {len(data["steps"])}')
    print('\n--- Step 5 (Sample AddRoundKey step) ---')
    step5 = data['steps'][4]  # Index 4 = Step 5
    print(f'Name: {step5.get("name")}')
    print(f'Type: {step5.get("type")}')
    print(f'Round: {step5.get("round")}')
    print(f'Explanation: {step5.get("explanation")}')
    print(f'Input present: {"input" in step5}')
    print(f'Key present: {"key" in step5}')
    print(f'Output present: {"output" in step5}')
    if 'input' in step5:
        print(f'Input shape: {len(step5["input"])}x{len(step5["input"][0]) if step5["input"] else 0}')
    
    # Show first row of input, key, output
    if 'input' in step5 and 'key' in step5 and 'output' in step5:
        print(f'\nInput row 0: {[hex(v) for v in step5["input"][0]]}')
        print(f'Key row 0: {[hex(v) for v in step5["key"][0]]}')
        print(f'Output row 0: {[hex(v) for v in step5["output"][0]]}')
else:
    print(f'❌ API Error: Status {response.status_code}')
    print(response.text)
