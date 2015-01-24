'''
Created on 24-Oct-2013

@author: Kashaj
'''
f = open('uniqueEdges.txt','r')

#f2 = open('spaceOfStations.txt','a')
def openfile():
   
    
    for lines4 in f.readlines():
        lines = lines4.split(',')
        #doThis(lines[0],lines[1].strip('\n'))
        doThis('AJJ','MAS')
        break 
        
                    
        
        
    
def doThis(str1,str2):
    mark = 0;
    healthy = 0
    listr = []
    if(healthy == 0):
        f1 = open('EdgeswithTrainNumbers.txt','r')
        #f3 = open('takeShortcuts.txt','a')
        text = f1.read()
        mylist = text.split('\n')
       
        
        for lines3 in mylist:
                lines1 = lines3.split(',')
                
                
                if (mark == 0):
                    if ((str1 == lines1[1]) & (str2 != lines1[2].strip('\n'))):
                        trainnum = lines1[0]
                        mark = 1
                        continue
                
               
                if(mark == 1):
                    if((lines1[0] == str(trainnum)) & (str2 == lines1[2].strip('\n'))):
                        
                        healthy = 1;
                        take = trainnum+','+str1+','+str2+'\n'
                        #f3.write(take)
                        print take
                        listr.append(str(trainnum))
                        mark = 0;
                        
                if(mark == 1):
                    if(str1 != str(trainnum)):
                        mark = 0;
                        
                        
        f1.close()  
        print 'This is list :'
        print listr  
                    
    if(healthy == 0):
            wrt = str1+','+str2+'\n'
            #f2.write(wrt)
            print wrt
        
    
openfile() 
                   
                        
                
                
                
                    
            
                
                
                
        