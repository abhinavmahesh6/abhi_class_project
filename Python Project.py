import mysql.connector as sqltor
import random
import csv
import datetime
#import Aeroplane_Seats
filename = "c:/workspace/abhi_class_project/Aeroplane_Ctr.txt"
def main():
    TravelID()
    Getinputs()
def TravelID():
    global TravelList#p
    TravelList=[]
    for i in range(65,93):
        for j in range(0,10):
            for k in range(0,10):
                for l in range(0,10):
                    for m in range(0,10):
                        if j==0 and k==0 and l==0 and m==0:
                            pass
                        else:
                            s=str(chr(i))+str(j)+str(k)+str(l)+str(m)
                            TravelList.append(s)
def Getinputs():        
    mycon=sqltor.connect(host="localhost",user="root",passwd="mysql",database="Project",auth_plugin="mysql_native_password")
    cursor=mycon.cursor()
    oneround=input("Enter 1 for one-way and 2 for round trip: ")
    LA=[]
    LC=[]
    LI=[]
    emplist1=[]
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
        query1="select a.plane_id,a.Company,a.place_of_departure,a.Destination,ac.cost,time(a.Time_of_Dep) from aeroplane a,aeroplane_cost ac where a.plane_id=ac.plane_id and a.place_of_departure='%s' and a.destination='%s' and ac.class='%s'"%(_From,_To,_Class)
        cursor.execute(query1)
        _Fetch1=cursor.fetchall()#Y
        def displayplanes():
            print("These are the flights available:")
            print()
            for traverse1 in _Fetch1:
                for traverse3 in traverse1:
                    print(traverse3,end=' ')
                print()    
                    
        if _Fetch1==[]:
            query2="select a.plane_id,a.Company,a.place_of_departure,a.Destination,ac.cost,time(a.Time_of_Dep) from aeroplane a,aeroplane_cost ac where a.plane_id=ac.plane_id and a.place_of_departure='%s' and a.destination='%s' and ac.class='%s'"%(_To,_From,_Class)
            cursor.execute(query2)
            _Fetch1=cursor.fetchall()
            
            if _Fetch1==[]:
                print("There are no flights to the given destination from your location")
                print()
                print("Select again")
                continue
            else:
                displayplanes()
                    
        else:
            displayplanes()
                
        
        
        InpPlane_ID=input("Enter plane_ID from above: ")#Z
        for traverse2 in _Fetch1:
            if InpPlane_ID in traverse2:
                time_of_dep = str(traverse2[-1]) 
                #_duration = str(traverse[-1])
                print(time_of_dep)
                
                
         
                        
            
            
                
                
            
        fileread=open(filename,'r')
        travelidvar=fileread.read()#read1
        travelidvar=int(travelidvar)
        
        
        
        for inp1 in range(0,_NoAdults):
            name1=input("Enter Name:")
            age1=input("Enter Age:")
            gender1=input('Enter Gender(M/F/O):')
            passno1=input('Enter Passport Number:')
            meal1=input("Enter meal preferences:(Veg/Non-Veg):")
            print("\n",name1,age1,gender1,passno1,meal1)
            travelid1=TravelList[travelidvar]
            travelidvar+=1
            list1=[name1,passno1,gender1,age1,travelid1,meal1]
            query3="insert into Cust_info(Name,Passport_No,Gender,Age,Travel_ID,meal_pref,Plane_ID,Date_of_Dep,Time_of_Dep) values('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(name1,passno1,gender1,age1,travelid1,meal1,InpPlane_ID,_Departure+' 00:00:00',time_of_dep)
            cursor.execute(query3)
            mycon.commit()
            LA.append(list1)
        for inp2 in range(0,_NoChildren):
            name2=input("Enter Name:")
            age2=input("Enter Age:")
            gender2=input('Enter Gender(M/F/O):')
            passno2=input('Enter Passport Number:')
            meal2=input("Enter meal preferences:(Veg/Non-Veg):")
            print("\n",name2,age2,gender2,passno2,meal2)
            travelid2=TravelList[travelidvar]
            travelidvar+=1
            list2=[name2,passno2,gender2,age2,travelid2,meal2]
            query4="insert into Cust_info(Name,Passport_No,Gender,Age,Travel_ID,meal_pref,Plane_ID,Date_of_Dep,Time_of_Dep) values('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(name2,passno2,gender2,age2,travelid2,meal2,InpPlane_ID,_Departure+' 00:00:00',time_of_dep)
            cursor.execute(query4)
            mycon.commit()
            LC.append(list2)
        for inp3 in range(0,_NoInfants):
            name3=input("Enter Name:")
            age3=input("Enter Age:")
            gender3=input('Enter Gender(M/F/O):')
            passno3=input('Enter Passport Number:')
            meal3=input("Enter meal preferences:(Veg/Non-Veg):")
            print("\n",name3,age3,gender3,passno3,meal3)
            travelid3=TravelList[travelidvar]
            travelidvar+=1
            query5="insert into Cust_info(Name,Passport_No,Gender,Age,Travel_ID,meal_pref,Plane_ID,Date_of_Dep,Time_of_Dep) values('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(name3,passno3,gender3,age3,travelid3,meal3,InpPlane_ID,_Departure+' 00:00:00',time_of_dep)
            cursor.execute(query5)
            mycon.commit()
            list3=[name3,passno3,gender3,age3,travelid3,meal3]
            LI.append(list3)
            
        mobile=int(input("Enter Mobile Number:"))
        email_ID=input("Enter Email_ID:")
        print("\n",mobile,email_ID)
        fileread.close()
        filewrite=open(filename,'w')
        travelidvar=str(travelidvar)
        filewrite.write(travelidvar)
        filewrite.close()
        break
    mycon.close()

    
    
    
    
if __name__ == "__main__":
    main()
    
#need to add time of departure and duration to aeroplane table
#need to input cost
#need to add window/aisle
#need to put payment details
#need to create bill file



