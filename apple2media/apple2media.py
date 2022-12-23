#####################
#                   #
#    _/_  _  _  /_  #
#  /_//_|/ //_//\   #
#                   #
#    danok.net      #
#    2020-01-10     #
#####################

# STRATEGY FOR PHOTOS/VIDEOS EXPORTED FROM APPLE PHOTOS

#(0) remove all hidden files that start with a dot.
#(1) Export fotos as originals into direcotries with dates.
#(2) Lowecase all filenames (for extensions to end in .mov and .jpg)
#(3) Separate Movie and Photo files into two separate directories.
#(4) Photos seem to have proper DateTime Info and existing labeling program should work.
#(5) Videos:
#(5a) Rename Files using their creation date: exiftool "-Filename<CreationDate" *.mov
#(5b) Replace colons and spaces in file name with - and _. Remove Timezone information.
#(5c) Use ffmpeg to re-encode move as mp4: ffmpeg -i input.mov -q:v 0 output.mp4 (All metadata will be lost).
#(5d) Use filename to set alldates in .mp4 file: exiftool "-AllDates<Filename" *.mp4
#(5e) Run labeling program to set the filename to the expected format.
#(6) Delete empty directories
#(7) Rename jpeg files to jpg in output_photos directory

import subprocess
import os
import sys
import string
import shutil
import datetime
import datefinder
from pathlib import Path

def CreateTempDirs(fileextensions,auxdirs,outputdirs):
    for fileextension in fileextensions:
        subprocess.call(["mkdir",fileextension])
    for auxdir in auxdirs:
        subprocess.call(["mkdir",auxdir])
    for outputdir in outputdirs:
        subprocess.call(["mkdir",outputdir])
    return None

#Generate the file paths to traverse, or a single path if a file name was given
def GetFiles(path):
    if os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for name in files:
                yield os.path.join(root, name)
    else:
        yield path

def DeleteAllSmallDotfiles(inputdir):
    subprocess.call(["find",inputdir,"-name",".*","-size","-300k","-delete"])
    return None


# Step 01
# Take directory tree of existing photo library and flatten it out.
# Include incremental counter in front of file name, to make sure duplicats are not overwritten.
def FlattenDirectoriesWithDatesinFilename(inputdir,outputdir):

    i=0
    for f in GetFiles(inputdir):
        i+=1
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
        shutil.copy(f, outputdir+newfilename.lower())

    return None

def SortFilesByType(fileextensions):
    for fileextension in fileextensions:
        subprocess.run("mv flatdir/*."+fileextension+" "+fileextension,shell=True)
    subprocess.run("mv flatdir/* other_files",shell=True)

    return None

def RenameFilesByType(inputdir,fileextensioninput,fileextensionoutput):
    files=[]
    for filename in os.listdir(inputdir):
        files.append(filename)

    for file in files:
        if fileextensioninput in file:
            inputfilename="./"+inputdir+"/"+file
            outputfilename=inputfilename.replace(fileextensioninput,fileextensionoutput)
            os.rename(inputfilename,outputfilename)
    return None

def MovsFilenameFromCreationDateAndConvertToMp4(inputdir):
    subprocess.run('exiftool -q "-Filename<CreationDate" '+inputdir+'/*',shell=True)

    files=[]
    for filename in os.listdir(inputdir):
        files.append(filename)
    files.sort()

    for file in files:
        inputfilename="./"+inputdir+"/"+file
        movfilename=inputfilename.replace(":","-").replace(" ","_")[:-6]+".mov"
        mp4filename=movfilename.replace(".mov",".mp4")
        os.rename(inputfilename,movfilename)
        subprocess.run("ffmpeg -i "+movfilename+" -q:v 0 "+mp4filename,shell=True)
        subprocess.run("rm "+movfilename,shell=True)

def Cleanup(auxdirs,notprocesseddir):
    #move all remaining files from the aux dirs to the not processed directory, delete empty aux dirs.
    for auxdir in auxdirs:
        subprocess.run("mv "+auxdir+"/* "+notprocesseddir,shell=True)
        subprocess.run("rmdir "+auxdir,shell=True)
    return None

def ProcessFiles(inputdir,outputdir,fileextension,zerosdir="zeros"):

    files=[]
    for filename in os.listdir(inputdir):
        if(fileextension in filename):
            files.append(filename)
    files.sort()

    for i in range(len(files)):
        print(files[i])
        if(fileextension==".mp4"):
            inputfilename="./"+inputdir+"/"+files[i]
            inputfilenameoriginal="./"+inputdir+"/"+files[i]+"_original"
            subprocess.call(["exiftool","-alldates<filename",inputfilename])
            subprocess.call(["rm",inputfilenameoriginal])
        try:
            EXIFoutputaux1=subprocess.Popen(["exiftool","-CreateDate","./"+inputdir+"/"+files[i]],stdout=subprocess.PIPE)
            EXIFoutputaux2=EXIFoutputaux1.stdout.read()
            EXIFoutputaux3=str(EXIFoutputaux2)
            print(EXIFoutputaux3)
            EXIFoutputaux4=EXIFoutputaux3.split(" ")
            TimeString=EXIFoutputaux4[-1][:-3]
            DateString=EXIFoutputaux4[-2]
            if DateString == "0000:00:00":
                os.rename("./"+inputdir+"/"+files[i], "./"+zerosdir+"/"+files[i])
                print("Zeros File: "+files[i])
            elif len(DateString)==10:
                DateString=DateString.replace(":","-")
                TimeString=TimeString.replace(":","")
                FileNameDateTime=DateString+"_"+TimeString+"a"
                ProposedFilePath = Path("./"+outputdir+"/"+FileNameDateTime+fileextension)
                if ProposedFilePath.is_file():
                    FileNameDateTime=FileNameDateTime[:-1]+"b"
                    ProposedFilePath = Path("./"+outputdir+"/"+FileNameDateTime+fileextension)
                    if ProposedFilePath.is_file():
                        FileNameDateTime=FileNameDateTime[:-1]+"c"
                        ProposedFilePath = Path("./"+outputdir+"/"+FileNameDateTime+fileextension)
                        if ProposedFilePath.is_file():
                            FileNameDateTime=FileNameDateTime[:-1]+"d"
                            ProposedFilePath = Path("./"+outputdir+"/"+FileNameDateTime+fileextension)
                            if ProposedFilePath.is_file():
                                FileNameDateTime=FileNameDateTime[:-1]+"e"
                                ProposedFilePath = Path("./"+outputdir+"/"+FileNameDateTime+fileextension)
                                if ProposedFilePath.is_file():
                                    FileNameDateTime=FileNameDateTime[:-1]+"f"
                                    ProposedFilePath = Path("./"+outputdir+"/"+FileNameDateTime+fileextension)
                                    if ProposedFilePath.is_file():
                                        FileNameDateTime=FileNameDateTime[:-1]+"g"
                                        ProposedFilePath = Path("./"+outputdir+"/"+FileNameDateTime+fileextension)
                                        if ProposedFilePath.is_file():
                                            FileNameDateTime=FileNameDateTime[:-1]+"h"
                                            ProposedFilePath = Path("./"+outputdir+"/"+FileNameDateTime+fileextension)
                                            if ProposedFilePath.is_file():
                                                FileNameDateTime=FileNameDateTime[:-1]+"i"
                                                ProposedFilePath = Path("./"+outputdir+"/"+FileNameDateTime+fileextension)
                                                if ProposedFilePath.is_file():
                                                    FileNameDateTime=FileNameDateTime[:-1]+"j"
                                                    ProposedFilePath = Path("./"+outputdir+"/"+FileNameDateTime+fileextension)
                                                    if ProposedFilePath.is_file():
                                                        FileNameDateTime=FileNameDateTime[:-1]+"k"
                                                        ProposedFilePath = Path("./"+outputdir+"/"+FileNameDateTime+fileextension)
                                                        if ProposedFilePath.is_file():
                                                            FileNameDateTime=FileNameDateTime[:-1]+"l"
                                                            ProposedFilePath = Path("./"+outputdir+"/"+FileNameDateTime+fileextension)
                                                            if ProposedFilePath.is_file():
                                                                FileNameDateTime=FileNameDateTime[:-1]+"m"
                                                                ProposedFilePath = Path("./"+outputdir+"/"+FileNameDateTime+fileextension)
                os.rename("./"+inputdir+"/"+files[i], "./"+outputdir+"/"+FileNameDateTime+fileextension)
                print("Succesfully Moded: "+FileNameDateTime+fileextension)
            else:
                print("ERROR, could not move: "+files[i])
        except:
            print("ERROR, could not move: "+files[i])



if __name__ == '__main__':

    inputdir = "./input/"
    fileextensions=["jpg","mp4","png","mov","jpeg"]
    auxdirs=["flatdir","other_files","zeros"]
    outputdirs=["output_photos","output_videos","output_notprocessed"]

    DeleteAllSmallDotfiles(inputdir)
    CreateTempDirs(fileextensions,auxdirs,outputdirs)
    FlattenDirectoriesWithDatesinFilename(inputdir,"flatdir/")
    SortFilesByType(fileextensions)
    ProcessFiles("jpg","output_photos",".jpg")
    ProcessFiles("jpeg","output_photos",".jpeg")
    MovsFilenameFromCreationDateAndConvertToMp4("mov")
    ProcessFiles("mov","output_videos",".mp4")
    Cleanup(auxdirs,"output_notprocessed")
    Cleanup(fileextensions,"output_notprocessed")
    RenameFilesByType("output_photos","jpeg","jpg")
