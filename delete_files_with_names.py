import os


def delete_files_with_names(directory, files):
	if os.path.isdir(directory) and os.path.exists(directory):
		count = 0
		if len(files) > 0:
			list_of_items = os.listdir(directory)

			for root, dirs, files in os.walk(directory):
				for file in files:
					if file in files:
						count += 1
						os.remove(os.path.join(root, file))

		print(f"{count} files deleted.") if count > 1 else print(f"File not found") if count == 0 else print(f"{count} file is deleted.")

	else:
		print("Path doesn't exists")


if __name__ == "__main__":
	directory = input("Enter directory path:- ").strip()
    files = []
		print("Enter all file names one by one to be deleted \nEnter 0 to delete entered files")
		count = 1
		while True:
			item = input(f"Input {count}: ").strip()
			if item == "0":
				break
			else:
				files.append(item)
			count += 1
	delete_files_with_names(directory, files)