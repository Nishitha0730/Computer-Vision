from PIL import Image
from Histogram_Equalization import histogram_equalization


def main():
    source = Image.open("apple.jpeg").convert("GRAY")
    enhanced = histogram_equalization(source)
    enhanced.save("histogram_equalized_output.jpeg")
    enhanced.show()

if __name__ == "__main__":
    main()