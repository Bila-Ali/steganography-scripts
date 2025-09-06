import sys
from PIL import Image

def decode_image(image_path):
    img = Image.open(image_path)
    binary_message = ''
    width, height = img.size

    for row in range(height):
        for col in range(width):
            pixel = list(img.getpixel((col, row)))
            for i in range(3):
                binary_message += str(pixel[i] & 1)

    end_delimiter = '1111111111111110'
    end_index = binary_message.find(end_delimiter)

    if end_index == -1:
        print("❌ No hidden message found.")
        return None

    extracted_binary = binary_message[:end_index]
    message = ''
    for i in range(0, len(extracted_binary), 8):
        byte = extracted_binary[i:i+8]
        message += chr(int(byte, 2))
    return message

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 decode.py <stego_image.png>")
        sys.exit(1)

    image_file = sys.argv[1]
    decoded_text = decode_image(image_file)

    if decoded_text:
        print("✅ Hidden message found:")
        print(decoded_text)
