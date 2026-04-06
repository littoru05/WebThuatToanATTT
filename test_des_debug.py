import requests
import json

# Test DES API
response = requests.post('http://127.0.0.1:5000/api/des/encrypt-detailed', 
    json={'plaintext': 'Hello!!!', 'key': 'mysecrets'})

if response.status_code == 200:
    data = response.json()
    print("✅ API Response OK")
    print(f"Total steps: {len(data['steps'])}")
    
    # Check each step structure
    for idx, step in enumerate(data['steps'][:3]):  # Check first 3 steps
        print(f"\n--- Step {step['step']}: {step['name']} ---")
        print(f"  type: {step.get('type')}")
        print(f"  round: {step.get('round')}")
        print(f"  has input: {'input' in step}")
        print(f"  has output: {'output' in step}")
        
        if 'input' in step and step['input']:
            print(f"  input type: {type(step['input'])}")
            print(f"  input[0] type: {type(step['input'][0]) if step['input'] else None}")
            print(f"  input[0]: {step['input'][0]}")
            
        if 'output' in step and step['output']:
            print(f"  output type: {type(step['output'])}")
            print(f"  output[0] type: {type(step['output'][0]) if step['output'] else None}")
            print(f"  output[0]: {step['output'][0]}")
else:
    print(f"❌ API Error: {response.status_code}")
    print(response.text)
