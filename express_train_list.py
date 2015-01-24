'''
Created on 06-Oct-2013

@author: Kashaj
'''
"""Date extracted : 06/10/2013
This stores all the Train Numbers and their names and their related info"""

import sqlite3
db = sqlite3.connect('Train_Database.db')
db.text_factory = str;
db.row_factory = sqlite3.Row
db.execute('drop table  if exists Trainlist');
db.execute('create table Trainlist(Train_Num char[6] PRIMARY KEY, Train_Name text, Source text, Source_Dep_Time text, Dest text, Dest_Arr_Time text)')
def openfile():
    f = open('Train_Info.txt','r')
    for lines in f:
        lines = lines.split(',')
        db.execute('insert into Trainlist(Train_Num,Train_Name,Source,Source_Dep_Time,Dest,Dest_Arr_Time) values (?,?,?,?,?,?)',(lines))
        
        
    cursor = db.execute('Select Train_Num,Train_Name,Source,Source_Dep_Time,Dest,Dest_Arr_Time from Trainlist')
       
    for row in cursor:
        print row['Train_Num'],row['Train_Name']
       
           
    db.commit()
    f.close()
            
if __name__ == '__main__':
    openfile()            
            
    
    