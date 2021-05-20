import os

def delete_empty_folders(path):
    if os.path.exists(path):
        for root_folder, folders, files in os.walk(path):
            for folder in folders:
                if len(os.listdir(os.path.join(root_folder, folder))) == 0:
                    os.rmdir(os.path.join(root_folder, folder))
        print("Empty folders deleted successfully")
    else:
        print("Path doesn't exists")

if __name__ == '__main__':
    path = input("Enter path: ")
    delete_empty_folders(path)
