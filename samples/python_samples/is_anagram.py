#!/usr/bin/python

StringA = "efg"
StringB = "ge"

StringC = "racecar"
StringD = "rraacce"

def IsAnagram(String1, String2):
    # Error check that we were given strings

    for c in String1:
        for x in range(len(String2)):
           if c == x:
               String2[x] = ""
           elif c != x:
               continue
           else:
                print "Strings1 and String2 are not Anagrams"
                return 0
    if len(String2) == 0:
        print "Anagrams!"
    else:
        print "Not Anagrams"
        print "String1" + String1
        print "String2" + String2

IsAnagram(StringA, StringB)

IsAnagram(StringC, StringD)

