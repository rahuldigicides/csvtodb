from db import *
from sechmas import *
from tokens import AuthHandler
from fastapi import Depends, APIRouter, HTTPException, status
from datetime import datetime, timedelta

from fastapi import UploadFile , File
from fastapi.responses import FileResponse
import pandas as pd
from collections import Counter

import csv







handlecsv = APIRouter()
auth_handler = AuthHandler()


@handlecsv.get("/handlecsv/hello")
async def get_hello():
    return {"message": "Hello from handle csv"}


filename="rahul"
# fieldname1= ["id","email","password","role","reporting","status","company_id","blocked","deleted","phone","name","created_at","updated_at","company"]

# Write the CSV File
def writeCsvFile(rows,fieldname1):
    with open(filename , 'w' , encoding='UTF8', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldname1, delimiter=',',)
        # ! Header and Rows of Csv Data 
        writer.writeheader() 
        writer.writerows(rows)


@handlecsv.get("/download")
def downloadCsvFile():
    q1='select * from users'
    q2=() 
    result=commondbs(q1, q2)
    fieldname=result[0].keys()
    # print(list(heads))
    writeCsvFile(result, list(fieldname))
    return  FileResponse(path=filename, media_type='application/octet-stream', filename="csvFile")



@handlecsv.post("/uploadfilemonogdb")
async def uploadCsvMongoDb(csv_file : UploadFile =File(...)) :
  # mongodbs = MongoDbs() 
  mongoDb=MongoDbs() 
  
  try:
    df = pd.read_csv(csv_file.file) 
    print(len(df.index))
    lName= df.columns.values
    
    pList=list(df[f'{lName[1]}'].values)
    # pList=list(df.iloc[:, 1].values)
    # for i in range(1, len(pList)) :
    #   if len(str(pList[i])) !=10:
    #     return {"msg":f"{i+1} Row is Not Valid"}
    
    # print(df)
    dup=df.duplicated(subset=[f"{lName[1]}"] ,keep='last').sum()
    
    df.drop_duplicates(subset =f"{lName[1]}",keep='last',inplace = True)
    # df.fillna('', inplace = True)
   # ! end method 
    dictData= df.to_dict('records')
    sucssRow=None
    try:
      farmers = mongoDb.collection.insert_many(dictData)
      # print(len(farmers.inserted_ids) )
      sucssRow = str(len(farmers.inserted_ids))
      pass
    except :
           return {"Error": "File Have Error"}
    return {"Insert Row": f"{sucssRow} " , "Duplicate": f"{dup}" }
    
    
  except pd.errors.ParserError as e:
    print(e) 
    return {"msg" :"Row  have Exrta Field"}
    # raise e 



def csvtodb(df):
 
  try: 
      # q1='INSERT INTO farmers  VALUES(%s, %s, %s, %s, %s, %s, %s)'
      q1='INSERT INTO farmers (id,name,phone,state,created_at,updated_at,district) VALUES(%s, %s, %s, %s, %s, %s, %s)'
      res=blukdbs(q1, df) 
      return f"{len(df)}"
  except:
   
      return "Error:Data not Store"






  
  

# # ! CSV FILE UPLOAD WITH MYSQL
@handlecsv.post("/mysql")
async def uploadMySql(csv_file : UploadFile =File(...)) :
  try:
    df = pd.read_csv(csv_file.file) 
    # print(df)
    lName= df.columns.values
    
    pList=list(df[f'{lName[1]}'].values)
    df.fillna('', inplace = True)
    # pList=list(df.iloc[:, 1].values)
    # for i in range(1, len(pList)) :
    #   if len(str(pList[i])) !=10:
    #     return {"msg":f"{i} Row is Not Valid"}
    
     
    dup=df.duplicated(subset=[f"{lName[1]}"] ,keep='last').sum()
    df.drop_duplicates(subset =f"{lName[1]}",keep='last',inplace = True)
   
    tpls = [tuple(x) for x in df.to_numpy()]
  
    # tpls=list(df.itertuples(index=False, name=None))
      # print(tpls)
    pList=[]
    for i in tpls:
      # print(i)
      userid = '' 
      state=''
      district=''
      updated_at=''  
      created_at=''
      fname=i[0] 
      phone=i[1]
      pList.append([userid, fname,phone,state,created_at,updated_at,district])
      
    
    result= csvtodb(pList)
    return {"Insert Row": f"{result}" , "Duplicate": f"{dup}" }
  
  except pd.errors.ParserError as e:
   
    # print(e) 
    return {"msg" :"Row  have Exrta Field"}
    # raise e 





# ! Farmers 

def csvtodbss(df):
  # print(df)
  try: 
      
      q1='INSERT INTO farmer_raw (name,phone)  VALUES(%s,%s)'
      res=blukdbs(q1, df) 
    
      # print("result dataa  a" , res)
      return f"{len(df)}"
  except :
      # print(e) 
      return "Error:Data not Store"
  

@handlecsv.post("/csvwithmysqldb")
async def uploadMySqlFile(csv_file : UploadFile =File(...)) :
  try:
    df = pd.read_csv(csv_file.file) 
    # print(df)
    lName= df.columns.values
    
    pList=list(df[f'{lName[1]}'].values)
    df.fillna('', inplace = True)
    # pList=list(df.iloc[:, 1].values)

    # for i in range(1, len(pList)) :
    #   if len(str(pList[i])) !=10:
    #     return {"msg":f"{i+2} Row is Not Valid"}
    
     
    dup=df.duplicated(subset=[f"{lName[1]}"] ,keep='last').sum()
    df.drop_duplicates(subset =f"{lName[1]}",keep='last',inplace = True)
   
    tpls = [tuple(x) for x in df.to_numpy()]
  
    # tpls=list(df.itertuples(index=False, name=None))
      # print(tpls)
    ids=0
    pList=[]
    for i in tpls:
      fname=i[0] 
      phone=i[1]
      pList.append([fname,phone])
      
    
    result= csvtodbss(pList)

    return {"Insert Row": f"{result}" , "Duplicate": f"{dup}" }
  
  except pd.errors.ParserError as e:
    # return {"Insert Row": "row " , "Duplicate": f"{dup}" }
    # print(e) 
    return {"msg" :"Row  have Exrta Field"}


































# def csvtodatabse(df):
#   for i , row in df.iterrows():
    
#       # if len(str(row.phone)) !=10:
#       #   return {"msg":f"{i+1} Phone Number Not Valid"}
#       userid = None if pd.isna(row.id) ==True  else row.id 
#       names=None if pd.isna(row.names) ==True  else row.names
#       phone=None if pd.isna(row.phone) ==True  else row.phone
#       state=None if pd.isna(row.state) ==True  else row.state 
#       district=None if pd.isna(row.district) ==True  else row.district
#       updated_at=None if pd.isna(row.updated_at) ==True else row.updated_at 
#       created_at=None if pd.isna(row.created_at) ==True else row.created_at
      
      
#       q1='INSERT INTO farmers VALUES(%s, %s, %s, %s, %s, %s, %s)'
#       q2=(userid,names,phone,state,created_at,updated_at,district)
     
#       # commondbs(q1, q2) 
#       print(f"{i} row insert" )
#   return {"msg":f"{i+1} row insert"}


# # ! CSV FILE UPLOAD WITH MONGODB AND MYSQL
# @handlecsv.post("/uploadcsvmongowithsql")
# async def uploadCsvMongowithSql(csv_file : UploadFile =File(...)) :
#   # mongoDb=mongoDbs() 
  
#   try:
#     df = pd.read_csv(csv_file.file) 
    
#     # if len(df.index) >1000:
#     #   return {"status":"1", "msg":"File data too Large" }
#     # print(df['phone'].astype(str).str.len())
#     # print(df[df.columns[0]].count())
#     # print(df.loc[df.phone !=10].index)
#     # print(df.index[df.phone != 10])
   
#     if len(str(df['phone'].astype(str).str.len())) != str(10):
       
#       return {"msg": f"{len(df[df['phone'] != 10])} Row is not Valid"}
      

#     df.drop_duplicates(inplace = True)
#     df.fillna('', inplace = True)

#     df.rename(columns = {'name':'names','phone':'phone'}, inplace = True)
#     dbtable=['id', 'names' ,'phone' ,'state', 'created_at', 'updated_at', 'district']
    
#     if set(dbtable) == set(df.columns.to_list()):
     
#       result=csvtodatabse(df)
#       return result

#     else:
      
#       result=csvtodatabse(df)
#       field= set(df.columns.to_list()).difference(set(dbtable))
#       extField= list(field)
#       fList=['id','created_at', 'updated_at' ]
#       fList.extend(extField)
#       df2= df[fList].copy()
#       # dictData= df2.to_dict('record')
#       dictData=df2.to_dict('records')
      
    
#       # for i in list(dictData):
#       #   # farmers = mongoDb.collection2.insert_one(i).inserted_id
#       #   print(farmers)
#       # return {"msg":"Data Successfully Fill"}
#       return result
    
    
#   except pd.errors.ParserError as e:
#     print(e) 
#     return {"msg" :"Row  have Exrta Field"}
#     # raise e 




