import cv2
import os

# Input and output folder paths
#input_folder = "cropped images/"
#output_folder = "crooped-flipped-img/"
input_folder = "crap test/"
output_folder = "crap test/"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    # Check if the file is an image (you can modify this condition based on your specific image file types)
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
        # Load the image
        img_path = os.path.join(input_folder, filename)
        img = cv2.imread(img_path)

        # Flip the image by 180 degrees
        flipped_img = cv2.flip(img, 0)

        # Extract the file extension from the original filename
        file_extension = filename.split(".")[-1]

        # Generate the output filename by appending "_180" to the original filename
        output_filename = filename.replace("." + file_extension, "_180." + file_extension)

        # Save the flipped image to the output folder
        output_path = os.path.join(output_folder, output_filename)
        cv2.imwrite(output_path, flipped_img)

print("Image flipping complete!")
