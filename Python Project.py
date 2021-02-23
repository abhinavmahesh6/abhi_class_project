import mysql.connector as sqltor
import random
import csv
import time
from datetime import date
filename = "c:/workspace/abhi_class_project/Aeroplane_Ctr.txt"
global mycon
mycon=sqltor.connect(host="localhost",user="root",passwd="secret",database="Project",auth_plugin="mysql_native_password")
global listbookid
listbookid=[]

def main():
    TravelID()
    bookingID()
    getChoices()
    printticket()
    mycon.close()

def TravelID():
    global TravelList
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

def getChoices():
    _choice = int(input("Enter 1 to book ticket, 2 to update reservation, 3 to cancel reservation, 0 to exit : "))
    print("Choice entered", _choice)
    if _choice == 1:
        getInputs()
    elif _choice == 2:
        _bookingId = input("Enter Booking id (10 digits) : ")   
        # Write logic to fetch booking
        # Ask for update - only class change allowed. Cost will change if class changes
        updateBooking(_bookingId)
    elif _choice == 3:
        _bookingId = input("Enter booking id (10 digits) : ")   
        # Delete all rows with this booking id
        deleteBooking(_bookingId)
    elif _choice == 0:
        return          

def getInputs():             
    tempvar=1
    global _Class
    global _NoAdults
    global _NoChildren
    global _NoInfants
    global _From
    global _To
    global email_ID
    global mobile
    while tempvar==1:
        _From=input('Travelling From: ')
        _To=input('Travelling To: ')
        _Departure=input('Date of Departure(yyyy-mm-dd): ')
        _NoAdults=int(input('Number of Adults(12+): '))
        _NoChildren=int(input('Number of Children(2-12): '))
        _NoInfants=int(input('Number of Infants(Under 2): '))
        _Class=input('Class(Economy,Premium Economy,Business): ')
        query1="select a.plane_id,a.Company,a.place_of_departure,a.Destination,ac.cost,time(a.Time_of_Dep) from aeroplane a,aeroplane_cost ac where a.plane_id=ac.plane_id and a.place_of_departure='%s' and a.destination='%s' and ac.class='%s'"%(_From,_To,_Class)
        cursor=mycon.cursor()
        cursor.execute(query1)
        _Fetch1=cursor.fetchall()
        def displayplanes():
            print()
            print()
            print("These are the flights available between cities:")
            print()
            sep = "|"
            _plane_id_h = "Plane Id"
            _airline_h = "Airline"
            _city1_h = "City 1"
            _city2_h = "City 2"
            _cost_h = "Cost"
            _time_of_dep_h = "Time of Dep"
            print(_plane_id_h.ljust(10)+sep+_airline_h.ljust(30)+sep+_city1_h.ljust(20)+sep+_city2_h.ljust(20)+sep+str(_cost_h).ljust(10)+sep+str(_time_of_dep_h).ljust(10)+sep)
            print()
            for traverse1 in _Fetch1:
                _plane_id = traverse1[0]
                _airline = traverse1[1]
                _city1 = traverse1[2]
                _city2 = traverse1[3]
                _cost = traverse1[4]
                _time_of_dep = traverse1[5]
                print(_plane_id.ljust(10)+sep+_airline.ljust(30)+sep+_city1.ljust(20)+sep+_city2.ljust(20)+sep+str(_cost).ljust(10)+sep+str(_time_of_dep).ljust(10)+sep)

                print()
                print()
                
        if _Fetch1==[]:            
            query2="select a.plane_id,a.Company,a.place_of_departure,a.Destination,ac.cost,time(a.Time_of_Dep) from aeroplane a,aeroplane_cost ac where a.plane_id=ac.plane_id and a.place_of_departure='%s' and a.destination='%s' and ac.class='%s'"%(_To,_From,_Class)
            cursor.execute(query2)
            _Fetch1=cursor.fetchall()
            
            if _Fetch1==[]:
                print("There are no flights to the given destination from your location")
                print()
                print("Please enter another destination")
                print()
                continue
            else:
                displayplanes()
                    
        else:
            displayplanes()
                
        
        global InpPlane_ID
        InpPlane_ID=input("Select plane_ID from above: ")
        for traverse2 in _Fetch1:
            if InpPlane_ID in traverse2:
                time_of_dep = str(traverse2[-1]) 
        fileread=open(filename,'r')
        travelidvar=fileread.read()
        travelidvar=int(travelidvar)
        
        for inp1 in range(0,_NoAdults):
            name1=input("Enter Name: ")
            age1=input("Enter Age: ")
            gender1=input('Enter Gender(M/F/O): ')
            passno1=input('Enter Passport Number(12 digits): ')
            meal1=input("Enter on flight meal preference:(Veg/Non-Veg): ")
            travelid1=TravelList[travelidvar]
            travelidvar+=1
            query3="insert into Cust_info(Name,Passport_No,Gender,Age,Travel_ID,meal_pref,Plane_ID,Date_of_Dep,Time_of_Dep,BookingID,Class,Adult) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(name1,passno1,gender1,age1,travelid1,meal1,InpPlane_ID,_Departure+' 00:00:00',time_of_dep,BookingID,_Class,'Adult')
            cursor.execute(query3)
            mycon.commit()
        for inp2 in range(0,_NoChildren):            
            name2=input("Enter Name: ")
            age2=input("Enter Age: ")
            gender2=input('Enter Gender(M/F/O): ')
            passno2=input('Enter Passport Number(12 digits): ')
            meal2=input("Enter on flight meal preferences:(Veg/Non-Veg): ")
            travelid2=TravelList[travelidvar]
            travelidvar+=1
            query4="insert into Cust_info(Name,Passport_No,Gender,Age,Travel_ID,meal_pref,Plane_ID,Date_of_Dep,Time_of_Dep,BookingID,Class,Adult) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(name2,passno2,gender2,age2,travelid2,meal2,InpPlane_ID,_Departure+' 00:00:00',time_of_dep,BookingID,_Class,'Child')
            cursor.execute(query4)
            mycon.commit()
        for inp3 in range(0,_NoInfants):
            name3=input("Enter Name: ")
            age3=input("Enter Age(in months): ")
            gender3=input('Enter Gender(M/F/O): ')
            passno3=input('Enter Passport Number: ')
            meal3="None"
            travelid3=TravelList[travelidvar]
            travelidvar+=1
            query5="insert into Cust_info(Name,Passport_No,Gender,Age,Travel_ID,meal_pref,Plane_ID,Date_of_Dep,Time_of_Dep,BookingID,Class,Adult) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(name3,passno3,gender3,age3+' months',travelid3,meal3,InpPlane_ID,_Departure+' 00:00:00',time_of_dep,BookingID,_Class,'Infant')
            cursor.execute(query5)
            mycon.commit()

        mobile=int(input("Enter Mobile Number: "))
        email_ID=input("Enter Email_ID: ")
        print()
        cost()
        query6="insert into Booking values('%s','%s','%s')"%(cardDetails(),BookingID,date.today())
        cursor.execute(query6)
        mycon.commit()
        
        fileread.close()
        filewrite=open(filename,'w')
        travelidvar=str(travelidvar)
        filewrite.write(travelidvar)
        filewrite.close()
        break

def cost():
    query8="select Cost from aeroplane_cost where Class='%s' and Plane_ID='%s'"%(_Class,InpPlane_ID)
    cursor=mycon.cursor()
    cursor.execute(query8)
    _Fetch3=cursor.fetchall()
    for traverse6 in _Fetch3:
        for traverse7 in traverse6:
            cost=int(traverse7)
    onewaycost=(_NoAdults*cost)+(_NoChildren*(cost/2))               
    global costvar
    print()        
    costvar="Total cost: "+str(round(onewaycost))
    print(costvar)      
    print()

def bookingID():
    while True:
        _idvar=''
        for i in range(0,10):
            tempvar1=random.randint(0,9)
            _idvar+=str(tempvar1)        
        if _idvar not in listbookid:
            listbookid.append(_idvar)
        else:
            continue
        global BookingID
        BookingID = _idvar
        break
    return _idvar

def deleteBooking(_bookingId):
    query1="select count(*) from booking where bookingid = " + _bookingId
    cursor=mycon.cursor()
    cursor.execute(query1)
    _Fetch1=cursor.fetchall()
    _count = 0
    for row in _Fetch1:
        _count = row[0]
    if _count == 0:
        print(_bookingId, " is not found")
    else:
        print(_bookingId, " is found")   
        query_d="delete from booking where bookingid = " + _bookingId
        cursor.execute(query_d)
        query_c="delete from cust_info where bookingid = " + _bookingId
        cursor.execute(query_c)
        mycon.commit()
        print(_bookingId, " has been deleted")   

def updateBooking(_bookingId):
    query1="select count(*) from booking where bookingid = " + _bookingId
    cursor=mycon.cursor()
    cursor.execute(query1)
    _Fetch1=cursor.fetchall()
    _count = 0
    for row in _Fetch1:
        _count = row[0]
    if _count == 0:
        print(_bookingId, " is not found")
    else:
        print(_bookingId, " is found")  
        # Display the travel Ids
        query1="select * from cust_info where bookingid = " + _bookingId
        cursor.execute(query1)
        _Fetch2=cursor.fetchall()
        for row in _Fetch2:
            print(row)

        # You can update name, passport_no, gender, age, meal_pref, class
        _travelId = input("Enter Travel Id :")
        _choice = int(input("Enter 1 to update name, 2 for passport no, 3 for gender, 4 for age, 5 for meal_pref, 6 for class : "))
        if _choice == 1:
            _name = input("Enter New Name : ")
            query_u="update cust_info set Name = '%s' where bookingid = '%s' and Travel_ID = '%s'"%(_name,_bookingId,_travelId)
            cursor.execute(query_u)
            print("Name updated to '%s' for Booking Id '%s' and Travel_ID '%s'"%(_name, _bookingId,_travelId))
        elif _choice == 2:
            _passportNo = input("Enter New Passport No : ")
        elif _choice == 3:
            _gender = input("Enter Gender : ")
        elif _choice == 4:
            _age = input("Enter Age : ")
        elif _choice == 5:
            _mealpref = input("Enter Meal Pref : ")
        elif _choice == 6:
            _class = input("Please enter new class (Economy, Premium Economy, Business): ")
            if _class == "Economy":
                query_u="update cust_info set Class = '%s' where bookingid = '%s' and Travel_ID = '%s'"%(_class,_bookingId,_travelId)
                cursor.execute(query_u)
                print("Class updated to '%s' for Booking Id '%s' and Travel Id '%s'"%(_class, _bookingId,_travelId))
            elif _class == "Premium Economy":    
                query_u="update cust_info set Class = '%s' where bookingid = '%s' and Travel_ID = '%s'"%(_class,_bookingId,_travelId)
                cursor.execute(query_u)
                print("Class updated to '%s' for Booking Id '%s' and Travel Id '%s'"%(_class, _bookingId,_travelId))
            elif _class == "Business":    
                query_u="update cust_info set Class = '%s' where bookingid = '%s' and Travel_ID = '%s'"%(_class,_bookingId,_travelId)
                cursor.execute(query_u)
                print("Class updated to '%s' for Booking Id '%s' and Travel Id '%s'"%(_class, _bookingId,_travelId))
            else:
                print("You have entered an incorrect class. Please choose from (Economy, Premium Economy, Business)")    
        mycon.commit()

def cardDetails():
    _cardno=input("Enter Card Number(XXXX-XXXX-XXXX-XXXX): ")
    _expdate=input("Enter expiry date(mm/yy): ")
    _name=input("Enter Full Name on Card: ")
    _cvv=input("Enter CVV: ")
    return _name

def printticket():
    outfile = r'C:\workspace\abhi_class_project\printticket_' + BookingID + '.txt'
    _fh=open(outfile,'w')
    cursor=mycon.cursor()
    query7="select * from aeroplane natural join booking natural join cust_info where booking.bookingid = " + BookingID + " group by Travel_ID"
    
    cursor.execute(query7)
    _Fetch2=cursor.fetchall()
    global d
    d={}
    rowcnt = 0
    for row in _Fetch2:
        rowcnt = rowcnt + 1
        length=len(_Fetch2)
        d={'Name':row[10],'Age':row[13],'Gender':row[12],'TravelID':row[14],'Mealpref':row[15],'Passport Number':row[11],'PlaneID':row[0],'Date of Departure':row[16].strftime("20%y-%m-%d"),'Time of Departure':row[1],'Airline':row[3],'From':_From,'To':_To,'Duration of Flight':str(row[7]),'BookingID':row[2],'DateofBooking':row[9],'Class':row[17],'Bookedby':row[8],'Adult':row[18]}
        stringtest1="BookingID,Date of Booking,From,To,PlaneID,Airline,Class,Date of Departure,Time of Departure,Duration of Flight,Time of arrival,Date of arrival,Name,Age,Gender,Passport Number,TravelID,Meal preference,email,mobile,Name,Cost"
        
        if (rowcnt == 1):
            _fh.write("BookingID: " + str(d['BookingID'])+ "\t\t"+"Date of Booking: " + str(d['DateofBooking'])+ "\t\t"+"Booked by: "+str(d['Bookedby'])+"\n\n")
            _fh.write("Date of Departure: " + str(d['Date of Departure'])+"\t\t"+"From: " + str(d['From'])+"\t\t"+"To: " + str(d['To'])+"\t\t"+ "Duration of Flight: " + str(d['Duration of Flight'])+"\n\n")   
            
            _fh.write("PlaneID: " + str(d['PlaneID'])+"\t\t"+"Time of Departure: " + str(d['Time of Departure'])+"\t\t"+"Class: "+str(d['Class'])+"\t\t"+"Time of Arrival: "+timeofarrival()+"\n\n")
            passenger_h = "Passenger(s)"
            travelid_h = "Travel ID"
            age_h = "Age"
            gender_h = "Gender"
            passport_h = "Passport Number"
            meal_pref_h = "Meal Preference"
            sep = "|"
            _fh.write(passenger_h.ljust(30)+sep+travelid_h.ljust(20)+sep+age_h.ljust(5)+sep+gender_h.ljust(8)+sep+str(passport_h).ljust(15)+sep+meal_pref_h.ljust(20)+sep+"\n\n")
            

        _adult = row[10]+"("+str(d['Adult'])+")"
        _fh.write(_adult.ljust(30)+sep+row[14].ljust(20)+sep+row[13].ljust(5)+sep+row[12].ljust(8)+sep+str(row[11]).ljust(15)+sep+row[15].ljust(20)+sep+"\n")
         
        
        if rowcnt==length:
            _fh.write("\n"+costvar+"\n\n")
            _fh.write("Email Address: "+email_ID+"\n\n"+"Mobile Number: "+str(mobile)+"\n")
        
    _fh.close()
    
def timeofarrival():    
    ctr1=2
    ctr2=2
    split1=str(d['Duration of Flight']).split(':')
    split2=str(d['Time of Departure']).split(':')
    totsec1=0
    for time1 in split1:
        totsec1+=round(int(time1)*((60)**ctr1))
        ctr1-=1
    for time2 in split2:
        totsec1+=round(int(time2)*((60)**ctr2))
        ctr2-=1
        
    arrival=time.strftime("%H:%M:%S", time.gmtime(totsec1))
    split3=str(arrival).split(':')
    totsec2=0
    ctr3=2
    for time3 in split3:        
        totsec2+=round(int(time3)*((60)**ctr3))
        ctr3-=1
    if totsec2>86400:    
        totsec3=totsec2-86400
        arrival=time.strftime("%H:%M:%S", time.gmtime(totsec3))    
    return arrival

if __name__ == "__main__":
    main()
    