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

    all_target_list = []
    for sub_p in os.listdir(path):
        full_p = os.path.join(path,sub_p)
        
        if os.path.isdir(full_p):
            target_list = find_files(suffix,full_p)
            all_target_list += target_list
        elif sub_p.endswith(suffix):
            all_target_list.append(full_p.replace('\\','/'))
            
    return all_target_list


print('Find .c: ',find_files('.c','./testdir/'))
# Return:
#        ['./testdir/subdir1/a.c',
#         './testdir/subdir3/subsubdir1/b.c',
#         './testdir/subdir5/a.c',
#         './testdir/t1.c']


print('Find .c: ',find_files('.c','./testdir/subdir1/'))
# Return:
#        ['./testdir/subdir1/a.c']


print('Find blank ',find_files('','./testdir/'))
# Return:
#        ['./testdir/subdir1/a.c', './testdir/subdir1/a.h', './testdir/subdir2/.gitkeep', 
#         './testdir/subdir3/subsubdir1/b.c', './testdir/subdir3/subsubdir1/b.h', 
#         './testdir/subdir4/.gitkeep', './testdir/subdir5/a.c', 
#         './testdir/subdir5/a.h', './testdir/t1.c', './testdir/t1.h']

