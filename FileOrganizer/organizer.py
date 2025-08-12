import os
import logging
from pathlib import Path

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Executables": [".exe", ".msi"],
    "Archives": [".zip", ".rar"],
    "Scripts": [".py", ".ipynb"]
}

downloads_path = Path.home() / 'Downloads'
log_folder = downloads_path / '.logs'
log_folder.mkdir(parents=True, exist_ok=True)
log_file_path = log_folder / 'file_organizer.log'

logging.basicConfig(filename=log_file_path, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

for category in CATEGORIES:
    (downloads_path / category).mkdir(parents=True, exist_ok=True)

(downloads_path / "Other").mkdir(parents=True, exist_ok=True)

for file_name in os.listdir(downloads_path):
    file_path = downloads_path / file_name
    
    if file_path.is_dir():
        continue
    
    file_extension = file_path.suffix
    
    if not file_extension:
        continue
    
    for category, extensions in CATEGORIES.items():
        if file_extension in extensions:
            destination_folder = downloads_path / category
            destination_path = destination_folder / file_name
            
            try:
                os.rename(file_path, destination_path)
                logging.info(f"Moved '{file_name}' to the '{category}' folder.")
            except FileExistsError:
                logging.warning(f"File '{file_name}' already exists in '{category}'. Skipping.")
            
            break
    else:
        other_folder = downloads_path / "Other"
        destination_path = other_folder / file_name
        
        try:
            os.rename(file_path, destination_path)
            logging.info(f"Moved '{file_name}' to the 'Other' folder.")
        except FileExistsError:
            logging.warning(f"File '{file_name}' already exists in 'Other'. Skipping.")