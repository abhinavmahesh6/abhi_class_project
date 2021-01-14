import mysql.connector as sqltor
import random
import csv
#import Aeroplane_Seats
filename = "c:/workspace/abhi_class_project/Aeroplane_Ctr.txt"
def main():
    TravelID()
    Getinputs()
def TravelID():
    global p
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
def Getinputs():        
    mycon=sqltor.connect(host="localhost",user="root",passwd="mysql",database="Project",auth_plugin='mysql_native_password')
    cursor=mycon.cursor()
    a=int(input('Enter 1 for one way and 2 for a roundtrip:'))
    LA=[]
    LC=[]
    LI=[]
    tempvar=1
    while tempvar==1:
        _From=input('Travelling From:')#b
        _To=input('Travelling To:')#c
        _Departure=input('Date of Departure(yyyy-mm-dd):')#d
        _NoAdults=int(input('Number of Adults(12+):'))#e
        _NoChildren=int(input('Number of Children(2-12):'))#f
        _NoInfants=int(input('Number of Infants(Under 2):'))#g
        _Class=input('Class(Economy,Premium Economy,Business):')#h
        print("\n",_From,_To,_Departure,_NoAdults,_NoChildren,_NoInfants,_Class)
        
        query1="select a.plane_id,a.Company,a.place_of_departure,a.Destination,ai.cost from aeroplane a,aeroplane_cost ai where a.plane_id=ai.plane_id and a.place_of_departure='%s' and a.destination='%s' and ai.class='%s'"%(_From,_To,_Class)
        cursor.execute(query1)
        _Fetch1=cursor.fetchall()#Y
        
        if _Fetch1==[]:
            query2="select a.plane_id,a.Company,a.place_of_departure,a.Destination,ai.cost from aeroplane a,aeroplane_cost ai where a.plane_id=ai.plane_id and a.place_of_departure='%s' and a.destination='%s' and ai.class='%s'"%(_To,_From,_Class)
            cursor.execute(query2)
            _Fetch2=cursor.fetchall()
            if _Fetch2==[]:
                print("There are no flights to the given destination from your location")
                print()
                print("Select again")
                continue
            else:
                for traverse2 in _Fetch2:
                    print(traverse2)
                tempvar=100
        else:
            for traverse1 in _Fetch1:
                print(traverse1)
            tempvar=100
            
            
        file1=open(filename,'r')
        read1=file1.read()
        read1=int(read1)
        Z=input("Enter plane_ID:")
        for i in range(0,_NoAdults):
            name1=input("Enter Name:")
            age1=input("Enter Age:")
            gender1=input('Enter Gender(M/F/O):')
            passno1=input('Enter Passport Number:')
            meal1=input("Enter meal preferences:(Veg/Non-Veg):")
            print("\n",name1,age1,gender1,passno1,meal1)
            travelid1=p[read1]
            read1+=1
            list1=[name1,passno1,gender1,age1,travelid1,meal1]
            query3="insert into Cust_info values('%s','%s','%s','%s','%s','%s','%s')"%(name1,passno1,gender1,age1,travelid1,meal1,Z)
            cursor.execute(query3)
            mycon.commit()
            LA.append(list1)
        for j in range(0,_NoChildren):
            name2=input("Enter Name:")
            age2=input("Enter Age:")
            gender2=input('Enter Gender(M/F/O):')
            passno2=input('Enter Passport Number:')
            meal2=input("Enter meal preferences:(Veg/Non-Veg):")
            print("\n",name2,age2,gender2,passno2,meal2)
            travelid2=p[read1]
            read1+=1
            list2=[name2,passno2,gender2,age2,travelid2,meal2]
            query4="insert into Cust_info values('%s','%s','%s','%s','%s','%s','%s')"%(name2,passno2,gender2,age2,travelid2,meal2,Z)
            cursor.execute(query4)
            mycon.commit()
            LC.append(list2)
        for k in range(0,_NoInfants):
            name3=input("Enter Name:")
            age3=input("Enter Age:")
            gender3=input('Enter Gender(M/F/O):')
            passno3=input('Enter Passport Number:')
            meal3=input("Enter meal preferences:(Veg/Non-Veg):")
            print("\n",name3,age3,gender3,passno3,meal3)
            travelid3=p[read1]
            read1+=1
            query5="insert into Cust_info values('%s','%s','%s','%s','%s','%s','%s')"%(name3,passno3,gender3,age3,travelid3,meal3,Z)
            cursor.execute(query5)
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
if __name__ == "__main__":
    main()
    

#need to input cost
#need to add window/aisle
#need to put payment details
#need to create bill file


