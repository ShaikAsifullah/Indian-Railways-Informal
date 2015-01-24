'''
Created on 15-Oct-2013

@author: Kashaj
'''
def main():
    f = open('Edges.txt','r')
    list1 = []
    text = ''
   
    for lines in f:
        tuples = lines.split(',')
        list1.append(tuples)
        
    list1 = sorted(list1)
    for things in list1:
        things = ','.join(things)
        text += things
 
    f1 = open('sortedEdges.txt','w')
    f1.write(text);
    f.close;
    f1.close;
    
    
    
if __name__ == '__main__':
    main()    