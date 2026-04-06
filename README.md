# 🔐 Ứng Dụng Mã Hóa Dữ Liệu - Encryption Web Application

Một ứng dụng web hoàn chỉnh để mã hóa và giải mã dữ liệu sử dụng các phương pháp mã hóa khác nhau.

## 📋 Tính Năng

Ứng dụng hỗ trợ các loại mã hóa sau:

1. **Caesar Cipher (Mã Hóa Caesar)**
   - Thay thế từng ký tự bằng ký tự cách nó một số vị trí cố định
   - Tham số: Dịch chuyển (Shift)

2. **Vigenere Cipher (Mã Hóa Vigenere)**
   - Sử dụng từ khóa để xác định dịch chuyển của mỗi ký tự
   - Tham số: Từ khóa

3. **Modulo Encryption (Mã Hóa Modulo)**
   - Sử dụng phép toán modulo để mã hóa dữ liệu
   - Tham số: Khóa, Modulo

4. **RSA Encryption (Mã Hóa RSA - Công Khai)**
   - Hệ thống mã hóa bất đối xứng
   - Tạo cặp khóa công khai-riêng tư
   - Tham số: Kích thước khóa (1024, 2048 bits)

5. **DES Encryption (Mã Hóa DES)**
   - Data Encryption Standard
   - Mã hóa khối sử dụng khóa 64 bit
   - Tham số: Khóa (8 ký tự)

6. **AES Encryption (Mã Hóa AES)**
   - Advanced Encryption Standard
   - Thuật toán mã hóa hiện đại
   - Tham số: Khóa (bất kỳ độ dài)

## 🚀 Cài Đặt và Chạy

### 1. Cài Đặt Dependencies

```bash
cd encryption_web
pip install -r requirements.txt
```

### 2. Chạy Ứng Dụng

```bash
python app.py
```

### 3. Mở Trình Duyệt

Truy cập `http://localhost:5000` trong trình duyệt của bạn.

## 📁 Cấu Trúc Dự Án

```
encryption_web/
├── app.py                      # Flask backend
├── encryption.py               # Module mã hóa
├── requirements.txt            # Dependencies
├── templates/
│   └── index.html              # Giao diện chính
└── static/
    ├── css/
    │   └── style.css           # CSS styling
    └── js/
        └── script.js           # JavaScript frontend
```

## 🔧 Cách Sử Dụng

### Caesar Cipher
1. Nhập dịch chuyển (Shift) - mặc định là 3
2. Nhập văn bản muốn mã hóa
3. Click "Mã Hóa" để mã hóa
4. Click "Giải Mã" để giải mã

### Vigenere Cipher
1. Nhập từ khóa (Key)
2. Nhập văn bản muốn mã hóa
3. Click "Mã Hóa" để mã hóa
4. Click "Giải Mã" để giải mã

### Modulo Encryption
1. Nhập Khóa và Modulo
2. Nhập văn bản muốn mã hóa
3. Click "Mã Hóa" để mã hóa
4. Click "Giải Mã" để giải mã

### RSA Encryption
1. Chọn kích thước khóa (1024 hoặc 2048 bits)
2. Click "Tạo Cặp Khóa"
3. Nhập văn bản muốn mã hóa
4. Click "Mã Hóa" (sử dụng khóa công khai)
5. Click "Giải Mã" (sử dụng khóa riêng tư)

### DES Encryption
1. Nhập khóa (8 ký tự)
2. Nhập văn bản muốn mã hóa
3. Click "Mã Hóa" để mã hóa
4. Click "Giải Mã" để giải mã

### AES Encryption
1. Nhập khóa (bất kỳ độ dài)
2. Nhập văn bản muốn mã hóa
3. Click "Mã Hóa" để mã hóa
4. Click "Giải Mã" để giải mã

## 🛠️ Yêu Cầu Hệ Thống

- Python 3.7+
- Flask
- pycryptodome

## 📝 Ghi Chú

- **Caesar & Vigenere**: Chỉ hoạt động tốt với ký tự chữ cái
- **RSA**: Hỗ trợ mã hóa văn bản dài bằng cách chia thành các khối
- **DES**: Khóa phải chính xác hoặc tự động được pad tới 8 ký tự
- **AES**: Sử dụng chế độ EAX với nonce ngẫu nhiên để bảo mật

## 📱 Đặc Điểm Giao Diện

- ✅ Thiết kế responsive (hoạt động tốt trên mobile)
- ✅ Giao diện hiện đại với gradient colors
- ✅ Chuyển động mượt mà (animations)
- ✅ Thông báo tức thời (notifications)
- ✅ Sao chép kết quả dễ dàng
- ✅ Hiển thị/ẩn mật khẩu

## 🔐 Bảo Mật

⚠️ **Lưu ý**: Ứng dụng này là cho mục đích học tập và thử nghiệm. Không sử dụng cho dữ liệu nhạy cảm trong production mà không kiểm tra kỹ lưỡng.

## 👨‍💻 Phát Triển

Để mở rộng ứng dụng:

1. **Thêm phương pháp mã hóa mới** trong `encryption.py`
2. **Thêm API endpoint** trong `app.py`
3. **Thêm UI** trong `templates/index.html`
4. **Thêm logic frontend** trong `static/js/script.js`

## 📞 Hỗ Trợ

Nếu bạn gặp vấn đề:

1. Kiểm tra xem tất cả dependencies đã được cài đặt
2. Đảm bảo Flask server đang chạy
3. Kiểm tra console browser để tìm lỗi JavaScript
4. Kiểm tra terminal để tìm lỗi Python

## 📄 License

Dự án này được tạo cho mục đích học tập.

---

**Tạo bởi**: GitHub Copilot
**Ngày**: 2024
