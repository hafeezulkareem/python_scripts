import os


def delete_empty_file(path):
    if os.path.exists(path):
        with open(path) as file:
            content = file.read()

        if len(content) == 0:
            if not os.remove(path):
                print(f"{path} is removed successfully")
            else:
                print(f"File deletion is unsuccessful")
        else:
            print(f"{path} is not empty")
    else:
        print(f"{path} is not found")


if __name__ == '__main__':
    path = input("Enter file path:- ")
    delete_empty_file(path)