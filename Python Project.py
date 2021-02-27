import mysql.connector as sqltor
import random
import csv
import time
from datetime import date
filename = "c:/workspace/abhi_class_project/Aeroplane_Ctr.txt"
global mycon
mycon=sqltor.connect(host="localhost",user="root",passwd="secret",database="Project",auth_plugin="mysql_native_password")

def main():
    getChoices()
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
    _choice = int(input("Enter 1 to book ticket, 2 to update reservation, 3 to cancel reservation, 4 to print ticket, 0 to exit : "))
    print("Choice entered", _choice)
    if _choice == 1:
        TravelID()
        _bookingId = bookingID()
        getInputs(_bookingId)
        printticket(_bookingId)
    elif _choice == 2:
        _bookingId = input("Enter Booking id (10 digits) : ")   
        # Write logic to fetch booking
        # Ask for update - only class change allowed. Cost will change if class changes
        updateBooking(_bookingId)
        printticket(_bookingId)
    elif _choice == 3:
        _bookingId = input("Enter booking id (10 digits) : ")   
        # Delete all rows with this booking id
        deleteBooking(_bookingId)
    elif _choice == 4:
        _bookingId = input("Enter booking id (10 digits) : ")   
        printBooking(_bookingId)
    elif _choice == 0:
        return          

def getInputs(var_bookingId):             
    tempvar=1
    BookingID = var_bookingId
    while tempvar==1:
        _From=input('Travelling From: ')
        _To=input('Travelling To: ')
        _Departure=input('Date of Departure(yyyy-mm-dd): ')
        _NoAdults=int(input('Number of Adults(12+): '))
        _NoChildren=int(input('Number of Children(2-12): '))
        _NoInfants=int(input('Number of Infants(Under 2): '))
        _Class=input('Class(Economy,Premium Economy,Business): ')
        query1="""select a.plane_id,a.Company,a.place_of_departure,a.Destination,ac.cost,time(a.Time_of_Dep) from aeroplane a,
            aeroplane_cost ac where a.plane_id=ac.plane_id and a.place_of_departure='%s' and a.destination='%s' and ac.class='%s'"""%(_From,_To,_Class)
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
            print(_plane_id_h.ljust(10)+sep+_airline_h.ljust(30)+sep+_city1_h.ljust(20)+sep+_city2_h.ljust(20)+sep+
                str(_cost_h).ljust(10)+sep+str(_time_of_dep_h).ljust(10)+sep)
            print()
            for traverse1 in _Fetch1:
                _plane_id = traverse1[0]
                _airline = traverse1[1]
                _city1 = traverse1[2]
                _city2 = traverse1[3]
                _cost = traverse1[4]
                _time_of_dep = traverse1[5]
                print(_plane_id.ljust(10)+sep+_airline.ljust(30)+sep+_city1.ljust(20)+sep+_city2.ljust(20)+sep+
                    str(_cost).ljust(10)+sep+str(_time_of_dep).ljust(10)+sep)

                print()
                print()
                
        if _Fetch1==[]:            
            query2="""select a.plane_id,a.Company,a.place_of_departure,a.Destination,ac.cost,time(a.Time_of_Dep) 
                from aeroplane a,aeroplane_cost ac where a.plane_id=ac.plane_id and a.place_of_departure='%s' and a.destination='%s' 
                and ac.class='%s'"""%(_To,_From,_Class)
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
                
        
        InpPlane_ID=input("Select plane_ID from above: ")
        print()
        for traverse2 in _Fetch1:
            if InpPlane_ID in traverse2:
                time_of_dep = str(traverse2[-1]) 
        fileread=open(filename,'r')
        travelidvar=fileread.read()
        travelidvar=int(travelidvar)
        
        for inp1 in range(0,_NoAdults):
            print("Adult")
            print()
            name1=input("Enter Name: ")
            age1=input("Enter Age(12+): ")
            gender1=input('Enter Gender(M/F/O): ')
            passno1=input('Enter Passport Number(12 digits): ')
            meal1=input("Enter on flight meal preference:(Veg/Non-Veg): ")
            travelid1=TravelList[travelidvar]
            travelidvar+=1
            query3="""insert into Cust_info(Name,Passport_No,Gender,Age,Travel_ID,meal_pref,Plane_ID,Date_of_Dep,
                Time_of_Dep,BookingID,Class,Adult) 
                values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""%(name1,passno1,gender1,age1,
                    travelid1,meal1,InpPlane_ID,_Departure+' 00:00:00',time_of_dep,BookingID,_Class,'Adult')
            cursor.execute(query3)
            mycon.commit()
            print()
        for inp2 in range(0,_NoChildren):            
            print("Child")
            print()
            name2=input("Enter Name: ")
            age2=input("Enter Age(2-12): ")
            gender2=input('Enter Gender(M/F/O): ')
            passno2=input('Enter Passport Number(12 digits): ')
            meal2=input("Enter on flight meal preferences:(Veg/Non-Veg): ")
            travelid2=TravelList[travelidvar]
            travelidvar+=1
            query4="""insert into Cust_info(Name,Passport_No,Gender,Age,Travel_ID,meal_pref,Plane_ID,Date_of_Dep,Time_of_Dep,BookingID,Class,Adult) 
            values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""%(name2,passno2,gender2,age2,travelid2,
                meal2,InpPlane_ID,_Departure+' 00:00:00',time_of_dep,BookingID,_Class,'Child')
            cursor.execute(query4)
            mycon.commit()
            print()
        for inp3 in range(0,_NoInfants):
            print("Infant")
            print()
            name3=input("Enter Name: ")
            age3=input("Enter Age(<2): ")
            gender3=input('Enter Gender(M/F/O): ')
            passno3=input('Enter Passport Number(12 digits): ')
            meal3="None"
            travelid3=TravelList[travelidvar]
            travelidvar+=1
            query5="""insert into Cust_info(Name,Passport_No,Gender,Age,Travel_ID,meal_pref,Plane_ID,Date_of_Dep,Time_of_Dep,BookingID,Class,Adult) 
            values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""%(name3,passno3,gender3,age3,travelid3,
                meal3,InpPlane_ID,_Departure+' 00:00:00',time_of_dep,BookingID,_Class,'Infant')
            cursor.execute(query5)
            mycon.commit()
            print()

        mobile=int(input("Enter Mobile Number: "))
        email_ID=input("Enter Email_ID: ")
        print()
        overallcost = cost(BookingID, _Class, InpPlane_ID)
        query6="""insert into Booking(BookedBy, BookingID, Date_of_Booking, Cost, email_ID, mobile) 
        values('%s','%s','%s','%s','%s','%s')"""%(cardDetails(),BookingID,date.today(),overallcost, email_ID, mobile)
        cursor.execute(query6)
        mycon.commit()
        
        fileread.close()
        filewrite=open(filename,'w')
        travelidvar=str(travelidvar)
        filewrite.write(travelidvar)
        filewrite.close()
        break

def cost(var_booking_id, var_class, var_plane_id):
    query8="select Cost from aeroplane_cost where Class='%s' and Plane_ID='%s'"%(var_class,var_plane_id)
    cursor=mycon.cursor()
    cursor.execute(query8)
    _Fetch3=cursor.fetchall()
    for traverse6 in _Fetch3:
        for traverse7 in traverse6:
            cost=int(traverse7)

    adult_count = 0
    child_count = 0
    infant_count = 0
    query_adult="select Adult, count(*) from cust_info where Bookingid='%s' group by Adult"%(var_booking_id)
    cursor=mycon.cursor()
    cursor.execute(query_adult)
    _Fetch3=cursor.fetchall()
    for row in _Fetch3:
        if row[0] == "Adult":
            adult_count = row[1]
        elif row[0] == "Child":    
            child_count = row[1]
        elif row[0] == "Infant":    
            infant_count = row[1]

    print("Adult : '%s', Child : '%s', Infant: '%s'"%(adult_count, child_count, infant_count))
    onewaycost=(adult_count*cost)+(child_count*(cost/2))               
    print()        
    costvar="Total cost: "+str(round(onewaycost))
    return onewaycost
    print(costvar)      
    print()

def bookingID():
    while True:
        _idvar=''
        for i in range(0,10):
            tempvar1=random.randint(0,9)
            _idvar+=str(tempvar1)        
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

def printBooking(_bookingId):
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
        # Write the code for printing the ticket
        printticket(_bookingId)
        mycon.commit()
           


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
        sep='|'
        print("Name".ljust(20)+sep+"PassportNo".ljust(20)+sep+"Gender".ljust(1)+sep+"Age".ljust(10)+sep+
            "Travel_ID".ljust(10)+sep+"Meal Pref".ljust(10)+sep+"PlaneId".ljust(6)+sep+"Date of Dep".ljust(15)+sep+
            "Time of Dep".ljust(15)+sep+"BookingId".ljust(10)+sep+"Class".ljust(15)+sep+"Adult".ljust(10)+sep+"\n")

        query2="select * from cust_info where bookingid = " + _bookingId
        cursor.execute(query2)
        _Fetch2=cursor.fetchall()
        for row in _Fetch2:
            print(row[0].ljust(20)+sep+str(row[1]).ljust(20)+sep+row[2].ljust(6)+sep+row[3].ljust(10)+sep+
                row[4].ljust(10)+sep+row[5].ljust(10)+sep+row[6].ljust(7)+sep+str(row[7]).ljust(15)+sep+
                str(row[8]).ljust(15)+sep+str(row[9]).ljust(10)+sep+row[10].ljust(15)+sep+row[11].ljust(10)+sep)

        # You can update name, passport_no, gender, age, meal_pref, class
        print()
        _travelId = input("Enter Travel Id :")
        query3="select count(*) from cust_info where Travel_Id = '%s'"%(_travelId)
        cursor=mycon.cursor()
        cursor.execute(query3)
        _Fetch3=cursor.fetchall()
        for row in _Fetch3:
            _count = row[0]
        if _count == 0:
            print(_travelId, " is not found")
            return
        else:
            print(_travelId, " is found")  


        invalid = True    
        while invalid:
            _choice = int(input("Enter 1 to update name, 2 for passport no, 3 for gender, 4 for age, 5 for meal_pref, 6 for class : "))
            if _choice == 1:
                _name = input("Enter New Name : ")
                query_u="update cust_info set Name = '%s' where bookingid = '%s' and Travel_ID = '%s'"%(_name,_bookingId,_travelId)
                cursor.execute(query_u)
                print("Name updated to '%s' for Booking Id '%s' and Travel_ID '%s'"%(_name, _bookingId,_travelId))
                invalid=False
            elif _choice == 2:
                _passportNo = input("Enter New Passport No (12 digits numeric): ")
                query_u="update cust_info set Passport_No = '%s' where bookingid = '%s' and Travel_ID = '%s'"%(_passportNo,_bookingId,_travelId)
                cursor.execute(query_u)
                print("Passport No updated to '%s' for Booking Id '%s' and Travel_ID '%s'"%(_passportNo, _bookingId,_travelId))
                invalid=False
            elif _choice == 3:
                _gender = input("Enter Gender(M/F/O) : ")
                if _gender in 'MFO':
                    query_u="update cust_info set Gender = '%s' where bookingid = '%s' and Travel_ID = '%s'"%(_gender,_bookingId,_travelId)
                    cursor.execute(query_u)
                    print("Gender updated to '%s' for Booking Id '%s' and Travel_ID '%s'"%(_gender, _bookingId,_travelId))
                    invalid=False
                else:
                    print("Invalid gender. Please enter M, F, O")
            elif _choice == 4:
                _age = int(input("Enter Age : "))
                query_u="update cust_info set Age = '%s' where bookingid = '%s' and Travel_ID = '%s'"%(_age,_bookingId,_travelId)
                cursor.execute(query_u)
                print("Age updated to '%s' for Booking Id '%s' and Travel_ID '%s'"%(_age, _bookingId,_travelId))
                if _age <= 12 and _age > 2:
                    query_u="update cust_info set Adult = '%s' where bookingid = '%s' and Travel_ID = '%s'"%("Child",_bookingId,_travelId)
                    cursor.execute(query_u)
                    print("Adult column updated as Child")
                elif _age <= 2:    
                    query_u="update cust_info set Adult = '%s',meal_pref = '%s' where bookingid = '%s' and Travel_ID = '%s'"%("Infant","None",
                        _bookingId,_travelId)
                    cursor.execute(query_u)
                    print("Adult column updated as Infant and Meal Pref updated as None")
                elif _age > 12:    
                    query_u="update cust_info set Adult = '%s' where bookingid = '%s' and Travel_ID = '%s'"%("Adult",_bookingId,_travelId)
                    cursor.execute(query_u)
                    print("Adult column updated as Adult")
                invalid=False
            elif _choice == 5:
                _mealpref = input("Enter Meal Pref(Veg/Non-Veg) : ")
                if _mealpref.lower() != 'veg' and _mealpref.lower() != 'non-veg':
                    print("Your meal pref is incorrect. Please choose from (Veg/Non-Veg)")                    
                else:
                    query_u="update cust_info set meal_pref = '%s' where bookingid = '%s' and Travel_ID = '%s'"%(_mealpref,_bookingId,_travelId)
                    cursor.execute(query_u)
                    print("Meal Pref updated to '%s' for Booking Id '%s' and Travel_ID '%s'"%(_mealpref, _bookingId,_travelId))
                    invalid=False
            elif _choice == 6:
                _class = input("Please enter new class (Economy, Premium Economy, Business): ")
                if _class.lower() == "economy":
                    query_u="update cust_info set Class = '%s' where bookingid = '%s' and Travel_ID = '%s'"%("Economy",_bookingId,_travelId)
                    cursor.execute(query_u)
                    print("Class updated to '%s' for Booking Id '%s' and Travel Id '%s'"%("Economy", _bookingId,_travelId))
                    invalid=False
                elif _class.lower() == "premium economy":    
                    query_u="update cust_info set Class = '%s' where bookingid = '%s' and Travel_ID = '%s'"%("Premium Economy",_bookingId,_travelId)
                    cursor.execute(query_u)
                    print("Class updated to '%s' for Booking Id '%s' and Travel Id '%s'"%("Premium Economy", _bookingId,_travelId))
                    invalid=False
                elif _class.lower() == "business":    
                    query_u="update cust_info set Class = '%s' where bookingid = '%s' and Travel_ID = '%s'"%("Business",_bookingId,_travelId)
                    cursor.execute(query_u)
                    print("Class updated to '%s' for Booking Id '%s' and Travel Id '%s'"%("Business", _bookingId,_travelId))
                    invalid=False
                else:
                    print("You have entered an incorrect class. Please choose from (Economy, Premium Economy, Business)") 
                # Check if class update, and recalculate cost
                #        
                if invalid==False:
                    query_planeid="select Plane_ID from cust_info where Travel_Id = '%s'"%(_travelId)
                    cursor=mycon.cursor()
                    cursor.execute(query_planeid)
                    _Fetch3=cursor.fetchall()
                    for row in _Fetch3:
                        var_plane_id = row[0]
                        calculated_cost = cost(_bookingId, _class, var_plane_id)
                        query_updatecost = "update booking set cost = '%s' where bookingid = '%s'"%(calculated_cost, _bookingId)
                        cursor=mycon.cursor()
                        cursor.execute(query_updatecost)
                        print("Cost updated as '%s' for booking id '%s'"%(calculated_cost, _bookingId))
            else:
                print("Incorrect choice")
        
        mycon.commit()

def cardDetails():
    _cardno=input("Enter Card Number(XXXX-XXXX-XXXX-XXXX): ")
    _expdate=input("Enter expiry date(mm/yy): ")
    _name=input("Enter Full Name on Card: ")
    _cvv=input("Enter CVV: ")
    return _name

def printticket(_bookingId):
    print("Booking Id:", _bookingId)
    outfile = r'C:\workspace\abhi_class_project\tickets\printticket_' + _bookingId + '.txt'
    _fh=open(outfile,'w')
    cursor=mycon.cursor()
    query7='''select Plane_ID,Time_of_Dep,BookingID,Company,Type,Place_of_Departure,Destination,Duration,
        Bookedby,Date_of_Booking,Name,Passport_No,Gender,Age,Travel_ID,meal_pref,Date_of_Dep,Class,Adult,cost,email_ID,mobile  
        from aeroplane natural join booking natural join cust_info where booking.bookingid = ''' + _bookingId 
    
    cursor.execute(query7)
    _Fetch2=cursor.fetchall()
    d={}
    rowcnt = 0
    for row in _Fetch2:
        rowcnt = rowcnt + 1
        length=len(_Fetch2)
        d={'Name':row[10],'Age':row[13],'Gender':row[12],'TravelID':row[14],'Mealpref':row[15],
            'Passport Number':row[11],'PlaneID':row[0],'Date of Departure':row[16].strftime("20%y-%m-%d"),
            'Time of Departure':row[1],'Airline':row[3],'From':row[5],'To':row[6],'Duration of Flight':str(row[7]),
            'BookingID':row[2],'DateofBooking':row[9],'Class':row[17],'Bookedby':row[8],'Adult':row[18],
            'cost':row[19],'Email_ID':row[20],'Mobile':row[21]}
        
        if (rowcnt == 1):
            _fh.write("BookingID: " + str(d['BookingID'])+ "\t\t"+"Date of Booking: " + str(d['DateofBooking'])+ "\t\t"+
                "Booked by: "+str(d['Bookedby'])+"\n\n")
            _fh.write("Date of Departure: " + str(d['Date of Departure'])+"\t\t"+"From: " + str(d['From'])+"\t\t"+"To: " + 
                str(d['To'])+"\t\t"+ "Duration of Flight: " + str(d['Duration of Flight'])+"\n\n")   
            
            _fh.write("PlaneID: " + str(d['PlaneID'])+"\t\t"+"Time of Departure: " + str(d['Time of Departure'])+
                "\t\t"+"Class: "+str(d['Class'])+"\t\t"+"Time of Arrival: "+timeofarrival(d)+"\n\n")
            passenger_h = "Passenger(s)"
            travelid_h = "Travel ID"
            age_h = "Age"
            gender_h = "Gender"
            passport_h = "Passport Number"
            meal_pref_h = "Meal Preference"
            sep = "|"
            _fh.write(passenger_h.ljust(30)+sep+travelid_h.ljust(20)+sep+age_h.ljust(5)+sep+gender_h.ljust(8)+sep+
                str(passport_h).ljust(15)+sep+meal_pref_h.ljust(20)+sep+"\n\n")
            

        _adult = row[10]+"("+str(d['Adult'])+")"
        _fh.write(_adult.ljust(30)+sep+row[14].ljust(20)+sep+row[13].ljust(5)+sep+row[12].ljust(8)+sep+
            str(row[11]).ljust(15)+sep+row[15].ljust(20)+sep+"\n")
         
        
        if rowcnt==length:
            # This needs to be fixed
            costvar=str(d['cost'])
            email_ID=d['Email_ID']
            mobile=d['Mobile']
            _fh.write("\n"+"Total Cost: "+costvar+"\n\n")
            _fh.write("Email Address: "+email_ID+"\n\n"+"Mobile Number: "+str(mobile)+"\n")       
    _fh.close()
    print("Booking ID",_bookingId,"has been printed") 
    
def timeofarrival(d):    
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
    