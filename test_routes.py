import requests

urls = [
    'http://127.0.0.1:5000/',
    'http://127.0.0.1:5000/playfair.html',
    'http://127.0.0.1:5000/modulo.html',
    'http://127.0.0.1:5000/rsa.html',
    'http://127.0.0.1:5000/des.html',
    'http://127.0.0.1:5000/aes.html',
    'http://127.0.0.1:5000/aes-detailed.html',
]

print("Route Testing Results:")
print("=" * 50)
for url in urls:
    page_name = url.split('/')[-1] or 'index'
    try:
        r = requests.get(url)
        status = r.status_code
        status_text = "✅" if status == 200 else "❌"
        print(f"{status_text} {page_name:<25} : {status}")
    except Exception as e:
        print(f"❌ {page_name:<25} : ERROR - {str(e)}")
