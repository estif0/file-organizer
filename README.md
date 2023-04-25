## File Organizer

This is a Python script that organizes files in a specified directory based on their file extension. The script loops through each file in the directory and moves it to its respective folder based on its file extension. The script is designed to be customized by the user to specify the directory path and the folder names.

### Prerequisites

- Python 3.x installed on your system

### Usage

1. Open the script in a text editor of your choice.
2. Modify the `directory` variable to specify the directory path you want to organize.
3. Modify the `extensions` dictionary to map file extensions to folder names.
4. Run the script by executing the command `python file_organizer.py` in the terminal.

### Example

Let's say you have a directory called `Downloads` in your home directory, and you want to organize the files in this directory. You would modify the `directory` variable in the script to point to this directory:

```python
directory = "/home/user/Downloads"
```

Next, you would modify the extensions dictionary to specify the folder names for each file extension:

```
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
```

Finally, you would run the script by executing the command `python file_organizer.py` in the terminal.

### License

This project is licensed under the MIT License - see the LICENSE file for details.
