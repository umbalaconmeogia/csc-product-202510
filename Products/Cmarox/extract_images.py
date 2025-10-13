# -*- coding: utf-8 -*-
"""Quick script to extract images from the local PowerPoint file"""
import sys
import os
import io
from zipfile import ZipFile
import glob

# Force UTF-8
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# Find the PPTX file in current directory
pptx_files = glob.glob("*.pptx")
pptx_files = [f for f in pptx_files if not f.startswith("~$")]

if not pptx_files:
    print("❌ No PowerPoint file found in current directory")
    sys.exit(1)

pptx_file = pptx_files[0]
print(f"📂 Found: {pptx_file}")

# Extract images
try:
    with ZipFile(pptx_file, 'r') as zip_ref:
        # Find all media files
        media_files = [f for f in zip_ref.namelist() if f.startswith('ppt/media/')]
        
        if not media_files:
            print("⚠️  No images found in PowerPoint file")
            sys.exit(0)
        
        print(f"📸 Extracting {len(media_files)} images...")
        
        for media_file in media_files:
            filename = os.path.basename(media_file)
            file_data = zip_ref.read(media_file)
            
            with open(filename, 'wb') as f:
                f.write(file_data)
            
            print(f"   ✓ {filename}")
        
        print(f"\n✅ Extracted {len(media_files)} images successfully!")
        
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

