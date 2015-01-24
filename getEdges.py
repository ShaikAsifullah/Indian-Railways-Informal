'''
Created on 15-Oct-2013

@author: Kashaj
'''
import re, sqlite3,os
db = sqlite3.connect('Train_Database.db')
db.text_factory = str
db.row_factory = sqlite3.Row
db.execute('drop table if exists TrainStationNode')

db.execute('create table TrainStationNode(Train_Num char[6],stn_code char[6],route int,arr_time text,dep_time text)')

def main():
    tr_num = open('List_Of_All_Train_Nums.txt','r')
   
    for num in tr_num:
        
        num = str(num)
        num = num.replace("\xa0","");
        num = num.replace("\n","");
        num = num.strip(' ')
        num = num.strip('\n')
        
        hread(num)
        tuples = hwork()
        hdatab(num,tuples)
       
        
        
        
   
    getData()
    db.commit() 
    


def hread(filename):
    save_path = r'C:/Users/kashaj/Desktop/proj/data/schedule/'
    filename += '.html'
    completeName = os.path.join(save_path, filename)

    f = open(completeName,'r')
    text = f.read()
    text = text.strip('\n')
    f2 = open('loolws.txt','w')
    f2.write(text)
    f2.close() 
    
def hwork():    
    f = open('loolws.txt','r')
    text = f.read()
    tuples = re.findall(r'<TR>\n<TD>\d+</TD>\n<TD>(\w+\s*)</TD>\n<TD>\w+.*</TD>\n<TD>(\d)+</TD>\n<TD>(.+)</TD>\n<TD>(.+)</TD>\n<TD>.*</TD>\n<TD>\d+</TD>\n<TD>\d+</TD>',text,re.IGNORECASE)
    f.close() 
    return(tuples)
    
             
def hdatab(num,tuples):
    for i in range(0,len(tuples)):
        if(i==0):
            db.execute('insert into TrainStationNode(Train_Num,stn_code,route,arr_time,dep_time) values (?,?,?,?,?)',(num,tuples[i][0],tuples[i][1],(tuples[i][2]).replace('<FONT COLOR = red>', ''),(tuples[i][3])))
        elif(i == (len(tuples)-1)):
            db.execute('insert into TrainStationNode(Train_Num,stn_code,route,arr_time,dep_time) values (?,?,?,?,?)',(num,tuples[i][0],tuples[i][1],tuples[i][2],(tuples[i][3]).replace('<FONT COLOR = red>', '')))
        
        else:
            db.execute('insert into TrainStationNode(Train_Num,stn_code,route,arr_time,dep_time) values (?,?,?,?,?)',(num,tuples[i][0],tuples[i][1],tuples[i][2],(tuples[i][3]).replace('<FONT COLOR = red>', '')))
               

def getData():
    cursor = db.execute('Select Train_Num,stn_code,route,arr_time,dep_time from TrainStationNode')
    for row in cursor:
        print(row['Train_Num'],row['stn_code'],row['route'],row['arr_time'],row['dep_time'])
              
if __name__ == '__main__':
    main()    