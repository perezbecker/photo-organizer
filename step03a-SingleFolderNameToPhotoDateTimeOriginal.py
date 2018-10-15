import datetime
import os
import subprocess

# Function to rename multiple files
def main():
    inputdir="2017-12-08"
    fileextension=".jpg"

    DateTimeStartString=inputdir+" 00:00:01"
    files=[]
    for filename in os.listdir(inputdir):
        files.append(filename)
    files.sort()

    for i in range(len(files)):
        print(files[i])
        DateTime=datetime.datetime.strptime(DateTimeStartString, "%Y-%m-%d %H:%M:%S")
        NewDateTime=DateTime+datetime.timedelta(seconds=i)
        NewDateTimeString=NewDateTime.strftime("%Y:%m:%d %H:%M:%S")
        print(NewDateTimeString)
        subprocess.call(["exiftool","-DateTimeOriginal=\""+NewDateTimeString+"\"","./"+inputdir+"/"+files[i]])
        DestinationName = NewDateTime.strftime("%Y-%m-%d_%H%M%S")+"a"+fileextension
        print(DestinationName)
        os.rename("./"+inputdir+"/"+files[i], "./"+inputdir+"/"+DestinationName)
        subprocess.call(["rm","./"+inputdir+"/"+files[i]+"_original"])

# Driver Code
if __name__ == '__main__':

    # Calling main() function
    main()

