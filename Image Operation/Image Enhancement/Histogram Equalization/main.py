from PIL import Image
from Histogram_Equalization import histogram_equalization


def main():
    source = Image.open("Apple_GRAY.jpg")  # Load the grayscale image
    enhanced = histogram_equalization(source)
    enhanced.save("histogram_equalized_output.jpg")
    enhanced.show()

if __name__ == "__main__":
    main()