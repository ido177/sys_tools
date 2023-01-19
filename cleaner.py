import os
import sys
import time


days = int(sys.argv[1])
folder = sys.argv[2]

deleted_size = 0
deleted_file = 0
deleted_dirs = 0

age_time = time.time() - 60 * 60 * 24 * days


def delete_old_files(fld):
    global deleted_file
    global deleted_size
    for path, dirs, files in os.walk(fld):
        for file in files:
            file_name = os.path.join(path, file)
            file_time = os.path.getmtime(file_name)
            if file_time < age_time:
                deleted_size += os.path.getsize(file_name)
                deleted_file += 1
                print('Deleting fild: ' + file_name)
                # os.remove(file_name)


def delete_empty_dir(fld):
    global deleted_dirs
    empty_folders = 0
    for path, dirs, files in os.walk(fld):
        if not dirs and not files:
            deleted_dirs += 1
            empty_folders += 1
            print('Deleting empty dir: ' + path)
            # os.removedirs(path)
    if empty_folders > 0:
        delete_empty_dir(fld)


for item in folder:
    delete_old_files(item)
    delete_empty_dir(item)


print(f'''
Total deleted files: {deleted_file}
Total deleted dirs: {deleted_dirs}
Total freed space: {deleted_size // 1024 // 1024}Mb
''')
