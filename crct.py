'''
Created on 14-Nov-2013

@author: Kashaj
'''
f1 = open('soledge.txt','a')
def go():
    f = open('uniquefinalErrors.txt','r')
    for lines in f.readlines():
        lines = lines.split('--->')
        if(len(lines[0])>2):
            lines[0] += '\n'
            f1.write(lines[0])
             
go()