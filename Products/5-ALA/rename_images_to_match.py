# -*- coding: utf-8 -*-
"""
Intelligent image renaming to match README.md references
Analyzes README structure and maps images correctly
"""
import sys
import io
import os
import re
from collections import OrderedDict

# Force UTF-8
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

print("🔍 Analyzing README.md and images...")

# Read README.md
with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all image references with their positions
image_pattern = r'!\[\]\(([^)]+)\)'
matches = list(re.finditer(image_pattern, content))

print(f"\n📋 Found {len(matches)} image references in README.md")

# Get unique image names in order of first appearance
seen = set()
unique_refs = []
for match in matches:
    img = match.group(1)
    if img not in seen:
        unique_refs.append(img)
        seen.add(img)

print(f"📌 Unique images: {len(unique_refs)}")
for ref in unique_refs:
    count = content.count(f'![]({ref})')
    print(f"   - {ref} (used {count} times)")

# Get actual image files (sorted by number)
actual_images = sorted([f for f in os.listdir('.') 
                       if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))
                       and f.startswith('image')],
                      key=lambda x: int(re.search(r'\d+', x).group()))

print(f"\n📁 Found {len(actual_images)} actual image files")

# For object2.jpg, we need ONE representative image (probably a logo)
# For other images, we'll map sequentially
print(f"\n🎯 Creating rename mapping...")

# First, let's see if we can identify which image is the logo/template (object2.jpg)
# Usually it's a small PNG or the first/last image
# Let's use the first PNG as the template/logo
template_image = next((img for img in actual_images if img.endswith('.png')), actual_images[0])

# Create mapping
rename_map = {}
other_refs = [ref for ref in unique_refs if ref != 'object2.jpg']
other_images = [img for img in actual_images if img != template_image]

# Map object2.jpg to template
if 'object2.jpg' in unique_refs:
    rename_map[template_image] = 'object2.jpg'

# Map other references sequentially
for i, ref in enumerate(other_refs):
    if i < len(other_images):
        rename_map[other_images[i]] = ref

print(f"\n📝 Rename plan:")
for old, new in rename_map.items():
    print(f"   {old} → {new}")

# Ask for confirmation
print(f"\n⚠️  This will rename {len(rename_map)} files.")
response = input("Continue? (y/N): ").strip().lower()

if response != 'y':
    print("❌ Cancelled")
    sys.exit(0)

# Perform renames (use temporary names first to avoid conflicts)
print(f"\n🔄 Renaming files...")
temp_renames = {}

# First pass: rename to temporary names
for old_name, new_name in rename_map.items():
    temp_name = f"_temp_{new_name}"
    try:
        os.rename(old_name, temp_name)
        temp_renames[temp_name] = new_name
        print(f"   ✓ {old_name} → {temp_name}")
    except Exception as e:
        print(f"   ❌ Error renaming {old_name}: {e}")

# Second pass: rename from temporary to final names
for temp_name, new_name in temp_renames.items():
    try:
        os.rename(temp_name, new_name)
        print(f"   ✓ {temp_name} → {new_name}")
    except Exception as e:
        print(f"   ❌ Error renaming {temp_name}: {e}")

print(f"\n✅ Rename completed!")
print(f"\n💡 Tip: View README.md in a Markdown viewer to verify images display correctly")

