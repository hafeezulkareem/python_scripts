import os


def delete_file_with_extension(path, extension):
    if os.path.exists(path):
        if os.path.isdir(path):
            for root_folder, folders, files in os.walk(path):
                for file in files:
                    file_path = os.path.join(root_folder, file)
                    file_extension = os.path.splitext(file_path)
                    if "." + extension == file_extension:
                        if not os.remove(file):
                            print(f"{file} deleted successfully")
                        else:
                            print(f"Unable to delete the {file}")
        else:
            print(f"{path} is not a directory")
    else:
        print(f"{path} doesn't exist")


if __name__ == '__main__':
    path = input("Enter directory path:- ")
    extension = input("Enter file extension:- ")
    delete_file_with_extension(path, extension)
