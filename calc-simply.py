#IDEKWIMTBIWN v1.4
#I Don't Even Know Why I Made This, But It Works Nonetheless
#by Simply

#This started as a calculator program for my Python Add-On course
#Provided to me by my college, but I know I'm too good for it
#So I added function by function, until I created this unwanted
#Pile of code-junk

#Basically, this program has a binary encoded account system
#Used to login to the program, this is still being developed
#Where I'll add a line or two here and there to add more
#Features down the line

#Use this given details to add or view the stored accounts
#Username:simply    Password:123456

#This is easily extendible and lots of blanks to be filled
#Just a little time pass program

lim=20      #Global Limit for all FOR loops

def bin2string(con1):       #function to convert binary to string
#funtion body start-----------------------
    chars = [con1[i:i+8] for i in range(0, len(con1), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)
#function body end-----------------------


def string2bin(con2):       #function to convert string to binary
#funtion body start-----------------------
    return ''.join(format(ord(char),'08b')for char in con2)
#function body end-----------------------


def pal():
#function body start---------------------
    try:
        str1=input("Palindrome Checker\n\nEnter String to check: ")     #input string into str1 
        if str1==str1[::-1]:        #check if reverse of given string is equal to original
            print("The given string IS a Palindrome")
        else:
            print("The given string IS NOT a Palindrome")
    except:     #exception handling for all cases
        print("There has been some error")
#function body end-----------------------


def cond():  # function for condition checker
# function body start---------------------
    try:
        ch = int(input("\nDo you want to continue?\nYes:1\nNo:0\n: "))
        if ch == 0:
            return False  # indicate to terminate program
        else:
            return True  # continue program to next line of function call
    except:
        print("Invalid input, assuming No")
        return False  # terminate program on invalid input
# function body end-----------------------


def calc():    #function for calculator
# function body start---------------------
    num1=float(input("\nEnter First Number: "))
    num2=float(input("Enter Second Number: "))
    if num2==0:   #check if second number is zero
        print("Second Number can't be Zero, Retry")
        cond()
    else:
        print("Sum        :",num1+num2)
        print("Difference :",num1-num2)
        print("Product    :",num1*num2)
        print("Quotient   :",num1/num2)
        print("Remainder  :",num1%num2)
# function body end-----------------------


def simply():    #function for main body
#function body start-----------------------
    for i in range(lim):    #definite loop to prevent crash 
        print("\nIDEKWIMTBIWN v1.4\nWelcome ",user,"\n-------------------------------------\n")
        ch2=int(input("1.Palindrome Check\n2.Simple Calculation\n3.List Addition\n4.List Sorting\n0.Logout:   "))
        if ch2==1:
            pal()       #calls palindrome fucntion
            continue
        elif ch2==2:
            calc()      #calls simple calculation
            continue
        else:
            print("\nLogging Out\n")
            break
#function body end----------------------- 
       

def login():    #function for login
#funtion body start-----------------------
    global user     #global variable to set username
    for i in range(lim):    #definite loop to prevent crash
        try:
            y=input("\nEnter Username : ")   #line to receive input as string
            x=input("Enter Password : ")   #line to receive input as integer
            file1=open("pass.txt","r")      #opens file in read mode
            lines = file1.readlines()       #reads all the lines in the file
            for line in lines:      #iterating through each line of the file
                binuser, binpass = line.strip().split(',')      #splits the line into user and pass by comma seperator
                usr = bin2string(binuser)       #convert binary to string
                pas = bin2string(binpass)
                if y==usr:
                    if x==pas:
                        print("Login Successful")
                        file1.close()
                        user=usr
                        return True
                    else:
                        print("\nUsername or Password incorrect")
                        if not cond():
                            continue
            print("\nUsername NOT Found in Database")
            return False
        except:
            print("\nThere has been some issue")  # exception for all cases
            file1.close()
            return False
#function body end-----------------------



def readpass():     #function to read stored user data
#funtion body start-----------------------
    file1=open("pass.txt","r")      #opens file in read mode
    lines = file1.readlines()       #reads all the lines in the file
    for line in lines:      #iterating through each line of the file
        binuser, binpass = line.strip().split(',')      #splits the line into user and pass by comma seperator
        usr = bin2string(binuser)       #convert binary to string
        pas = bin2string(binpass)
        print("\nUsername: ", usr,"\nPassword: ",pas)
    file1.close()
#function body end-----------------------
 

def adduser():      #fucntion to add a user to  the password list
#funtion body start-----------------------
    for i in range(lim):        #definite list to avoid crashes
        try:
            inp1=input("\nTo ADD a New User\n\nEnter the Username: ")      #recieve username
            inp2=input("Enter the Password: ")     #recieve password
            print("Before Commit, is this what you wanted:\nUsername: ",inp1,"\nPassword: ",inp2,"\n")
            ch3=int(input("If Yes:1 or No:2 or Cancel:3\n: "))
            if ch3==1:      #checks if the entered value is what user wanted
                file1=open("pass.txt","a")      #opens the file in append mode
                bin1=string2bin(inp1)       #converts username to binary using function
                bin2=string2bin(inp2)       #converts password to binary using function
                file1.write(f"{bin1},{bin2}\n")     #writes both binary seperated by comma, and moves cursor to new line
                print("Done")
                file1.close()
                break     #terminates function
            elif ch3==2:
                continue
            else:
                break
        except:     #exception for password not being integer
            print("There has been some error")
            continue
#function body end-----------------------


#----------------------------------------------


print("\nIDEKWIMTBIWN v1.4")    #first line interpreted
for i in range(lim):
    ch4=int(input("\n1.Login\n2.Add User\n3.Read pass.txt\n0.Exit\n:   "))
    if ch4==1:
        if login():
            simply()
            continue
        else:
            print("\nLogin Unsuccesful")
            continue
    elif ch4==2:
        print("\nFirstly, Login with existing username\n")
        if login():
            adduser()       #calling function to add a user
            continue
        else:
            print("Login Unsuccesful")
            continue
    elif ch4==3:
        print("\nFirstly, Login with existing username\n")
        if login():
            readpass()      #calling fucntion to read contents of pass.txt
            continue
        else:
            print("Login Unsuccesful")
            continue
    else:
        break       #program terminates

print("\nTerminating all current Processes\n\n----------------------\n")


#end of code
#by Simply