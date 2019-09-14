import os
import pprint
import platform
import re
from time import sleep
 
path=''
dict={}

# CreateFile.tx with folder name   
def CreateFile(Path=None):
    DirList=Path.split('/')
    l=len(DirList)
    return open("{}/{} {}".format(Path,DirList[l-1],"#file_size"),'w')
   

# GetSize of each file and print into proper formant of bytes , kb, mb,gb
def GetSize(entry):
    size= entry.stat().st_size
    if size <= 1024 :
        return "{}bytes".format(size)
    elif size <= 1024000:
        return "{:.2f}KB".format(size/ 1024)
    elif size <= 1024000000:
        return "{:.2f}MB".format(size/1024000)
    else:
        return "{:.2f}GB".format(size/1024000000)

# provides key in sorted() basing on size
def comparator (entry):
    return entry.stat().st_size  

# deletes all files.text by CreateFile()
def GetFilepath (Path=None):
    Filename=Path.split('/')[len(Path.split('/'))-1]
    Filepath="{}/{}".format(Path,Filename) 
    return Filepath


# fx tha excludes hiden files that starts with .
def ExeptinalFile (Path=None):
        patten=(r'\.[\w\s-]+$')
        match=re.findall(patten,GetFilepath(Path))
        if  match:
            return True

# fx that gives space between the name and size
def Space (Path=None): 
    space=143-len(Path.name)-len(GetSize(Path))
    result=" "*space
    return result


# gets file dir open all folders to highest level and creats/delets required file
def GetFile (Path=None):
    File=CreateFile(Path)
    File.write("FILENAME:{}FILSIZE\n{}\n".format(" "*127,"_"*143))

    for entry in sorted(os.scandir(Path),key= comparator):
        if entry.is_file():
            File.write("{}{}{}\n{}\n".format(entry.name.upper(),Space(entry),GetSize(entry),"-"*143))

        if entry.is_file() and filter(entry.name):
            print("done")
            dict[entry.name]=entry.path
            
        elif entry.is_dir():
            if ExeptinalFile(entry.path):
                print("skiping {}".format(entry.name))
                continue
            pprint.pprint("SubFolder:{}".format(entry.name.upper()))
            GetFile(entry.path)

        else:
            print(entry.name)
    


# this deletes all filesize.text created previos
def delete_all_Sfile(path=None):
    for entry in os.scandir(path):
        partten=r'(#file_size)$'
        match=re.findall(partten,entry.name)
        if match and entry.is_file():
            os.remove(entry.path)
            print("file deleted")
        elif entry.is_dir():
            delete_all_Sfile(entry.path)

#this collects all filesize.txt from entire target directory
def collect_targets(path=None):
        for f in os.scandir(path):
            if f.is_file():
                for _ in filter(f.name):
                    dict[f.name]=f.path
            elif f.is_dir():
                collect_targets(f.path)

#this filters files to get filesize.txt only
def filter(source):
            partten=r'(#file_size)'
            return re.findall(partten,source)

