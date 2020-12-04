import numbers

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
        print("1. \n2. \n3. \n4. ")
        temp = int(input())
        if temp == 1:
            #ENTER NEW CASE
            
            x = 0
        elif temp == 2:
            #UPDATE CASE
            
            x = 0
        elif temp == 3:
            #UPDATE SYMPTOM

            x = 0
        elif temp == 4:
            #UPDATE COMMENT

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
        print("1. \n2. \n3. ")
        temp = int(input())
        if temp == 1:
            #CHECK LOCKDOWN STATUS

            print("")
        elif temp == 2:
            #VIEW SYMPTOM STATS
            
            print("")
        elif temp == 3:
            #BROWSE PUBLIC INFO

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
    x = -1
    while x == -1:
        print("What would you like to do?")
        print("1. \n2. \n3. \n4. \n5. \n6. ")
        temp = int(input())
        if temp == 1:
            #ADD LOCATION
            print("")
        elif temp == 2:
            #ADD HOSPITAL
            print("")
        elif temp == 3:
            #DELETE TUPLE
            print("")
        elif temp == 4:
            #DISPLAY FULL TABLE
            print("")
        elif temp == 5:
            #INSERT NEW SQL STATEMENT
            print("")
        elif temp == 6:
            #RESET TABLES
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