from extract_all_zip_files import extract_all_zip_files
from delete_zip_files import delete_zip_files
from move_files_from_child_folders_to_current_folder import move_files_from_child_folders_to_current_folder
from delete_empty_folders import delete_empty_folders

def completeTheWork(path):
    # extract_all_zip_files(path)
    # delete_zip_files(path)
    move_files_from_child_folders_to_current_folder(path)
    delete_empty_folders(path)

if __name__ == "__main__":
    path = input("Enter path: ")
    completeTheWork(path)