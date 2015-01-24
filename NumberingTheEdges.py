'''
Created on 15-Oct-2013

@author: Kashaj
'''
def fileopen(filename):
    f = open(filename,'r')
    list1 = []
    for lines in f:
        lines = lines.strip('\n')
        lines = lines.strip(' ')
        list1.append(lines)
    f.close()
    
    f = open('sortedEdges.txt','r')
    f1 = open('EdgesInNumbers.txt','a')
    for lines in f:
        lines = lines.strip('\n')
        lines = lines.strip(' ')
        text = lines
        lines = lines.split(',')
        
        for i in range(0,len(list1)):
            if(str(lines[0]) == str(list1[i])):
                break
        text += ','
        text += str(i)
        text += ','
        for i in range(0,len(list1)):
            if(str(lines[1]) == str(list1[i])):
                break
        
        text += str(i)
        f1.write(text)
        f1.write('\n')    
        
    f.close()
    f1.close()    
        
if __name__ == '__main__':
    fileopen('SortedUniqueStations.txt')        
        