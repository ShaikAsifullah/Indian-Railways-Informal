'''
Created on 13-Oct-2013

@author: Kashaj
'''
import sqlite3
db = sqlite3.connect('Train_Database.db')
db.text_factory = str
db.row_factory = sqlite3.Row
db.execute('drop table if exists StationCodesAndNames')
db.execute('create table StationCodesAndNames(StnCode text PRIMARY KEY,StnName text)')

def openfile(filename):
    f = open(filename,'r')
    for lines in f:
        lines = str(lines)
        lines=lines.replace("\xa0","");
        lines=lines.replace("\n","");
        lines = lines.strip(' ')
        lines = lines.strip('\n')
        lines = lines.split(',')
        datawrite(lines)
    
    showdatabase()    
    db.commit()
    
        
def datawrite(data):
    db.execute('insert into StationCodesAndNames(StnCode,StnName) values (?,?)',(data[1],data[0]))        
     
def showdatabase():
    cursor = db.execute('Select StnCode,StnName from StationCodesAndNames')        
    for row in cursor:
        print(row['StnName'],row['StnCode'])
        



if __name__ == '__main__':
    openfile('StationNamesAndCodes.txt')