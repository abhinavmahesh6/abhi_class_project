import mysql.connector as sqltor
import random
import csv
from datetime import datetime
filename = "c:/workspace/abhi_class_project/Aeroplane_Ctr.txt"
mycon=sqltor.connect(host="localhost",user="root",passwd="mysql",database="Project",auth_plugin="mysql_native_password")
cursor=mycon.cursor()


def main():
    TravelID()
    bookingID()
    Getinputs()
    printticket()
    
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
    global oneround
    oneround=int(input("Enter 1 for one-way and 2 for round trip: "))
    LA=[]
    LC=[]
    LI=[]
    emplist1=[]
    tempvar=1
    global _Class
    global _NoAdults
    global _NoChildren
    global _NoInfants
    global _From
    global _To
    while tempvar==1:
        _From=input('Travelling From: ')#b
        _To=input('Travelling To: ')#c
        _Departure=input('Date of Departure(yyyy-mm-dd): ')#d
        _NoAdults=int(input('Number of Adults(12+): '))#e
        _NoChildren=int(input('Number of Children(2-12): '))#f
        _NoInfants=int(input('Number of Infants(Under 2): '))#g
        _Class=input('Class(Economy,Premium Economy,Business): ')#h
        #print("\n",_From,_To,_Departure,_NoAdults,_NoChildren,_NoInfants,_Class)
        query1="select a.plane_id,a.Company,a.place_of_departure,a.Destination,ac.cost,time(a.Time_of_Dep) from aeroplane a,aeroplane_cost ac where a.plane_id=ac.plane_id and a.place_of_departure='%s' and a.destination='%s' and ac.class='%s'"%(_From,_To,_Class)
        cursor.execute(query1)
        global _Fetch1
        _Fetch1=cursor.fetchall()#Y
        
        
            

                
        if _Fetch1==[]:
            query2="select a.plane_id,a.Company,a.place_of_departure,a.Destination,ac.cost,time(a.Time_of_Dep) from aeroplane a,aeroplane_cost ac where a.plane_id=ac.plane_id and a.place_of_departure='%s' and a.destination='%s' and ac.class='%s'"%(_To,_From,_Class)
            cursor.execute(query2)
            _Fetch1=cursor.fetchall()
            
            if _Fetch1==[]:
                print("There are no flights to the given destination from your location")
                print()
                print("Enter again")
                print()
                continue
            else:
                displayplanes()
                    
        else:
            displayplanes()
                
        
        global InpPlane_ID
        InpPlane_ID=input("Select plane_ID from above: ")#Z
        for traverse2 in _Fetch1:
            if InpPlane_ID in traverse2:
                time_of_dep = str(traverse2[-1]) 
                #_duration = str(traverse[-1])
                #print(time_of_dep)
                
                
         
                        
            
            
                
                
            
        fileread=open(filename,'r')
        travelidvar=fileread.read()#read1
        travelidvar=int(travelidvar)
        
        
        
        for inp1 in range(0,_NoAdults):
            name1=input("Enter Name: ")
            age1=input("Enter Age: ")
            gender1=input('Enter Gender(M/F/O): ')
            passno1=input('Enter Passport Number(12 digits): ')
            meal1=input("Enter on flight meal preference:(Veg/Non-Veg): ")
            #print("\n",name1,age1,gender1,passno1,meal1)
            travelid1=TravelList[travelidvar]
            travelidvar+=1
            list1=[name1,passno1,gender1,age1,travelid1,meal1]
            query3="insert into Cust_info(Name,Passport_No,Gender,Age,Travel_ID,meal_pref,Plane_ID,Date_of_Dep,Time_of_Dep,BookingID) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(name1,passno1,gender1,age1,travelid1,meal1,InpPlane_ID,_Departure+' 00:00:00',time_of_dep,BookingID)
            cursor.execute(query3)
            mycon.commit()
            LA.append(list1)
        for inp2 in range(0,_NoChildren):
            name2=input("Enter Name: ")
            age2=input("Enter Age: ")
            gender2=input('Enter Gender(M/F/O): ')
            passno2=input('Enter Passport Number(12 digits): ')
            meal2=input("Enter on flight meal preferences:(Veg/Non-Veg): ")
            #print("\n",name2,age2,gender2,passno2,meal2)
            travelid2=TravelList[travelidvar]
            travelidvar+=1
            list2=[name2,passno2,gender2,age2,travelid2,meal2]
            query4="insert into Cust_info(Name,Passport_No,Gender,Age,Travel_ID,meal_pref,Plane_ID,Date_of_Dep,Time_of_Dep,BookingID) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(name2,passno2,gender2,age2,travelid2,meal2,InpPlane_ID,_Departure+' 00:00:00',time_of_dep,BookingID)
            cursor.execute(query4)
            mycon.commit()
            LC.append(list2)
        for inp3 in range(0,_NoInfants):
            name3=input("Enter Name: ")
            age3=input("Enter Age(in months): ")
            gender3=input('Enter Gender(M/F/O): ')
            passno3=input('Enter Passport Number: ')
            meal3="None"
            #print("\n",name3,age3,gender3,passno3,meal3)
            travelid3=TravelList[travelidvar]
            travelidvar+=1
            query5="insert into Cust_info(Name,Passport_No,Gender,Age,Travel_ID,meal_pref,Plane_ID,Date_of_Dep,Time_of_Dep,BookingID) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(name3,passno3,gender3,age3+' months',travelid3,meal3,InpPlane_ID,_Departure+' 00:00:00',time_of_dep,BookingID)
            cursor.execute(query5)
            mycon.commit()
            list3=[name3,passno3,gender3,age3,travelid3,meal3]
            LI.append(list3)

    
    
        mobile=int(input("Enter Mobile Number: "))
        email_ID=input("Enter Email_ID: ")
        cost()
        query6="insert into Booking values('%s','%s')"%(cardDetails(),BookingID)
        cursor.execute(query6)
        mycon.commit()
        
        
        print("\n",mobile,email_ID)
        fileread.close()
        filewrite=open(filename,'w')
        travelidvar=str(travelidvar)
        filewrite.write(travelidvar)
        filewrite.close()
        break
    mycon.close()
def cost():
    mycon=sqltor.connect(host="localhost",user="root",passwd="mysql",database="Project",auth_plugin="mysql_native_password")
    cursor=mycon.cursor()
    query8="select Cost from aeroplane_cost where Class='%s' and Plane_ID='%s'"%(_Class,InpPlane_ID)
    cursor.execute(query8)
    _Fetch3=cursor.fetchall()
    for traverse6 in _Fetch3:
        for traverse7 in traverse6:
            cost=int(traverse7)
    onewaycost=(_NoAdults*cost)+(_NoChildren*(cost/2))            
    roundtripcost=onewaycost*2   
    if oneround==1:
        print("Total cost = ",round(onewaycost))
    elif oneround==2:
        print("Total cost = ",round(roundtripcost))

def bookingID():
    _idvar=''
    for i in range(0,10):
        tempvar1=random.randint(0,9)
        _idvar+=str(tempvar1)
    global BookingID
    BookingID = _idvar
    return _idvar

def cardDetails():
    _cardno=input("Enter Card Number(XXXX-XXXX-XXXX-XXXX): ")
    _expdate=input("Enter expiry date(mm/yy): ")
    _name=input("Enter Name on Card: ")
    _cvv=input("Enter CVV: ")
    return _name
def printticket():
    mycon=sqltor.connect(host="localhost",user="root",passwd="mysql",database="Project",auth_plugin="mysql_native_password")
    cursor=mycon.cursor()
    outfile = r'C:\workspace\abhi_class_project\printticket_' + InpPlane_ID + '.txt'
    _fh=open(outfile,'w')
    query7="select c.name,c.age,c.gender,c.Travel_ID,c.meal_pref,c.Passport_No,c.Plane_ID,c.Date_of_Dep,c.Time_of_Dep,a.company,a.Place_of_Departure,a.Destination,a.Duration,b.bookingid from cust_info c,aeroplane a,booking b where b.bookingid=c.bookingid and a.Plane_ID=c.Plane_ID"
    cursor.execute(query7)
    _Fetch2=cursor.fetchall()
    d={}
    for row in _Fetch2:
        d={'Name':row[0],'Age':row[1],'Gender':row[2],'TravelID':row[3],'Mealpref':row[4],'Passport Number':row[5],'PlaneID':row[6],'Date of Departure':row[7].strftime("20%y-%m-%d"),'Time of Departure':str(row[8]),'Airline':row[9],'From':_From,'To':_To,'Duration of Flight':str(row[12]),'BookingID':row[13]}
        print(d)       
        _fh.write(d['Name'])
        _fh.write('\n')
    
    
    _fh.close()
def displayplanes():
    print()
    print()
    print("These are the flights available between cities:")
    print()
    print("Plane_ID|Airline\t\t|City 1\t\t|City 2\t|Cost\t|Time of Departure|")
    print()
    for traverse1 in _Fetch1:
        for traverse3 in traverse1:
            print(traverse3,end='\t|')
        print()
        print()
if __name__ == "__main__":
    main()
    
#need to add time of departure and duration to aeroplane table
#need to input cost
#need to add window/aisle
#need to put payment details
#need to create bill file
