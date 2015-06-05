#!/usr/bin/python

import re

def re_search():
    found = re.search(r'[15]', "Once 15 years ago, I was 15")
    print found.groups

re_search()
