import os
import shutil



# Dictionary mapping file extensions to folder names
FILE_CATEGORIES = {
    'TextFiles': ['.txt', '.doc', '.docx', '.pdf'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Audio': ['.mp3', '.wav', '.aac', '.ogg', '.m4a'],
    'Video': ['.mp4', '.mkv', '.flv', '.avi'],
    'Archives': ['.zip', '.rar', '.7z', '.tar'],
    'Scripts': ['.py', '.js', '.html', '.css'],
    'Spreadsheets': ['.xls', '.xlsx', '.csv'],
    'Presentations': ['.ppt', '.pptx'],
}



# Function to create folders if they don't exist
def create_folders(base_dir):
    for folder in FILE_CATEGORIES.keys():
        folder_path = os.path.join(base_dir, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)


# Function to move files to appropriate folders
def move_files(base_dir):
    for item in os.listdir(base_dir):
        item_path = os.path.join(base_dir, item)
        if os.path.isfile(item_path):
            file_ext = os.path.splitext(item)[1].lower()
            moved = False
            for folder, extensions in FILE_CATEGORIES.items():
                if file_ext in extensions:
                    shutil.move(item_path, os.path.join(base_dir, folder, item))
                    moved = True
                    break
            if not moved:
                other_folder_path = os.path.join(base_dir, 'OtherFiles')
                if not os.path.exists(other_folder_path):
                    os.makedirs(other_folder_path)
                shutil.move(item_path, other_folder_path)


# Main function
def main():
    base_dir = input("Enter the directory path to organize: ").strip()
    if not os.path.isdir(base_dir):
        print("Invalid directory path.")
        return

    create_folders(base_dir)
    move_files(base_dir)
    print("Files have been organized successfully.")


# Usage instructions
def usage_instructions():
    print("This script organizes files in a specified directory into categorized folders based on file extensions.")
    print("Example: python organize_files.py")
    print("You'll be prompted to enter the directory path you want to organize.")


# Detailed steps
def detailed_steps():
    print("Detailed steps for using the script:")
    print("1. Open the script in a text editor.")
    print("2. Save the script.")
    print("3. Run the script using a Python interpreter.")
    print("4. Enter the directory path you want to organize when prompted.")
    print("5. The script will create folders and move files accordingly.")


if __name__ == "__main__":
    usage_instructions()
    detailed_steps()
    main()
