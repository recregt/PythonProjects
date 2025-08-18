# File Organizer

This Python script automatically moves files in your `Downloads` folder to relevant folders based on their file extensions. This helps to eliminate clutter and create a more organized workspace.

## Features

* **Automation:** Can be set to run automatically using the Windows Task Scheduler.
* **Categorization:** Sorts files with extensions like `.pdf`, `.png`, and `.mp4` into folders such as `Documents`, `Images`, and `Videos`.
* **Customizable:** Users can modify the `CATEGORIES` dictionary to add new file types and corresponding folders.
* **Error Handling:** If a file already exists in the destination folder, the script skips the move operation and logs a warning instead of crashing.

## How to Use

1. Place the project files (`organizer.py` and `run_organizer_template.bat`) into a folder on your computer.
2. Make a copy of `run_organizer_template.bat` and rename it `run_organizer.bat`.
3. Edit `run_organizer.bat` and replace the placeholder path with the full path to your `organizer.py` file.
    ```batch
    @echo off
    python "C:\Users\recregt\...\FileOrganizer\organizer.py"
    ```
4. Use the Windows **Task Scheduler** to set the `run_organizer.bat` file to run automatically.

## Customization

You can customize the script by editing the `CATEGORIES` dictionary in `organizer.py` to add new file types and their corresponding folder names.

```python
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx"],
    # New categories can be added here
}
```

---

### **Extra: Hiding the Log Folder**

The `.logs` folder created by the `organizer.py` script might be visible in your file explorer. To hide this folder, you can follow the steps for your specific operating system.

#### **For Windows**

1. Open the Command Prompt by searching for **cmd**.
2. Copy and paste the following command, but be sure to replace the path with the exact location of your `.logs` folder:
    ```
    attrib +h "C:\Users\recregt\...\FileOrganizer\.logs"
    ```
3. This command will add the **hidden** attribute to the folder.

#### **For macOS and Linux**

On these operating systems, a file or folder is automatically hidden if its name begins with a dot (`.`). Therefore, the `.logs` folder will be invisible by default.