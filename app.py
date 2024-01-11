from PIL import Image

def image_to_ascii(image_path):
    image = Image.open(image_path).convert('L')  # convert image to grayscale
    ascii_chars = "@%#*+=-:. "  # define ascii characters
    width, height = image.size

    # Increase the resize factor for better quality, and use the LANCZOS filter
    image = image.resize((int(width/5), int(height/10)), Image.LANCZOS)  # resize image

    ascii_str = ''
    for y in range(image.height):
        for x in range(image.width):
            brightness = image.getpixel((x, y))  # get brightness

            # Adjust the brightness factor to match the new number of ascii characters
            ascii_str += ascii_chars[brightness // 32]  # choose ascii char
        ascii_str += '\n'
    return ascii_str

print(image_to_ascii('F-XEkduXAAA6kuL.png'))