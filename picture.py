import os
import shutil

# Define source and destination folders

source_folder = '/home/ajay/Downloads'
destination_folder = '/home/ajay/Pictures'

# Create the destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Iterate through all files in the source folder
for filename in os.listdir(source_folder):
    # Check if the file has a .mp3 extension
    if filename.endswith('.jpg'):
        # Construct full file path
        source_file = os.path.join(source_folder,filename)
        destination_file = os.path.join(destination_folder, filename)
        # Move the file
        shutil.move(source_file, destination_file)
        print(f"Moved: {filename}")
print("All .jpg files have been moved.")

