"""
Script to generate a multi-size favicon.ico from a source PNG icon.
Requires Pillow: pip install Pillow
"""
import os
from PIL import Image

def generate_favicon(source_path, target_path):
    if not os.path.exists(source_path):
        print(f"Error: Source file {source_path} not found.")
        return

    # Create target directory if it doesn't exist
    target_dir = os.path.dirname(target_path)
    if target_dir and not os.path.exists(target_dir):
        os.makedirs(target_dir)

    img = Image.open(source_path)
    # Ensure it's in RGBA mode for transparency support
    img = img.convert("RGBA")
    
    sizes = [16, 32, 48, 64, 128, 256]
    img.save(target_path, format='ICO', sizes=[(s, s) for s in sizes])
    print(f"Favicon generated at {target_path} with sizes: {sizes}")

if __name__ == "__main__":
    # Base directory is the project root
    source = "static/img/brand/source-favicon-icon.png"
    target = "static/img/favicon.ico"
    generate_favicon(source, target)
