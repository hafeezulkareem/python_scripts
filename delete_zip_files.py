import os
import zipfile

def delete_zip_files(path):
    if os.path.exists(path):
        for item in os.listdir(path):
            os.remove(os.path.join(path, item))
        print("Zip files deleted successfully")
    else:
        print("Path doesn't exists")

if __name__ == '__main__':
    path = input("Enter path: ")
    delete_zip_files(path)
