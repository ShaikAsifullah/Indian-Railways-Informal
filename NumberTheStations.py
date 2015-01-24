'''
Created on 15-Oct-2013

@author: Kashaj
'''

def openfile(filename):
    
    f = open(filename,'r')
    f1 = open('UniqueStationNames.txt','a')
 
    UniqueStationList = []
    
     
    for lines in f:
        tuples = lines.split(',')
        tuples[0] = tuples[0].strip('\n')
        tuples[0] = tuples[0].strip(' ')
        tuples[1] = tuples[1].strip('\n')
        tuples[1] = tuples[1].strip(' ')
        if tuples[0] not in UniqueStationList:
              
            UniqueStationList.append(tuples[0])
            
        if tuples[1] not in UniqueStationList:
                  
            UniqueStationList.append(tuples[1])
            
    UniqueStationList = list(set(UniqueStationList))       
    for text in UniqueStationList:
        text = text.strip('\n')
        text = text.replace(' ','')
        f1.write(text)
        f1.write('\n')
        

        
            
    f.close()
    f1.close()
    
if __name__ == '__main__':
    openfile('sortedEdges.txt')
        
