import datetime
import os
import glob
import subprocess
from pathlib import Path


# Function to rename directories after the datetime of the first picture
def renameDirectories(inputdir):
    for directory in os.listdir(inputdir):
        newdirdatetimeaux1=subprocess.Popen(["exiftool", "-DateTimeOriginal", "./"+inputdir+"/"+directory+"/DJI_0001.JPG"],stdout=subprocess.PIPE)
        newdirdatetimeaux2=newdirdatetimeaux1.stdout.read()
        newdirdatetime=str(newdirdatetimeaux2)
        newdirdate=newdirdatetime[-22:-12].replace(":","-")
        newdirtime=newdirdatetime[-11:-3].replace(":","")
        newdirname=newdirdate+"_"+newdirtime
        os.rename("./"+inputdir+"/"+directory,"./"+inputdir+"/"+newdirname)

# Function to generate panoramas
def makePanoramas(inputdir,outputdir):
    for directory in os.listdir(inputdir):
        subprocess.call("pto_gen -o panorama_"+directory+".pto ./"+inputdir+"/"+directory+"/*.JPG",shell=True)
        subprocess.call(["hugin_executor","-a","panorama_"+directory+".pto"])
        subprocess.call(["hugin_executor","-s","--prefix="+directory,"panorama_"+directory+".pto"])
        subprocess.call("convert "+directory+".tif -quality 100 "+directory+".jpg",shell=True)
        subprocess.call(["exiftool","-alldates<filename",directory+".jpg"])
        os.rename(directory+".jpg",directory+"a.jpg")
        subprocess.call("mv "+directory+"a.jpg "+outputdir,shell=True)
        subprocess.call("rm "+directory+".tif",shell=True)
        subprocess.call("rm "+directory+".jpg_original",shell=True)
        subprocess.call("rm panorama_"+directory+".pto",shell=True)


# Driver Code
if __name__ == '__main__':

    # Calling main() function
    renameDirectories("pano_input")
    makePanoramas("pano_input","pano_output")
    #toLowerAndRemoveHtml("input")
    #main("input","photos",".jpg")
    #main("input","videos",".mp4",TimeOffsetSign="-",TimeOffsetHours="4")

