import sys
import os

def ParseArgs():
    Error1 = """
# usage: which.py [executable name]
# usage: which.py cat
"""
    if len(sys.argv) != 2:
        print Error1
        exit
    else:
        findExec(sys.argv[1])

def findExec(execName):
    print "execName: ", execName
    print "$HOME: ", os.environ['HOME']
    print "$PATH: ", os.environ['PATH']
    PathEntries = os.environ['PATH'].split(":")
    print PathEntries
    for entry in PathEntries:
        if os.path.isdir(entry):
            for file in os.listdir(entry):
                if execName in file:
                    print "The path is: ", os.path.join(entry,file)
                    return  
    print "I didn't find the command ", execName
    

ParseArgs()

