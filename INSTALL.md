# 📖 Hướng Dẫn Cài Đặt và Chạy Ứng Dụng

## 🎯 Bước 1: Chuẩn Bị Thư Mục

Dự án đã được tạo tại: `d:\University\TTNT\BTCN\encryption_web\`

Cấu trúc thư mục:
```
encryption_web/
├── app.py
├── encryption.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── script.js
```

## 🔧 Bước 2: Cài Đặt Python Dependencies

### Trên Windows (PowerShell hoặc Command Prompt):

```powershell
# Chuyển vào thư mục dự án
cd d:\University\TTNT\BTCN\encryption_web

# Cài đặt virtual environment (tuỳ chọn nhưng khuyến nghị)
python -m venv venv

# Kích hoạt virtual environment
# Trên Windows:
.\venv\Scripts\Activate.ps1

# Hoặc nếu dùng Command Prompt:
venv\Scripts\activate.bat
```

### Cài đặt dependencies:

```bash
pip install -r requirements.txt
```

Lệnh này sẽ cài đặt:
- Flask (web framework)
- Werkzeug (Flask dependency)
- pycryptodome (cryptographic library)

## ▶️ Bước 3: Chạy Ứng Dụng

```bash
python app.py
```

Bạn sẽ thấy output tương tự:
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

## 🌐 Bước 4: Mở Ứng Dụng

Mở trình duyệt (Chrome, Firefox, Edge, Safari, v.v.) và truy cập:
```
http://localhost:5000
```

hoặc

```
http://127.0.0.1:5000
```

## 🎨 Bước 5: Sử Dụng Ứng Dụng

### Giao Diện Chính

1. **Thanh Menu** ở phía trên cùng với 6 nút chọn phương pháp mã hóa
2. **Form nhập liệu** tùy thuộc vào phương pháp được chọn
3. **Nút Mã Hóa / Giải Mã** để xử lý dữ liệu
4. **Kết quả** hiển thị trong vùng soạn thảo chỉ đọc

### Ví Dụ Sử Dụng 1: Caesar Cipher

1. Click nút "📝 Caesar"
2. Nhập dịch chuyển: `3`
3. Nhập văn bản: `Hello World`
4. Click "Mã Hóa"
5. Kết quả: `Khoor Zruog`
6. Để giải mã, click "Giải Mã" để quay lại văn bản gốc

### Ví Dụ Sử Dụng 2: Vigenere Cipher

1. Click nút "🔑 Vigenere"
2. Nhập từ khóa: `SECRET`
3. Nhập văn bản: `Hello World`
4. Click "Mã Hóa"
5. Kết quả sẽ hiển thị

### Ví Dụ Sử Dụng 3: RSA Encryption

1. Click nút "🔓 RSA"
2. Chọn kích thước khóa: `1024 bits` (hoặc 2048)
3. Click "Tạo Cặp Khóa" - cặp khóa sẽ được tạo
4. Nhập văn bản muốn mã hóa
5. Click "Mã Hóa" - sẽ mã hóa bằng khóa công khai
6. Click "Giải Mã" - sẽ giải mã bằng khóa riêng tư

## 🐛 Khắc Phục Sự Cố

### Lỗi: "No module named 'flask'"

**Giải pháp**: Cài đặt Flask
```bash
pip install Flask
```

### Lỗi: "No module named 'Crypto'"

**Giải pháp**: Cài đặt pycryptodome
```bash
pip install pycryptodome
```

### Cổng 5000 đã được sử dụng

**Giải pháp**: Chỉnh sửa app.py, dòng cuối cùng:
```python
# Thay từ:
app.run(debug=True, port=5000)

# Sang một cổng khác, ví dụ:
app.run(debug=True, port=8000)
```

### Không thấy CSS hoặc JavaScript

**Giải pháp**: 
- Đảm bảo cấu trúc thư mục đúng
- Làm mới trang (F5 hoặc Ctrl+Shift+R)
- Kiểm tra console browser (F12) để xem lỗi

## 📝 Các Tệp Quan Trọng

| Tệp | Mô Tả |
|-----|-------|
| `app.py` | Ứng dụng Flask chính, điểm vào của server |
| `encryption.py` | Các hàm mã hóa và giải mã |
| `templates/index.html` | Giao diện HTML |
| `static/css/style.css` | Kiểu dáng CSS |
| `static/js/script.js` | Xử lý sự kiện JavaScript |
| `requirements.txt` | Danh sách thư viện cần cài |

## 🔄 Quy Trình Hoạt Động

```
1. User nhập dữ liệu trong giao diện web
   ↓
2. JavaScript gửi request tới Flask backend (/api/encrypt)
   ↓
3. Python xử lý yêu cầu mã hóa
   ↓
4. Kết quả được gửi trở lại frontend
   ↓
5. JavaScript hiển thị kết quả trên giao diện
```

## 💡 Mẹo Hữu Ích

1. **Sao chép Kết Quả**: Click "Sao Chép" để copy kết quả vào clipboard
2. **Hiển thị Mật Khẩu**: Click nút 👁️ để xem/ẩn mật khẩu
3. **Xóa Dữ Liệu**: Click "Xóa" để xóa toàn bộ dữ liệu trong form
4. **Thử Lại**: Thay đổi thông số và mã hóa lại dễ dàng

## 🛑 Dừng Ứng Dụng

Để dừng server, nhấn `Ctrl+C` trong terminal/command prompt.

## 📚 Tham Khảo Thêm

- [Flask Documentation](https://flask.palletsprojects.com/)
- [pycryptodome Documentation](https://www.dlitz.net/software/pycryptodome/)
- Các tài liệu PDF yêu cầu thực hành được cung cấp

## ✅ Kiểm Tra Cài Đặt

Sau khi chạy ứng dụng, bạn có thể kiểm tra:

```bash
# Mở một terminal mới
curl http://localhost:5000
```

Nếu nhận được HTML response, ứng dụng đang chạy bình thường.

---

**Chúc bạn sử dụng ứng dụng vui vẻ! 🎉**
