import os
import shutil
path = input("Enter the directory you want to organise: ")
p = os.path.exists(path)
if p :
    listOfFiles = os.listdir(path)
    for file in listOfFiles:
        name, ext = os.path.splitext(file)
        ext = ext[1:]
        if ext == "":
            continue
        if os.path.exists(path+'/'+ext):
            shutil.move(path+'/'+file,path + '/'+ext+'/'+file)
        else:
            os.mkdir(path+'/'+ext)  
            shutil.move(path+'/'+file,path + '/'+ext+'/'+file)
else:
    print("Please enter the correct path")