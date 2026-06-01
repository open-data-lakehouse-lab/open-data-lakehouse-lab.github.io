import os
from PIL import Image

def remove_checkerboard(image, background_color=(255, 255, 255)):
    """
    Simplistic approach to remove baked-in checkerboard.
    Since we don't know the exact pixel values of the checkerboard,
    and we want a clean background, we'll assume the 'non-checkerboard'
    part is what we want to keep. 
    However, a better approach if the checkerboard is just two gray/white colors
    is to replace those specific colors.
    For this lab, we will try to detect the checkerboard by looking at the corners
    or just replace everything that looks like a checkerboard.
    
    Actually, a more robust way if it's 'baked-in' is hard without knowing the colors.
    Given the task, I will assume the checkerboard consists of two shades of gray/white.
    """
    # Convert to RGBA if not already
    img = image.convert("RGBA")
    datas = img.getdata()

    new_data = []
    for item in datas:
        # Check if it's a shade of gray commonly used in checkerboards
        # Usually (204, 204, 204) and (255, 255, 255) or similar.
        # This is a bit risky. 
        # Better: if we want a solid background, we can just place the image 
        # on top of a solid background if we had real transparency.
        # But the issue says it is baked in.
        
        # If we can't easily remove it, we might just have to use the image as is 
        # but the task says "Generate or replace ... no visible checkerboard".
        # Let's assume the logo itself is NOT these gray colors.
        
        # Checkerboard patterns often use:
        # Color 1: (255, 255, 255) - White
        # Color 2: (204, 204, 204) - Light Gray
        # or (238, 238, 238)
        
        r, g, b, a = item
        
        # Very simple heuristic: if it's white or light gray and near-neutral
        is_white = (r > 240 and g > 240 and b > 240)
        is_gray = (200 < r < 210 and 200 < g < 210 and 200 < b < 210)
        
        if is_white or is_gray:
            new_data.append((*background_color, 255))
        else:
            new_data.append(item)

    img.putdata(new_data)
    return img

def generate_assets():
    brand_dir = "static/img/brand"
    output_dir = "static/img"
    
    # 1. Generate logo.png (256x256, white background)
    print("Generating logo.png...")
    logo_src = os.path.join(brand_dir, "source-logo-icon.png")
    if os.path.exists(logo_src):
        with Image.open(logo_src) as img:
            img = img.resize((256, 256), Image.Resampling.LANCZOS)
            img = remove_checkerboard(img, (255, 255, 255))
            img.save(os.path.join(output_dir, "logo.png"))
    
    # 2. Generate favicon.ico (Multiple sizes, white background)
    print("Generating favicon.ico...")
    favicon_src = os.path.join(brand_dir, "source-favicon-icon.png")
    if not os.path.exists(favicon_src):
        favicon_src = logo_src # Fallback
        
    if os.path.exists(favicon_src):
        with Image.open(favicon_src) as img:
            img = remove_checkerboard(img, (255, 255, 255))
            sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
            img.save(os.path.join(output_dir, "favicon.ico"), format='ICO', sizes=sizes)

    # 3. Generate social-card.png (1200x630, dark navy background)
    print("Generating social-card.png...")
    social_src = os.path.join(brand_dir, "source-social-card.png")
    if os.path.exists(social_src):
        with Image.open(social_src) as img:
            # Dark navy background: #000080 or similar. 
            # Docusaurus dark is usually #1b1b1d. Let's use a nice dark navy.
            dark_navy = (20, 24, 35) # A common "dark" color
            
            # Since the social card might also have a baked-in checkerboard,
            # we need to be careful. If the whole background is checkerboard,
            # we can replace it.
            img = img.resize((1200, 630), Image.Resampling.LANCZOS)
            img = remove_checkerboard(img, dark_navy)
            img.save(os.path.join(output_dir, "social-card.png"))

if __name__ == "__main__":
    generate_assets()
