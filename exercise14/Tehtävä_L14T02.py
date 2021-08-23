import os

BASEDIR = "C:\\"

files_folders=os.listdir(BASEDIR)


for item in files_folders:
    print(item)
