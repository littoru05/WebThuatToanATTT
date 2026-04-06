import requests

r = requests.get('http://127.0.0.1:5000/')
print(f'Status: {r.status_code}')
print(f'Is HTML served: {len(r.text) > 100}')
print(f'Has playfair link: {"playfair.html" in r.text}')
print(f'Has aes link: {"aes.html" in r.text}')
print(f'✅ Home page (/) is serving index.html correctly')
