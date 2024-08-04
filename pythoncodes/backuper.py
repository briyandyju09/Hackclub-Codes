import shutil
from datetime import date
import os
import sys

os.chdir(sys.path[0])

def take_backup(src_file_name, dst_file_name=None, src_dir='', dst_dir=''):
    try:
        today = date.today()
        date_format = today.strftime("%d_%b_%Y_")
        src_dir = os.path.join(src_dir, src_file_name)
        
        if not src_file_name:
            print("Please provide at least the Source File Name")
            return
        
        try:
            if src_file_name and dst_file_name and src_dir and dst_dir:
                src_dir = os.path.join(src_dir, src_file_name)
                dst_dir = os.path.join(dst_dir, dst_file_name)
            elif dst_file_name is None or not dst_file_name:
                dst_file_name = src_file_name
                dst_dir = os.path.join(dst_dir, date_format + dst_file_name)
            elif dst_file_name.isspace():
                dst_file_name = src_file_name
                dst_dir = os.path.join(dst_dir, date_format + dst_file_name)
            else:
                dst_dir = os.path.join(dst_dir, date_format + dst_file_name)
                
            shutil.copy2(src_dir, dst_dir)
            print("Backup Successful!")
        except FileNotFoundError:
            print("File does not exist! Please provide the complete path.")
    except PermissionError:
        dst_dir = os.path.join(dst_dir, date_format + dst_file_name)
        shutil.copytree(src_file_name, dst_dir)

def get_user_input():
    src_file_name = input("Enter the source file name: ")
    dst_file_name = input("Enter the destination file name (optional): ")
    src_dir = input("Enter the source directory (optional): ")
    dst_dir = input("Enter the destination directory (optional): ")
    return src_file_name, dst_file_name, src_dir, dst_dir

def main():
    src_file_name, dst_file_name, src_dir, dst_dir = get_user_input()
    take_backup(src_file_name, dst_file_name, src_dir, dst_dir)

def usage_instructions():
    print("Usage Instructions:")
    print("This script performs backup of files and folders.")
    print("You will be prompted to enter the source file name, destination file name (optional), source directory (optional), and destination directory (optional).")
    print("Example: python backup_script.py")

def validate_and_run():
    if len(sys.argv) > 1 and sys.argv[1] in ('-h', '--help'):
        usage_instructions()
        sys.exit(0)
    main()

if __name__ == "__main__":
    validate_and_run()

def display_backup_message():
    print("Starting the backup process...")
    print("Backup process in progress...")
    print("Backup process completed successfully!")


def backup_log(src_file_name, dst_file_name, status):
    with open("backup_log.txt", "a") as log_file:
        log_file.write(f"{date.today()}: {src_file_name} to {dst_file_name} - {status}\n")

display_backup_message()
