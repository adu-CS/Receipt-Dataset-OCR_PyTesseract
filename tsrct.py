import os
from PIL import Image

image_folder = "images"  # Path to the folder containing images

# List all files in the folder
image_files = os.listdir(image_folder)

# Loop through the image files and display them
for file_name in image_files:
    if file_name.endswith((".jpg", ".png")):  # Filter for image files
        img_path = os.path.join(image_folder, file_name)
        img = Image.open(img_path)
        img.show()  # Display the image
