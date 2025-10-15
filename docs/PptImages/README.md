# Nhúng ảnh toàn bộ các slide vào tài liệu Markdown

## Overview

Ta chuyển nội dung của file PowerPoint vào file Markdown. Để tiện lưu trữ lâu dài, ta muốn lưu lại ảnh chụp toàn bộ của slide vào trong tài liệu này để sau này có thể tham khảo nhanh chóng (hoặc AI trong tương lai có thể trực tiếp đọc hiểu nội dung từ file ảnh này).

Các bước thực hiện:
1. Convert toàn bộ file PowerPoint thành các file ảnh (dùng chức năng của PowerPoint).
2. Nhúng (embed) các ảnh đó vào vị trí đầu các slide trong Markdown (yêu cầu AI thực hiện).

## Convert file PowerPoint thành các file ảnh

TBD

## Nhúng file ảnh vào Markdown

Prompt
> File Products\5-ALA\README.md là file được convert nội dung từ file PowerPoint ra markdown. Trong markdown, thì mỗi slide của powerPoint được bắt đầu bằng dòng chữ kiểu <!-- Slide number: 1 -->.
> Ngoài ra, trong thư mục Products\5-ALA\ppt_images là ảnh chụp toàn bộ các slide của file powerpoint, đặt tên file theo số slide, kiểu selide_1.png cho slide 1.
> DƯới mỗi dòng phân trang trong file README.md (ví dụ <!-- Slide number: 1 -->), hãy chèn link ảnh của slide tương ứng (ví dụ như ![slide 1](ppt_images/slide_1.png) )