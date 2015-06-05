import re

def matching():
    p = re.match('[a-z]+', "tempo0decel")
    print "Match [a-z]+ for string 'tempo0decel' returns one Match Object ", p.group()
#    n = re.match('[a-z]+', "01tempo0decel")
#    if len(n.group()) ==0:
#        print "Match [a-z]+ for string 01tempo0decel returns nothing because the beginning of the string doesn't match " 

def searching():
    s = re.search('[a-z]+', "tenio9decal")    
    print "Search returns one Match Object ", s.group()
    n = re.search('[a-z]+', "01tempo0decel")
    print "Seach [a-z]+ for string 01tempo0decel returns the first instance of the match", n.group()


def subgroups():
    ipv4 = re.match(r'(\d+).(\d+).(\d+).(\d+)', "200.13.45.128")
    print "Using subgroups in Patterns returns more Match Objects."
    for n in range(len(ipv4.groups())):
        print n, " Match Object ", ipv4.groups()[n]
    print ipv4.groups()
    print "GROUP: ", ipv4.group(), " isString: ", type(ipv4.group())
    print "Group Inclusive Range", [ipv4.group(x) for x in range(5)] #list comprehension  

def compfindall():
    # This doesn't work because it returns each digit separately
    ipv4 = re.findall(r'[(\d)+]', "200.13.45.128")
    print "Using re.findall is much better than using subgroups with re.match -- because you don't have to unpack the re.group objects"
    print "ipv4 = re.findall(r'[(\d+)]', \"200.13.45.128\") returns the list", ipv4

def subReplString():
    original = "the original string the"
    print "before sub:", original
    original = re.sub('the', 'AAAA', original)
    print "after re.sub", original

def subReplFunction():
    print re.sub('-{1,2}', dashrepl, 'pro----gram-files')    

def subReplList():
    "This will not work re.sub() doesn't take a list as an input"
    origList = ['a', 'fat cat', 'wonderful']
    newList = re.sub('a', 'AAA', origList)
    print "origList", origList
    print "newList", newList

def dashrepl(matchobj):
    if matchobj.group(0) == '-': return ' '
    else: return '-'

def findall():
    original = "Cami loved cheese and butter, but Pippin loved baccon. Jeni loved Cami and Pippin"
    found = re.findall(r'[A-Z][a-z]*', original) 
    print found

def regexSplit():
    original = "1. another fine day 2 twelve days 3 caturday 8991 final"
    print re.split(r'[1-9]+', original)


def stringSplit():
    original = "1. another fine day 2 twelve days 3 caturday 8991 final"
    found = original.split()
    print "string.split(): ", found
    regexFound = re.split(r'\s', original)
    print "re.split(): ", regexFound


#matching()
#searching()
subgroups()
#compfindall()
subReplString()
#subReplFunction()
findall()
regexSplit()
#stringSplit()
#subReplList() # This will not work re.sub cannot take a list as input
