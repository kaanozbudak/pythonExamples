# Connect to the database
import random

import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='rosekaan1',
                             port=3306,
                             db='bank_database',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

sqlSelectBank = "select * from bank"
# cursor.execute(sqlSelectBank)


def rand_number():
    rand_number = random.randint(0, 4)
    return rand_number
def rand_bank():
    list = ['isbank','ziraat','garanti','teb','halk']
    bank = list[rand_number()]
    return bank# Connect to the database
import random

import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='rosekaan1',
                             port=3306,
                             db='bank_database',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

sqlSelectBank = "select * from bank"
cursor.execute(sqlSelectBank)

print(cursor.fetchall())

def rand_number():
    rand_number = random.randint(0, 4)
    return rand_number
def rand_bank():
    list = ['isbank','ziraat','garanti','teb','halk']
    bank = list[rand_number()]
    return bank
#sqlInsertBank = "insert into bank values(null,'%s')" % rand_bank()
#cursor.execute(sqlInsertBank)

connection.commit()
connection.close()



#sqlInsertBank = "insert into bank values(null,'%s')" % rand_bank()
#cursor.execute(sqlInsertBank)
#connection.commit()
#connection.close()


