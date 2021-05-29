import os


def change_files_extensions(from_extension, to_extension):
	if os.path.exists(path):
		for root_path, folders, files in os.walk(path):
			for file in files:
				file_path = os.path.join(root_path, file)
				file_path_without_extension, file_extension = os.path.splitext(file_path)
				if from_extension == file_extension:
					os.rename(file_path, file_path_without_extension + to_extension)
	else:
		print(f"'{path}' doesn't exists.")


if __name__ == '__main__':
	print('This program will change all the files with [a] to [b] extension.')
	path = input('Enter folder path:- ')
	from_extension = input('Enter file extension to be changed:- ')
	to_extension = input('Enter file extension to be used:- ')
    change_files_extensions(path, from_extension, to_extension)