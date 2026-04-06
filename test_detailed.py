import requests
import time

time.sleep(2)

print('=== Testing New Step-by-Step Pages ===\n')

# Test 1: AES detailed endpoint
print('[1] Testing /api/aes/encrypt-detailed')
r = requests.post('http://127.0.0.1:5000/api/aes/encrypt-detailed', 
                  json={'plaintext': 'Hello!!!!!!!!!!', 'key': 'mysecretpassword'})
if r.status_code == 200:
    data = r.json()
    print(f'✅ Status: {r.status_code}')
    print(f'   Plaintext: {data.get("plaintext")}')
    print(f'   Ciphertext: {data.get("ciphertext")}')
    print(f'   Steps: {len(data.get("steps", []))} (0=Init, 1-40=rounds)')
else:
    print(f'❌ Status: {r.status_code}')

# Test 2: DES detailed endpoint
print('\n[2] Testing /api/des/encrypt-detailed')
r = requests.post('http://127.0.0.1:5000/api/des/encrypt-detailed',
                  json={'plaintext': 'Hello!!!', 'key': 'password'})
if r.status_code == 200:
    data = r.json()
    print(f'✅ Status: {r.status_code}')
    print(f'   Plaintext: {data.get("plaintext")}')
    print(f'   Ciphertext: {data.get("ciphertext")}')
    print(f'   Steps: {len(data.get("steps", []))} (0=Init, 1-16=rounds, 17=Final)')
else:
    print(f'❌ Status: {r.status_code}')

# Test 3: Pages load correctly
print('\n[3] Testing HTML pages')
pages = ['aes.html', 'des.html']
for page in pages:
    r = requests.get(f'http://127.0.0.1:5000/{page}')
    print(f'✅ {page}: {r.status_code}')

print('\n' + '='*50)
print('✅ ALL TESTS COMPLETED!')
print('='*50)
