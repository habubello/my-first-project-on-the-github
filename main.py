import psycopg2

conn = psycopg2.connect(database='homework',
                        user='postgres',host='localhost',password='1234',port='5432')
