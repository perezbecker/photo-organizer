# Step 01
# Take directory tree of existing photo library and flatten it out.
# Include incremental counter in front of file name, to make sure duplicats are not overwritten.
# update destination and fromdir for personal use. 

import os
import sys
import string
import shutil
import datetime
import datefinder

#Generate the file paths to traverse, or a single path if a file name was given
def getfiles(path):
    if os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for name in files:
                yield os.path.join(root, name)
    else:
        yield path

destination = "./flattened/"
fromdir = "./exported_photos/"

i=0
for f in getfiles(fromdir):
    i+=1
    print(f)
    filename = f.split('/')[-1]
    datestringraw=f.split('/')[-2]
    datestringcooked=datestringraw.split(",")[-2]+datestringraw.split(",")[-1]
    directorydatelist=list(datefinder.find_dates(datestringcooked))
    directorydate=directorydatelist[0]
    directorydatestring=directorydate.strftime("%Y-%m-%d")
    newfilename=directorydatestring+"-item-"+str(i).zfill(5)+"-"+filename
    print(newfilename.lower())
    #if os.path.isfile(destination+filename):
    #    filename = f.replace(fromdir,"",1).replace("/","_")
    #os.rename(f, destination+filename)
    shutil.copy(f, destination+newfilename.lower())
