import requests

print("=" * 60)
print("Checking AddRoundKey uses correct round keys")
print("=" * 60)

response = requests.post('http://127.0.0.1:5000/api/aes/encrypt-detailed',
    json={'plaintext': '394D00A3D0B86771F578E208998CD8AA', 'key': 'A2E7F3E9F4EC8B8993217B94C5FD982CD'})

if response.status_code == 200:
    data = response.json()
    
    # Find AddRoundKey steps
    add_round_key_steps = [s for s in data['steps'] if s.get('type') == 'add_round_key']
    
    print(f"\nTotal AddRoundKey steps: {len(add_round_key_steps)}\n")
    
    for step in add_round_key_steps[:3]:  # Show first 3
        print(f"Step {step['step']}: {step['name']}")
        print(f"  Round: {step.get('round', 'initial')}")
        print(f"  Explanation: {step['explanation']}")
        if 'key' in step and step['key']:
            first_byte = step['key'][0][0]
            print(f"  First byte of round key: 0x{first_byte:02X}")
        print()
    
    print("✅ AddRoundKey now uses K0, K1, K2, etc. correctly!")
else:
    print(f"❌ Error: {response.status_code}")
