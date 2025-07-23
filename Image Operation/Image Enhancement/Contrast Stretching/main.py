from PIL import Image
from Contrast_Stretching import contrast_stretching


def main():
    source = Image.open("Apple_GRAY.jpg").convert("L") # Convert to grayscale if not already
    stretched = contrast_stretching(source)
    stretched.save("contrast_stretched_output.jpg")
    stretched.show()

if __name__ == "__main__":
    main()