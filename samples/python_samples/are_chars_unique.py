#!/usr/bin/python

#1.1  Implement an algorithm to determine if a string has all unique characters. 

def areCharsUnique(givenString):

   if not isinstance(givenString, str):
	print givenString, " is not a string"
	return False

   LetterDict = {}

   for c in givenString:
	if c in LetterDict:
	    print givenString + " contains this character twice: " + c
	    return False
	else: 
	    LetterDict[c] = 1

   print givenString + " Contains no duplicate characters" 
   return True

areCharsUnique("A String!")
areCharsUnique(293874)
areCharsUnique("Not Unique-oo At all")
