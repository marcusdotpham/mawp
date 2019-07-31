import os
import shutil

def understand_walk_with_for_loop(path):
	for root, folders_in_root, files_in_root in os.walk(path):
		print('root is :', root)
		print('folders in root are : ', folders_in_root)
		print('files in root are : ', files_in_root)
		print('\n')

understand_walk_with_for_loop('source')


def copy_files_with_extension(source, destination, extension):
	for root, folders_in_root, files_in_root in os.walk(source):
		for file in files_in_root:
			if file.endswith(extension):
				print(file)
				shutil.copy(os.path.join(root,file), destination)

copy_files_with_extension('source', 'destination', 'txt')





