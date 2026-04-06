"""
Flask application for encryption web interface
Complete implementation: Playfair, Modulo, RSA, DES, AES
"""

from flask import Flask, render_template, request, jsonify
from encryption import (
    PlayfairCipher, ModuloOperations,
    RSAEncryption, DESEncryption, DESDetailedEncryption, AESEncryption, AESDetailedEncryption
)
import json
import os

app = Flask(__name__, 
            static_folder=os.path.join(os.path.dirname(__file__), 'static'),
            static_url_path='/static')

@app.route('/')
def index():
    """Render main page"""
    return render_template('index.html')

@app.route('/playfair.html')
def playfair_page():
    """Render playfair page"""
    return render_template('playfair.html')

@app.route('/modulo.html')
def modulo_page():
    """Render modulo page"""
    return render_template('modulo.html')

@app.route('/rsa.html')
def rsa_page():
    """Render rsa page"""
    return render_template('rsa.html')

@app.route('/des.html')
def des_page():
    """Render des page"""
    return render_template('des.html')

@app.route('/aes.html')
def aes_page():
    """Render aes page"""
    return render_template('aes.html')

@app.route('/aes-detailed.html')
def aes_detailed_page():
    """Render detailed AES step-by-step page"""
    return render_template('aes-detailed.html')

# ==================== PLAYFAIR CIPHER ====================

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    """Encrypt using Playfair cipher"""
    try:
        data = request.json
        plaintext = data.get('plaintext', '')
        key = data.get('key', '')
        result = PlayfairCipher.encrypt(plaintext, key)
        return jsonify({'success': True, 'result': result})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    """Decrypt using Playfair cipher"""
    try:
        data = request.json
        ciphertext = data.get('ciphertext', '')
        key = data.get('key', '')
        result = PlayfairCipher.decrypt(ciphertext, key)
        return jsonify({'success': True, 'result': result})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# ==================== MODULO OPERATIONS (10 Bài Tập) ====================

@app.route('/api/modulo/exercise1', methods=['POST'])
def modulo_ex1():
    """Exercise 1: Power mod reduction"""
    try:
        data = request.json
        a = int(data.get('a', 0))
        m = int(data.get('m', 0))
        n = int(data.get('n', 0))
        result = ModuloOperations.exercise1_power_mod_reduction(a, m, n)
        return jsonify({'success': True, 'result': result, 'formula': f'{a}^{m} mod {n} = {result}'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/modulo/exercise2', methods=['POST'])
def modulo_ex2():
    """Exercise 2: Modular inverse"""
    try:
        data = request.json
        a = int(data.get('a', 0))
        n = int(data.get('n', 0))
        result = ModuloOperations.exercise2_mod_inverse(a, n)
        return jsonify({'success': True, 'result': result, 'formula': f'{a}^-1 mod {n} = {result}'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/modulo/exercise3', methods=['POST'])
def modulo_ex3():
    """Exercise 3: Fermat's theorem"""
    try:
        data = request.json
        a = int(data.get('a', 0))
        m = int(data.get('m', 0))
        n = int(data.get('n', 0))
        result = ModuloOperations.exercise3_fermat_theorem(a, m, n)
        return jsonify({'success': True, 'result': result})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/modulo/exercise4', methods=['POST'])
def modulo_ex4():
    """Exercise 4: Euler phi function"""
    try:
        data = request.json
        n = int(data.get('n', 0))
        result = ModuloOperations.exercise4_euler_phi(n)
        return jsonify({'success': True, 'result': result, 'formula': f'φ({n}) = {result}'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/modulo/exercise5', methods=['POST'])
def modulo_ex5():
    """Exercise 5: Euler's theorem"""
    try:
        data = request.json
        a = int(data.get('a', 0))
        m = int(data.get('m', 0))
        n = int(data.get('n', 0))
        result = ModuloOperations.exercise5_euler_theorem(a, m, n)
        return jsonify({'success': True, 'result': result})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/modulo/exercise6', methods=['POST'])
def modulo_ex6():
    """Exercise 6: CRT power"""
    try:
        data = request.json
        a = int(data.get('a', 0))
        k = int(data.get('k', 0))
        n = int(data.get('n', 0))
        result = ModuloOperations.exercise6_crt_power(a, k, n)
        return jsonify({'success': True, 'result': result})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/modulo/exercise7', methods=['POST'])
def modulo_ex7():
    """Exercise 7: CRT system"""
    try:
        data = request.json
        m1 = int(data.get('m1', 0))
        m2 = int(data.get('m2', 0))
        m3 = int(data.get('m3', 0))
        a1 = int(data.get('a1', 0))
        a2 = int(data.get('a2', 0))
        a3 = int(data.get('a3', 0))
        result = ModuloOperations.exercise7_crt_system(m1, m2, m3, a1, a2, a3)
        return jsonify({'success': True, 'result': result})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/modulo/exercise8', methods=['POST'])
def modulo_ex8():
    """Exercise 8: Primitive root check"""
    try:
        data = request.json
        a = int(data.get('a', 0))
        n = int(data.get('n', 0))
        result = ModuloOperations.exercise8_primitive_root(a, n)
        msg = "là" if result else "không là"
        return jsonify({'success': True, 'result': result, 'message': f'{a} {msg} căn nguyên thủy của {n}'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/modulo/exercise9', methods=['POST'])
def modulo_ex9():
    """Exercise 9: Discrete logarithm"""
    try:
        data = request.json
        a = int(data.get('a', 0))
        b = int(data.get('b', 0))
        n = int(data.get('n', 0))
        result = ModuloOperations.exercise9_discrete_log(a, b, n)
        return jsonify({'success': True, 'result': result, 'formula': f'log_{a}({b}) mod {n} = {result}'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/modulo/exercise10', methods=['POST'])
def modulo_ex10():
    """Exercise 10: Modulo expressions"""
    try:
        data = request.json
        a = int(data.get('a', 0))
        b = int(data.get('b', 0))
        x = int(data.get('x', 0))
        y = int(data.get('y', 0))
        n = int(data.get('n', 0))
        result = ModuloOperations.exercise10_modulo_expressions(a, b, x, y, n)
        return jsonify({'success': True, 'result': result})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# ==================== RSA ENCRYPTION (Bài Toán 2) ====================

@app.route('/api/rsa/generate', methods=['POST'])
def rsa_generate():
    """Generate RSA keys from p, q, e"""
    try:
        data = request.json
        p = int(data.get('p', 0))
        q = int(data.get('q', 0))
        e = int(data.get('e', 0))
        result = RSAEncryption.generate_keys(p, q, e)
        return jsonify(result)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/rsa/encrypt', methods=['POST'])
def rsa_encrypt():
    """RSA encrypt"""
    try:
        data = request.json
        plaintext = data.get('plaintext', '')
        e = int(data.get('e', 0))
        n = int(data.get('n', 0))
        result = RSAEncryption.encrypt(plaintext, e, n)
        return jsonify({'success': True, 'result': result})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/rsa/decrypt', methods=['POST'])
def rsa_decrypt():
    """RSA decrypt"""
    try:
        data = request.json
        ciphertext = data.get('ciphertext', '')
        d = int(data.get('d', 0))
        n = int(data.get('n', 0))
        result = RSAEncryption.decrypt(ciphertext, d, n)
        return jsonify({'success': True, 'result': result})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# ==================== DES ENCRYPTION ====================

@app.route('/api/des/encrypt', methods=['POST'])
def des_encrypt():
    """DES encrypt"""
    try:
        data = request.json
        plaintext = data.get('plaintext', '')
        key = data.get('key', '')
        result = DESEncryption.encrypt(plaintext, key)
        return jsonify({'success': True, 'result': result})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/des/decrypt', methods=['POST'])
def des_decrypt():
    """DES decrypt"""
    try:
        data = request.json
        ciphertext = data.get('ciphertext', '')
        key = data.get('key', '')
        result = DESEncryption.decrypt(ciphertext, key)
        return jsonify({'success': True, 'result': result})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/des/encrypt-detailed', methods=['POST'])
def des_encrypt_detailed():
    """DES detailed step-by-step encryption"""
    try:
        data = request.json
        plaintext = data.get('plaintext', '')
        key = data.get('key', '')
        result = DESDetailedEncryption.encrypt_detailed(plaintext, key)
        return jsonify(result)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# ==================== AES ENCRYPTION ====================

@app.route('/api/aes/encrypt', methods=['POST'])
def aes_encrypt():
    """AES encrypt"""
    try:
        data = request.json
        plaintext = data.get('plaintext', '')
        key = data.get('key', '')
        result = AESEncryption.encrypt(plaintext, key)
        return jsonify({'success': True, 'result': result})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/aes/decrypt', methods=['POST'])
def aes_decrypt():
    """AES decrypt"""
    try:
        data = request.json
        ciphertext = data.get('ciphertext', '')
        key = data.get('key', '')
        result = AESEncryption.decrypt(ciphertext, key)
        return jsonify({'success': True, 'result': result})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/aes/encrypt-detailed', methods=['POST'])
def aes_encrypt_detailed():
    """AES detailed step-by-step encryption"""
    try:
        data = request.json
        plaintext = data.get('plaintext', '')
        key = data.get('key', '')
        result = AESDetailedEncryption.encrypt_detailed(plaintext, key)
        return jsonify(result)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
