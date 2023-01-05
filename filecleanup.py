import os

# Function to delete files after movie has been made
def delete_files(folder_path):
    # Check if the folder path is valid
    if not os.path.isdir(folder_path):
        print(f"Error: The folder path '{folder_path}' is not a valid directory.")
        return

    # Delete all files in the folder
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            os.unlink(file_path)