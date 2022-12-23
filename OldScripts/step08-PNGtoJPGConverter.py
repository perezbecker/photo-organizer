
import os
import sys
import string
import shutil
import subprocess

#Generate the file paths to traverse, or a single path if a file name was given
def getfiles(path):
    if os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for name in files:
                yield os.path.join(root, name)
    else:
        yield path

fromdir = "./dpb_photos_jpg/"

for f in getfiles(fromdir):
    filename = f.split('/')[-1]
    monthdir = f.split('/')[-2]
    fileextension=filename[-4:]
    filenameNoExtension=filename[:-4]
    filenameNoExtensionNorLetter=filename[:-5]
    if fileextension==".png":
        outputfilename=filenameNoExtensionNorLetter+"g.jpg"
        print("converting to jpg: "+filename)
        subprocess.call(["convert",fromdir+monthdir+"/"+filename,fromdir+monthdir+"/"+outputfilename])
        subprocess.call(["exiftool","-AllDates<filename",fromdir+monthdir+"/"+outputfilename])
        os.remove(fromdir+monthdir+"/"+outputfilename+"_original")
        os.remove(f)

