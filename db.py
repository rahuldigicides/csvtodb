import pymysql
import os
import pymongo



db_name = 'digicides'
db_user= 'kingadmin'
db_password = '12345678'
db_host = 'database-1.czaglb0mlalx.ap-south-1.rds.amazonaws.com'
db_port = str(os.getenv('DB_PORT'))

def commondbs(q1,q2):
    con = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    try:
        with con.cursor() as cur:
            cur.execute(q1,q2)   
            result = cur.fetchall()
            con.commit() 
            
    finally:
        con.close()
    return result



def blukdbs(q1,q2):
    con = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    try:
        with con.cursor() as cur:
            cur.executemany(q1,q2)   
            result = cur.fetchall()
            con.commit()
            return result 
    except pymysql.Error as e:
        print("could not close connection error pymysql %d: %s" %(e.args[0], e.args[1])) 
        return str(e)
              
    finally:
        con.close()
    


#  MongoDB
class MongoDbs():
        url = "mongodb+srv://king:king-2022@serverlessinstance0.gpdju.mongodb.net/testfarmer?retryWrites=true&w=majority"
        # url ="mongodb+srv://rahuldigicides10:8764625547@cluster0.uyb44.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(url)
        # Creating a Database for a Farmers
        db = client['farmer'] 
        # Creating a Collection     
        collection = db.farmer_csv
        collection2 =db.farmer_props
        