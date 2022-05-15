import os
import shutil
source = input("Enter the source path: ")
dest = input("Enter the destination path: ")
if os.path.exists(source) and os.path.exists(dest):
    source += '/'
    dest += '/'
    listOfFiles = os.listdir(source)
    for file in listOfFiles:
        shutil.copy((source+file),dest)
else:
    print("Please enter the correct path")