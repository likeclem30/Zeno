import csv
import mysql.connector


connection = mysql.connector.connect(host = 'localhost', user ='root', passwd ='Mama199420')

cursor = connection.cursor()


with open("task_data.csv") as csv_file:
    reader = csv.reader(csv_file)
    i = next(reader)
    for row in reader:
        print(row)
        cursor.execute("INSERT INTO twitter.test_data (id,timestamp,temperature,duration) VALUES(%s,%s,%s,%s)",row)


connection.commit()
connection.close()
