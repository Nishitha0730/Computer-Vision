import cv2 as cv
from matplotlib import pyplot as plt

from Gamma_Correction import gamma_correction

def main():
    img = cv.imread("light_nature.jpg")

    corrected_img = gamma_correction(img, 2)
    corrected_img_rgb = cv.cvtColor(corrected_img, cv.COLOR_BGR2RGB)

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.imshow(corrected_img_rgb)
    ax.set_title("Gamma Corrected Image")

    # cv.cvtColor(corrected_img, cv.COLOR_BGR2RGB).save("gamma_corrected_output.jpg")
    cv.imwrite("gamma_corrected_output_gamma_2.jpg", corrected_img)
    plt.show()

if __name__ == "__main__":
    main()