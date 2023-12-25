# Create tree structure
import os

c_courses = 'tree/c/other_courses'
cpp_courses = 'tree/cpp/other_courses'
python_courses = 'tree/python/other_courses'

c_dir_name = '/c'
cpp_dir_name = '/cpp'
python_dir_name = '/python'

try:
    os.makedirs(f'{c_courses}{c_dir_name}')
    os.makedirs(f'{c_courses}{python_dir_name}')

    os.makedirs(f'{cpp_courses}{c_dir_name}')
    os.makedirs(f'{cpp_courses}{python_dir_name}')

    os.makedirs(f'{python_courses}{c_dir_name}')
    os.makedirs(f'{python_courses}{cpp_dir_name}')

except FileExistsError:
    print('Not gonna create the files, they\'re already there')

# Perform dir finding

paths = []

def recursive_search(parent_dir, dir_name):
    dir_structure = os.listdir(parent_dir)
    
    for directory in dir_structure:
        directory_path = parent_dir + '/' + directory
        if directory == dir_name:
            paths.append(directory_path)
        else:
            recursive_search(directory_path, dir_name)

recursive_search('tree', 'python')

for path in paths:
    print('.../' + path)

# Delete tree structure

# os.removedirs(f'{c_courses}{c_dir_name}')
# os.removedirs(f'{c_courses}{python_dir_name}')

# os.removedirs(f'{cpp_courses}{c_dir_name}')
# os.removedirs(f'{cpp_courses}{python_dir_name}')

# os.removedirs(f'{python_courses}{c_dir_name}')
# os.removedirs(f'{python_courses}{cpp_dir_name}')