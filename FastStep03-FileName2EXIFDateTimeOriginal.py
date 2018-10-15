import datetime
import os
import subprocess
import shutil

def step03b(inputdir,fileextension):

    directories=[]
    for directory in os.listdir(inputdir):
        DateStartString=str(directory)
        TimeStartString="00:00:01"
        DateTimeStartString=DateStartString+" "+TimeStartString
        files=[]
        for filename in os.listdir("./"+inputdir+"/"+directory):
            files.append(filename)
        files.sort()

        for i in range(len(files)):
            print(files[i])
            DateTime=datetime.datetime.strptime(DateTimeStartString, "%Y-%m-%d %H:%M:%S")
            NewDateTime=DateTime+datetime.timedelta(seconds=i)
            NewDateTimeString=NewDateTime.strftime("%Y:%m:%d %H:%M:%S")
            NewDateTimeNameString=NewDateTime.strftime("%Y-%m-%d_%H%M%S")+"a"+fileextension
            print(NewDateTimeNameString)
            subprocess.call(["exiftool","-DateTimeOriginal=\""+NewDateTimeString+"\"","./"+inputdir+"/"+directory+"/"+files[i]])
            os.rename("./"+inputdir+"/"+directory+"/"+files[i], "./"+inputdir+"/"+NewDateTimeNameString)
            subprocess.call(["rm","./"+inputdir+"/"+directory+"/"+files[i]+"_original"])

        subprocess.call(["rmdir","./"+inputdir+"/"+directory])


def FileName2EXIF(inputdir,fileextension):

    for filename in os.listdir(inputdir):
        DateString=filename[0:10]
        print(DateString)
        if not os.path.exists("./"+inputdir+"/"+DateString):
            os.makedirs("./"+inputdir+"/"+DateString)
        shutil.move("./"+inputdir+"/"+filename,"./"+inputdir+"/"+DateString+"/"+filename)

    step03b(inputdir,fileextension)

if __name__ == '__main__':

    inputdir="no_exif_jpg"
    fileextension=".jpg"
    FileName2EXIF(inputdir,fileextension)

