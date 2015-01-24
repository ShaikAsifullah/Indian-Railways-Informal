'''
Created on 19-Nov-2013

@author: Kashaj
'''
import sqlite3,re
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
f1.close()
count = 0   
listf = []

spofstat = open('spaceofstat.txt','a')
errstat = open('ErrorsInSpaceofStat.txt','a')

def removobj(liste,elem):
    global count
    while elem in liste:
        liste.remove(elem)
        count += 1
    return liste     

def go():
    global listf
    f = open('sortedEdges.txt','r')
    for lines in f.readlines():
        lines=lines.strip('\n')
        listf.append(lines)
    f.close()
    
    remlist = []
    f = open('45.txt','r')
    for lines in f.readlines():
        lines= lines.strip('\n')
        remlist.append(lines)
    f.close()
    
    for elems in remlist:
        listf = removobj(listf,elems)
        
def start():
    for lines in listf:
        lines = lines.split(',')
        getlist = sendthis(lines[0],lines[1])
        if(len(getlist) > 0):
            count = 0
            for i in range(0,len(getlist)):
                try:
                    path = getdetail(lines[0],lines[1],getlist[i])
                    if(len(path) >1):
                        
                        thirst = lines[0]+','+lines[1]+'---->'+path+'\n'
                        spofstat.write(thirst)
                        break
                except:
                    
                    err = lines[0]+','+lines[1]+' for train num '+getlist[i]+'\n'
                    errstat.write(err)
                    count += 1
                    if(count == 2):
                        break
                    continue
                
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
                                         
                        listr.append(str(trainnum))
                        mark = 0;
                        
                if(mark == 1):
                    if(str1 != str(trainnum)):
                        mark = 0;
        f1.close()  
        return listr
           
def getdetail(stn1,stn2,numtrain):
    cursor = db.execute('Select StnCode from Train_Schedule where Train = ?',(str(numtrain),))
    
    stnlistfin = ''
    for row in cursor:
        stnlistfin = row['StnCode']
    #print '1. '    
    #print stnlistfin    
    regex = ';'+stn1+'(.*'+';'+stn2+')'+';'
    #print regex
    if(stnlistfin.startswith(stn1)):
        regex = stn1+'(;'+'.*'+stn2+')'+';'
    else:    
        regex = ';'+stn1+'(;'+'.*'+stn2+')'+';'
        
    if(stnlistfin.endswith(stn2)):
        regex = regex[:-1]
    taketh = re.findall(regex,stnlistfin)   
    if ((';'+stn1+';') in taketh[0]):
        taketh = re.findall(regex,taketh[0])
    
    taketh = stn1+taketh[0]
    fullstr = []
    taketh = taketh.split(';')
    for j in range(1,len(taketh)):
        text = taketh[j-1]+','+taketh[j]
        fullstr.append(text)
    
    for k in range(0,len(fullstr)):
        if(fullstr[k] in shortcutlist):
            replac = findPath(fullstr[k])
            fullstr[k] = replac
            
    fullstr = ';'.join(fullstr)
    return(fullstr)


def findPath(edgstr):
    #print '\nEvaluating Regex'
    regex = '(\d+)'+'.'+edgstr+'\n'
    trnNum = re.findall(regex,mytext)
    #print ' This is the train number I got '+str(trnNum)
    cursor = db.execute('Select StnCode from Train_Schedule where Train = ?',str(trnNum[0]).split(' '))
    stnlistfin = ''
    for row in cursor:
        stnlistfin = row['StnCode']
    #print ' This is the stnlist'+stnlistfin
    edgstr = edgstr.split(',')
    if(stnlistfin.startswith(edgstr[0])):
        regex = edgstr[0]+'(;'+'.*'+edgstr[1]+')'+';'
    else:    
        regex = ';'+edgstr[0]+'(;'+'.*'+edgstr[1]+')'+';'
        
    if(stnlistfin.endswith(edgstr[1])):
        regex = regex[:-1]
    #print 'This is regex :'+regex        
    taketh = re.findall(regex,stnlistfin)
    #print ' This is cutout portion from the string'
    #print taketh
    if ((';'+edgstr[0]+';') in taketh[0]):
        taketh = re.findall(regex,taketh[0])
    #print taketh[0]   
    taketh = edgstr[0]+taketh[0]
    
    fullstr = []
    taketh = taketh.split(';')
    for i in range(1,len(taketh)):
        text = taketh[i-1]+','+taketh[i]
        fullstr.append(text)

    #print 'This is the full String shown as list :'
    #print fullstr
    for i in range(0,len(fullstr)):
        if(fullstr[i] in shortcutlist):
            replac = findPath(fullstr[i])
            fullstr[i] = replac
 
    fullstr = ';'.join(fullstr)
    return(fullstr)
   
go() 
start()       

    