# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 15:22:18 2018

@author: Administrator

@use:3618网站搜索引擎爬虫日志入库
"""
import pymysql
import hashlib
import os 

#唯一性
def md5(str):
    m2=hashlib.md5()
    m2.update(str.encode("utf-8"))
    return(m2.hexdigest())


def readOneLogFile_M(filename):
    cn=pymysql.Connection(host="localhost",user="root",password="root",database="3618med",charset="utf8")
    cursor = cn.cursor()
    for line in open(filename):
        #print(line)
        list_str=line.split(" ")
        md5str=md5(line)
        if len(list_str) > 13:
            useragent=" ".join(list_str[12:len(list_str) -1])
            useragent=useragent.replace("\"","").strip()
            if useragent.lower().find("spider") < 0:
                continue
            ip=list_str[0].strip()
            day_str=list_str[3]
            day_list_str=day_str.split(":")
            day=day_list_str[0].replace("[","")
            time=day_list_str[1]+":"+day_list_str[2]+":"+day_list_str[3]
            time=time.strip()
            domain=list_str[5].strip()
            method=list_str[6].replace("\"","").strip()
            uri=list_str[7].strip()
            http=list_str[8].replace("\"","").strip()
            status=list_str[9].strip()
            datasize=list_str[10].strip()
            referer=list_str[11].replace("\"","").strip()
            cdnip=list_str[len(list_str) - 1]
            cdnip=cdnip.replace('"','').strip()
            
            
            #print("ip:" + ip)
            #print("day:" + day)
            #print("time:" + time)
            #print("domain:" + domain)
            #print("method:" + method)
            print("uri:" + uri)
            #print("http:" + http)
            #print("status:" + status)
            #print("datasize:" + datasize)
            #print("referer:" + referer)
            #print("cdnip:" + cdnip)
            #print("useragent:" + useragent)

            
            sql = "SELECT count(*) FROM logtable  WHERE md5str='"+md5str+"'"
            count=0
            try:
              cursor.execute(sql)
              results = cursor.fetchall()
              count=results[0][0]
            except:
               print("Error: select data error! sql:" +sql );
               
            if count < 1:
                  sql = "INSERT INTO logtable(ip, \
                          day,time, domain, method,uri,http,status,datasize,referer,cdnip,useragent,md5str) \
                          VALUES ('%s','%s','%s','%s','%s','%s','%s','%d','%d','%s','%s','%s','%s')" % \
                            (ip,day,time,domain,method,uri,http,int(status),int(datasize),referer,cdnip,useragent,md5str)    
        
            try:
              cursor.execute(sql)
              
            except:
               print("Error: insert into data error! sql:" +sql );
    cn.commit()           
    cn.close()
    
#读取PC端格式日志    
def readOneLogFile_PC(filename):
    cn=pymysql.Connection(host="localhost",user="root",password="root",database="3618med",charset="utf8")
    cursor = cn.cursor()
    for line in open(filename):
        #print(line)
        list_str=line.split(" ")
        md5str=md5(line)
        if len(list_str) > 13:
            useragent=" ".join(list_str[12:len(list_str) -1])
            useragent=useragent.replace("\"","").strip()
            if useragent.lower().find("spider") < 0:
                continue
            ip=list_str[0].strip()
            day_str=list_str[3]
            day_list_str=day_str.split(":")
            day=day_list_str[0].replace("[","")
            time=day_list_str[1]+":"+day_list_str[2]+":"+day_list_str[3]
            time=time.strip()
            domain=""
            method=list_str[5].replace("\"","").strip()
            uri=list_str[6].strip()
            http=list_str[7].replace("\"","").strip()
            status=list_str[8].strip()
            datasize=list_str[9].strip()
            referer=list_str[10].replace("\"","").strip()
            cdnip=list_str[len(list_str) - 1]
            cdnip=cdnip.replace('"','').strip()
            
            
            #print("ip:" + ip)
            #print("day:" + day)
            #print("time:" + time)
            #print("domain:" + domain)
            #print("method:" + method)
            print("uri:" + uri)
            #print("http:" + http)
            #print("status:" + status)
            #print("datasize:" + datasize)
            #print("referer:" + referer)
            #print("cdnip:" + cdnip)
            #print("useragent:" + useragent)
            #break
            
            sql = "SELECT count(*) FROM logtable  WHERE md5str='"+md5str+"'"
            count=0
            try:
              cursor.execute(sql)
              results = cursor.fetchall()
              count=results[0][0]
            except:
               print("Error: select data error! sql:" +sql );
               
            if count < 1:
                  sql = "INSERT INTO logtable(ip, \
                          day,time, domain, method,uri,http,status,datasize,referer,cdnip,useragent,md5str) \
                          VALUES ('%s','%s','%s','%s','%s','%s','%s','%d','%d','%s','%s','%s','%s')" % \
                            (ip,day,time,domain,method,uri,http,int(status),int(datasize),referer,cdnip,useragent,md5str)    
        
            try:
              cursor.execute(sql)
              
            except:
               print("Error: insert into data error! sql:" +sql );
    cn.commit()           
    cn.close()    

   
rootdir = 'e:\weblog'
list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
for i in range(0,len(list)):
    path = os.path.join(rootdir,list[i])
    if os.path.isfile(path):
        #你想对文件的操作
        print("开始读取:" + path)
        #readOneLogFile_PC(path)
        readOneLogFile_M(path)
        #break