#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert PowerPoint files to Markdown with proper UTF-8 encoding for Vietnamese text
Usage: python convert_pptx_to_markdown.py <input.pptx> [output.md] [--extract-images]
"""
import sys
import io
import os
import shutil
from zipfile import ZipFile
from pathlib import Path

# Force UTF-8 encoding for Windows console
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

try:
    from markitdown import MarkItDown
except ImportError:
    print("❌ Error: markitdown is not installed.")
    print("Install it with: pip install markitdown")
    sys.exit(1)

def extract_images_from_pptx(pptx_file, output_dir):
    """Extract all images from PowerPoint file to output directory"""
    try:
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # PowerPoint files are actually ZIP archives
        with ZipFile(pptx_file, 'r') as zip_ref:
            # List all files in the archive
            file_list = zip_ref.namelist()
            
            # Find all media files (images are in ppt/media/)
            media_files = [f for f in file_list if f.startswith('ppt/media/')]
            
            if not media_files:
                print("⚠️  No images found in PowerPoint file")
                return 0
            
            print(f"📸 Extracting {len(media_files)} images...")
            
            # Extract each media file
            for media_file in media_files:
                # Get just the filename (e.g., "image1.png" from "ppt/media/image1.png")
                filename = os.path.basename(media_file)
                
                # Read the file from ZIP
                file_data = zip_ref.read(media_file)
                
                # Write to output directory
                output_path = os.path.join(output_dir, filename)
                with open(output_path, 'wb') as f:
                    f.write(file_data)
                
                print(f"   ✓ {filename}")
            
            return len(media_files)
            
    except Exception as e:
        print(f"❌ Error extracting images: {e}")
        import traceback
        traceback.print_exc()
        return 0

def convert_pptx_to_markdown(input_file, output_file=None, extract_images=False):
    """Convert PowerPoint file to Markdown with proper UTF-8 encoding"""
    
    # Check if input file exists
    if not os.path.exists(input_file):
        # Try to find file with glob pattern (handles encoding issues)
        import glob
        pattern = input_file.replace('tiếng Việt', '*').replace('ti?ng Vi?t', '*').replace('ti蘯ｿng Vi盻㏄', '*')
        matches = glob.glob(pattern)
        if matches:
            input_file = matches[0]
            print(f"📝 Found file: {input_file}")
        else:
            print(f"❌ Error: File '{input_file}' not found")
            print(f"   Tried pattern: {pattern}")
            sys.exit(1)
    
    # Default output file name
    if output_file is None:
        base_name = os.path.splitext(input_file)[0]
        output_file = "README.md"
    
    try:
        # Convert the PowerPoint file
        print(f"🔄 Converting '{input_file}'...")
        md = MarkItDown()
        result = md.convert(input_file)
        
        # Write to file with UTF-8 encoding (no BOM)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result.text_content)
        
        print(f"✅ Conversion completed successfully!")
        print(f"✅ Output saved to: {output_file}")
        print(f"✅ Converted {len(result.text_content):,} characters")
        
        # Extract images if requested
        if extract_images:
            print()
            output_dir = os.path.dirname(output_file) or '.'
            num_images = extract_images_from_pptx(input_file, output_dir)
            if num_images > 0:
                print(f"✅ Extracted {num_images} images to: {output_dir}")
        
    except Exception as e:
        print(f"❌ Error during conversion: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_pptx_to_markdown.py <input.pptx> [output.md] [--extract-images]")
        print("\nExamples:")
        print("  python convert_pptx_to_markdown.py presentation.pptx")
        print("  python convert_pptx_to_markdown.py presentation.pptx output.md")
        print("  python convert_pptx_to_markdown.py presentation.pptx output.md --extract-images")
        print("\nOptions:")
        print("  --extract-images    Extract all images from PowerPoint to output directory")
        sys.exit(1)
    
    # Parse arguments
    input_file = sys.argv[1]
    extract_images = '--extract-images' in sys.argv
    
    # Get output file (if not --extract-images flag)
    output_file = None
    for arg in sys.argv[2:]:
        if arg != '--extract-images':
            output_file = arg
            break
    
    convert_pptx_to_markdown(input_file, output_file, extract_images)

