# 🔐 Hướng Dẫn Sử Dụng Ứng Dụng Mã Hóa

## 📋 Danh Sách Bài Tập Đã Implement

### 1. **PLAYFAIR CIPHER** (Nhóm 4 - Mã Hóa Cổ Điển)
- ✅ Mã hóa: `POST /api/playfair/encrypt`
- ✅ Giải mã: `POST /api/playfair/decrypt`
- Input: 
  - `plaintext`: Văn bản gốc
  - `key`: Từ khóa (sẽ được chuẩn hóa thành 5x5 ma trận)
- Output: Văn bản mã hóa/giải mã

**Ví dụ:**
```
Plaintext: "HELLO"
Key: "SECRET"
Ciphertext: "XYZA..."
```

---

### 2. **MODULO OPERATIONS** (10 Bài Tập)

#### 2.1 Bài 1: Lũy Thừa Modulo (Hạ Bậc)
- **API:** `POST /api/modulo/exercise1`
- **Input:** a, m, n
- **Output:** b = a^m mod n
- **URL:** http://localhost:5000 → Modulo → Ex1

#### 2.2 Bài 2: Nghịch Đảo Modulo
- **API:** `POST /api/modulo/exercise2`
- **Input:** a, n
- **Output:** x = a^-1 mod n
- **Phương Pháp:** Extended Euclidean Algorithm

#### 2.3 Bài 3: Định Lý Fermat
- **API:** `POST /api/modulo/exercise3`
- **Input:** a, m, n (n phải là số nguyên tố)
- **Output:** b = a^m mod n

#### 2.4 Bài 4: Hàm Euler φ(n)
- **API:** `POST /api/modulo/exercise4`
- **Input:** n
- **Output:** φ(n) = tổng số nguyên nhỏ hơn n mà nguyên tố cùng nhau với n

#### 2.5 Bài 5: Định Lý Euler
- **API:** `POST /api/modulo/exercise5`
- **Input:** a, m, n
- **Output:** b = a^m mod n (sử dụng φ(n) để tối ưu)

#### 2.6 Bài 6: Định Lý Số Dư Trung Hoa (CRT) Lũy Thừa
- **API:** `POST /api/modulo/exercise6`
- **Input:** a, k, n
- **Output:** b = a^k mod n

#### 2.7 Bài 7: Giải Hệ Phương Trình Modulo (CRT)
- **API:** `POST /api/modulo/exercise7`
- **Input:** m1, m2, m3, a1, a2, a3
- **Output:** x thỏa mãn:
  - x ≡ a1 (mod m1)
  - x ≡ a2 (mod m2)
  - x ≡ a3 (mod m3)

#### 2.8 Bài 8: Kiểm Tra Căn Nguyên Thủy
- **API:** `POST /api/modulo/exercise8`
- **Input:** a, n
- **Output:** Boolean (a có phải căn nguyên thủy của n?)

#### 2.9 Bài 9: Logarithm Rời Rạc
- **API:** `POST /api/modulo/exercise9`
- **Input:** a, b, n
- **Output:** k = log_a(b) mod n
- **Phương Pháp:** Baby-step Giant-step

#### 2.10 Bài 10: Biểu Thức Modulo
- **API:** `POST /api/modulo/exercise10`
- **Input:** a, b, x, y, n
- **Output:**
  - A1 = (a*x + b*y) mod n
  - A2 = (a*x - b*y) mod n
  - A3 = (a*x * b*y) mod n
  - A4 = (b*y)^-1 mod n
  - A5 = (a*x / b*y) mod n

---

### 3. **RSA ENCRYPTION** (Bài Toán 2 - Nhóm k=4)

#### 3.1 Tạo Khóa RSA
- **API:** `POST /api/rsa/generate`
- **Input:** p (số nguyên tố), q (số nguyên tố), e (mũ công khai)
- **Output:** 
  - n = p * q
  - φ(n) = (p-1)(q-1)
  - d = e^-1 mod φ(n) (khóa riêng tư)
  - Public Key: {e, n}
  - Private Key: {d, n}

**Ví dụ:**
```
p = 61, q = 53, e = 17
→ n = 3233
→ φ(n) = 3120
→ d = 2753
```

#### 3.2 Mã Hóa RSA
- **API:** `POST /api/rsa/encrypt`
- **Input:** plaintext, e, n
- **Output:** C = M^e mod n

#### 3.3 Giải Mã RSA
- **API:** `POST /api/rsa/decrypt`
- **Input:** ciphertext, d, n
- **Output:** M = C^d mod n

---

### 4. **DES ENCRYPTION**
- ✅ Existing: `/api/des/encrypt` & `/api/des/decrypt`

### 5. **AES ENCRYPTION**
- ✅ Existing: `/api/aes/encrypt` & `/api/aes/decrypt`

---

## 🚀 Cách Chạy

1. **Cài đặt dependencies:**
```bash
pip install -r requirements.txt
```

2. **Chạy ứng dụng:**
```bash
python app.py
```

3. **Mở trình duyệt:**
```
http://localhost:5000
```

4. **Test các API bằng cURL hoặc Postman:**
```bash
# Playfair encrypt
curl -X POST http://localhost:5000/api/playfair/encrypt \
  -H "Content-Type: application/json" \
  -d '{"plaintext":"HELLO","key":"SECRET"}'

# Modulo exercise 1
curl -X POST http://localhost:5000/api/modulo/exercise1 \
  -H "Content-Type: application/json" \
  -d '{"a":2,"m":5,"n":13}'

# RSA generate
curl -X POST http://localhost:5000/api/rsa/generate \
  -H "Content-Type: application/json" \
  -d '{"p":61,"q":53,"e":17}'
```

---

## 📊 Test Data

### Playfair:
- Plaintext: "HELLO"
- Key: "SECRETKEY"

### Modulo:
- Ex1: a=2, m=5, n=13 → 32 mod 13 = 6
- Ex2: a=3, n=11 → 3^-1 mod 11 = 4
- Ex4: n=10 → φ(10) = 4
- Ex8: a=2, n=5 → True (căn nguyên thủy)

### RSA:
- p=61, q=53, e=17
- n=3233, φ(n)=3120, d=2753
- Plaintext: 65 (ASCII 'A')
- Ciphertext: 65^17 mod 3233 = ...

---

## 🎯 Kết Thúc

Ứng dụng hỗ trợ đầy đủ các bài tập theo yêu cầu:
- ✅ Playfair (nhóm 4 mã cổ điển)
- ✅ 10 bài Modulo operations
- ✅ RSA bài toán 2 (k=4)
- ✅ DES, AES

**Hãy test bằng giao diện web hoặc API trực tiếp!**
