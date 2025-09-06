import sys
from PIL import Image

def encode_image(image_path, message, output_path):
    img = Image.open(image_path)
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '1111111111111110'  # End marker

    if len(binary_message) > len(list(img.getdata())) * 3:
        print("Error: Message is too long for this image.")
        sys.exit(1)

    encoded_img = img.copy()
    data_index = 0
    width, height = img.size

    for row in range(height):
        for col in range(width):
            pixel = list(img.getpixel((col, row)))
            for i in range(3):
                if data_index < len(binary_message):
                    pixel[i] = pixel[i] & ~1 | int(binary_message[data_index])
                    data_index += 1
            encoded_img.putpixel((col, row), tuple(pixel))

    encoded_img.save(output_path)
    print(f"✅ Message hidden in {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 incode.py <image.png> <secret.txt>")
        sys.exit(1)

    image_file = sys.argv[1]
    text_file = sys.argv[2]

    with open(text_file, 'r') as f:
        secret_text = f.read()

    encode_image(image_file, secret_text, "stego_image.png")
