import random

import pymysql.cursors



# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='rosekaan1',
                             port = 3306,
                             db='courses',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()
var = random.randint(0, 100)
name = "try"

sqlInsert = "insert into student_table(student_name,student_lastname,birthday_year,birthday_city) values (%s, %s, %s, %s)"
insertVal = ("eto","acar",1990,"istanbul")
cursor.execute(sqlInsert, insertVal)
connection.commit()

sql = "select * from student_table where student_name ='kaan'"
cursor.execute(sql)

#deleteSql ="delete from courses where course_id=1"
#cursor.execute(deleteSql)
#connection.commit()

myresult = cursor.fetchall()
for x in myresult:
    print(x)

connection.close()

