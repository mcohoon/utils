#/usr/bin/python
# import os for the os.walk() function
# os.walk returns a list of tuples: 3-tuple (dirpath, dirnames, filenames)

import os
import sys

def ParseArgs():
    Error1 = """    # USAGE #
    # filesystemWalk.py [directory]
    # filesystemWalk.py /Users/mcohoon/Devel/PythonPractice """

    if len(sys.argv) != 2:
        print Error1
    elif not os.path.abspath(sys.argv[1]):
        print Error1
    else:
        start = sys.argv[1]
        filesystemWalk(start)

def filesystemWalk(start):
    path = os.path.abspath(start)
    print "path = " +path
    for dirpath, dirnames, filenames in os.walk(path):
        print "Found the initial directory " + dirpath
        for file in filenames:
            print "Found the file ", os.path.join(dirpath, file)
        for dir in dirnames:
            print "Found the directory ", os.path.join(dirpath, dir)

ParseArgs()

#start = "/Users/mcohoon/Devel/PythonPractice"
#start = "."
#filesystemWalk(start)

#os.path to take a string and make it into a full directory path
#os.walk gives you the path to the directory as the first value in the loop
#use os.path.join() to create full filename:
