# os module lets you interact with any os using python

import os

# Get current working directory
current_dir=os.getcwd()
print(f'current working directory is {current_dir}')

# list the contents of a directory
print('Directory contents:',os.listdir('.'))

# creating a directory
# os.mkdir('./new_dir')

# deleting a file
# os.remove('file_name_here')

# joining paths
# file_path= os.path.join('folder','file_here')
# print(f'Joined {file_path}')

# check if file exists or its a file or directory
# print(f"File exists {os.path.exists('path_here')}")
# print(f"Is a file {os.path.isfile('file_here')}")
# print(f"Is a directory {os.path.isdir('dir_here')}")

# executing shell commands
# os.system('ls')

# ID OS type
# print(f'OS NAME {os.name}')


# get env variables
# for key,value in os.environ.items():
#     print(key,value)

# set env
os.environ['ENV_HERE']='env_value'

# GET ENV
print(f'retrieving ENV HERE {os.getenv("TEST_VARIABLE")}')


# deleting env var
if 'ENV_HERE' in os.environ:
    del os.environ['ENV_HERE']
    
