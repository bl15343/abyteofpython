import os;
import subprocess;
import time;

def get_path(dir_entry):
    return dir_entry.path

def build_zip_cmd(files, archive):
    cmd = [ "zip" ]

    cmd.append(archive)

    for file in list(files):
        cmd.append(file)

    return cmd

backup_files = map(get_path, os.scandir())
archive_name = time.strftime("%Y%m%d %H:%M:%S") + ".zip"

subprocess.run(build_zip_cmd(backup_files, archive_name))