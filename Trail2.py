import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="mysql",database="Project")
cursor=mycon.cursor()
Z="ER3404"
u="select type from Aeroplane where Plane_Id='%s'"%(Z,)
cursor.execute(u)
A_ListType=list(cursor.fetchone())
A_Type=A_ListType[0]
v="select class from Aeroplane_Cost where Plane_Id='%s'"%(Z,)
cursor.execute(v)
A_ListClass=list(cursor.fetchone())
A_Class=A_ListClass[0]
print(A_Class)
print(A_Type)
mycon.close()
