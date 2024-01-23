import cv2
import os

# Directory containing the input images
input_dir = "F:/Meg docs/PERIOD 4/ADV IMG/PROJECT/semantic_image_inpainting-extensions/test-images-1/"  # Update with your input folder path
#input_dir = "F:/Meg docs/PERIOD 4/ADV IMG/PROJECT/semantic_image_inpainting-extensions/crap test/"

# Directory to save the cropped images
output_dir = "F:/Meg docs/PERIOD 4/ADV IMG/PROJECT/semantic_image_inpainting-extensions/cropped images/"  # Update with your output folder path

# Loop through all files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Load the original image
        image_path = os.path.join(input_dir, filename)
        image = cv2.imread(image_path)

        # Get the dimensions of the original image
        image_height, image_width = image.shape[:2]

        # Calculate the coordinates for cropping the center
        center_x = image_width // 2
        center_y = image_height // 2
        half_crop_size = 32  # Half of the desired crop size (64 // 2)

        # Crop the center of the image to 64x64 pixels
        cropped_image = image[center_y - half_crop_size:center_y + half_crop_size,
                              center_x - half_crop_size:center_x + half_crop_size]

        # Save the cropped image
        output_path = os.path.join(output_dir, f"cropped_{filename}")  # Update with your desired output file path
        cv2.imwrite(output_path, cropped_image)

        print(f"Cropped image saved to: {output_path}")
