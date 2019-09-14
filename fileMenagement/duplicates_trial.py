import os
from pprint import pprint
# fx find files dictionary by size
def Create_files_dictionary(Path,dictionary):
    for entry in os.scandir(Path):
        if entry.is_file():
            if dictionary.get(entry.stat().st_size):
                dictionary[entry.stat().st_size].append(entry.path)
            else:
                dictionary[entry.stat().st_size]= [entry.path]
        elif entry.is_dir():
                Create_files_dictionary(entry.path,dictionary)
    return dictionary

# pprint(Create_files_dictionary(r'/home/judethaddeus/Documents/tester',dictionary))

# get duplicates
def Get_duplicates(Path):
    dictionary={}
    Create_files_dictionary(Path,dictionary)
    duplicates={}
    for size,files in dictionary.items():
        if len(files)> 1:
            duplicates[size]=files
    return duplicates

# pprint(Get_duplicates(r'/home/judethaddeus/Documents/tester'))
# get user confirmation
def Get_user_Confirmation():
    confirm=input(print("The file marked should be deleted! \n press [Y/y] to confirm or [N/n] to cancel:")  )  
    if confirm[0].lower() == 'y':
         return True
    elif confirm[0].lower()=='n':
        print("Canceling process....")
        exit()
    else:
        print("Wrong choice!\n Quiting....")
        exit()


# present duplicates
def Present_duplicates(duplicates):
    index=1
    for size,files in duplicates.items():
        print("The files with {}bytes".format(size))       
        for file in files:
            print("[]{}.....{}".format(index,file))
            index+=1
    try:
        choice= input("Enter the number of file to be deleted:")
        choice=int(choice)
    except OSError as error:
        print("Make choice again!")
    except ValueError or TypeError:
        print("Number was expected!")
        print(" Quiting.....")
        exit()
    # finally:
    index= 1
    for size,files in duplicates.items():
        print("###The choosen file to be deleted is marked with [X]###")
        for file in files:
            # check= 'X' if index == int(choice) else ''
            # print("{}{}.....{}".format([check],index,file))
            if index == int(choice):
                print("[X]{}.....{}".format(index,file))
            else:
                print("[]{}.....{}".format(index,file))
            index+=1

    
    if  Get_user_Confirmation():
        index=1
        for size,files in duplicates.items():
            for file in files:
                if index == int(choice):
                    print("{}Removed".format(files[index-1]))
                    os.remove(files[index-1])
                else:
                    pass
                    print("wrong logic")
                index+=1



dupicates=Get_duplicates(r'/home/judethaddeus/Documents/tester')
pprint(Present_duplicates(dupicates))


     
   

# get user decision
# confirm user decision
# delete duplicate

