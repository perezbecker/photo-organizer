import datetime
import os
import glob
import subprocess
from pathlib import Path



# Function to make filenames lower case

def toLowerAndRemoveHtml(inputdir):
    htmlList=glob.glob("./"+inputdir+"/*.html")
    for htmlPath in htmlList:
        os.remove(htmlPath)
    for filename in os.listdir(inputdir):
        inputfilename="./"+inputdir+"/"+filename
        os.rename(inputfilename, inputfilename.replace(" ","-").lower())


# Function to rename multiple files
def main(inputdir,outputdir,fileextension,zerosdir="zeros",TimeOffsetHours="0",TimeOffsetSign="-"):

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
            subprocess.call(["exiftool","-CreateDate"+TimeOffsetSign+"=0:0:0 "+TimeOffsetHours+":0:0",inputfilename])
            subprocess.call(["exiftool","-DateTimeOriginal<CreateDate",inputfilename])
            subprocess.call(["exiftool","-ModifyDate<CreateDate",inputfilename])
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
#        DateTime=datetime.datetime.strptime(DateTimeStartString, "%Y-%m-%d %H:%M:%S")
#        NewDateTime=DateTime+datetime.timedelta(seconds=i)
#        NewDateTimeString=NewDateTime.strftime("%Y:%m:%d %H:%M:%S")
#        print(NewDateTimeString)
#        subprocess.call(["exiftool","-DateTimeOriginal=\""+NewDateTimeString+"\"","./"+inputdir+"/"+files[i]])
#        dst = filestart + str(i+1).zfill(3)+".jpg"
#        print(dst)
#        os.rename("./"+inputdir+"/"+files[i], "./"+inputdir+"/"+dst)

# Driver Code
if __name__ == '__main__':

    # Calling main() function
    toLowerAndRemoveHtml("input")
    main("input","photos",".jpg")
    main("input","videos",".mp4",TimeOffsetSign="-",TimeOffsetHours="4")

