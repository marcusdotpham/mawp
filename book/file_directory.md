Understand and working with `os.path` , `glob.glob`, `os.walk`.

#### Objectives

Suppose we have `source`. Inside `source` are 3 levels of folder 1,2,3. In each folder has one `txt` file with name same with folder name.

![](images/2019-07-29_10-34-56.png)



We want to write a program to copy all `.txt` file from `source` folder to `destination` folder.

#### Use os.path

We use **os.path.join()** function to constructs a pathname out of one or more partial pathnames. For example, following code print out the full name of file `1.txt`

```python
import os

directory_name = r'C:\automate\code\file_directory\source'
file_name = '1.txt'
full_name = os.path.join(directory_name, file_name)

print(full_name)
```

Out put is

```python
"""
C:\automate\code\file_directory\source\1.txt
"""
```



Opposite with `join` is `split` function. Let try following code.

```python
full_name = r'C:\automate\code\file_directory\source\1.txt'
split_result = os.path.split(full_name)

print(split_result)
```

Result will be a tuple contain directory and file name.

```python
"""
('C:\\automate\\code\\file_directory\\source', '1.txt')
"""
```



#### Understand glob

Glob work base on pattern. 

* '*' replace for any string

* '?' replace for any character

  

#### Search use wildcards at one level

To search all `.txt` file right under `source` folder, we use pattern `*.txt`

```python
# search only right inside root
pattern = '*.txt'

# joint to create absolute path
absolute_pattern = os.path.join('source', pattern)
result = glob.glob(absolute_pattern)
print(result)
```

Result will have only file `1.txt`

```python
"""
['source\\1.txt']
"""
```



#### Search use wildcards at all level

To search all `.txt` file under all folder level, we use pattern `**\*.txt`

`**` tell to glob that we want to search recursively.

And we also need to specify parameter `recursive=True`. Following coding will search for '.txt' file in all directory level.

```python
# recursive pattern
pattern = '**\*.txt'

absolute_pattern = os.path.join('source', pattern)
result = glob.glob(absolute_pattern, recursive=True)
print(result)
```

Print out result

```python
'''
['source\\1.txt', 'source\\1\\2.txt', 'source\\1\\2\\3.txt']
'''
```



#### Copy all ".txt" files recursively use glob

Now we already know how to search for all `.txt` file. To copy a file to directory, we use function `copy` inside `shutil` package.

```python
def copy_files_with_extension(source, destination, extension):
	pattern = os.path.join(source,'**\*.{0}'.format(extension))
	files = glob.glob(pattern, recursive=True)

	for file in files:
		shutil.copy(file, destination)

copy_files_with_extension('source', 'destination', 'txt')
```

After running, inside `destination` will have copied file.  That it, mission accomplished.

![](images/2019-07-29_14-22-30.png)

#### Understand walk

Function `os.walk` travel tree structure layer by layer. At each layer it return 3 things:

* root of current layer
* folders right inside root
* files right inside root

Let run following code

```python
import os
import shutil

def understand_walk_with_for_loop(path):
	for root, folders_in_root, files_in_root in os.walk(path):
		print('root is :', root)
		print('folders in root are : ', folders_in_root)
		print('files in root are : ', files_in_root)
		print('\n')

understand_walk_with_for_loop('source')
```

following result will print out as we expected

```python
"""
root is : source
folders in root are :  ['1']
files in root are :  ['1.txt']


root is : source\1
folders in root are :  ['2']
files in root are :  ['2.txt']


root is : source\1\2
folders in root are :  ['3']
files in root are :  ['3.txt']


root is : source\1\2\3
folders in root are :  []
files in root are :  []
"""
```

From above understanding, we could construct following function for copy all file with specific extension.

```python
def copy_files_with_extension(source, destination, extension):
	for root, folders_in_root, files_in_root in os.walk(source):
		for file in files_in_root:
			if file.endswith(extension):
				print(file)
				shutil.copy(os.path.join(root,file), destination)

copy_files_with_extension('source', 'destination', 'txt')
```

That it, mission completed.