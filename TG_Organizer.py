import os
import shutil

# Set the directory path
directory = r"C:\Users\home\Downloads\Telegram Desktop"

# Create a dictionary to map file extensions to folder names
extensions = {
    ".mp4": "Videos",
    ".avi": "Videos",
    ".mkv": "Videos",
    ".mp3": "Audios",
    ".wav": "Audios",
    ".m4a": "Audios",
    ".ogg": "Audios",
    ".pdf": "Documents",
    ".docx": "Documents",
    ".xlsx": "Documents",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
}

# Loop through each file in the directory and move it to its respective folder
for file_name in os.listdir(directory):
    file_path = os.path.join(directory, file_name)
    if os.path.isfile(file_path):
        extension = os.path.splitext(file_name)[1].lower()
        folder_name = extensions.get(extension, "Other")
        folder_path = os.path.join(directory, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        try:
            shutil.move(file_path, os.path.join(folder_path, file_name))
            print(f"{file_name} moved to {folder_name} folder")
        except Exception as e:
            print(f"Error moving {file_name}: {e}")

print("Done!")
