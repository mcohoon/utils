#!/usr/bin/python

# A python script to return your Pinterest boards
# reference to pinterest api: https://developers.pinterest.com/docs/api/access_token/
# requires the file .pinterest_token.txt in the cwd access_token:Provide_Access_token
 
# curl https://api.pinterest.com/v1/me/boards/?access_token=.....

import os
import requests
import logging
import sys

# create logger
logger = logging.getLogger('pinterest_api_logger')

logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel('DEBUG')
if logger.getEffectiveLevel() == logging.DEBUG:
   print "Loging level debug"

# dictionary for http params
token = {}

def returnboards():
    request_url = 'https://api.pinterest.com/v1/me/boards'
    makeRequest(request_url, token)

def makeRequest(request_url, token):
    response = requests.get(request_url, params=token)
    if response.status_code == 200:
        logger.debug("It's all good 200 OK")
        print "response " + response.text
    else:
        logger.error( "http status code " + str(type(response.status_code)))
        logger.error( "http message" + response.text)
        logger.error( "request url " + response.url)

	# InsecurePlatformWarning: A true SSLContext object is not available.  status_code 401
    # sudo pip install requests[security]

def readPinterestToken(tokenFile):
    if os.path.isfile(tokenFile):
    	TokenFile = open(tokenFile, "r")
    	for line in TokenFile:
    		lineList = line.rstrip().split(':')
    		token[lineList[0]] = lineList[1]
    		print token[lineList[0]]
    else:
    	print "Didn't file the Token File"

if __name__ == "__main__":
	PinterestApiTokenFile = ".pinterest_token.txt"
	readPinterestToken(PinterestApiTokenFile)
	returnboards()

