import os
import zipfile

def extract_all_zip_files(path):
    if os.path.exists(path):
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if zipfile.is_zipfile(item_path):
                with zipfile.ZipFile(item_path, 'r') as zip:
                    zip.extractall(path)
        print("Extracted successfully")
    else:
        print("Path doesn't exists")

if __name__ == '__main__':
    path = input("Enter path: ")
    extract_all_zip_files(path)
