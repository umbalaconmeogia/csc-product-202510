# Hướng Dẫn Xử Lý Hình Ảnh Khi Convert PowerPoint sang Markdown

## Vấn Đề

Khi sử dụng `markitdown` để convert PowerPoint sang Markdown, công cụ này:
- ✅ Tạo các tham chiếu hình ảnh trong Markdown (ví dụ: `![](Picture4.jpg)`)
- ❌ **KHÔNG** tự động trích xuất các file hình ảnh từ PowerPoint

## Giải Pháp

Có 3 cách để xử lý hình ảnh:

### Cách 1: Trích Xuất Thủ Công (Đơn Giản Nhất)

1. **Đổi tên file PowerPoint** từ `.pptx` thành `.zip`
   ```powershell
   Rename-Item "file.pptx" "file.zip"
   ```

2. **Giải nén file ZIP**
   - Click chuột phải → Extract All

3. **Lấy hình ảnh**
   - Vào thư mục: `ppt\media\`
   - Tất cả hình ảnh sẽ ở đây (image1.jpg, image2.png, v.v.)

4. **Copy hình ảnh** vào cùng thư mục với file `README.md`

5. **Đổi tên file PowerPoint** trở lại `.pptx`
   ```powershell
   Rename-Item "file.zip" "file.pptx"
   ```

### Cách 2: Dùng Script Python (Tự Động)

Tôi đã tạo sẵn script `extract_images.py` trong mỗi thư mục sản phẩm.

**Cách sử dụng:**
```powershell
cd "Products\5-ALA"
python3.12 extract_images.py
```

Script sẽ:
- Tự động tìm file `.pptx` trong thư mục hiện tại
- Trích xuất tất cả hình ảnh
- Lưu vào thư mục hiện tại với tên gốc (image1.png, image2.jpg, v.v.)

**Ví dụ output:**
```
📂 Found: 5ALA Presentation tiếng Việt.pptx
📸 Extracting 48 images...
   ✓ image1.png
   ✓ image2.jpg
   ...
✅ Extracted 48 images successfully!
```

### Cách 3: Script Tích Hợp (Nâng Cao)

Script `convert_pptx_to_markdown.py` đã được nâng cấp với tùy chọn `--extract-images`:

```powershell
python3.12 convert_pptx_to_markdown.py "file.pptx" "README.md" --extract-images
```

Lệnh này sẽ:
1. Convert PowerPoint sang Markdown
2. Tự động trích xuất tất cả hình ảnh
3. Lưu hình ảnh cùng thư mục với README.md

## Lưu Ý Quan Trọng ⚠️

### Vấn Đề Tên File

`markitdown` tạo tham chiếu với tên như:
- `Picture4.jpg`
- `object2.jpg`
- `Picture8.jpg`

Nhưng file thực tế trong PowerPoint có tên:
- `image1.png`
- `image2.jpg`
- `image3.jpeg`

**Giải pháp:**
1. Sau khi trích xuất, bạn có thể **giữ nguyên tên markitdown** và **đổi tên ảnh thực tế** cho khớp
2. Hoặc sử dụng script `fix_image_references.py` để tự động cập nhật tham chiếu

### Script Tạo File Ảnh Khớp Với README (Khuyên Dùng) ⭐

Cách đơn giản nhất: **Tạo copy của ảnh với tên đúng** mà README.md mong đợi

```powershell
cd "Products\5-ALA"
python3.12 create_dummy_images.py
```

Script sẽ:
- Phân tích các tham chiếu ảnh trong README.md
- Tạo copy các file ảnh với tên đúng (Picture4.jpg, object2.jpg, v.v.)
- Giữ nguyên file gốc (imageN.jpg)

**Ví dụ output:**
```
📋 README.md expects these images:
   - Picture4.jpg
   - Picture6.jpg
   - object2.jpg
   ...

📝 Mapping plan:
   image1.png → object2.jpg
   image3.jpeg → Picture4.jpg
   ...

✅ Done! Images are now available
```

### Script Đổi Tên Tự Động (Nâng Cao)

Nếu bạn muốn cập nhật README.md thay vì đổi tên ảnh:

```powershell
cd "Products\5-ALA"
python3.12 fix_image_references.py
```

Script sẽ:
- Đọc tất cả tham chiếu ảnh trong README.md
- Tìm tất cả file ảnh thực tế
- Cập nhật README.md với tên file thực tế
- Backup file gốc thành `README.md.backup`

## Quy Trình Khuyến Nghị 🌟

Để có kết quả tốt nhất, làm theo thứ tự:

### Bước 1: Convert PowerPoint
```powershell
cd D:\data\csc\csc-product-202510
python3.12 convert_pptx_to_markdown.py "Products\5-ALA\5ALA Presentation tiếng Việt.pptx" "Products\5-ALA\README.md"
```

### Bước 2: Trích Xuất Hình Ảnh
```powershell
cd "Products\5-ALA"
python3.12 extract_images.py
```

### Bước 3: Tạo File Ảnh Với Tên Đúng ⭐
```powershell
python3.12 create_dummy_images.py
```

✅ **Xong!** Giờ README.md sẽ hiển thị đúng hình ảnh khi xem trong Markdown viewer.

## Copy Script vào Thư Mục Sản Phẩm

Để tiện sử dụng, copy script vào từng thư mục:

```powershell
# Copy extract_images.py vào tất cả thư mục sản phẩm
Copy-Item "Products\5-ALA\extract_images.py" "Products\Acropass\"
Copy-Item "Products\5-ALA\extract_images.py" "Products\Albumin\"
Copy-Item "Products\5-ALA\extract_images.py" "Products\AmabiRes\"
Copy-Item "Products\5-ALA\extract_images.py" "Products\Cmarox\"
Copy-Item "Products\5-ALA\extract_images.py" "Products\ProImmilk\"
```

Hoặc dùng vòng lặp:
```powershell
Get-ChildItem -Path "Products" -Directory | ForEach-Object {
    Copy-Item "Products\5-ALA\extract_images.py" $_.FullName -Force
    Write-Host "Copied to $($_.Name)"
}
```

## Kiểm Tra Kết Quả

Sau khi trích xuất hình ảnh, kiểm tra:

```powershell
# Xem các tham chiếu ảnh trong README
Select-String -Path "README.md" -Pattern "!\[\]"

# Đếm số file ảnh
(Get-ChildItem -Filter "*.jpg","*.png","*.jpeg" | Measure-Object).Count
```

## Tóm Tắt

| Phương Pháp | Ưu Điểm | Nhược Điểm |
|-------------|---------|------------|
| **Thủ công (ZIP)** | Đơn giản, không cần code | Mất thời gian, dễ nhầm |
| **Script extract_images.py** | Tự động, nhanh | Cần Python |
| **Script tích hợp** | Làm tất cả trong 1 lệnh | Phức tạp hơn |

**Khuyến nghị:** Sử dụng **Script extract_images.py** - đơn giản và hiệu quả nhất!

