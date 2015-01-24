'''
Created on 16-Nov-2013

@author: Kashaj
'''
import re,sqlite3
db = sqlite3.connect('Train_Database.db')
db.text_factory = str
db.row_factory = sqlite3.Row
shortcutlist = []

f = open('onlyShortcuts.txt','r')
for lines in f.readlines():
    lines = lines.strip('\n')
    shortcutlist.append(lines) 
f.close()

f1 = open('takeShortcuts.txt','r')
mytext = f1.read()    
first = 0
takethistrainnum = 0;

f9 = open('refinedErrors.txt','a')

def findPath(edgstr):
    regex = '(\d+)'+'.'+edgstr+'\n'
    trnNum = re.findall(regex,mytext)
    #print(len(trnNum),trnNum)
    #dot = 'Select StnCode from Train_Schedule where Train ='+str(trnNum[0]).split(' ')
    cursor = db.execute('Select StnCode from Train_Schedule where Train = ?',str(trnNum[0]).split(' '))
    stnlistfin = ''
    for row in cursor:
        stnlistfin = row['StnCode']
    
      
    
    edgstr = edgstr.split(',')
    regex = ';'+edgstr[0]+'(.*'+';'+edgstr[1]+')'+';'
             
    taketh = re.findall(regex,stnlistfin)
    
    if ((';'+edgstr[0]+';') in taketh[0]):
        taketh = re.findall(regex,taketh[0])
        
    taketh = edgstr[0]+taketh[0]
    
    
    fullstr = []
    taketh = taketh.split(';')
    for i in range(1,len(taketh)):
        text = taketh[i-1]+','+taketh[i]
        fullstr.append(text)
    
    #fullstr = ';'.join(fullstr)
    for i in range(0,len(fullstr)):
        if(fullstr[i] in shortcutlist):
            replac = findPath(fullstr[i])
            fullstr[i] = replac
            
        
    fullstr = ';'.join(fullstr)
    
    return(fullstr)


def start():
    f8 = open('uniquefinalErrors.txt','r')
    for lines in f8.readlines():
        regex = '(.+)'+'--->'
        
        lines = re.findall(regex,lines)
        
        lines = lines[0].split(',')
        getlist = sendthis(lines[0],lines[1])
        if(len(getlist)>1):
            for i in range(1,len(getlist)):
                takethistrainnum = getlist[i];
                first = 0;
                try:
                    
                    linest = lines[0]+','+lines[1];
                    detailpath = ''
                    
                    
                    
                    cursor = db.execute('Select StnCode from Train_Schedule where Train = ?',str(takethistrainnum).split(' '))
                    stnlistfin = ''
                    print 'Got That'
                    for row in cursor:
                        stnlistfin = row['StnCode']
                    
                      
                    edgstr = linest
                    edgstr = edgstr.split(',')
                    regex = ';'+edgstr[0]+'(.*'+';'+edgstr[1]+')'+';'
                             
                    taketh = re.findall(regex,stnlistfin)
                    print taketh
                    if ((';'+edgstr[0]+';') in taketh[0]):
                        taketh = re.findall(regex,taketh[0])
                        print taketh
                    taketh = edgstr[0]+taketh[0]
                    
                    
                    fullstr = []
                    taketh = taketh.split(';')
                    for i in range(1,len(taketh)):
                        text = taketh[i-1]+','+taketh[i]
                        fullstr.append(text)
                    
                    #fullstr = ';'.join(fullstr)
                    for i in range(0,len(fullstr)):
                        if(fullstr[i] in shortcutlist):
                            replac = findPath(fullstr[i],0)
                            fullstr[i] = replac
                            
                        
                    fullstr = ';'.join(fullstr)
                                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    if(len(detailpath) > 2):
                        detailpath = linest+'----->'+detailpath+'\n'
                        f9.write(detailpath)
                        break
                except:
                    tes = getlist[i]+' NoMatching for '+lines[0]+','+lines[1]
                    print tes
                    continue;    
                
            


        
        











def sendthis(str1,str2):
    mark = 0;
    healthy = 0
    listr = []
    if(healthy == 0):
        f1 = open('EdgeswithTrainNumbers.txt','r')
        
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
                        
                        listr.append(str(trainnum))
                        mark = 0;
                        
                if(mark == 1):
                    if(str1 != str(trainnum)):
                        mark = 0;
                        
                        
        f1.close()  
        return listr
                    
    
start()