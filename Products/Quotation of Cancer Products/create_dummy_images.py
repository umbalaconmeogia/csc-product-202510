# -*- coding: utf-8 -*-
"""
Create placeholder/symlink images with names that match README.md references
This is the simplest solution - just create files with the expected names
"""
import sys
import io
import os
import shutil

# Force UTF-8
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# Find what images README expects
expected = ['Picture4.jpg', 'Picture6.jpg', 'object2.jpg', 'Picture8.jpg', 'Picture9.jpg', 'Picture3.jpg']

# Find actual images
actual_images = sorted([f for f in os.listdir('.') 
                       if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))
                       and f.startswith('image')],
                      key=lambda x: int(''.join(filter(str.isdigit, x)) or '0'))

print(f"📋 README.md expects these images:")
for img in expected:
    print(f"   - {img}")

print(f"\n📁 Available actual images: {len(actual_images)}")
for img in actual_images[:5]:
    print(f"   - {img}")
print(f"   ... and {len(actual_images) - 5} more")

print(f"\n🔄 Creating copies with expected names...")

# Find PNGs (likely logos/templates) for object2.jpg
png_images = [img for img in actual_images if img.endswith('.png')]
template_img = png_images[0] if png_images else actual_images[0]

# Simple mapping strategy:
# - object2.jpg = first PNG (logo/template, used many times)
# - Other Pictures = sequential JPEGs
mapping = {}
mapping['object2.jpg'] = template_img

# Map other expected names to sequential images
other_expected = [e for e in expected if e != 'object2.jpg']
jpg_images = [img for img in actual_images if img.endswith(('.jpg', '.jpeg')) and img != template_img]

for i, expected_name in enumerate(other_expected):
    if i < len(jpg_images):
        mapping[expected_name] = jpg_images[i]
    elif i < len(actual_images):
        mapping[expected_name] = actual_images[i]

print(f"\n📝 Mapping plan:")
for expected_name, source_file in mapping.items():
    print(f"   {source_file} → {expected_name}")

# Create copies
print(f"\n💾 Creating image files with expected names...")
for expected_name, source_file in mapping.items():
    if not os.path.exists(source_file):
        print(f"   ⚠️  Source not found: {source_file}")
        continue
    
    if os.path.exists(expected_name):
        print(f"   ○ {expected_name} already exists, skipping")
        continue
    
    try:
        shutil.copy2(source_file, expected_name)
        print(f"   ✓ Created {expected_name}")
    except Exception as e:
        print(f"   ❌ Error creating {expected_name}: {e}")

print(f"\n✅ Done! Images are now available with the names expected by README.md")
print(f"\n💡 Note: Original imageN.jpg files are kept unchanged")

