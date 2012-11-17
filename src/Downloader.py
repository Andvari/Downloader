#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Created on Nov 17, 2012

@author: nemo
'''

import urllib2

BLOCK_SIZE = 60000

def get_url(url, filename):
    fl = open(filename, "wb")
    req = urllib2.urlopen(url)
    print "Start reading"

    l = 0
    page = req.read(BLOCK_SIZE)

    l += len(page)
    print l/1000.
    while(len(page) == BLOCK_SIZE):
        fl.write(page)
        page = req.read(BLOCK_SIZE)
        l += len(page)
        print l/1000.
    
    fl.write(page)
    print "Stop reading"


url = "<here must be URL>"
print "Start downloading"
get_url(url, "<here must be FILENAME>")
print "Download complete"
