'''
Created on 15-Nov-2013

@author: Kashaj
'''
f1 = open('realthingnow.txt','a')
f2 = open('Errors.txt','a')
def ak():
    f = open('NoteDown.txt','r')
    for lines in f.readlines():
        lines = lines.split('----->')
        edge = lines[0].split(',')
        listc = lines[1]+':'
        test = edge[0]+','
        if(test == listc[0:len(test)]):
            test = ';'+test
            tew = listc.rfind(test)
            if(tew != -1):
                listc = listc[tew+1:len(listc)]
            test1 = ','+edge[1]+':'
            if(test1 == (listc[-(len(test1)):-1] + listc[-1])):
                testw = edge[0]+','+edge[1]+'------>'+listc+'\n'
                f1.write(testw)
                
            else:
                testw = edge[0]+','+edge[1]+'------>'+listc+'\n'
                f2.write(testw)
                
        else:
            test = ';'+test
            tew = listc.rfind(test)
            if(tew != -1):
                listc = listc[tew+1:len(listc)]
                
            else:
                testw = edge[0]+','+edge[1]+'------>This is s special Error'+listc+'\n'
                f2.write(testw)
                continue
                
            test1 = ','+edge[1]+':'
            if(test1 == (listc[-(len(test1)):-1] + listc[-1])):
                testw = edge[0]+','+edge[1]+'------>'+listc+'\n'
                f1.write(testw)
            
            else:
                testw = edge[0]+','+edge[1]+'------>'+listc+'\n'
                f2.write(testw)
                
def thiss():
    f3 = open('Errors.txt','r+')
    count = 0;
    text = ''
    for lines in f3.readlines():
        if(count%2 == 0):
            text += lines;
        count += 1   
    f3.write(text) 

def tryy():   
    lines_seen = set() # holds lines already seen
    outfile = open('newErrors.txt', "w")
    for line in open('Errors.txt', "r"):
        if line not in lines_seen: # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()
                
tryy()
f1.close()
f2.close()
                
                
                
        
        