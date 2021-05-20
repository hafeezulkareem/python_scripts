import os
import shutil

from delete_empty_folders import delete_empty_folders

def move_files_from_child_folders_to_current_folder(path):
    if os.path.exists(path):
        for root_folder, folders, files in os.walk(path):
            for file in files:
                shutil.move(os.path.join(root_folder, file), path)
        print("Moved files successfully")

        delete_empty_folders(path)
    else:
        print("Path doesn't exists")

if __name__ == '__main__':
    path = input("Enter path: ")
    move_files_from_child_folders_to_current_folder(path)
