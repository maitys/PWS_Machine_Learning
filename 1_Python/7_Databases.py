import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE if not exists smaity_test_db2")
mycursor.execute("CREATE TABLE if not exists smaity_test_db2.smaity_test_table1 (c1 INT, c2 VARCHAR(50), c3 INT, c4 FLOAT, c5 VARCHAR(40));")
mycursor.execute("insert into smaity_test_db2.smaity_test_table1 values(233, 'sidd', 234, 34.56, 'maity')")
mycursor.execute("insert into smaity_test_db2.smaity_test_table1 values(233, 'sidd', 234, 34.56, 'maity')")
mycursor.execute("insert into smaity_test_db2.smaity_test_table1 values(233, 'sidd', 234, 34.56, 'maity')")
mycursor.execute("insert into smaity_test_db2.smaity_test_table1 values(233, 'sidd', 234, 34.56, 'maity')")
mycursor.execute("select * from smaity_test_db2.smaity_test_table1")
for i in mycursor.fetchall():
    print(i)
mydb.close()