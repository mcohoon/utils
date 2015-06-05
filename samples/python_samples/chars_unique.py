#!/usr/bin/python

#1.1  Implement an algorithm to determine if a string has all unique characters. 
def AreCharsUnique(input):

   if not isinstance(input, str):
      print "Input given, %s was not a string" %input
      return(0)

   CharDictionary = {}

   for c in input:
      if c in CharDictionary:
         print "The string, %s, contains duplicate characters %s" %(input, c)
         return(0)
      else:
         CharDictionary[c] = 1
   print "The string %s contains unique characters" %input

AreCharsUnique(890.239)
AreCharsUnique("inthesam")
AreCharsUnique("These are not")
   
   
