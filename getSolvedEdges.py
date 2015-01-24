'''
Created on 15-Oct-2013

@author: Kashaj
'''
import sqlite3
db = sqlite3.connect('Train_Database.db')
db.text_factory = str
db.row_factory = sqlite3.Row

def main():
    f1 = open('Edges.txt','w')
    info = getData();
    f1.write(info)
    
    db.commit();
    print 'Done'
    f1.close();

def getData():
    cursor = db.execute('Select Train_Num,stn_code,route,arr_time,dep_time from TrainStationNode')
    i = 0;
    text = ''  
    

    for row1 in cursor:
        if(i == 0):
           
            trainnum1 = str(row1['Train_Num'])
            stnname1 =  str(row1['stn_code']).strip(' ')
            route1 = str(row1['route']).strip(' ')
            i += 1
            continue
        
        
        
        else:
            i += 1; 
            if(trainnum1 == str(row1['Train_Num']) and route1 == str(row1['route']).strip(' ')):
                text += stnname1 + ',' + str(row1['stn_code']).strip(' ') + '\n'
            
            stnname1 = str(row1['stn_code']).strip(' ');
            trainnum1 = str(row1['Train_Num']);
            route1 = str(row1['route']).strip(' ')
            
    print text 
           
    return text;    
    
if __name__ == '__main__':
    main()    