import pygame

def parse_gpl_to_palette(file_path):
    palette = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Skip the first few header lines in the .gpl format
        start_reading = False
        for line in lines:
            line = line.strip()
            if start_reading:
                if line:  # Ignore empty lines
                    parts = line.split()
                    if len(parts) >= 3:  # RGB values must have at least 3 parts
                        # r, g, b = map(int, parts[:3])
                        # color = f"#{r:02x}{g:02x}{b:02x}"  # Convert to hex format
                        hex = parts[:4]
                        color = f"#{hex[3]}"
                        palette.append(color)
            elif line.startswith("##"):  # The color list starts after this line
                start_reading = True
    except Exception as e:
        print(f"Error reading .gpl file: {e}")
    
    return palette

# Example usage
file_path = "./assets/palette/endesga-64.gpl"
PALETTE = parse_gpl_to_palette(file_path)
print(PALETTE)
