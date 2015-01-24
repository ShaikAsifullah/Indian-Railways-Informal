'''
Created on 30-Oct-2013

@author: Kashaj
'''
import re
def doWork():
    f = open('TakeCountOfSpaceOfStations.txt','r')
    f1 = open('countingDone.txt','r')
    f2 = open('spaceofstationsEdgesNumbers.txt','w')
    text = f1.read()
    for lines in f:
        lines = lines.strip('\n')
        take = lines;
        lines = lines.split(',')
        lines = lines[1]+ ',' + lines[2]
        lines += ','
        regex = lines+'(.*)'
        tuple = re.findall(regex,text)
        #print(len(tuple))
        if(len(tuple)>0):
            take += ','
            take += tuple[0]
            f2.write(take)
            f2.write('\n')
        
  
        
doWork()        
        
        
        
        
            