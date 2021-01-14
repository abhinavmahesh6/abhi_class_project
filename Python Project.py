import mysql.connector as sqltor
import random
import csv
#import Aeroplane_Seats
filename = r'c:\\workspace\\abhi_school_project\\Aeroplane_Ctr.txt'

p=[]
for i in range(65,93):
    for j in range(0,10):
        for k in range(0,10):
            for l in range(0,10):
                for m in range(0,10):
                    if j==0 and k==0 and l==0 and m==0:
                        pass
                    else:
                        s=str(chr(i))+str(j)+str(k)+str(l)+str(m)
                        p.append(s)
    
mycon=sqltor.connect(host="localhost",user="root",passwd="secret",database="Project")
cursor=mycon.cursor()
a=int(input('Enter 1 for one way and 2 for a roundtrip:'))
LA=[]
LC=[]
LI=[]
while a==1:
    b=input('Travelling From:')
    c=input('Travelling To:')
    d=input('Date of Departure(yyyy-mm-dd):')
    e=int(input('Number of Adults(12+):'))
    f=int(input('Number of Children(2-12):'))
    g=int(input('Number of Infants(Under 2):'))
    h=input('Class(Economy,Premium Economy,Business):')
    print("\n",b,c,d,e,f,g,h)
    w="select a.plane_id,a.Company,a.place_of_departure,a.Destination,ai.cost from aeroplane a,aeroplane_cost ai where a.plane_id=ai.plane_id and a.place_of_departure='%s' and a.destination='%s' and ai.class='%s'"%(b,c,h)
    cursor.execute(w)
    Y=cursor.fetchall()
    
    if Y==[]:
        print("There are no flights to the given destination from your location")
        print()
        print("Select again")
        continue
    else:
        for v in Y:
            print(v)
        a=100
        
        
    file1=open(filename,'r')
    read1=file1.read()
    read1=int(read1)
    Z=input("Enter plane_ID:")
    for i in range(0,e):
        name1=input("Enter Name:")
        age1=input("Enter Age:")
        gender1=input('Enter Gender(M/F/O):')
        passno1=input('Enter Passport Number:')
        meal1=input("Enter meal preferences:(Veg/Non-Veg):")
        print("\n",name1,age1,gender1,passno1,meal1)
        travelid1=p[read1]
        read1+=1
        list1=[name1,passno1,gender1,age1,travelid1,meal1]
        query1="insert into Cust_info values('%s','%s','%s','%s','%s','%s','%s')"%(name1,passno1,gender1,age1,travelid1,meal1,Z)
        cursor.execute(query1)
        mycon.commit()
        LA.append(list1)
    for j in range(0,f):
        name2=input("Enter Name:")
        age2=input("Enter Age:")
        gender2=input('Enter Gender(M/F/O):')
        passno2=input('Enter Passport Number:')
        meal2=input("Enter meal preferences:(Veg/Non-Veg):")
        print("\n",name2,age2,gender2,passno2,meal2)
        travelid2=p[read1]
        read1+=1
        list2=[name2,passno2,gender2,age2,travelid2,meal2]
        query2="insert into Cust_info values('%s','%s','%s','%s','%s','%s','%s')"%(name2,passno2,gender2,age2,travelid2,meal2,Z)
        cursor.execute(query2)
        mycon.commit()
        LC.append(list2)
    for k in range(0,g):
        name3=input("Enter Name:")
        age3=input("Enter Age:")
        gender3=input('Enter Gender(M/F/O):')
        passno3=input('Enter Passport Number:')
        meal3=input("Enter meal preferences:(Veg/Non-Veg):")
        print("\n",name3,age3,gender3,passno3,meal3)
        travelid3=p[read1]
        read1+=1
        query3="insert into Cust_info values('%s','%s','%s','%s','%s','%s','%s')"%(name3,passno3,gender3,age3,travelid3,meal3,Z)
        cursor.execute(query3)
        mycon.commit()
        list3=[name3,passno3,gender3,age3,travelid3,meal3]
        LA.append(list3)
        
    mobile=int(input("Enter Mobile Number:"))
    email_ID=input("Enter Email_ID:")
    print("\n",mobile,email_ID)
    file1.close()
    file1=open(filename,'w')
    read1=str(read1)
    file1.write(read1)
    file1.close()

mycon.close()
        

#need to input cost
#need to add window/aisle
#need to put payment details
#need to create bill file


