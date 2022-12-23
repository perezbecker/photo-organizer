#!/usr/bin/python

import os, sys
import shutil

#Generate the file paths to traverse, or a single path if a file name was given
def getfiles(path):
    if os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for name in files:
                yield os.path.join(root, name)
    else:
        yield path

fromdir = "./ALLIMAGES/"
destination_root = "./date_directories/"

for filepath in getfiles(fromdir):
    filename=filepath.split("/")[-1]
    dest_directory=filename[0:7]
    print("* * * * * *")
    print(filename)
    print(dest_directory)
    print(fromdir+filename)
    print(destination_root+dest_directory+"/"+filename)

    shutil.copy(fromdir+filename,destination_root+dest_directory+"/"+filename)

