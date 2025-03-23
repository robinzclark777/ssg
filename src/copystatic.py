import os
import shutil

def copy_files(source_dir_path, dest_dir_path):
    parts = os.path.split(source_dir_path)
    print(f"parts are {parts}")
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f"copying file {from_path} to {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files(from_path, dest_path)