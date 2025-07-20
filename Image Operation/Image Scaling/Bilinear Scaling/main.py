from PIL import Image
from Bilinear import bilinear_interpolation

def main():
    source = Image.open("apple.jpeg").convert("RGB")
    resized = bilinear_interpolation(source, 789, 573)  # 3 times larger than original
    resized.save("bilinear_output.jpeg")
    resized.show()

if __name__ == "__main__":
    main()
