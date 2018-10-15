import datetime
import os
import subprocess
from pathlib import Path

# Function to rename multiple files
def main():
    inputdir="photos_jpg"
    outputdir="dated_jpg"
    zerosdir="zeros_jpg"
    fileextension=".jpg"

    files=[]
    for filename in os.listdir(inputdir):
        files.append(filename)
    files.sort()

    for i in range(len(files)):
        print(files[i])
        try:
            EXIFoutputaux1=subprocess.Popen(["exiftool","-DateTimeOriginal","./"+inputdir+"/"+files[i]],stdout=subprocess.PIPE)
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
    main()

