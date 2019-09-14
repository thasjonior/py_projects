import os
from pprint import pprint 
import time
# file manager: to see duplicate files and decide to delete or whatever
# find duplicates in a folder
    # find duplicates in all folders
    # group possible duplicates
# present duplicates to user with options: delete, etc
# user selects files and an action on the files
# perform user action: delete if user selected to delete or whatever

# containers
# Set: contains only unique items
# List: can contain duplicates, grouping may not be easy
# tuples: mutable (non-modifiable)
# dictionary: {key: value}
# listPCM = [1, 2, 3, 4, 5]
# listPCB = [6, 3, 9, 10]
# listXXXXXX = [f, fdask, fdsaa, fd, rwr]
# dictionary(listPCM: [1, 2, 3, 4, 5], listPCB: [6, 3, 9, 10], listXXXXXX = [f, fdask, fdsaa, fd, rwr], listPCM: [])
# dictionary(12343: [file1.txt, file2.java, file5.csv], 4323243:[file, file.jpg, file8.asd], 4322433: [file.djvu, file.mov, file.webm])
# dictionary(file1.txt: [/opt/projects, /opt/home/Desktop, /home/fugit/Downloads], file8.dsl: [c:\Users\halla\Documents, c:\halla_projects\webproject])
#

def getDuplicates(path, dictionary):
    for entry in os.scandir(path):
        if entry.is_file():
            # check if this file size is a key in found_files
            if dictionary.get(entry.stat().st_size):
                dictionary[entry.stat().st_size].append(entry.path)
            else:
                dictionary[entry.stat().st_size] = [entry.path]
        elif entry.is_dir():
            getDuplicates(entry.path, dictionary)

# using file size as a key
def findDuplicates(path):
    found_files = {}
    getDuplicates(path, found_files)
    duplicates = {}
    for size, files in found_files.items():
        if len(files) > 1:
            duplicates[size] = files
    return duplicates

def presentDuplicateFiles(duplicate_files):
    index = 1
    """
    Enter number to select file to delete
    Files with size: {}
    []    --location1
    []    --location2
    []    --location3
    """
    for size, files in duplicate_files.items():
        print("Files with size {}".format(size))
        for f in files:
            print("[] {} - {}".format(index, f))
            index += 1
    try:
        choice = input("Enter a file number to delete: ")
        choice = int(choice)
    except OSError as error:
        print("Make a wise choice: {}".format(error))
    except ValueError:
        print("A number was expected.")
    # finally:
    #     print("Quitting")
    #     exit(0)
    index = 1
    print("Files marked with X are going to be deleted")
    for size, files in duplicate_files.items():
        print("Files with size {}".format(size))
        for f in files:
            check = 'x' if index == int(choice) else ''
            print("[{}] {} - {}".format(check, index, f))
            index += 1
    confirm = input("Confirm to delete the file marked x: [Y/y]es/[N/n]o or q to quit: ")
    if confirm[0].lower() == 'y':
        os.remove()
    elif confirm[0].lower() == 'n':
        pass
    elif confirm[0].lower() == 'q':
        print("Quiting", end='')
        time.sleep(1)
        print('.', end='')
        time.sleep(1)
        print('.', end='')
        time.sleep(1)
        print('.')
    else:
        second_confirm = input("Choice not recognized. Confirm to delete the file marked x: [Y/y]es/[N/n]o, or q to quit: ")
        index = 1
        for size, files in duplicate_files.items():
            print("Files with size {}".format(size))
            for f in files:
                check = 'x' if index == int(choice) else ''
                print("[{}] {} - {}".format(check, index, f))
                index += 1
        if second_confirm[0].lower() == 'y':
            os.remove()
        elif second_confirm[0].lower() == 'n':
            pass
        elif second_confirm[0].lower() == 'q':
            print("Quiting", end='')
            time.sleep(1)
            print('.', end='')
            time.sleep(1)
            print('.', end='')
            time.sleep(1)
            print('.')
        else:
            print("Option not recognized. Quitting", end='')
            time.sleep(1)
            print('.', end='')
            time.sleep(1)
            print('.', end='')
            time.sleep(1)
            print('.')

if __name__ == '__main__':
    duplicates = findDuplicates(r'/home/judethaddeus/Documents/tester')
    presentDuplicateFiles(duplicates)