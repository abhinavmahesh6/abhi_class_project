import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="mysql",database="Project")
cursor=mycon.cursor()
u="select Type from Aeroplane where Plane_Id='%s'"%('AA5545',)
cursor.execute(u)
A_TupleType=list(cursor.fetchone())
for i1 in A_TupleType:
    A_Type=i1
print(A_Type)
