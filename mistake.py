'''
Created on 24-Oct-2013

@author: Kashaj
'''
import re

def findThis():
    f = open('takeshortcuts.txt','rw')
    text = f.read()
    tuples = re.findall(r'(\d\d\d\d\d[A-Z]+)',text)
    print len(tuples)
    stri = ''
    for i in tuples:
        stri += i
    f.write(stri)

findThis()