from PIL import Image

def add_background_to_icon(input_path, output_path, hex_color):
    try:
        # Open the provided transparent icon
        icon = Image.open(input_path).convert("RGBA")
        
        # Parse hex color to RGB tuple
        hex_color = hex_color.lstrip('#')
        r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        bg_color = (r, g, b, 255)
        
        # Create a new image with the pastel background color
        bg = Image.new("RGBA", icon.size, bg_color)
        
        # Paste the icon using its alpha channel as the mask
        bg.paste(icon, (0, 0), icon)
        
        # Save the result
        bg.save(output_path, format="PNG")
        print("Favicon processed with background color successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    add_background_to_icon('icon16x16.png', 'favicon.png', '#faf7eb')
