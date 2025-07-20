from PIL import Image
from Scaling import nearest_neighbor_scaling

def main():
    input_path = "apple.jpeg"         # Path to the input image
    output_path = "nearest neighbor scaled_output_2.jpeg"
    new_width = 789
    new_height = 573

    # Load the image
    source = Image.open(input_path)

    # Scale it
    scaled = nearest_neighbor_scaling(source, new_width, new_height)

    # Save and show
    scaled.save(output_path)
    scaled.show()

if __name__ == "__main__":
    main()
