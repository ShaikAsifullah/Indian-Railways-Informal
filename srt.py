'''
Created on 16-Nov-2013

@author: Kashaj
'''
import re
f2 = open('addon.txt','a')
f3 = open('NoteDown.txt','r')
f5 = open('uniquefinalErrors.txt','a')
this = f3.read();
def got():
    f = open('Gotcha.txt','r')
    for lines in f.readlines():
        lines = lines.strip('\n')
        trym = lines.split(',')
        regex = lines+'----->'+'('+trym[0]+'.+)'
        lines1 = re.findall(regex,this)
        if(len(lines1)>0):
            lines = lines+'----->'+lines1[0]+'\n'
            f2.write(lines)

def dosome():
    f = open('gotErrorsagain.txt','r')
    text = ''
    for lines in f.readlines():
        if(text != lines):
            f5.write(lines)
            text = lines
            
        
            
        
            
dosome()
            
            