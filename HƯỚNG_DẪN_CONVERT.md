# Hướng Dẫn Convert PowerPoint sang Markdown với Tiếng Việt

## Vấn Đề
Khi sử dụng lệnh `markitdown` trực tiếp trên Windows PowerShell, tiếng Việt bị hiển thị sai do vấn đề encoding (console mặc định sử dụng cp932 thay vì UTF-8).

## Giải Pháp
Sử dụng script Python `convert_pptx_to_markdown.py` đã được tạo sẵn để convert với encoding UTF-8 đúng cách.

## Cách Sử Dụng

### 1. Convert với tên file mặc định (README.md)
```powershell
python3.12 convert_pptx_to_markdown.py "Products\5-ALA\5ALA Presentation tiếng Việt.pptx"
```
Kết quả sẽ được lưu vào file `README.md` trong cùng thư mục với script.

### 2. Convert với tên file tùy chỉnh
```powershell
python3.12 convert_pptx_to_markdown.py "đường/dẫn/file.pptx" "đường/dẫn/output.md"
```

### 3. Ví dụ cho các sản phẩm khác

**Acropass:**
```powershell
python3.12 convert_pptx_to_markdown.py "Products\Acropass\Quotation of Acropass Beauty_20205_ ver01.pptx" "Products\Acropass\README.md"
```

**Albumin:**
```powershell
python3.12 convert_pptx_to_markdown.py "Products\Albumin\Quotation of Albumin Drinking.pptx" "Products\Albumin\README.md"
```

**AmabiRes:**
```powershell
python3.12 convert_pptx_to_markdown.py "Products\AmabiRes\AmabiRis Quotation 2025_ver01.pptx" "Products\AmabiRes\README.md"
```

**Cmarox:**
```powershell
python3.12 convert_pptx_to_markdown.py "Products\Cmarox\Trace Mineral Cmarox Quotation_2025_Ver02.pptx" "Products\Cmarox\README.md"
```

**ProImmilk:**
```powershell
python3.12 convert_pptx_to_markdown.py "Products\ProImmilk\Quotation of ProImmilk.pptx" "Products\ProImmilk\README.md"
```

## Lưu Ý
- Script tự động xử lý encoding UTF-8 cho tiếng Việt
- Cảnh báo về ffmpeg có thể bỏ qua (chỉ cần khi file có audio/video)
- File đầu ra luôn được lưu với encoding UTF-8 không có BOM
- Script hoạt động với cả tên file có ký tự Unicode

## Yêu Cầu
- Python 3.12 (đã cài từ Microsoft Store)
- Package `markitdown` (đã cài: `pip install markitdown`)

## Khắc Phục Sự Cố

### Lỗi: "No module named 'markitdown'"
```powershell
pip install markitdown
```

### Lỗi: "python3.12 không được nhận dạng"
Sử dụng `python` thay vì `python3.12`:
```powershell
python convert_pptx_to_markdown.py "file.pptx"
```

### Lỗi: "File not found" với tên file có tiếng Việt
**Vấn đề:** PowerShell truyền tên file với encoding sai đến Python

**Giải pháp 1 (Khuyên dùng):** Chạy từ trong thư mục sản phẩm
```powershell
cd "Products\5-ALA"
python3.12 ..\..\convert_pptx_to_markdown.py "5ALA Presentation tiếng Việt.pptx" "README.md"
```

**Giải pháp 2:** Script đã có fallback - tự động tìm file bằng pattern matching
```
📝 Found file: 5ALA Presentation tiếng Việt.pptx
```

**Giải pháp 3:** Sử dụng `convert_all.ps1` - đã được tối ưu để xử lý vấn đề này

### Tiếng Việt vẫn bị lỗi
Đảm bảo bạn đang dùng script `convert_pptx_to_markdown.py` chứ KHÔNG dùng lệnh `markitdown` trực tiếp.

