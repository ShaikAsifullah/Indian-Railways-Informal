'''
Created on 08-Oct-2013

@author: Kashaj
'''

"""This fetched the train RunDays info and insert into the database"""

import re, sqlite3, os
db = sqlite3.connect('Train_Database.db')
db.text_factory = str
db.row_factory = sqlite3.Row
db.execute('drop table if exists TrainDaysInfo')
db.execute('create table TrainDaysInfo(Train_Num char[5],Week_Days char[30])')

def main():
    tr_num = open('List_Of_All_Train_Nums.txt','r')
    count=0
    for num in tr_num:
        
        num = str(num)
        num=num.replace("\xa0","");
        num=num.replace("\n","");
        num = num.strip(' ')
        num = num.strip('\n')
        
        Days = hwork(num)
        hdatab(num,Days)
        count += 1
        
    
    getData()
    db.commit() 
    
def hwork(filename):    
    save_path = r'C:/Users/kashaj/Desktop/proj/data/schedule/'
    filename += '.html'
    completeName = os.path.join(save_path, filename)
    f = open(completeName,'r')
    text = f.read()
    Days = ''
    tuples = re.findall(r'<TD>(\w\w\w\s)</TD>\n<TD>(\w\w\w\s)</TD>',text)
    #print(len(tuples))
    for item in tuples:
        for items in item:
            Days += items
    Days = Days.strip(' ')
              
    tuples1 = re.findall(r'<TD>(\w\w\w)\s</TD></TR>\n</TABLE>',text)
    if(len(tuples1)): match = re.search(tuples1[0],Days)
    else: 
        #print Days
        return Days
    
    if match: tuples
    else: 
        Days += (' ' +tuples1[0])  
        #print(len(Days))  
    #print Days
    return(Days)
    f.close() 
             
def hdatab(num,Days):
    db.execute('insert into TrainDaysInfo(Train_Num,Week_Days) values (?,?)',(num,Days))
    

def getData():
    cursor = db.execute('Select Train_Num, Week_Days from TrainDaysInfo')
    f = open("TrainsDays.txt",'a')
    count = 0;
    for row in cursor:
        text = str(row['Train_Num'])
        text += ','
        text += str(row['Week_Days'])
        text += '\n'
        f.write(text)
        count -= 1
    print count 
    f.close()
              
if __name__ == '__main__':
    main()    
            
