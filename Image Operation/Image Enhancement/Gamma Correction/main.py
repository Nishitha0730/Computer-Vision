import cv2 as cv
from matplotlib import pyplot as plt

from Gamma_Correction import gamma_correction

def main():
    img = cv.imread("light_nature.jpg")

    corrected_img = gamma_correction(img, 1.5)

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.imshow(cv.cvtColor(corrected_img, cv.COLOR_BGR2RGB))
    ax.set_title("Gamma Corrected Image")
    plt.show()

if __name__ == "__main__":
    main()