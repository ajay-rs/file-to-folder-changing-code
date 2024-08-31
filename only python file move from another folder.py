import os
import shutil
import time

def list_files_in_folder(folder_path):
    """List all files in a folder and return their names with metadata."""
    files = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            file_info = {
                'name': filename,
                'format': os.path.splitext(filename)[1],
                'size': os.path.getsize(file_path),
                'created': time.ctime(os.path.getctime(file_path)),
                'modified': time.ctime(os.path.getmtime(file_path)),
            }
            files.append(file_info)
    return files

def move_py_files(folder_path, destination_folder):
    """Move all .py files from one folder to another."""
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(folder_path):
        if filename.endswith('.py'):
            source_path = os.path.join(folder_path, filename)
            destination_path = os.path.join(destination_folder, filename)
            shutil.move(source_path, destination_path)

# Define the paths
folder_path = '/home/ajay/Documents/folder1'  # replace with your folder path
destination_folder = '/home/ajay/Documents/folder2'  # replace with your destination folder path

# List files and get metadata
files = list_files_in_folder(folder_path)
for file in files:
    print(file)

# Move .py files to the destination folder
move_py_files(folder_path, destination_folder)

print(f".py files moved to {destination_folder}.")



