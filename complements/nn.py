# get the main file Path
# open all the directories in it
# get file extensions onl
# groupfile accoding to their extension in dictionar



import os
import pprint
import re
# regular expression to check for extension
def re_ext(name):
    pertten=(r'\.\w+$')
    results=re.findall(pertten,name)
# fx creating file dictionary base on extension name
def ext_dic(name):
    ext={}
    key=get(re_ext(name))
    if ext.key:
        ext.append()
    else:
        ext[key]=[entry.name]
    return ext

# fx tha calls directory and access the content

def FileOpen(Path):
    lv=0
    for entry in os.scandir(Path):
        if entry.is_file():
            pprint.pprint("FileName:{}\t size:{}bytes".format(re_ext(entry.name),os.stat(entry.path).st_size))
        elif entry.is_dir():
            lv+=1
            print("Subfolder:{} \t level No:{}".format(entry.name.upper(),lv))
            print("--"*30)
            FileOpen(entry.path)

def Call():
    FileOpen(r'/home/judethaddeus/Documents')

Call()
