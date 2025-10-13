# csc-product-202510
Phân tích sản phẩm của CSC tháng 10/2025

## Sản Phẩm

Dự án này chứa thông tin chi tiết về các sản phẩm của CSC:

- **5-ALA** - Giải pháp giữ trọn Thanh Xuân (Neo Pharma JP)
- **Acropass** - Beauty patches
- **Albumin** - Albumin Drinking
- **AmabiRes** - Sản phẩm dinh dưỡng
- **Cmarox** - Trace Mineral supplement
- **N3 - Night Serum** - Serum chăm sóc da ban đêm
- **ProImmilk** - Sản phẩm sữa tăng cường miễn dịch
- **Quotation of Cancer Products** - Bảng báo giá ODM/OEM (18 sản phẩm)

## Chuyển Đổi PowerPoint/Excel sang Markdown

### Vấn Đề với Tiếng Việt

Khi sử dụng `markitdown` trực tiếp trên Windows, tiếng Việt thường bị hiển thị sai do vấn đề encoding.

❌ **KHÔNG nên dùng trực tiếp:**
```shell
markitdown 'file.pptx' > README.md
```

### Giải Pháp ✅

Sử dụng script Python `convert_pptx_to_markdown.py` đã được tối ưu cho tiếng Việt.

**PowerPoint:**
```shell
python3.12 convert_pptx_to_markdown.py "Products\5-ALA\5ALA Presentation tiếng Việt.pptx" "Products\5-ALA\README.md"
```

**Excel:**
```shell
python3.12 convert_pptx_to_markdown.py "Products\Quotation of Cancer Products\ODM-0EM 2025.xlsx" "Products\Quotation of Cancer Products\README.md"
```

### Cài Đặt

1. **Cài đặt Python 3.12** từ Microsoft Store (nếu chưa có)

2. **Cài đặt Markitdown:**
```shell
pip install markitdown
```

3. **Cài đặt FFmpeg** (tùy chọn, để tránh cảnh báo):
```shell
winget install --id Gyan.FFmpeg -e --silent
```
Sau đó khởi động lại PowerShell.

### Hướng Dẫn Chi Tiết

- **[QUICK_START.md](QUICK_START.md)** - ⚡ Bắt đầu nhanh với các lệnh cơ bản
- [HƯỚNG_DẪN_CONVERT.md](HƯỚNG_DẪN_CONVERT.md) - Hướng dẫn convert PowerPoint sang Markdown
- [XỬ_LÝ_HÌNH_ẢNH.md](XỬ_LÝ_HÌNH_ẢNH.md) - Hướng dẫn trích xuất và xử lý hình ảnh

## Trích Xuất Hình Ảnh

`markitdown` **không tự động trích xuất hình ảnh**. Để lấy hình ảnh từ PowerPoint:

### Cách Nhanh Nhất ⚡
```shell
cd Products\5-ALA
python3.12 extract_images.py
```

Script sẽ tự động tìm file PowerPoint và trích xuất tất cả hình ảnh.

### Xem Chi Tiết
Đọc file [XỬ_LÝ_HÌNH_ẢNH.md](XỬ_LÝ_HÌNH_ẢNH.md) để biết:
- Cách trích xuất thủ công
- Cách xử lý tên file ảnh không khớp
- Script tự động đổi tên và cập nhật tham chiếu

## Cấu Trúc Thư Mục

```
csc-product-202510/
├── Products/
│   ├── 5-ALA/
│   │   ├── 5ALA Presentation tiếng Việt.pptx
│   │   └── README.md
│   ├── Acropass/
│   ├── Albumin/
│   ├── AmabiRes/
│   ├── Cmarox/
│   ├── N3 - Night Serum/
│   └── ProImmilk/
├── convert_pptx_to_markdown.py  # Script chuyển đổi
└── HƯỚNG_DẪN_CONVERT.md         # Hướng dẫn chi tiết
```