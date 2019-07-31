import os

def join():
	directory_name = r'C:\automate\code\file_directory\source'
	file_name = '1.txt'
	full_name = os.path.join(directory_name, file_name)
	print(full_name)


def split():
	full_name = r'C:\automate\code\file_directory\source\1.txt'
	split_result = os.path.split(full_name)
	print(split_result)

