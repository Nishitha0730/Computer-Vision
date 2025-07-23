from PIL import Image
from Contrast_Stretching import contrast_stretching

# Use only for 8-bit grayscale images

def main():
    source = Image.open("Apple_GRAY.jpg").convert("L") # Converts a color image to 8-bit grayscale
    stretched = contrast_stretching(source)
    stretched.save("contrast_stretched_output.jpg")
    stretched.show()

if __name__ == "__main__":
    main()