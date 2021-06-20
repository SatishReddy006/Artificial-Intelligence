#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if path is None or suffix is None:
        return []
    if os.path.exists(path):
        files_with_suffix = []
        dirs_to_walk = [path]
        
        while dirs_to_walk:
            folder = dirs_to_walk.pop(0) + "/"  # removing first element from walk list
            items = os.listdir(folder)  # getting all items from the folder

            # Going through all items and checking if item is directory or file. If it is a directory, adding it to walk
            # list else if it is file and ends with suffix, adding the item in files list
            for i in items:
                i = folder + i
                if os.path.isdir(i):
                    dirs_to_walk.append(i)
                elif str(i).endswith(suffix):
                    files_with_suffix.append(i)

        return files_with_suffix
    else:
        return []

print(find_files('.c', 'testdir'))   #return ['testdir/t1.c', 'testdir/subdir1/a.c', 'testdir/subdir5/a.c', 'testdir/subdir3/subsubdir1/b.c']
print(find_files('.h', 'testdir'))   #return ['testdir/t1.h', 'testdir/subdir1/a.h', 'testdir/subdir5/a.h', 'testdir/subdir3/subsubdir1/b.h']
print(find_files('.c', ''))          #return []
print(find_files('.c', 'testdir/subdir3'))   #return ['testdir/subdir3/subsubdir1/b.c']

# Let us print the files in the directory in which you are running this script
print(find_files(None, None))       #return []

