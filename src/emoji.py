from PIL import Image
import os

INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"

def in_path(filename):
    return os.path.join(INPUT_FOLDER, filename)

def flag(emoji_flag):
    height = 500
    width = 750
    WHITE = (255, 255, 255)

    image = Image.new('RGB', (width, height), (WHITE))

    if emoji_flag == '🇫🇷':
        BLUE = (0, 85, 154)
        RED = (239, 65, 53)
        image = Image.new('RGB', (width, height), (WHITE))

        offset = width//3
        for x in range(offset):
            for y in range(height):
                image.putpixel((x, y), BLUE)
                image.putpixel((x + 2*offset, y), RED)

    if emoji_flag == '🇮🇹':
        GREEN = (0, 146, 70)
        RED = (239, 65, 53)
        image = Image.new('RGB', (width, height), (WHITE))

        offset = width//3
        for x in range(offset):
            for y in range(height):
                image.putpixel((x, y), GREEN)
                image.putpixel((x + 2*offset, y), RED)

    if emoji_flag == '🇯🇵':
        RED = (173, 35, 52)

        radius = 3*height//10
        center = (width//2, height//2)

        for x in range(center[0]-radius, center[0]+radius):
            for y in range(center[1]-radius, center[1]+radius):
                if (x-center[0])**2 + (y-center[1])**2 <= radius**2:
                    image.putpixel((x, y), RED)
    
    return image

    

    