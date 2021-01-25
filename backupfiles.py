import os
import shutil
source=input("Enter the source folder name")
destination=input("Enter destination folder name")
source=source+'/'
destination=destination+'/'
listoffiles=os.listdir(source)
for file in listoffiles:
    shutil.copy((source+file),destination)