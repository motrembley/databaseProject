#!!! username for admin function is either "Morgan" OR "Fernando" and the password is "admin" !!!
import numbers
import sqlite3 
from sqlite3 import Error 


def openConnection(_dbFile):
    conn = None
    try:
        conn = sqlite3.connect(_dbFile)

    except Error as e:
        print(e)
    return conn

def closeConnection(_conn, _dbFile):

    try:
        _conn.close()
    except Error as e:
        print(e)

def patient(_conn):
    print("---PATIENT FUNCTION---")
    x = -1
    while x == -1:
        print("What would you like to do?")
        print("1. Add your information\n2. Check your results\n3. Update your comment")
        temp = int(input())
        if temp == 1:
            #ADD PERSON
            print("Enter your name:")
            name = input()
            print("Enter your address:")
            addr = input()
            print("Enter your date of birth: (mm/dd/yyyy)")
            dob = input()
            print("Enter any comments or concerns:")
            comment = input()
            #SQL GOES HERE
            try:
                elf = _conn.execute("SELECT MAX(p_ID) FROM Person")
                
                _conn.commit()
                for i in elf:
                    test = int(i[0]) + 1
                    print("Your ID # is:",test,"Rememeber this to make future changes.")
               
                sql = _conn.execute("INSERT into Person VALUES ('"+str(test)+"','"+str(name)+"','" +str(addr)+ "','"+str(dob)+"','" +str(comment)+"')  ")
                _conn.commit()

                sql = _conn.execute("INSERT into TestingAvailability VALUES ('"+str(test)+"', 'No Test Yet', 0, 'No', 'No comment')")
                _conn.commit()

                elf = _conn.execute("SELECT MAX(r_caseID) FROM Results")
                _conn.commit()
                for i in elf:
                    newcase = int(i[0]) + 1

                sql = _conn.execute("INSERT into Results VALUES('"+str(newcase)+"', '"+str(test)+"', 'N/A', 'Waiting for result')")
                _conn.commit()

                sql = _conn.execute("SELECT p_ID from Person")
             

            #FINISHED MESSAGE GOES HERE
            except Error as e:
                print(e)
                print("++++++++++++++++++++++++++++")

            x = 0
        elif temp == 2:
            #CHECK RESULTS
            print("Enter your case ID:")
            temp = input()
            if temp[0].isdigit():   #FOR CASE ID AS INPUT
                caseID = temp
                #SQL GOES HERE
                try:
                    ### WORKING....
                
                    sql = _conn.execute("SELECT p_name from Person where p_ID = ?",(caseID,))
                    for r in sql:
                        l = '{:>5}'.format(r[0])
                        print(l)

                    sql = _conn.execute("SELECT r_caseID, r_result,r_date from Results where r_caseID = ? ",(caseID,))
                    for r in sql:
                        l = '{:>1}{:>1}{:>1}{:>1}{:>1}'.format(r[0],',',r[1],',',r[2])
                        print(l)

                    sql = _conn.execute("SELECT nh_descision from NeedsHospital where nh_caseID = ?",(caseID,))
                    for r in sql:
                        l = '{:>1}'.format(r[0])
                        print(l)

                
                except Error as e:
                    print(e)
            x = 0

        elif temp == 3:
            #UPDATE PERSON COMMENT
            print("Enter your name or case ID:")
            temp = input()
            print("Enter your comments or concerns:")
            comment = input()
            if temp[0].isdigit():   #FOR CASE ID AS INPUT
                caseID = temp
                #SQL GOES HERE
                try:
                    sql = _conn.execute(" UPDATE Person SET p_comment = ? where p_ID = ?",(comment,int(caseID),))
                    _conn.commit()
                    print("success")
                   
                except Error as e:
                    print(e)
            
            else:                  
                name = temp
                #SQL GOES HERE
                try:

                    sql = _conn.execute(" UPDATE Person SET p_comment = ? where p_name = ?",(comment, name))
                    _conn.commit()
                    print("success")
                   
                except Error as e:
                    print(e)

            x = 0
   
        else:
            print("---Invalid Entry!---")
            print("Would you like to try again?")
            print("1. YES\n2. NO")
            temp = int(input())
            if temp == 1:
                x = -1
            else:
                x = 0



def doctor(_conn):
    print("---DOCTOR FUNCTION---")
    x = -1
    while x == -1:
        print("What would you like to do?")
        print("1. Enter new case\n2. Update existing case\n3. Update patient symptoms\n4. Update a comment")
        temp = int(input())
        if temp == 1:
            #ENTER NEW CASE
            # HALF WORKS 
            print("Enter patient name:")
            name = input()
            print("Enter type of test administered:")
            testType = input()
            givenTest = "YES"
            print("Enter any comments or concerns:")
            comment = input()
            #SQL GOES HERE
            try:
                elf = _conn.execute("SELECT MAX(ta_personID) FROM TestingAvailability")
                _conn.commit()
                for i in elf:
                    test = int(i[0]) + 1

                sql = _conn.execute("INSERT into TestingAvailability VALUES ('"+str(test)+"','"+str(testType)+"', (SELECT t_units FROM Testing WHERE t_type = '" + str(testType) + "'), '"+str(givenTest)+"','"+str(comment)+"')")
                _conn.commit()
                #sql = _conn.execute("UPDATE Testing SET t_requests = 15 where t_type = ?",(testType))
                #_conn.commit()

                #_conn.commit()
               # for i in elf:
                #    newcase = int(i[0]) + 1

               # sql = _conn.execute("UPDATE Testing SET t_requests = ? WHERE t_type = '?'",(newcase,))
               # _conn.commit()
                
            except Error as e:
                print(e)


            #FINISHED MSG GOES HERE
            x = 0
        elif temp == 2:
            #UPDATE CASE 
            #WORKING...
            print("Which table would you like to update?")
            print("1. Testing Availability\n2. Results\n3. Needs Hospital\n 4. Outcome")
            temp = int(input())
            if temp == 1:
                #TESTING AVAILABILITY
                print("Enter patient ID:")
                name = input()
                print("Enter type of test given:")
                testType = input()
                print("Enter number of units:")
                unit = input()
                print("Is the test given?:")
                given = input()
                print("Enter any comments or concerns:")
                comment = input()
                #SQL GOES HERE
                try:

                    sql = _conn.execute("UPDATE TestingAvailability SET ta_type = ?, ta_units = ?, ta_givenTest = ?, ta_comment = ? where ta_personID = ? ",(testType,unit,given,comment,int(name),))
                    _conn.commit()
                except Error as e:
                    print(e)
                


                #FINISHED MSG GOES HERE
                x = 0
            elif temp == 2:
                #RESULT
                #WORKING...
                print("Enter case ID")
                caseID = input()
                print("Enter date: (mm/dd/yyyy)")
                date = input()
                print("Enter result of test:")
                result = input()
                #SQL GOES HERE
                try:
                    sql = _conn.execute("UPDATE Results SET r_date = ?, r_result = ? WHERE r_caseID = ? ",(date,result,int(caseID),))
                    _conn.commit()
                    print("success")
                
                except Error as e:
                    print(e)

                #FINISHED MSG GOES HERE
                x = 0
            elif temp == 3:
                #NEEDS HOSPITAL
                #WORKING...
                print("Enter case ID:")
                caseID = input()
                print("Enter ""YES"" if the patient is recomended to seek medical attention. Otherwise, enter ""NO"":")
                descision = input()
                #SQL GOES HERE
                try:
                    sql = _conn.execute("UPDATE NeedsHospital SET nh_descision = ? WHERE nh_caseID = ?",(descision,int(caseID),))
                    _conn.commit()
                    print("success")
                except Error as e:
                    print(e)


                #FINISHED MSG GOES HERE
                x = 0
            elif temp == 4:
                #OUTCOME
                #WORKING...
                print("Enter case ID:")
                caseID = input()
                print("Enter patient status:")
                status = input()
                #SQL GOES HERE
                try:
                   
                    sql = _conn.execute("UPDATE Outcome SET o_status = ? WHERE o_caseID = ?",(status,int(caseID),))
                    _conn.commit()
                    print("success")
                except Error as e:
                    print(e)

                #FINISHED MSG GOES HERE
                x = 0
            else:
                print("---Invalid Entry!---")
            x = 0
        elif temp == 3:
            #UPDATE SYMPTOM
            print("Enter case ID:")
            caseID = input()
            print("If the following symptoms are present, Enter ""YES"", if not, Enter ""NO"". Seperate each entry with a "","".")
            print("Fever, Tiredness, Dry Cough, Difficulty Breathing, Sore Throat")
            tempSymptoms = input()
            symptoms = tempSymptoms.split(",")
            print("Enter severity of case:")
            severity = int(input())
            #SQL GOES HERE
            try:
                dummy = _conn.execute("SELECT count(s_caseID) FROM Symptoms where s_caseID = " + str(caseID) + "")
                for i in dummy:
                    if (i[0] == 0):
                        sql = _conn.execute("INSERT INTO Symptoms VALUES(?,?,?,?,?,?,?)",(int(caseID),symptoms[0],symptoms[1],symptoms[2],symptoms[3],symptoms[4],severity))
                        _conn.commit()
                        sql = _conn.execute("INSERT INTO NeedsHospital VALUES(?,'Unknown',5,?,?,?,?,?,?,'NO')",(int(caseID),symptoms[0],symptoms[1],symptoms[2],symptoms[3],symptoms[4],severity))
                        _conn.commit()
                    else:
                        sql = _conn.execute("UPDATE Symptoms SET s_fever = ?, s_tiredness = ?, s_dryCough = ?, s_breathingDifficulty = ?, s_soreThroat = ?, s_severity = ? where s_caseID = ?",(symptoms[0],symptoms[1],symptoms[2],symptoms[3],symptoms[4],severity,int(caseID),))
                        _conn.commit()
                        sql = _conn.execute("UPDATE NeedsHospital SET nh_fever = ?, nh_tiredness = ?, nh_dryCough = ?, nh_breathingDifficulty = ?, nh_soreThroat = ?, nh_severity = ? where nh_caseID = ?",(symptoms[0],symptoms[1],symptoms[2],symptoms[3],symptoms[4],severity,int(caseID),))
                        _conn.commit()

            except Error as e:
                print(e)

            #FINISHED MSG GOES HERE
            x = 0
        elif temp == 4:
            #UPDATE COMMENT
            #WORKING...
            print("Which comment would you like to update?")
            print("1. Testing Availability\n2. Outcome")
            temp = int(input())
            if temp == 1:
                #TESTING AVAILABILITY
                print("Enter case ID:")
                caseID = int(input())
                print("Enter comment:")
                comment = input()
                #SQL GOES HERE
                try:
                     sql = _conn.execute("UPDATE TestingAvailability SET ta_comment = ? WHERE ta_personID = ?",(comment,int(caseID),))
                     _conn.commit()
                     print("success")
                except Error as e:
                    print(e)



                #FINISHED MSG GOES HERE
                x = 0
            elif temp == 2:
                #OUTCOME
                #WORKING...
                print("Enter case ID:")
                caseID = int(input())
                print("Enter comment:")
                comment = input()
                #SQL GOES HERE
                try:
                    sql = _conn.execute("UPDATE Outcome SET o_comments = ? WHERE o_caseID = ?",(comment,int(caseID),))
                    _conn.commit()
                    print("success")
                except Error as e:
                    print(e)



                #FINISHED MSG GOES HERE
                x = 0
            else:
                print("---Invalid Entry!---")
            x = 0
        else:
            print("---Invalid Entry!---")
            print("Would you like to try again?")
            print("1. YES\n2. NO")
            temp = int(input())
            if temp == 1:
                x = -1
            else:
                x = 0



def visitor(_conn):
    print("---VISITOR FUNCTION---")
    x = -1
    while x == -1:
        print("What would you like to do?")
        print("1. Check lockdown status\n2. View symptom statistics\n3. Browse public information")
        temp = int(input())
        if temp == 1:
            #CHECK LOCKDOWN STATUS
            print("Enter state:")
            state = input()
            print("Enter country:")
            country = input()
            #SQL GOES HERE

            try:
                 args = [state,country]
                 sql = _conn.execute("SELECT * from Location WHERE l_state = ? and l_country = ?",(state,country,))
                 
            
            except Error as e:
                print(e)
            

            #DISPLAY GOES HERE
            for r in sql:
                l ='{:>1}{:>1}{:>1}{:>1}{:>1}{:>1}{:>1}'.format(r[0],', ',r[2],'. ',r[1],'. Lockdown Status: ', r[3], '.')
               
                print(l)
            

        elif temp == 2:
            #VIEW SYMPTOM STATS
            #SQL GOES HERE
            try:
                sql = _conn.execute(""" SELECT count(s_caseID) from Symptoms WHERE s_fever = 'YES'""")
                for i in sql:
                    fevers = i[0]

                sql = _conn.execute(""" SELECT count(s_caseID) from Symptoms WHERE s_tiredness = 'YES'""")
                for i in sql:
                    tiredness = i[0]

                sql = _conn.execute(""" SELECT count(s_caseID) from Symptoms WHERE s_dryCough = 'YES'""")
                for i in sql:
                    cough = i[0]

                sql = _conn.execute(""" SELECT count(s_caseID) from Symptoms WHERE s_breathingDifficulty = 'YES'""")
                for i in sql:
                    bDiff = i[0]

                sql = _conn.execute(""" SELECT count(s_caseID) from Symptoms WHERE s_soreThroat = 'YES'""")
                for i in sql:
                    soreThroat = i[0]

                sql = _conn.execute(""" SELECT count(s_caseID) from Symptoms""")
                for i in sql:
                    total = i[0]

                ratio1 = fevers/total
                ratio2 = tiredness/total
                ratio3 = cough/total
                ratio4 = bDiff/total
                ratio5 = soreThroat/total
                
                print("Ratio of symptoms to total cases: Fever: " + str(ratio1) + ", Tiredness: " + str(ratio2) + ", Dry Cough: " + str(ratio3) + ", Difficulty Breathing: " + str(ratio4) + ", Sore Throat: " + str(ratio5) + ".")
            except Error as e:
                print(e)

           

        elif temp == 3:
            #BROWSE PUBLIC INFO
            print("Enter table name you would like to view:")    #should probably include a list of tables
            print("Hospitals, Location, Symptoms, Testing")
            tableName = input()
            #SQL GOES 
            if tableName in ('Hospitals', 'Location', 'Symptoms', 'Testing'):
                sql = _conn.execute("SELECT * FROM " + tableName)
                print("Printing " + tableName + " table:")
                for i in sql:
                    print(i)

        else:
            print("---Invalid Entry!---")
            print("Would you like to try again?")
            print("1. YES\n2. NO")
            temp = int(input())
            if temp == 1:
                x = -1
            else:
                x = 0
        print("Would you like to look around some more?")
        print("1. YES\n2. NO")
        temp = int(input())
        if temp == 1:
            x = -1
        else:
            x = 0



def admin(_conn):
    print("---ADMIN FUNCTION---")
    print("Enter Username:")
    name = input()
    if name in ("Morgan","Fernando"):
        print("Enter password:")
        pwd = input()
        if pwd == "admin":
            x = -1
        else:
            print("Invalid Password. Exiting function!")
            x = 0
    else:
        print("Invalid username. Exiting function!")
        x = 0
    x = -1
    while x == -1:
        print("What would you like to do?")
        print("1. Add location\n2. Add hospital\n3. Delete an entry\n4. Display a table\n5. Run an SQL statement")
        temp = int(input())
        if temp == 1:
            #ADD LOCATION
            # WORKS.....
            print("Enter city:")
            city = input()
            print("Enter state:")
            state = input()
            print("Enter country:")
            country = input()
            print("Enter lockdown status")
            status = input()
            #SQL GOES HERE
            try:
                sql = _conn.execute("INSERT into Location VALUES ('"+str(city)+"', '"+str(country)+ "', '"+str(state)+"', '"+str(status)+"')")
                _conn.commit()

              
            except Error as e:
                print(e)


            #FINISHED MSG GOES HERE
        elif temp == 2:
            #ADD HOSPITAL
            #WORKS
            print("Enter hospital name:")
            name = input()
            print("Enter number of doctors with privelages at this hospital:")
            doctors = int(input())
            print("Enter number of patients at this hospital:")
            patients = int(input())
            print("Enter risk of visiting this hospital:")
            risk = int(input())
            print("Enter hospital address:")
            addr = input()
            print("Enter a general review of the hospital:")
            review = input()
            #SQL GOES HERE
            try:
                
                sql = _conn.execute("INSERT into Hospitals VALUES ('"+str(name)+"', '"+str(doctors)+ "', '"+str(patients)+"', '" +str(risk)+ "','"+str(addr)+"', '"+str(review)+"')")
                _conn.commit()

                
            except Error as e:
                print(e)


            #FINISHED MSG GOES HERE
        ############### Check??
        elif temp == 3:
            #DELETE TUPLE
            print("Enter table name:")
            tableName = input()
          #  print("Enter column you would like to use for a key:")
          #  col = input()
           # print("Enter key value:")
           # key = int(input())
            #SQL GOES HERE
            try:

                if tableName in ('Person'):
                    print("Enter person's case ID:")
                    caseID = input()
                #    print("Enter your full name:")
                #    name = input()
                #    print("Enter your address")
                #    address = input()
                 #   print("Enter your date of birth:")
                 #   dob = input()
                  #  print("Enter your comments:")
                  #  comment = input()
                  #  sql = _conn.execute("DELETE FROM Person where p_ID = ? and p_name = ? and p_address = ? and p_dob = ? and p_comment = ?",(caseID,name,address,dob,comment,))
                    sql = _conn.execute("DELETE FROM Person where p_ID = ?",(caseID,))
                    _conn.commit()
                    print("Person entry case deleted!")
                     

                elif tableName in ('Hospital'):
                    print("Enter Hospital name:")
                    name = input()
                    sql = _conn.execute("DELETE FROM NeedsHospital where h_name = ?",(name,))
                    _conn.commit()
                    print("Needs Hospital entry case deleted!")

                elif tableName in ('NeedsHospital'):
                    print("Enter Hospital case ID:")
                    caseID = input()
                    sql = _conn.execute("DELETE FROM NeedsHospital where nh_caseID = ?",(caseID,))
                    _conn.commit()
                    print("Needs Hospital entry case deleted!")
                
                elif tableName in ('Outcome'):
                    print("Enter Outcome case ID:")
                    caseID = input()
                    sql = _conn.execute("DELETE FROM Outcome where o_caseID = ?",(caseID,))
                    _conn.commit()
                    print("Outcome entry case deleted!")
                
                elif tableName in ('Results'):
                    print("Enter result's case ID:")
                    caseID = input()
                    sql = _conn.execute("DELETE FROM Results where r_caseID = ?",(caseID,))
                    _conn.commit()
                    print("Result entry case deleted!")
                
                elif tableName in ('Symptoms'):
                    print("Enter symptom case ID:")
                    caseID = input()
                    sql = _conn.execute("DELETE FROM Symptoms where s_caseID = ?",(caseID,))
                    _conn.commit()
                    print("Symptom entry case deleted!")
                
                elif tableName in ('TestingAvailability'):
                    print("Enter testing case ID:")
                    caseID = input()
                    sql = _conn.execute("DELETE FROM TestingAvailability where ta_personID = ?",(caseID,))
                    _conn.commit()
                    print("Availability entry case deleted!")

                
            except Error as e:
                print(e)
                    
        
            #FINISHED MSG GOES HERE
            print("")
        elif temp == 4:
            #DISPLAY FULL TABLE
            print("Enter table you would like to view:")
            tableName = input()
            #SQL GOES HERE
            try:
                if tableName in ('Hospitals', 'Location', 'Symptoms', 'Testing', 'NeedsHospital', 'Outcome', 'Person', 'Results', 'TestingAvailability'):
                    sql = _conn.execute("SELECT * FROM " + tableName)
                    print("Printing " + tableName + " table:")
                    for i in sql:
                        print(i)

               
                
            except Error as e:
                print(e)

        elif temp == 5:
            #INSERT NEW SQL STATEMENT
            print("Enter SQL statement:")
            statement = input()
            #SQL GOES HERE
            sql = _conn.execute('"' + statement + '"')
            _conn.commit()

            #FINISHED MSG GOES HERE
            print("")
      
        else:
            print("---Invalid Entry!---")
            print("Would you like to try again?")
            print("1. YES\n2. NO")
            temp = int(input())
            if temp == 1:
                x = -1
            else:
                x = 0
        print("Would you like to look around some more?")
        print("1. YES\n2. NO")
        temp = int(input())
        if temp == 1:
            x = -1
        else:
            x = 0



#--- SHOULD GO IN MAIN ---

def main():

    database = r"phase2.db"
    conn = openConnection(database)

x = 0
while x != -1:
    
    y = -1
    while y == -1:
    
        print("Are you a doctor, patient or visitor?")
        print("Enter the number to access the menu")
        print("1. Patient\n2. Doctor\n3. Visitor\n4. Administrator")
        database = r"phase2.db"
        conn = openConnection(database)
        y = int(input())
    with conn:
        if y == 1:
            #call patient function
            patient(conn)
        elif y == 2:
            #call doctor function
            doctor(conn)
        elif y == 3:
            #call visitor function
            visitor(conn)
        elif y == 4:
            #call admin function
            admin(conn)
        else:
            print("---Invalid Entry!---")
            print("Would you like to try again?")
            print("1. YES\n2. NO")
            temp = int(input())
            if temp == 1:
                y = -1
            else:
                y = 0


    print("Would you like to Exit?\n1. YES\n2. NO")
    temp = int(input())
    if temp == 2:
        x = 0
    else:
        print("---Exiting---")
        x = -1
    closeConnection(conn,database)
#--- SHOULD GO IN MAIN ---
    
if __name__ == '__main__':
    main()

#---REMOVE ALL print("") STATEMENTS BEFORE TURN IN!!!---