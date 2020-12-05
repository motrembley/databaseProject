#!!! username for admin function is either "Morgan" OR "Fernando" and the password is "admin" !!!

def patient():
    print("---PATIENT FUNCTION---")
    x = -1
    while x == -1:
        print("What would you like to do?")
        print("1. Add your information\n2. Check your results\n3. Update your comment\n4. Find a nearby Hospital")
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



            #FINISHED MESSAGE GOES HERE



            x = 0
        elif temp == 2:
            #CHECK RESULTS
            print("Enter your name or case ID:")
            temp = input()
            if temp[0].isdigit():   #FOR CASE ID AS INPUT
                caseID = temp
                #SQL GOES HERE



                print("")
            else:                   #FOR NAME AS INPUT
                name = temp
                #SQL GOES HERE
                


            #DISPLAY GOES HERE



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



                print("")
            else:                   #FOR NAME AS INPUT
                name = temp
                #SQL GOES HERE


            #FINISHED MSG GOES HERE



            x = 0
        elif temp == 4:
            #FIND NEARBY HOSPITAL
            print("Enter your name or case ID:")
            temp = input()
            if temp[0].isdigit():   #FOR CASE ID AS INPUT
                caseID = temp
                #SQL GOES HERE



                print("")
            else:                   #FOR NAME AS INPUT
                name = temp
                #SQL GOES HERE
                


            #DISPLAY ADDRESS HERE



            #DISPLAY HOSPITAL HERE



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



def doctor():
    print("---DOCTOR FUNCTION---")
    x = -1
    while x == -1:
        print("What would you like to do?")
        print("1. Enter new case\n2. Update existing case\n3. Update patient symptoms\n4. Update a comment")
        temp = int(input())
        if temp == 1:
            #ENTER NEW CASE
            print("Enter patient name:")
            name = input()
            print("Enter type of test administered:")
            testType = input()
            givenTest = "YES"
            print("Enter any comments or concerns:")
            comment = input()
            #SQL GOES HERE



            #FINISHED MSG GOES HERE
            x = 0
        elif temp == 2:
            #UPDATE CASE
            print("Which table would you like to update?")
            print("1. Testing Availability\n2. Results\n3. Needs Hospital\n 4. Outcome")
            temp = int(input())
            if temp == 1:
                #TESTING AVAILABILITY
                print("Enter patient name:")
                name = input()
                print("Enter type of test given:")
                testType = input()
                print("Enter any comments or concerns:")
                comment = input()
                #SQL GOES HERE



                #FINISHED MSG GOES HERE
                x = 0
            elif temp == 2:
                #RESULT
                print("Enter case ID")
                caseID = input()
                print("Enter date: (mm/dd/yyyy)")
                date = input()
                print("Enter result of test:")
                result = input()
                #SQL GOES HERE



                #FINISHED MSG GOES HERE
                x = 0
            elif temp == 3:
                #NEEDS HOSPITAL
                print("Enter case ID:")
                caseID = input()
                print("Enter ""YES"" if the patient is recomended to seek medical attention. Otherwise, enter ""NO"":")
                descision = input()
                #SQL GOES HERE



                #FINISHED MSG GOES HERE
                x = 0
            elif temp == 4:
                #OUTCOME
                print("Enter case ID:")
                caseID = input()
                print("Enter patient status:")
                status = input()
                #SQL GOES HERE



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



            #FINISHED MSG GOES HERE
            x = 0
        elif temp == 4:
            #UPDATE COMMENT
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



                #FINISHED MSG GOES HERE
                x = 0
            elif temp == 2:
                #OUTCOME
                print("Enter case ID:")
                caseID = int(input())
                print("Enter comment:")
                comment = input()
                #SQL GOES HERE



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



def visitor():
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



            #DISPLAY GOES HERE



            print("")
        elif temp == 2:
            #VIEW SYMPTOM STATS
            #SQL GOES HERE



            #DISPLAY GOES HERE



            print("")
        elif temp == 3:
            #BROWSE PUBLIC INFO
            print("Enter table you would like to view:")    #should probably include a list of tables
            tableName = input()
            #SQL GOES HERE



            #DISPLAY GOES HERE



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



def admin():
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
        print("1. Add location\n2. Add hospital\n3. Delete an entry\n4. Display a table\n5. Run an SQL statement\n6. Reset tables")
        temp = int(input())
        if temp == 1:
            #ADD LOCATION
            print("Enter city:")
            city = input()
            print("Enter state:")
            state = input()
            print("Enter country:")
            country = input()
            print("Enter lockdown status")
            status = input()
            #SQL GOES HERE



            #FINISHED MSG GOES HERE
            print("")
        elif temp == 2:
            #ADD HOSPITAL
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



            #FINISHED MSG GOES HERE
            print("")
        elif temp == 3:
            #DELETE TUPLE
            print("Enter table name:")
            tableName = input()
            print("Enter column you would like to use for a key:")
            col = input()
            print("Enter key value:")
            key = int(input())
            #SQL GOES HERE



            #FINISHED MSG GOES HERE
            print("")
        elif temp == 4:
            #DISPLAY FULL TABLE
            print("Enter table you would like to view:")
            tableName = input()
            #SQL GOES HERE



            #DISPLAY GOES HERE



            print("")
        elif temp == 5:
            #INSERT NEW SQL STATEMENT
            print("Enter SQL statement:")
            statement = input()
            #SQL GOES HERE



            #FINISHED MSG GOES HERE
            print("")
        elif temp == 6:
            #RESET TABLES
            #SQL GOES HERE



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
print("---WELCOME MEESAGE---")
x = 0
while x != -1:
    y = -1
    while y == -1:
        print("Are you a doctor, patient or visitor?")
        print("1. Patient\n2. Doctor\n3. Visitor\n4. Administrator")
        y = int(input())
        if y == 1:
            #call patient function
            patient()
        elif y == 2:
            #call doctor function
            doctor()
        elif y == 3:
            #call visitor function
            visitor()
        elif y == 4:
            #call admin function
            admin()
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
#--- SHOULD GO IN MAIN ---

#---REMOVE ALL print("") STATEMENTS BEFORE TURN IN!!!---