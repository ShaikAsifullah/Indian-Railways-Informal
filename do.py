'''
Created on 22-Oct-2013

@author: Kashaj
'''
def doThis():
    #f = open('CountingEdges.txt','r')
    f1 = open('countingDone.txt','r')
    """count = 0
    for lines in f.readlines():
        count += 1
        lines = lines.strip(" ");
        lines = lines.strip('\n')
        f1.write(lines)
        if (count % 2 == 0):
            f1.write('\n')
        
    f.close()
    f1.close()"""
    count = 0;
    for lines in f1.readlines():
        lines = lines.split(' ');
        count += int(lines[0])
    print count    
    
if __name__ == '__main__':
    doThis()    
        