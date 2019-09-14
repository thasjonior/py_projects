import os 
import time
x=r'/home/judethaddeus/Documents/tester/fileX/'

def timediff(p):
    nn =time.time()
    maxtime= os.stat(p).st_atime
    diff= nn - maxtime
    return diff

for f in os.scandir(x):
    if f.is_file():
        # print("m")
        print("{} {}".format(f.name,timediff(f.path))
