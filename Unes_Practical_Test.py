
import mysql.connector

mydb=mysql.connector.connect(
host="localhost",
username="root",
password="karimi1234",
database="Products"
)

cur=mydb.cursor()
try:
    #cur.execute("create database Products")
    dbs=cur.execute("show databases")
    dbs=cur.execute("create table OrganizationProducts(Products varchar(20) not null, beginning balance varchar(20), quantity dispensed varchar(20), closing balance varchar (20)")
except:
    mydb.rollback()
for x in cur:
    print(x)
mydb.close()






