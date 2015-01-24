'''
Created on 06-Nov-2013

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
    


def getDetailPath(stationstr):
    stationstr = stationstr.strip('\n')
    if stationstr in shortcutlist:
        edgestr = findPath(stationstr)
        return(edgestr)
    if stationstr not in shortcutlist:
        return(stationstr)    
        
    

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

def startin():
    f4 = open('gare.txt','a')
    f9 = open('gotErrorsagain.txt','a')
    f5 = open('Gotcha.txt','r')
    textThis = ''
    writeThis = ''
    count = 0;
    for lines in f5:
        lines = lines.strip('\n')
        if(lines == textThis):
            f4.write(writeThis)
            
        if(lines != textThis):
            try:
                textThis = lines
                if (len(lines)> 2):
                    thisThing = getDetailPath(lines)
                    
                    text = lines+'----->'+thisThing+'\n'
                    writeThis = text
                    f4.write(text)
                    print count
                    count += 1
            except Exception, e:
               
                lines = lines + '--->This got an exception\n'
                f9.write(lines)
                textThis = ''
                print count
                count += 1
            
            
            
    f4.close()
    f5.close()
    f9.close()
        
startin()