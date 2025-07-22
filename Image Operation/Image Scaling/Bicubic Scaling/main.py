from PIL import Image
from Bicubic import bicubic_interpolation

def main():
    source = Image.open("apple.jpeg").convert("RGB")
    resized = bicubic_interpolation(source, 789, 573)
    resized.save("bicubic_output.jpg")
    resized.show()

if __name__ == "__main__":
    main()
