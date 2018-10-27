import os
import subprocess
from pathlib import Path

def main():
    inputdir="dated_mov"
    outputdir="dated_mp4"


    files=[]
    for filename in os.listdir(inputdir):
        files.append(filename)
    files.sort()

    for i in range(len(files)):
        print(files[i])
        try:
            filenameNoExt=files[i][:-4]
            print(filenameNoExt)
            subprocess.call(["ffmpeg","-i","./"+inputdir+"/"+files[i],"-q:v","0","./"+outputdir+"/"+filenameNoExt+".mp4"])
        except:
            print("ERROR could not process file "+files[i])

if __name__ == '__main__':

    main()
