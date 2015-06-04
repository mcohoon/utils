import sys, os, stat

def filemode(file):
    st = stat.S_IMODE (os.stat(file).st_mode)
    print "User read: ", bool(st & stat.S_IRUSR)
    print "User write: ", bool(st & stat.S_IWUSR)
    print "User exec: ", bool(st & stat.S_IXUSR)

    print "Group read: ", bool(st & stat.S_IRGRP)
    print "Group write: ", bool(st & stat.S_IWGRP)
    print "Group exec: ", bool(st & stat.S_IXGRP)

    print "Other read: ", bool(st & stat.S_IROTH)
    print "Other write: ", bool(st & stat.S_IWOTH)
    print "Other exec: ", bool(st & stat.S_IXOTH)

def parseArgs():
    Usage = "# usage: filemode.py filename.txt"

    if len(sys.argv) != 2:
        print Usage
    elif os.path.isfile(sys.argv[1]):
        filemode(sys.argv[1])     
    else:
        print Usage

parseArgs()
