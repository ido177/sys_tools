import shutil  # For CopyFile
import sys     # For GetFileSize and Check If File exist
import os      # For CLI Arguments


if len(sys.argv) < 4:
    print('Missing arg')
    exit(1)

file_name = sys.argv[1]
limit_size = int(sys.argv[2])
logs_number = int(sys.argv[3])

if os.path.isfile(file_name):
    log_file_size = os.stat(file_name).st_size // 1024  # Get filesize in bytes

    if log_file_size >= limit_size:
        if logs_number > 0:
            for currentFileNum in range(logs_number, 0, -1):
                src = file_name + '_' + str(currentFileNum - 1)
                dst = file_name + '_' + str(currentFileNum)
                if os.path.isfile(src):
                    shutil.copyfile(src, dst)
                    print(f'Copied {src} to {dst}')
        my_file = open(file_name, 'w')
        my_file.close()
