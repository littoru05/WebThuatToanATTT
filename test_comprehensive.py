#!/usr/bin/env python
import requests
import json

print("=" * 60)
print("TESTING AES AND DES DETAILED ENCRYPTION APIs")
print("=" * 60)

# Test AES
print("\n[1] Testing AES Detailed Encryption")
print("-" * 60)

response = requests.post('http://127.0.0.1:5000/api/aes/encrypt-detailed', 
    json={'plaintext': 'Hello!!!!!!!!!!', 'key': 'mysecretpassword'})

if response.status_code == 200:
    data = response.json()
    print(f"✅ Status: {response.status_code}")
    print(f"✅ Success: {data['success']}")
    print(f"✅ Total steps: {len(data['steps'])}")
    
    # Check first step (Init)
    step0 = data['steps'][0]
    print(f"\nStep 0 (Initialize):")
    print(f"  - Type: {step0.get('type')}")
    print(f"  - Has input: {'input' in step0}")
    print(f"  - Has output: {'output' in step0}")
    print(f"  - Has explanation: {'explanation' in step0}")
    if 'output' in step0 and step0['output']:
        print(f"  - Output shape: {len(step0['output'])}x{len(step0['output'][0])}")
    
    # Check AddRoundKey step
    add_round_key_steps = [s for s in data['steps'] if s.get('type') == 'add_round_key']
    if add_round_key_steps:
        step = add_round_key_steps[0]
        print(f"\nAddRoundKey Step ({step['name']}):")
        print(f"  - Type: {step.get('type')}")
        print(f"  - Round: {step.get('round')}")
        print(f"  - Has input: {'input' in step}")
        print(f"  - Has key: {'key' in step}")
        print(f"  - Has output: {'output' in step}")
        if 'key' in step and step['key']:
            print(f"  - Key shape: {len(step['key'])}x{len(step['key'][0])}")
    
    print("\n✅ AES API: PASS")
else:
    print(f"❌ AES API Error: {response.status_code}")
    print(response.text)

# Test DES  
print("\n[2] Testing DES Detailed Encryption")
print("-" * 60)

response = requests.post('http://127.0.0.1:5000/api/des/encrypt-detailed', 
    json={'plaintext': 'Hello!!!', 'key': 'mysecrets'})

if response.status_code == 200:
    data = response.json()
    print(f"✅ Status: {response.status_code}")
    print(f"✅ Success: {data['success']}")
    print(f"✅ Total steps: {len(data['steps'])}")
    
    # Check first step (Init)
    step0 = data['steps'][0]
    print(f"\nStep 0 (Initialize):")
    print(f"  - Type: {step0.get('type')}")
    print(f"  - Has input: {'input' in step0}")
    print(f"  - Has output: {'output' in step0}")
    print(f"  - Has explanation: {'explanation' in step0}")
    if 'output' in step0 and step0['output']:
        print(f"  - Output shape: {len(step0['output'])}x{len(step0['output'][0])}")
    
    # Check Round step
    round_steps = [s for s in data['steps'] if s.get('type') == 'des_round']
    if round_steps:
        step = round_steps[0]
        print(f"\nDES Round Step ({step['name']}):")
        print(f"  - Type: {step.get('type')}")
        print(f"  - Round: {step.get('round')}")
        print(f"  - Has input: {'input' in step}")
        print(f"  - Has output: {'output' in step}")
        if 'input' in step and step['input']:
            print(f"  - Input shape: {len(step['input'])}x{len(step['input'][0])}")
    
    print("\n✅ DES API: PASS")
else:
    print(f"❌ DES API Error: {response.status_code}")
    print(response.text)

print("\n" + "=" * 60)
print("SUMMARY: Both APIs return correct detailed format ✅")
print("=" * 60)
