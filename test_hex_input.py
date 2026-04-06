import requests

# Test with hex input (like the user's example)
plaintext_hex = "394D00A3D0B86771F578E208998CD8AA"
key_hex = "A2E7F3E9F4EC8B8993217B94C5FD982CD"

print("=" * 60)
print("Testing with HEX input")
print("=" * 60)

response = requests.post('http://127.0.0.1:5000/api/aes/encrypt-detailed',
    json={'plaintext': plaintext_hex, 'key': key_hex})

if response.status_code == 200:
    data = response.json()
    print(f"✅ AES Status: {response.status_code}")
    print(f"Plaintext (HEX): {data['plaintext']}")
    print(f"Key (HEX): {data['key']}")
    print(f"Ciphertext (HEX): {data['ciphertext']}")
    print(f"✅ Should use hex directly, NOT ASCII hex of the string")
else:
    print(f"❌ Error: {response.status_code}")
    print(response.text)

print("\n" + "=" * 60)
print("Testing DES with HEX input")
print("=" * 60)

plaintext_des = "394D00A3D0B86771"
key_des = "A2E7F3E9F4EC8B89"

response = requests.post('http://127.0.0.1:5000/api/des/encrypt-detailed',
    json={'plaintext': plaintext_des, 'key': key_des})

if response.status_code == 200:
    data = response.json()
    print(f"✅ DES Status: {response.status_code}")
    print(f"Plaintext (HEX): {data['plaintext']}")
    print(f"Key (HEX): {data['key']}")
    print(f"Ciphertext (HEX): {data['ciphertext']}")
    print(f"✅ Should use hex directly")
else:
    print(f"❌ Error: {response.status_code}")
    print(response.text)

# Test with text input (should still work as before)
print("\n" + "=" * 60)
print("Testing with TEXT input (should still work)")
print("=" * 60)

response = requests.post('http://127.0.0.1:5000/api/aes/encrypt-detailed',
    json={'plaintext': 'Hello!!!!!!!!!!', 'key': 'mysecretpassword'})

if response.status_code == 200:
    data = response.json()
    print(f"✅ AES Text Input Status: {response.status_code}")
    print(f"Plaintext (HEX): {data['plaintext'][:40]}...")
    print(f"Ciphertext (HEX): {data['ciphertext'][:40]}...")
else:
    print(f"❌ Error: {response.status_code}")
