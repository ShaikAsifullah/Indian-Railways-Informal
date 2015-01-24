'''
Created on 22-Oct-2013

@author: Kashaj
'''
def openfile():
    f = open('takeGraphmlOfSpaceOfStations.txt','a')
    f1 = open('spaceofstationsEdgesNumbers.txt','r')
    
    for lines in f1.readlines():
        lines = lines.strip('\n')
        lines = lines.split(',')
        strength = lines[0]
       
       
        node1 = 'n'
        node1 += str(lines[3])
        node2 = 'n'
        node2 += str(lines[4].strip('\n'))
       
        strn = '\t<edge source="'+node1+ '" target="' +node2+ '">\n\t\t<data key="e_weight">' +str(strength) + '</data>\n\t</edge>\n'  
        f.write(strn)
        
    f.close()
    f1.close()

openfile()    