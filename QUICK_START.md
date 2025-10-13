# Quick Start - Convert PowerPoint sang Markdown

## TL;DR - Lệnh Nhanh

### Convert PowerPoint/Excel có tiếng Việt:
```powershell
# PowerPoint
python3.12 convert_pptx_to_markdown.py "Products\TênSảnPhẩm\file.pptx" "Products\TênSảnPhẩm\README.md"

# Excel
python3.12 convert_pptx_to_markdown.py "Products\TênSảnPhẩm\file.xlsx" "Products\TênSảnPhẩm\README.md"
```

### Trích xuất hình ảnh (chỉ cho PowerPoint):
```powershell
cd "Products\TênSảnPhẩm"
python3.12 extract_images.py
python3.12 create_dummy_images.py
```

## Quy Trình Đầy Đủ

### 1. Convert PowerPoint → Markdown
```powershell
# Ví dụ cho sản phẩm 5-ALA
python3.12 convert_pptx_to_markdown.py "Products\5-ALA\5ALA Presentation tiếng Việt.pptx" "Products\5-ALA\README.md"
```

### 2. Trích xuất hình ảnh
```powershell
cd "Products\5-ALA"
python3.12 extract_images.py
```

### 3. Tạo file ảnh với tên đúng
```powershell
python3.12 create_dummy_images.py
```

### 4. Xong! ✅
- File `README.md` đã có nội dung với tiếng Việt chính xác
- Tất cả hình ảnh đã được trích xuất
- Ảnh đã có tên đúng để hiển thị trong README

## Convert Tất Cả Sản Phẩm

### Acropass
```powershell
python3.12 convert_pptx_to_markdown.py "Products\Acropass\Quotation of Acropass Beauty_20205_ ver01.pptx" "Products\Acropass\README.md"
cd Products\Acropass
python3.12 extract_images.py
python3.12 create_dummy_images.py
cd ..\..
```

### Albumin
```powershell
python3.12 convert_pptx_to_markdown.py "Products\Albumin\Quotation of Albumin Drinking.pptx" "Products\Albumin\README.md"
cd Products\Albumin
python3.12 extract_images.py
python3.12 create_dummy_images.py
cd ..\..
```

### AmabiRes
```powershell
python3.12 convert_pptx_to_markdown.py "Products\AmabiRes\AmabiRis Quotation 2025_ver01.pptx" "Products\AmabiRes\README.md"
cd Products\AmabiRes
python3.12 extract_images.py
python3.12 create_dummy_images.py
cd ..\..
```

### Cmarox
```powershell
python3.12 convert_pptx_to_markdown.py "Products\Cmarox\Trace Mineral Cmarox Quotation_2025_Ver02.pptx" "Products\Cmarox\README.md"
cd Products\Cmarox
python3.12 extract_images.py
python3.12 create_dummy_images.py
cd ..\..
```

### ProImmilk
```powershell
python3.12 convert_pptx_to_markdown.py "Products\ProImmilk\Quotation of ProImmilk.pptx" "Products\ProImmilk\README.md"
cd Products\ProImmilk
python3.12 extract_images.py
python3.12 create_dummy_images.py
cd ..\..
```

### Cancer Products (Excel)
```powershell
# File Excel không cần trích xuất hình ảnh
python3.12 convert_pptx_to_markdown.py "Products\Quotation of Cancer Products\ODM-0EM 2025.xlsx" "Products\Quotation of Cancer Products\README.md"
```

## Lệnh Batch - Convert Tất Cả Cùng Lúc

Tạo file `convert_all.ps1`:

```powershell
# Convert all products
$products = @(
    @{Dir="Acropass"; File="Quotation of Acropass Beauty_20205_ ver01.pptx"; Type="pptx"},
    @{Dir="Albumin"; File="Quotation of Albumin Drinking.pptx"; Type="pptx"},
    @{Dir="AmabiRes"; File="AmabiRis Quotation 2025_ver01.pptx"; Type="pptx"},
    @{Dir="Cmarox"; File="Trace Mineral Cmarox Quotation_2025_Ver02.pptx"; Type="pptx"},
    @{Dir="ProImmilk"; File="Quotation of ProImmilk.pptx"; Type="pptx"},
    @{Dir="Quotation of Cancer Products"; File="ODM-0EM 2025.xlsx"; Type="xlsx"}
)

foreach ($product in $products) {
    Write-Host "`n=== Converting $($product.Dir) ===" -ForegroundColor Cyan
    
    $filePath = "Products\$($product.Dir)\$($product.File)"
    $mdPath = "Products\$($product.Dir)\README.md"
    
    # Convert to markdown
    python3.12 convert_pptx_to_markdown.py $filePath $mdPath
    
    # Extract images (only for PowerPoint files)
    if ($product.Type -eq "pptx") {
        Push-Location "Products\$($product.Dir)"
        python3.12 extract_images.py
        python3.12 create_dummy_images.py
        Pop-Location
    }
    
    Write-Host "✓ Completed $($product.Dir)`n" -ForegroundColor Green
}

Write-Host "`n=== All conversions completed! ===" -ForegroundColor Green
```

Chạy:
```powershell
.\convert_all.ps1
```

## Xử Lý Lỗi

### Lỗi: "No module named 'markitdown'"
```powershell
pip install markitdown
```

### Lỗi: Tiếng Việt hiển thị sai
➡️ Đảm bảo dùng script `convert_pptx_to_markdown.py`, KHÔNG dùng lệnh `markitdown` trực tiếp

### Lỗi: Không tìm thấy file
➡️ Kiểm tra đường dẫn và đảm bảo có dấu ngoặc kép cho đường dẫn có khoảng trắng

### Cảnh báo ffmpeg
➡️ Có thể bỏ qua. Nếu muốn loại bỏ:
```powershell
winget install --id Gyan.FFmpeg -e --silent
```
Sau đó khởi động lại PowerShell.

## Kiểm Tra Kết Quả

```powershell
# Xem nội dung README.md
Get-Content "Products\5-ALA\README.md" -Encoding UTF8 | Select-Object -First 20

# Đếm số ảnh đã trích xuất
(Get-ChildItem "Products\5-ALA" -Filter "*.jpg","*.png","*.jpeg").Count

# Xem các tham chiếu ảnh trong README
Select-String -Path "Products\5-ALA\README.md" -Pattern "!\[\]"
```

## Tài Liệu Chi Tiết

- **README.md** - Tổng quan dự án
- **HƯỚNG_DẪN_CONVERT.md** - Chi tiết về convert với tiếng Việt
- **XỬ_LÝ_HÌNH_ẢNH.md** - Chi tiết về xử lý hình ảnh
- **QUICK_START.md** - File này, hướng dẫn nhanh

## Cần Trợ Giúp?

Các lỗi thường gặp và cách xử lý đều có trong:
- [HƯỚNG_DẪN_CONVERT.md](HƯỚNG_DẪN_CONVERT.md#khc-phc-s-c)
- [XỬ_LÝ_HÌNH_ẢNH.md](XỬ_LÝ_HÌNH_ẢNH.md)

