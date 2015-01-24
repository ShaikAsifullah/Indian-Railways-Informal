'''
Created on 25-Oct-2013

@author: Kashaj
'''
import re
def thisAgain():
    f = open('countingDone.txt','r')
    text = f.read();
    f1 = open('spaceOfStations.txt','r')
    f2 = open('TakeCountOfSpaceOfStations.txt','a')
    for lines in f1.readlines():
        lines = lines.strip('\n')
        regex = '(\d+)\s'+lines
        tuples = re.findall(regex,text)
        if(len(tuples) > 0):
            addthis = str(tuples[0])+','+lines+'\n'
            f2.write(addthis)
            
       
        
    f.close()
    f1.close()
    f2.close()
        
thisAgain()        
        
        