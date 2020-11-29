def patient():
    print("---PATIENT FUNCTION---")
    x = -1
    while x == -1:
        print("What would you like to do?")
        print("1. Enter your information\n2. check your results\n3. Find a nearby hospital")
        temp = int(input())
        if temp == 1:
            #Enter Information
            print("---Enter Info---")
            print("Enter your name:")
            name = input()
            print("Enter your address:")
            addr = input()
            print("Enter your date of birth(mm/dd/yyyy):")
            date = input()
            print("Any health complaints as of late?")
            comment = input()
            #---insert into person
            x = 0
        elif temp == 2:
            #Check Results
            print("---Check Results---")
            print("Do you know your case number?")
            print("1. YES\n2. NO")
            temp = int(input())
            if temp == 1:
                print("Enter your case number:")
                case = int(input())
                #---search DB for case and return result and print
            else:
                print("Enter your name:")
                name = input()
                #---search DB for name and return case result and print
            x = 0
        elif temp == 3:
            #Find Hospital
            print("---Find Hospital---")
            
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
        print("1. Enter new case\n2. Update existing Case")
        temp = int(input())
        if temp == 1:
            #Enter new case
            print("---Enter Case---")

            x = 0
        elif temp == 2:
            #Update existing Case
            print("---Update Case---")

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
        print("1. Browse public databases\n2. Check local lockdown status\n3. View statistics")
        temp = int(input())
        if temp == 1:
            #Browse Public Databases
            print("---Browse---")

            x = 0
        elif temp == 2:
            #Check Local Lockdown Status
            print("---Lockdown Status---")

            x = 0
        elif temp == 3:
            #View Statistics
            print("---View Stats---")

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
        print("Would you like to look around some more?")
        print("1. YES\n2. NO")
        temp = int(input())
        if temp == 1:
            x = -1
        else:
            x = 0
        


print("---WELCOME MEESAGE---")
x = 0
while x != -1:
    y = -1
    while y == -1:
        print("Are you a doctor, patient or visitor?")
        print("1. Patient\n2. Doctor\n3. Visitor")
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
