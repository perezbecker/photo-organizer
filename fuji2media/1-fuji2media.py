import os
import subprocess
from pathlib import Path



# Function to make filenames lower case

def to_lower(inputdir):
    for filename in os.listdir(inputdir):
        inputfilename="./"+inputdir+"/"+filename
        os.rename(inputfilename, inputfilename.replace(" ","-").lower())

def rename_mov_to_mp4(inputdir):
    for filename in os.listdir(inputdir):
        inputfilename="./"+inputdir+"/"+filename
        os.rename(inputfilename, inputfilename.replace(".mov",".mp4"))



# Function to rename multiple files
def main(inputdir,outputdir,fileextension,zerosdir="zeros"):

    files=[]
    for filename in os.listdir(inputdir):
        if(fileextension in filename):
            files.append(filename)
    files.sort()

    for i in range(len(files)):
        print(files[i])
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
                                                                if ProposedFilePath.is_file():
                                                                    FileNameDateTime=FileNameDateTime[:-1]+"n"
                                                                    ProposedFilePath = Path("./"+outputdir+"/"+FileNameDateTime+fileextension)
                                                                    if ProposedFilePath.is_file():
                                                                        FileNameDateTime=FileNameDateTime[:-1]+"o"
                                                                        ProposedFilePath = Path("./"+outputdir+"/"+FileNameDateTime+fileextension)
                                                                        if ProposedFilePath.is_file():
                                                                            FileNameDateTime=FileNameDateTime[:-1]+"p"
                                                                            ProposedFilePath = Path("./"+outputdir+"/"+FileNameDateTime+fileextension)
                                                                            if ProposedFilePath.is_file():
                                                                                FileNameDateTime=FileNameDateTime[:-1]+"q"
                                                                                ProposedFilePath = Path("./"+outputdir+"/"+FileNameDateTime+fileextension)
                                                                                if ProposedFilePath.is_file():
                                                                                    FileNameDateTime=FileNameDateTime[:-1]+"r"
                                                                                    ProposedFilePath = Path("./"+outputdir+"/"+FileNameDateTime+fileextension)
                                                                                    if ProposedFilePath.is_file():
                                                                                        FileNameDateTime=FileNameDateTime[:-1]+"s"
                                                                                        ProposedFilePath = Path("./"+outputdir+"/"+FileNameDateTime+fileextension)
                                                                                        if ProposedFilePath.is_file():
                                                                                            FileNameDateTime=FileNameDateTime[:-1]+"t"
                                                                                            ProposedFilePath = Path("./"+outputdir+"/"+FileNameDateTime+fileextension)
                                                                                            if ProposedFilePath.is_file():
                                                                                                FileNameDateTime=FileNameDateTime[:-1]+"u"
                                                                                                ProposedFilePath = Path("./"+outputdir+"/"+FileNameDateTime+fileextension)
                                                                                                if ProposedFilePath.is_file():
                                                                                                    FileNameDateTime=FileNameDateTime[:-1]+"v"
                                                                                                    ProposedFilePath = Path("./"+outputdir+"/"+FileNameDateTime+fileextension)
                                                                                                    if ProposedFilePath.is_file():
                                                                                                        FileNameDateTime=FileNameDateTime[:-1]+"w"
                                                                                                        ProposedFilePath = Path("./"+outputdir+"/"+FileNameDateTime+fileextension)
                                                                                                        if ProposedFilePath.is_file():
                                                                                                            FileNameDateTime=FileNameDateTime[:-1]+"x"
                                                                                                            ProposedFilePath = Path("./"+outputdir+"/"+FileNameDateTime+fileextension)
                                                                                                            if ProposedFilePath.is_file():
                                                                                                                FileNameDateTime=FileNameDateTime[:-1]+"y"
                                                                                                                ProposedFilePath = Path("./"+outputdir+"/"+FileNameDateTime+fileextension)
                                                                                                                if ProposedFilePath.is_file():
                                                                                                                    FileNameDateTime=FileNameDateTime[:-1]+"z"
                                                                                                                    ProposedFilePath = Path("./"+outputdir+"/"+FileNameDateTime+fileextension)
                os.rename("./"+inputdir+"/"+files[i], "./"+outputdir+"/"+FileNameDateTime+fileextension)
                print("Succesfully Moded: "+FileNameDateTime+fileextension)
            else:
                print("ERROR, could not move: "+files[i])
        except:
            print("ERROR, could not move: "+files[i])

# Driver Code
if __name__ == '__main__':

    # Calling main() function
    to_lower("input")
    rename_mov_to_mp4("input")
    main("input","photos",".jpg")
    main("input","videos",".mp4")
    main("input","raw",".raf")

