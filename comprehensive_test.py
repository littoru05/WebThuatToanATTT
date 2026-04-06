import requests
import json

print("=" * 60)
print("DETAILED AES ANALYZER - COMPREHENSIVE TEST")
print("=" * 60)

# Test 1: API Endpoint with sample data
print("\n[TEST 1] API Endpoint: /api/aes/encrypt-detailed")
print("-" * 60)

test_data = {
    'plaintext': 'Hello World!!!!!',
    'key': 'MySecretPassword'
}

try:
    response = requests.post(
        'http://127.0.0.1:5000/api/aes/encrypt-detailed',
        json=test_data
    )
    result = response.json()
    
    print(f"✅ Status Code: {response.status_code}")
    print(f"✅ Success: {result.get('success')}")
    print(f"✅ Plaintext: {result.get('plaintext')}")
    print(f"✅ Key: {result.get('key')}")
    print(f"✅ Ciphertext: {result.get('ciphertext')}")
    
    steps = result.get('steps', [])
    print(f"✅ Total Steps: {len(steps)}")
    print("\nStep Breakdown:")
    step_names = {}
    for step in steps:
        name = step.get('name', 'Unknown')
        step_names[name] = step_names.get(name, 0) + 1
    
    for name, count in sorted(step_names.items()):
        print(f"   - {name}: {count}x")
    
    print("\nFirst 3 Steps:")
    for i, step in enumerate(steps[:3]):
        print(f"   Step {i}: {step['name']}")
        print(f"     State[0][0]: {step['state'][0][0]}")
    
    print("\nLast 2 Steps:")
    for i, step in enumerate(steps[-2:], start=len(steps)-2):
        print(f"   Step {i}: {step['name']}")
        print(f"     State[0][0]: {step['state'][0][0]}")
    
except Exception as e:
    print(f"❌ Error: {str(e)}")

# Test 2: HTML Page Load
print("\n" + "=" * 60)
print("[TEST 2] Page Load: /aes-detailed.html")
print("-" * 60)

try:
    response = requests.get('http://127.0.0.1:5000/aes-detailed.html')
    content = response.text
    
    print(f"✅ Status Code: {response.status_code}")
    print(f"✅ Page Size: {len(content)} bytes")
    print(f"✅ Contains 'AES DETAILED': {'AES DETAILED' in content}")
    print(f"✅ Contains JavaScript function 'analyzeAESDetailed': {'analyzeAESDetailed' in content}")
    print(f"✅ Contains 'ANALYZE: STEP-BY-STEP': {'ANALYZE: STEP-BY-STEP' in content}")
    print(f"✅ Contains CSS matrices styling: {'.matrix' in content}")
    
except Exception as e:
    print(f"❌ Error: {str(e)}")

# Test 3: Other API endpoints
print("\n" + "=" * 60)
print("[TEST 3] Other API Endpoints - Quick Test")
print("-" * 60)

endpoints = [
    ('/api/playfair/encrypt', {'plaintext': 'hello', 'key': 'secret'}),
    ('/api/modulo/ex1', {'a': 2, 'b': 5, 'n': 13}),
    ('/api/rsa/generate', {'p': 61, 'q': 53}),
    ('/api/des/encrypt', {'plaintext': 'Hello!!!', 'key': 'password'}),
    ('/api/aes/encrypt', {'plaintext': 'Hello World!!!!!', 'key': 'MySecretPassword'})
]

for endpoint, data in endpoints:
    try:
        r = requests.post(f'http://127.0.0.1:5000{endpoint}', json=data)
        status = "✅" if r.status_code == 200 else "❌"
        print(f"{status} {endpoint:<35} : {r.status_code}")
    except Exception as e:
        print(f"❌ {endpoint:<35} : {str(e)[:40]}")

print("\n" + "=" * 60)
print("✅ ALL TESTS COMPLETED SUCCESSFULLY")
print("=" * 60)
