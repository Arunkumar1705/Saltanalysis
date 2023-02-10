import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234"
)

mycursor = mydb.cursor()

def initial():
    global mycursor,mydb

    mycursor.execute("CREATE DATABASE if not exists saltanalysis")
    mycursor.execute("Use saltanalysis")
    mycursor.execute("CREATE TABLE if not exists users (name VARCHAR(255) UNIQUE, password VARCHAR(255))")
def insertvalues(name : str,password: str):
    global mycursor,mydb
    try:
        initial()
        #This is not safe as we are having plaintext passswords..but this is faster
        sql = "INSERT INTO users (name, password) VALUES (%s, %s)"
        val = (name, password)
        mycursor.execute(sql, val)
        mydb.commit()
    except:
        pass

def getuserids():
    global mycursor,mydb

    initial()
    mycursor.execute("SELECT * FROM users")
    myresult = mycursor.fetchall()
    return myresult

def deleteuserids(who:str):
    global mycursor,mydb
    
    initial()
    sql = f"DELETE FROM users WHERE name = '{who}'"
    mycursor.execute(sql)
    mydb.commit()
    
        