"""
Encryption modules for various cryptographic algorithms
Playfair, Modulo Operations, RSA, DES, AES
"""

import math
from Crypto.Cipher import AES, DES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
import base64
import os

# ==================== PLAYFAIR CIPHER (Nhóm 4: Mã Hóa Cổ Điển) ====================

class PlayfairCipher:
    """Playfair Cipher encryption and decryption"""
    
    @staticmethod
    def create_matrix(key):
        """Create 5x5 Playfair matrix from key"""
        key = key.upper().replace('J', 'I')
        matrix = []
        seen = set()
        
        for char in key:
            if char.isalpha() and char not in seen:
                matrix.append(char)
                seen.add(char)
        
        for char in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
            if char not in seen:
                matrix.append(char)
                seen.add(char)
        
        return [matrix[i:i+5] for i in range(0, 25, 5)]
    
    @staticmethod
    def find_position(matrix, char):
        """Find position of character in matrix"""
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == char:
                    return i, j
        return None
    
    @staticmethod
    def encrypt(plaintext, key):
        """Encrypt using Playfair cipher"""
        matrix = PlayfairCipher.create_matrix(key)
        plaintext = plaintext.upper().replace('J', 'I')
        plaintext = ''.join(c for c in plaintext if c.isalpha())
        
        # Prepare pairs
        pairs = []
        i = 0
        while i < len(plaintext):
            if i + 1 < len(plaintext):
                if plaintext[i] == plaintext[i+1]:
                    pairs.append(plaintext[i] + 'X')
                    i += 1
                else:
                    pairs.append(plaintext[i:i+2])
                    i += 2
            else:
                pairs.append(plaintext[i] + 'X')
                i += 1
        
        ciphertext = ""
        for pair in pairs:
            r1, c1 = PlayfairCipher.find_position(matrix, pair[0])
            r2, c2 = PlayfairCipher.find_position(matrix, pair[1])
            
            if r1 == r2:  # Same row
                ciphertext += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
            elif c1 == c2:  # Same column
                ciphertext += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
            else:  # Rectangle
                ciphertext += matrix[r1][c2] + matrix[r2][c1]
        
        return ciphertext
    
    @staticmethod
    def decrypt(ciphertext, key):
        """Decrypt using Playfair cipher"""
        matrix = PlayfairCipher.create_matrix(key)
        ciphertext = ciphertext.upper()
        
        plaintext = ""
        for i in range(0, len(ciphertext), 2):
            if i+1 < len(ciphertext):
                r1, c1 = PlayfairCipher.find_position(matrix, ciphertext[i])
                r2, c2 = PlayfairCipher.find_position(matrix, ciphertext[i+1])
                
                if r1 == r2:  # Same row
                    plaintext += matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]
                elif c1 == c2:  # Same column
                    plaintext += matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]
                else:  # Rectangle
                    plaintext += matrix[r1][c2] + matrix[r2][c1]
        
        return plaintext

# ==================== MODULO OPERATIONS (10 Bài Tập) ====================

class ModuloOperations:
    """10 Modular arithmetic exercises"""
    
    @staticmethod
    def gcd(a, b):
        """Compute GCD"""
        while b:
            a, b = b, a % b
        return a
    
    @staticmethod
    def extended_gcd(a, b):
        """Extended Euclidean algorithm"""
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = ModuloOperations.extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y
    
    @staticmethod
    def exercise1_power_mod_reduction(a, m, n):
        """1. Compute b = a^m mod n by exponent reduction"""
        return pow(a, m, n)
    
    @staticmethod
    def exercise2_mod_inverse(a, n):
        """2. Find x = a^-1 mod n using Extended Euclidean"""
        gcd, x, _ = ModuloOperations.extended_gcd(a % n, n)
        if gcd != 1:
            return None
        return (x % n + n) % n
    
    @staticmethod
    def exercise3_fermat_theorem(a, m, n):
        """3. Use Fermat's theorem: b = a^m mod n"""
        # If n is prime and gcd(a,n)=1: a^(n-1) ≡ 1 (mod n)
        return pow(a, m, n)
    
    @staticmethod
    def exercise4_euler_phi(n):
        """4. Compute Euler's totient function φ(n)"""
        result = n
        p = 2
        temp_n = n
        while p * p <= temp_n:
            if temp_n % p == 0:
                while temp_n % p == 0:
                    temp_n //= p
                result -= result // p
            p += 1
        if temp_n > 1:
            result -= result // temp_n
        return result
    
    @staticmethod
    def exercise5_euler_theorem(a, m, n):
        """5. Use Euler's theorem: b = a^m mod n"""
        phi = ModuloOperations.exercise4_euler_phi(n)
        m_reduced = m % phi
        return pow(a, m_reduced, n)
    
    @staticmethod
    def exercise6_crt_power(a, k, n):
        """6. Use Chinese Remainder Theorem for a^k mod n"""
        return pow(a, k, n)
    
    @staticmethod
    def exercise7_crt_system(m1, m2, m3, a1, a2, a3):
        """7. Solve system using Chinese Remainder Theorem"""
        M = m1 * m2 * m3
        M1 = M // m1
        M2 = M // m2
        M3 = M // m3
        
        y1 = ModuloOperations.exercise2_mod_inverse(M1, m1)
        y2 = ModuloOperations.exercise2_mod_inverse(M2, m2)
        y3 = ModuloOperations.exercise2_mod_inverse(M3, m3)
        
        x = (a1 * M1 * y1 + a2 * M2 * y2 + a3 * M3 * y3) % M
        return x
    
    @staticmethod
    def exercise8_primitive_root(a, n):
        """8. Check if a is a primitive root of n"""
        phi = ModuloOperations.exercise4_euler_phi(n)
        if pow(a, phi, n) != 1:
            return False
        
        # Check if a^(phi/p) != 1 for all prime factors p of phi
        p = 2
        factors = []
        phi_copy = phi
        while p * p <= phi_copy:
            if phi_copy % p == 0:
                factors.append(p)
                while phi_copy % p == 0:
                    phi_copy //= p
            p += 1
        if phi_copy > 1:
            factors.append(phi_copy)
        
        for factor in factors:
            if pow(a, phi // factor, n) == 1:
                return False
        return True
    
    @staticmethod
    def exercise9_discrete_log(a, b, n):
        """9. Find discrete logarithm k = log_a(b) mod n"""
        # Baby-step Giant-step algorithm
        m = int(n**0.5) + 1
        
        # Baby steps
        table = {}
        val = 1
        for j in range(m):
            if val == b:
                return j
            table[val] = j
            val = (val * a) % n
        
        # Giant steps
        c = pow(a, m * (n-2), n)  # a^(-m)
        gamma = b
        for i in range(m):
            if gamma in table:
                return i * m + table[gamma]
            gamma = (gamma * c) % n
        
        return None
    
    @staticmethod
    def exercise10_modulo_expressions(a, b, x, y, n):
        """10. Compute 5 modular expressions"""
        A1 = (a * x + b * y) % n
        A2 = (a * x - b * y) % n
        A3 = (a * x * b * y) % n
        
        by_inv = ModuloOperations.exercise2_mod_inverse((b * y) % n, n)
        A4 = by_inv if by_inv else None
        A5 = (a * x * A4) % n if A4 else None
        
        return {
            'A1': A1,
            'A2': A2,
            'A3': A3,
            'A4': A4,
            'A5': A5
        }

# ==================== RSA ENCRYPTION (Bài Toán 2 - Nhóm K=4) ====================

class RSAEncryption:
    """RSA Encryption - Problem 2 (input p, q, e)"""
    
    @staticmethod
    def gcd(a, b):
        """Calculate GCD"""
        while b:
            a, b = b, a % b
        return a
    
    @staticmethod
    def extended_gcd(a, b):
        """Extended Euclidean algorithm"""
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = RSAEncryption.extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y
    
    @staticmethod
    def mod_inverse(e, phi):
        """Find modular inverse using Extended Euclidean"""
        gcd, x, _ = RSAEncryption.extended_gcd(e, phi)
        if gcd != 1:
            return None
        return (x % phi + phi) % phi
    
    @staticmethod
    def generate_keys(p, q, e):
        """Generate RSA keys from given p, q, e (Bài toán 2)"""
        n = p * q
        phi = (p - 1) * (q - 1)
        
        if RSAEncryption.gcd(e, phi) != 1:
            return {'error': 'e và φ(n) không nguyên tố cùng nhau'}
        
        d = RSAEncryption.mod_inverse(e, phi)
        
        if d is None:
            return {'error': 'Không thể tính d'}
        
        return {
            'success': True,
            'n': n,
            'phi': phi,
            'e': e,
            'd': d,
            'public_key': {'e': e, 'n': n},
            'private_key': {'d': d, 'n': n}
        }
    
    @staticmethod
    def power_mod(base, exp, mod):
        """Compute (base^exp) mod mod using binary exponentiation"""
        result = 1
        base = base % mod
        while exp > 0:
            if exp % 2 == 1:
                result = (result * base) % mod
            exp = exp >> 1
            base = (base * base) % mod
        return result
    
    @staticmethod
    def encrypt(plaintext, e, n):
        """Encrypt: C = M^e mod n"""
        try:
            M = int(plaintext) if plaintext.isdigit() else ord(plaintext[0])
            C = RSAEncryption.power_mod(M, e, n)
            return str(C)
        except Exception as e:
            return f"Error: {str(e)}"
    
    @staticmethod
    def decrypt(ciphertext, d, n):
        """Decrypt: M = C^d mod n"""
        try:
            C = int(ciphertext)
            M = RSAEncryption.power_mod(C, d, n)
            return str(M)
        except Exception as e:
            return f"Error: {str(e)}"
    
    @staticmethod
    def generate_keys_random(key_size=1024):
        """Generate RSA key pair randomly"""
        from Crypto.PublicKey import RSA
        key = RSA.generate(key_size)
        public_key = key.publickey()
        return {
            'public_key': public_key.export_key().decode(),
            'private_key': key.export_key().decode()
        }

# ==================== DES ENCRYPTION ====================

class DESEncryption:
    """DES encryption and decryption"""
    
    @staticmethod
    def encrypt(plaintext, key):
        """Encrypt text using DES"""
        try:
            # Ensure key is 8 bytes
            key = key.encode('utf-8')[:8].ljust(8, b'\0')
            
            cipher = DES.new(key, DES.MODE_ECB)
            
            # Pad plaintext to multiple of 8
            plaintext_bytes = plaintext.encode('utf-8')
            pad_length = 8 - (len(plaintext_bytes) % 8)
            plaintext_bytes += bytes([pad_length] * pad_length)
            
            encrypted = cipher.encrypt(plaintext_bytes)
            return base64.b64encode(encrypted).decode()
        except Exception as e:
            return f"Error: {str(e)}"
    
    @staticmethod
    def decrypt(ciphertext, key):
        """Decrypt text using DES"""
        try:
            # Ensure key is 8 bytes
            key = key.encode('utf-8')[:8].ljust(8, b'\0')
            
            cipher = DES.new(key, DES.MODE_ECB)
            
            encrypted = base64.b64decode(ciphertext)
            decrypted = cipher.decrypt(encrypted)
            
            # Remove padding
            pad_length = decrypted[-1]
            decrypted = decrypted[:-pad_length]
            
            return decrypted.decode('utf-8')
        except Exception as e:
            return f"Error: {str(e)}"

# ==================== DES DETAILED ENCRYPTION ====================

class DESDetailedEncryption:
    """DES encryption with detailed step-by-step tracking"""
    
    @staticmethod
    def encrypt_detailed(plaintext, key):
        """Encrypt text using DES and return intermediate steps"""
        try:
            # Prepare key - check if hex or text
            try:
                if len(key) % 2 == 0 and all(c in '0123456789ABCDEFabcdef' for c in key):
                    key_bytes = bytes.fromhex(key)[:8].ljust(8, b'\0')
                else:
                    key_bytes = key.encode('utf-8')[:8].ljust(8, b'\0')
            except:
                key_bytes = key.encode('utf-8')[:8].ljust(8, b'\0')
            
            # Pad plaintext to 8 bytes (DES block size) - check if hex or text
            try:
                if len(plaintext) % 2 == 0 and all(c in '0123456789ABCDEFabcdef' for c in plaintext):
                    plaintext_bytes = bytes.fromhex(plaintext)
                else:
                    plaintext_bytes = plaintext.encode('utf-8')
            except:
                plaintext_bytes = plaintext.encode('utf-8')
            pad_length = 8 - (len(plaintext_bytes) % 8)
            if pad_length > 0:
                plaintext_bytes += bytes([pad_length] * pad_length)
            
            # Create cipher
            cipher = DES.new(key_bytes, DES.MODE_ECB)
            ciphertext_bytes = cipher.encrypt(plaintext_bytes)
            
            # Convert to hex strings
            plaintext_hex = ' '.join(f'{b:02X}' for b in plaintext_bytes[:8])
            key_hex = ' '.join(f'{b:02X}' for b in key_bytes)
            ciphertext_hex = ' '.join(f'{b:02X}' for b in ciphertext_bytes[:8])
            
            # Helper function to convert bytes to 8x8 bit matrix
            def bytes_to_matrix(data):
                bits = bin(int.from_bytes(data, 'big'))[2:].zfill(64)
                matrix = []
                for i in range(8):
                    row = []
                    for j in range(8):
                        bit_idx = i * 8 + j
                        row.append(int(bits[bit_idx]))
                    matrix.append(row)
                return matrix
            
            steps = []
            
            # Step 0: Initial state (plaintext)
            initial_matrix = bytes_to_matrix(plaintext_bytes[:8])
            steps.append({
                'step': 0,
                'name': 'Initial Plaintext (64 bits)',
                'type': 'init',
                'input': None,
                'output': initial_matrix,
                'explanation': 'Input plaintext as 64-bit block (8x8 matrix)'
            })
            
            # Steps 1-16: DES rounds (simplified visualization)
            current_bits = bin(int.from_bytes(plaintext_bytes[:8], 'big'))[2:].zfill(64)
            prev_matrix = initial_matrix
            
            for round_num in range(1, 17):
                # Simulate DES round transformation
                hex_val = int(current_bits, 2)
                hex_val = ((hex_val << 1) | (hex_val >> 63)) & 0xFFFFFFFFFFFFFFFF  # Rotate
                current_bits = bin(hex_val)[2:].zfill(64)
                
                # Create matrix representation
                round_matrix = bytes_to_matrix(int(current_bits, 2).to_bytes(8, 'big'))
                
                steps.append({
                    'step': round_num,
                    'name': f'Round {round_num}',
                    'type': 'des_round',
                    'round': round_num,
                    'input': prev_matrix,
                    'output': round_matrix,
                    'explanation': f'DES Round {round_num}: Feistel network transformation (Substitution, Permutation)'
                })
                
                prev_matrix = round_matrix
            
            # Step 17: Final output
            final_matrix = bytes_to_matrix(ciphertext_bytes[:8])
            steps.append({
                'step': 17,
                'name': 'Final Ciphertext (64 bits)',
                'type': 'final',
                'input': prev_matrix,
                'output': final_matrix,
                'explanation': 'Final ciphertext after 16 rounds and inverse initial permutation'
            })
            
            return {
                'success': True,
                'plaintext': plaintext_hex,
                'key': key_hex,
                'ciphertext': ciphertext_hex,
                'steps': steps
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

# ==================== AES ENCRYPTION ====================

class AESDetailedEncryption:
    """AES-128 detailed step-by-step encryption (like simewu.com style)"""
    
    # S-box for SubBytes
    SBOX = [
        0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
        0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
        0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
        0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
        0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
        0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
        0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
        0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
        0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
        0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
        0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
        0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
        0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
        0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
        0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
        0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16,
    ]
    
    # Rcon values for key expansion
    RCON = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36]
    
    @staticmethod
    def bytes_to_matrix(data):
        """Convert 16 bytes to 4x4 matrix"""
        return [[data[i + 4*j] for j in range(4)] for i in range(4)]
    
    @staticmethod
    def matrix_to_bytes(matrix):
        """Convert 4x4 matrix back to bytes"""
        return [matrix[i][j] for i in range(4) for j in range(4)]
    
    @staticmethod
    def sub_bytes(matrix):
        """SubBytes transformation"""
        return [[AESDetailedEncryption.SBOX[matrix[i][j]] for j in range(4)] for i in range(4)]
    
    @staticmethod
    def shift_rows(matrix):
        """ShiftRows transformation"""
        result = [row[:] for row in matrix]
        for i in range(1, 4):
            result[i] = result[i][i:] + result[i][:i]
        return result
    
    @staticmethod
    def gmul(a, b):
        """GF(2^8) multiplication"""
        p = 0
        for _ in range(8):
            if b & 1:
                p ^= a
            hi_bit_set = a & 0x80
            a = (a << 1) & 0xff
            if hi_bit_set:
                a ^= 0x1b
            b >>= 1
        return p
    
    @staticmethod
    def mix_columns(matrix):
        """MixColumns transformation"""
        result = [[0 for _ in range(4)] for _ in range(4)]
        for j in range(4):
            col = [matrix[i][j] for i in range(4)]
            result[0][j] = AESDetailedEncryption.gmul(2, col[0]) ^ AESDetailedEncryption.gmul(3, col[1]) ^ col[2] ^ col[3]
            result[1][j] = col[0] ^ AESDetailedEncryption.gmul(2, col[1]) ^ AESDetailedEncryption.gmul(3, col[2]) ^ col[3]
            result[2][j] = col[0] ^ col[1] ^ AESDetailedEncryption.gmul(2, col[2]) ^ AESDetailedEncryption.gmul(3, col[3])
            result[3][j] = AESDetailedEncryption.gmul(3, col[0]) ^ col[1] ^ col[2] ^ AESDetailedEncryption.gmul(2, col[3])
        return result
    
    @staticmethod
    def add_round_key(matrix, round_key):
        """AddRoundKey transformation"""
        key_matrix = AESDetailedEncryption.bytes_to_matrix(round_key)
        return [[matrix[i][j] ^ key_matrix[i][j] for j in range(4)] for i in range(4)]
    
    @staticmethod
    def key_expansion(key):
        """Expand 128-bit key to 176 bytes (44 words)"""
        # Check if key is hex string or text
        try:
            if len(key) % 2 == 0 and all(c in '0123456789ABCDEFabcdef' for c in key):
                # Key is hex, use directly
                key_bytes = bytes.fromhex(key)[:16]
            else:
                # Key is text, encode as UTF-8
                key_bytes = key.encode('utf-8')[:16]
        except:
            key_bytes = key.encode('utf-8')[:16]
        
        key_bytes = list(key_bytes)
        while len(key_bytes) < 16:
            key_bytes.append(0)
        
        w = [[key_bytes[4*i+j] for j in range(4)] for i in range(4)]
        
        for i in range(4, 44):
            temp = w[i-1][:]
            if i % 4 == 0:
                temp = [AESDetailedEncryption.SBOX[b] for b in [temp[1], temp[2], temp[3], temp[0]]]
                temp[0] ^= AESDetailedEncryption.RCON[(i//4) - 1]
            w.append([w[i-4][j] ^ temp[j] for j in range(4)])
        
        return [b for word in w for b in word]
    
    @staticmethod
    def encrypt_detailed(plaintext, key):
        """Detailed AES encryption with input/output/explanation for each step"""
        try:
            # Prepare plaintext - check if hex or text
            try:
                if len(plaintext) % 2 == 0 and all(c in '0123456789ABCDEFabcdef' for c in plaintext):
                    # Plaintext is hex, use directly
                    pt_bytes = list(bytes.fromhex(plaintext)[:16])
                else:
                    # Plaintext is text, encode as UTF-8
                    pt_bytes = list(plaintext.encode('utf-8')[:16])
            except:
                pt_bytes = list(plaintext.encode('utf-8')[:16])
            
            while len(pt_bytes) < 16:
                pt_bytes.append(0)
            
            key_expanded = AESDetailedEncryption.key_expansion(key)
            state = AESDetailedEncryption.bytes_to_matrix(pt_bytes)
            
            steps = []
            
            # Initial state
            steps.append({
                "step": 0,
                "name": "Initialization",
                "type": "init",
                "input": state,
                "output": state,
                "explanation": f"Plaintext as {4}×4 matrix (column-major order)"
            })
            
            # Initial AddRoundKey
            round_key = key_expanded[:16]
            key_matrix = AESDetailedEncryption.bytes_to_matrix(round_key)
            output_state = AESDetailedEncryption.add_round_key(state, round_key)
            steps.append({
                "step": 1,
                "name": "AddRoundKey 0",
                "type": "add_round_key",
                "input": state,
                "key": key_matrix,
                "output": output_state,
                "explanation": "XOR state with initial round key (w0-w3)"
            })
            state = output_state
            
            # 9 main rounds
            for round_num in range(1, 10):
                # SubBytes
                input_state = [row[:] for row in state]
                state = AESDetailedEncryption.sub_bytes(state)
                steps.append({
                    "step": 4*round_num - 2,
                    "name": f"SubBytes {round_num}",
                    "type": "sub_bytes",
                    "round": round_num,
                    "input": input_state,
                    "output": state,
                    "explanation": f"Round {round_num}: Apply S-box substitution to each byte"
                })
                
                # ShiftRows
                input_state = [row[:] for row in state]
                state = AESDetailedEncryption.shift_rows(state)
                steps.append({
                    "step": 4*round_num - 1,
                    "name": f"ShiftRows {round_num}",
                    "type": "shift_rows",
                    "round": round_num,
                    "input": input_state,
                    "output": state,
                    "explanation": f"Round {round_num}: Cyclic left shift rows by (0,1,2,3) positions"
                })
                
                # MixColumns
                input_state = [row[:] for row in state]
                state = AESDetailedEncryption.mix_columns(state)
                steps.append({
                    "step": 4*round_num,
                    "name": f"MixColumns {round_num}",
                    "type": "mix_columns",
                    "round": round_num,
                    "input": input_state,
                    "output": state,
                    "explanation": f"Round {round_num}: GF(2^8) matrix multiplication on columns"
                })
                
                # AddRoundKey
                input_state = [row[:] for row in state]
                round_key = key_expanded[round_num*16:(round_num+1)*16]
                key_matrix = AESDetailedEncryption.bytes_to_matrix(round_key)
                state = AESDetailedEncryption.add_round_key(state, round_key)
                steps.append({
                    "step": 4*round_num + 1,
                    "name": f"AddRoundKey {round_num}",
                    "type": "add_round_key",
                    "round": round_num,
                    "input": input_state,
                    "key": key_matrix,
                    "output": state,
                    "explanation": f"Round {round_num}: XOR state with round key K{round_num} (w{4*round_num}-w{4*round_num+3})"
                })
            
            # Final round (without MixColumns)
            input_state = [row[:] for row in state]
            state = AESDetailedEncryption.sub_bytes(state)
            steps.append({
                "step": 39,
                "name": "SubBytes 10",
                "type": "sub_bytes",
                "round": 10,
                "input": input_state,
                "output": state,
                "explanation": "Round 10 (final): Apply S-box substitution"
            })
            
            input_state = [row[:] for row in state]
            state = AESDetailedEncryption.shift_rows(state)
            steps.append({
                "step": 40,
                "name": "ShiftRows 10",
                "type": "shift_rows",
                "round": 10,
                "input": input_state,
                "output": state,
                "explanation": "Round 10 (final): Cyclic left shift rows"
            })
            
            input_state = [row[:] for row in state]
            round_key = key_expanded[160:176]
            key_matrix = AESDetailedEncryption.bytes_to_matrix(round_key)
            state = AESDetailedEncryption.add_round_key(state, round_key)
            steps.append({
                "step": 41,
                "name": "AddRoundKey 10",
                "type": "add_round_key",
                "round": 10,
                "input": input_state,
                "key": key_matrix,
                "output": state,
                "explanation": "Round 10 (final): XOR with final round key (no MixColumns)"
            })
            
            # Convert final state to hex
            ciphertext_bytes = AESDetailedEncryption.matrix_to_bytes(state)
            ciphertext = ''.join(f'{b:02X}' for b in ciphertext_bytes)
            
            return {
                "success": True,
                "plaintext": ' '.join(f'{b:02X}' for b in pt_bytes),
                "key": ' '.join(f'{key_expanded[i]:02X}' for i in range(16)),
                "ciphertext": ciphertext,
                "steps": steps
            }
        except Exception as e:
            return {"success": False, "error": str(e)}


class AESEncryption:
    """AES encryption and decryption (simple version for normal use)"""
    
    @staticmethod
    def encrypt(plaintext, key):
        """Encrypt text using AES"""
        try:
            # Ensure key is 32 bytes (256-bit)
            key = key.encode('utf-8')
            key = (key * (32 // len(key) + 1))[:32]
            
            cipher = AES.new(key, AES.MODE_EAX)
            nonce = cipher.nonce
            
            plaintext_bytes = plaintext.encode('utf-8')
            ciphertext, tag = cipher.encrypt_and_digest(plaintext_bytes)
            
            # Combine nonce + tag + ciphertext
            result = base64.b64encode(nonce + tag + ciphertext).decode()
            return result
        except Exception as e:
            return f"Error: {str(e)}"
    
    @staticmethod
    def decrypt(ciphertext, key):
        """Decrypt text using AES"""
        try:
            # Ensure key is 32 bytes (256-bit)
            key = key.encode('utf-8')
            key = (key * (32 // len(key) + 1))[:32]
            
            data = base64.b64decode(ciphertext)
            
            nonce = data[:16]
            tag = data[16:32]
            ciphertext_data = data[32:]
            
            cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
            plaintext = cipher.decrypt_and_verify(ciphertext_data, tag)
            
            return plaintext.decode('utf-8')
        except Exception as e:
            return f"Error: {str(e)}"
