'''
Created on 06-Oct-2013

@author: Kashaj
'''
"""This fetches the entire TrainDetails extracted on 8 october 2013"""


import httplib, urllib, re, sqlite3, os
db = sqlite3.connect('Train_Database.db')
db.text_factory = str
db.row_factory = sqlite3.Row
#db.execute('drop table if exists Train_Schedule')
#db.execute('create table Train_Schedule(Train char[6] PRIMARY KEY, StnCode text,  RouteNo text, ArrTime text, DeptTime text, HaltTime text, Distance text, Day text)')

def main():
    
    tr_num = open('List_Of_All_Train_Nums.txt','r')
    for num in tr_num:
        num = str(num)
        num=num.replace("\xa0","");
        num=num.replace("\n","");

        Matter = hwrite(num)
        Matter = Matter.strip('\n')
        hread(Matter)
        tuples = hwork()
        hdatab(tuples,num)

    showDatabase()
        
    




def hwrite(trainnum):
    
    params = urllib.urlencode({'lccp_trnname': trainnum, 'getIt': 'Please+Wait...'})
    headers = {"Host": "www.indianrail.gov.in", "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Referer": "http://www.indianrail.gov.in/train_Schedule.html", "Connection": "keep-alive", "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "39"}
    conn = httplib.HTTPConnection("www.indianrail.gov.in:80")
    conn.request("POST", "/cgi_bin/inet_trnnum_cgi.cgi", params, headers)
    response = conn.getresponse()
    print response.status, response.reason
    data = response.read()
    
    save_path = r'C:/Users/kashaj/Desktop/proj/data/schedule/'
    text = trainnum
    text += '.html'
    completeName = os.path.join(save_path, text)
    f = open(completeName,'w')
    f.write(data)
    f.close
    conn.close()  
          
    return data

def hread(htmltext):
    f2 = open('loolw.txt','w')
    f2.write(htmltext)
    f2.close()
    


def hwork():    
    f = open('loolw.txt','r')
    text = f.read()
    tuples = re.findall(r'<TR>\n<TD>(\d+)</TD>\n<TD>(\w+\s*)</TD>\n<TD>(\w+.*)</TD>\n<TD>(\d+)</TD>\n<TD>(.+)</TD>\n<TD>(.+)</TD>\n<TD>(.*)</TD>\n<TD>(\d+)</TD>\n<TD>(\d+)</TD>',text,re.IGNORECASE)
    #print tuples
    f.close()
    return tuples    


def hdatab(tuples,table):
    
    
    
    #print type(test)
    #db.execute('drop table if exists test')
    #db.execute('drop table if exists test2')
    train_num = table;
    stn_code = ''
    route_no = ''
    arr_time = ''
    dep_time = ''
    halt_time = ''
    dist = ''
    day = ''
    #db.execute('create table test (Serial int, StnCode text, StnName text, RouteNo text, ArrTime text, DeptTime text, HaltTime text, Distance text, Day text)')
    for i in range(0,len(tuples)):
        #if (i == 0):
            #db.execute('insert into test(Serial, StnCode, StnName, RouteNo, ArrTime, DeptTime, HaltTime, Distance, Day) values (?, ?, ?, ?, ?, ?, ?, ?, ?)',(int(tuples[i][0]),str(tuples[i][1]).strip(),str(tuples[i][2]).strip(),int(tuples[i][3]),str(tuples[i][4]).replace('<FONT COLOR = red>', ''),str(tuples[i][5]),str(tuples[i][6]),int(tuples[i][7]),int(tuples[i][8])))
        if(i == (len(tuples)-1)):
            stn_code += str(tuples[i][1]).strip()
            route_no += str(tuples[i][3])
            arr_time += str(tuples[i][4]).strip()
            dep_time += str(tuples[i][5]).replace('<FONT COLOR = red>', '')
            halt_time += str(tuples[i][6]).strip()
            dist += str(tuples[i][7]).strip()
            day += str(tuples[i][8]).strip()

            db.execute('insert into Train_Schedule(Train, StnCode,  RouteNo, ArrTime, DeptTime, HaltTime, Distance, Day) values (?, ?, ?, ?, ?, ?, ?, ? )',(train_num,stn_code,route_no,arr_time,dep_time,halt_time,dist,day))    
        else:
            
            stn_code += str(tuples[i][1]).strip()
            stn_code += ';'
            route_no += str(tuples[i][3])
            route_no += ';'
            arr_time += str(tuples[i][4]).replace('<FONT COLOR = red>', '')
            arr_time += ';'
            dep_time += str(tuples[i][5]).strip()
            dep_time += ';'
            halt_time += str(tuples[i][6]).strip()
            halt_time += ';'
            dist += str(tuples[i][7]).strip()
            dist += ';'
            day += str(tuples[i][8]).strip()
            day += ';'
            
            #db.execute('insert into test(Serial, StnCode, StnName, RouteNo, ArrTime, DeptTime, HaltTime, Distance, Day) values (?, ?, ?, ?, ?, ?, ?, ?, ?)',(int(tuples[i][0]),str(tuples[i][1]).strip(),str(tuples[i][2]).strip(),int(tuples[i][3]),str(tuples[i][4]),str(tuples[i][5]),str(tuples[i][6]),int(tuples[i][7]),int(tuples[i][8]))) 
                                                                                                                                                                                                                                     
     
def showDatabase():    
    cursor = db.execute('Select Train, StnCode,  RouteNo, ArrTime, DeptTime, HaltTime, Distance, Day from Train_Schedule')
    for row in cursor:
        print(row['Train'],row['StnCode'],row['RouteNo'],row['ArrTime'],row['DeptTime'],row['HaltTime'],row['Distance'],row['Day'])
        
    
    db.commit()   
    
if __name__ == '__main__':
    main()    