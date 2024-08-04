import os
import zipfile
from datetime import datetime

# Directory to be backed up
SOURCE_DIR = 'your_directory_path_here'  # Replace with your directory path
# Directory where backups will be stored
BACKUP_DIR = 'backup_directory_path_here'  # Replace with your backup directory path

def create_backup_filename():
    today = datetime.now().strftime('%Y_%m_%d')
    backup_filename = os.path.join(BACKUP_DIR, f'backup_{today}.zip')
    return backup_filename

def zip_directory(source_dir, backup_filename):
    with zipfile.ZipFile(backup_filename, 'w', zipfile.ZIP_DEFLATED) as backup_zip:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                backup_zip.write(file_path, os.path.relpath(file_path, source_dir))
    print(f"Backup created successfully: {backup_filename}")

def ensure_backup_directory_exists():
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
        print(f"Backup directory created: {BACKUP_DIR}")
    else:
        print(f"Backup directory already exists: {BACKUP_DIR}")

def main():
    ensure_backup_directory_exists()
    backup_filename = create_backup_filename()
    zip_directory(SOURCE_DIR, backup_filename)
    print("Backup process completed.")

def usage_instructions():
    print("This script backs up a specified directory by compressing it into a ZIP file.")
    print("Configure the source directory and backup directory in the script.")
    print("Example: python backup_script.py")

def additional_instructions():
    print("Make sure you have write permissions to the backup directory.")
    print("To automate this script, use a task scheduler like cron (Linux) or Task Scheduler (Windows).")
    print("You can customize the backup filename format by modifying the create_backup_filename() function.")
    print("Ensure that the source directory exists and contains the files you want to back up.")
    print("Check the backup directory after the script runs to verify the backup file is created.")
    print("If you encounter any issues, check the script's print statements for debugging information.")

def detailed_steps():
    print("Detailed steps for using the script:")
    print("1. Open the script in a text editor.")
    print("2. Replace 'your_directory_path_here' with the path to the directory you want to back up.")
    print("3. Replace 'backup_directory_path_here' with the path to the directory where you want to store the backups.")
    print("4. Save the script.")
    print("5. Run the script using a Python interpreter.")
    print("6. Verify the backup file is created in the backup directory.")

if __name__ == "__main__":
    usage_instructions()
    additional_instructions()
    detailed_steps()
    main()