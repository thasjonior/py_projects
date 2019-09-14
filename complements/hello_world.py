import os
import sys
import pprint
# translated, not compiled
# syntaxt
# no semicolons, no cruly braces, only indents
variables_passed = sys.argv
name = ''
if len(variables_passed) <= 1:
    print('--- Usage: hello_world.py user_name ---\n Username must be specified')
#   sys.exit()
else:
    print("Command line variables")
    for var in sys.argv:
        print(var)
    name = sys.argv[1]
if name:
    print("Hello {}".format(name))
else:
    print("Hello World {} ".format(os.getlogin()))

def print_hello():
    print("Hello World")

print_hello()
# data types
# Python is DYNAMICALLY typed, we don't need to specify data types for variables
# C is statically or strongly typed: you have to specify the variable data types
# new_module typing: an optional module to specify variable types
age = 34
name = "Jean"
print("My age is "+str(age))
def print_name():
    print("My name is {} and my age is {}".format(name, age)) # recommended
# control structures
# if elif else
age = 32
if age == 34:
    print_hello()
elif age < 34:
    print_name()
else:
    print("We couldn't tell your age")
# data structures: containers
# Lists [], tuples (), dictionary{key: value}, set: {} holds no duplicates
files = ['hello_world.py', 'parallel.py', 'README.md', 'synch.py']
# for f in files:
#     print(f)
# # lists zero-indexed and mutable
# files[0] = 'downloader'
# for f in files:
#     print(f)
# tuples: immutable
person_details = ('Ngwada', 'Kilocha', 'Iwungilo')

business_card = {"name": "Goodluck", "education": "JKS", "greeting": "Monili"}
# for key, value in business_card.items():
#     print("{}: {}".format(key, value))
# pc_details = {"sn":"123-432N", "model": "Dell", "os": "Windowx 10", "assigned_to": "Halla"}
# for key, value in pc_details.items():
#     print("{}: {}".format(key, value))

# library
# modules os, sys


print("My current working directory is: {}".format(os.getcwd()))
os.chdir("/home/judethaddeus/Documents/")
print("am now working in: {}".format(os.getcwd()))
print("I am logged in as {}".format(os.getlogin()))

import pprint
our_set = {"Sovello", "Sovello", "Ngwada", "Ngwada", "Halla", "Halla"}
pprint.pprint(our_set)
pprint.pprint(os.uname())
