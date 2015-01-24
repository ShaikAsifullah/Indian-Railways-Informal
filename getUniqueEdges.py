'''
Created on 24-Oct-2013

@author: Kashaj
'''
def openfile():
    f = open('uniqueEdges.txt','a')
    f1 = open('countingDone.txt','r')
    
    for lines in f1.readlines():
        lines = lines.split(' ')
        strength = lines[0]
        lines = lines[1].split(',')
        strng = lines[0]+','+lines[1]+'\n'
        f.write(strng)
    f.close()
    f1.close()

openfile()      