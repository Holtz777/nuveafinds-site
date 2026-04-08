from PIL import Image

def optimize_favicon(image_path, output_path):
    # Open image
    img = Image.open(image_path).convert("RGBA")
    
    # Find bounding box (removes empty transparent space)
    bbox = img.getbbox()
    
    if bbox:
        # Crop tight to the actual drawing
        cropped = img.crop(bbox)
        
        w, h = cropped.size
        size = max(w, h)
        
        # Create a new square image (favicons should be perfectly square)
        square = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        
        # Paste the drawing exactly in the center of the new square
        x = (size - w) // 2
        y = (size - h) // 2
        square.paste(cropped, (x, y))
        
        # Resize it down specifically for a clean favicon (e.g. 192x192)
        final_icon = square.resize((192, 192), Image.Resampling.LANCZOS)
        
        # Save as optimized PNG
        final_icon.save(output_path)
        print("Favicon optimized and cropped successfully!")
    else:
        print("Image was completely empty/transparent.")

if __name__ == '__main__':
    optimize_favicon('icon.png', 'icon.png')
