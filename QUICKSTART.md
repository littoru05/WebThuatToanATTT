# ⚡ Quick Start Guide - Hướng Dẫn Nhanh

## 🎯 Bắt Đầu trong 5 Phút

### Bước 1️⃣: Cài Đặt (1 phút)
```powershell
cd d:\University\TTNT\BTCN\encryption_web
pip install -r requirements.txt
```

### Bước 2️⃣: Chạy (30 giây)
```bash
python app.py
```

### Bước 3️⃣: Truy Cập (30 giây)
Mở trình duyệt và vào: **http://localhost:5000**

✅ **Xong! Ứng dụng đang chạy!**

---

## 🎮 Sử Dụng Nhanh

### 📝 Caesar Cipher (30 giây)
```
1. Click nút "📝 Caesar"
2. Shift = 3
3. Text = "Hello"
4. Click "Mã Hóa"
5. Kết quả: "Khoor"
```

### 🔑 Vigenere Cipher (30 giây)
```
1. Click nút "🔑 Vigenere"
2. Key = "SECRET"
3. Text = "Hello"
4. Click "Mã Hóa"
5. Kết quả sẽ hiển thị
```

### 🔓 RSA Encryption (1 phút)
```
1. Click nút "🔓 RSA"
2. Click "Tạo Cặp Khóa"
3. Khóa công khai & riêng tư sẽ hiển thị
4. Nhập Text muốn mã hóa
5. Click "Mã Hóa"
6. Để giải mã, click "Giải Mã"
```

### 🔒 DES Encryption (30 giây)
```
1. Click nút "🔒 DES"
2. Key = "12345678" (8 ký tự)
3. Text = "Hello World"
4. Click "Mã Hóa"
5. Kết quả Base64 hiển thị
```

### 🛡️ AES Encryption (30 giây)
```
1. Click nút "🛡️ AES"
2. Key = "MySecretKey"
3. Text = "Hello World"
4. Click "Mã Hóa"
5. Kết quả Base64 hiển thị
```

---

## 💡 Mẹo Nhanh

| Tính Năng | Cách Sử Dụng |
|-----------|------------|
| **Sao Chép Kết Quả** | Click nút "Sao Chép" |
| **Hiển Thị Mật Khẩu** | Click nút "👁️ Hiển Thị" |
| **Xóa Dữ Liệu** | Click nút "Xóa" |
| **Chuyển Phương Pháp** | Click nút trong menu trên |
| **Giải Mã** | Paste text mã hóa vào, click "Giải Mã" |

---

## ❓ FAQ (Câu Hỏi Thường Gặp)

**Q1: Làm sao để dừng ứng dụng?**
```
A: Nhấn Ctrl+C trong terminal
```

**Q2: Muốn chạy trên cổng khác?**
```
A: Chỉnh sửa app.py, dòng cuối:
   app.run(debug=True, port=8000)
```

**Q3: RSA key đủ lớn không?**
```
A: 1024 bits dùng được, nhưng 2048 bits an toàn hơn
```

**Q4: Dữ liệu có được lưu không?**
```
A: Không, mỗi session là mới. Sau khi đóng không còn
```

**Q5: Có hỗ trợ file lớn không?**
```
A: Còn tùy phương pháp. RSA có giới hạn kích thước
```

---

## 🔥 Troubleshooting Nhanh

| Vấn Đề | Giải Pháp |
|--------|----------|
| Module not found | `pip install -r requirements.txt` |
| Port 5000 occupied | Dùng port khác (xem Q2) |
| CSS/JS không load | Làm mới (Ctrl+Shift+R) |
| Lỗi mã hóa | Check lại input parameters |

---

## 📁 File Cần Biết

| File | Chỉnh Sửa Khi |
|------|----------|
| `app.py` | Muốn thêm API |
| `encryption.py` | Muốn thêm phương pháp |
| `index.html` | Muốn chỉnh UI |
| `style.css` | Muốn đổi giao diện |
| `script.js` | Muốn thay đổi logic |

---

## 🚀 Ví Dụ Thực Tế

### Ví dụ 1: Mã hóa Tin Nhắn
```
Text: "Tôi yêu cryptography"
Phương pháp: Caesar (shift=5)
Kết quả: "Ytôi dkz hduryptsgzald"
```

### Ví dụ 2: Gửi Tin Bí Mật
```
1. Tạo RSA keys
2. Chia khóa công khai cho người khác
3. Người khác dùng khóa công khai để mã hóa tin
4. Bạn dùng khóa riêng để giải mã
5. Chỉ bạn mới biết tin nhắn!
```

### Ví dụ 3: Mã Hóa File
```
1. Đọc nội dung file trong Notepad
2. Copy vào text area
3. Chọn phương pháp (AES an toàn nhất)
4. Mã hóa
5. Lưu kết quả vào file mới
```

---

## ✨ Điểm Đặc Biệt

🎨 **Đẹp**: Gradient colors, animations mượt
📱 **Mobile-Friendly**: Dùng tốt trên phone/tablet
⚡ **Nhanh**: Xử lý ngay lập tức
🔒 **An Toàn**: Dùng thư viện crypto chính thức
📚 **Đầy Đủ**: 6 phương pháp khác nhau

---

## 📚 Thêm Thông Tin

Xem file `README.md` hoặc `INSTALL.md` để chi tiết hơn.

---

**Chúc bạn thành công! 🎉**

*Nếu có vấn đề, kiểm tra terminal xem có lỗi Python không.*
