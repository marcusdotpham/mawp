import os
import glob
import shutil


def search_one_level(root):
	pattern = '*.txt'
	absolute_pattern = os.path.join(root, pattern)
	result = glob.glob(absolute_pattern)
	print(result)

search_one_level(root='source')


def search_all_level(root):
	pattern = '**\*.txt'
	absolute_pattern = os.path.join('source', pattern)
	result = glob.glob(absolute_pattern, recursive=True)
	print(result)

search_all_level(root='source')


def copy_files_with_extension(source, destination, extension):
	pattern = os.path.join(source,'**\*.{0}'.format(extension))
	files = glob.glob(pattern, recursive=True)

	for file in files:
		shutil.copy(file, destination)
		
copy_files_with_extension('source', 'destination', 'txt')
