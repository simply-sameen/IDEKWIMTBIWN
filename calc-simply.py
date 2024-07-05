#IDEKWIMTBIWN v1.0
#I Don't Even Know Why I Made This, But It Works Nonetheless
#by Simply

#This started as a calculator program for my Python Add-On course
#Provided to me by my college, but I know I'm too good for it
#So I added function by function, until I created this unwanted
#Pile of code-junk

#v1.2
#Added a menu system to move between calculator and newly added
#Palindrome finder, which checks whether given string is the
#same when reversed

#v1.3
#Changed all loops to be definite with a set value
#Default value 20
#This is to prevent input or syntax errors causing,
#Infinite print statements and thus crashing the console

#v1.4 ~ first version added to git
#Added binary encoded account login
#Used to login to the program, this is still being developed
#Use this given details to add or view the stored accounts
#Username:simply    Password:123456

#v1.5
#Added history.txt to file list, which stores all important
#Function accesses such as rpass(), calc(), adduser(), pal()
#etc, along with timestamp and user
#All file instances are closed within 10 lines of code
#whenever possible

#v1.6
#Added ANSI Color sequences to all text being printed
#Added placeholders for colors for easier implementation


#---------------------------------------------------------------------


from datetime import datetime       #module to find current system time

lim=20      #Global Limit for all FOR loops

#placeholders for ANSI Colors
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
RESET = '\033[0m'
#end of color placeholders


def b2s(con1):       #function to convert binary to string
#funtion body start-----------------------
    chars = [con1[i:i+8] for i in range(0, len(con1), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)
#function body end-----------------------


def s2b(con2):       #function to convert string to binary
#funtion body start-----------------------
    return ''.join(format(ord(char),'08b')for char in con2)
#function body end-----------------------


def pal():      #function to check for palindrome
#function body start---------------------
    try:
        file2=open("history.txt","a")
        tim=str(datetime.now())
        str1=input("Palindrome Checker\n\nEnter String to check: ")     #input string into str1 
        if str1==str1[::-1]:        #check if reverse of given string is equal to original
            print("The given string "+GREEN+"IS"+RESET+" a Palindrome")
        else:
            print("The given string "+RED+"IS NOT"+RESET+" a Palindrome")
        file2.write(f"{tim}: {user} used Palindrome Checker with: {str1}\n")
        file2.close()
    except:     #exception handling for all cases
        print("There has been some "+RED+"error"+RESET)
#function body end-----------------------





def cond():  # function for condition checker
# function body start---------------------
    try:
        ch = int(input("\nDo you want to continue?"+GREEN+"\nYes:1"+RED+"\nNo:0\n: "+RESET))
        if ch == 0:
            return False  # indicate to terminate program
        else:
            return True  # continue program to next line of function call
    except:
        print("Invalid input, "+RED+"assuming No"+RESET)
        return False  # terminate program on invalid input
# function body end-----------------------


def calc():    #function for calculator
# function body start---------------------
    tim=str(datetime.now())     #find current time
    file2=open("history.txt","a")
    num1=float(input("\nEnter "+BRIGHT_MAGENTA+"First"+RESET+" Number: "))
    num2=float(input("Enter "+BRIGHT_MAGENTA+"Second"+RESET+" Number: "))
    if num2==0:   #check if second number is zero
        print("Second Number can't be Zero, Retry")
        cond()
    else:
        print("Sum        :",num1+num2)
        print("Difference :",num1-num2)
        print("Product    :",num1*num2)
        print("Quotient   :",num1/num2)
        print("Remainder  :",num1%num2)
        file2.write(f"{tim}: {user} used Calculator with {num1} and {num2}\n")      #appends calculatr usage to history
        file2.close()
# function body end-----------------------


def rhis():      #function to read history
# function body start---------------------
    tim=str(datetime.now())     #find current system time
    file2=open("history.txt","a")       #file opened to append history access
    file2.write(f"{tim}: {user} viewed History\n")      #appends history access
    file2=open("history.txt","r")
    lines = file2.readlines()       #reads all the lines in the file
    for line in lines:      #iterating through each line of the file
        print(line,end="")
    file2.close()
# function body end-----------------------



def simply():    #function for main body
#function body start-----------------------
    for i in range(lim):    #definite loop to prevent crash
        tim=str(datetime.now())
        print(BRIGHT_CYAN+"\nIDEKWIMTBIWN v1.4"+RESET+"\nWelcome ",user,"\nTime: ",tim,"\n-------------------------------------\n")
        ch2=int(input("1.Palindrome Check\n2.Simple Calculation\n3.List Addition\n4.List Sorting\n0.Logout"+GREEN+"\n:   "+RESET))
        if ch2==1:
            pal()       #calls palindrome fucntion
            continue
        elif ch2==2:
            calc()      #calls simple calculation
            continue
        else:
            print(GREEN+"\nLogging Out\n"+RESET)
            break
#function body end----------------------- 
       

def login():    #function for login
#funtion body start-----------------------
    global user     #global to allow simply() to read username
    file2=open("history.txt","a")   #opens file in append mode
    tim=str(datetime.now())     #find current time
    for i in range(lim):    #definite loop to prevent crash
        try:
            y=input("\nEnter Username : ")  #line to receive input as string
            x=input("Enter Password : ")    #line to receive input as integer
            file1=open("pass.txt","r")      #opens file in read mode
            lines = file1.readlines()       #reads all the lines in the file
            for line in lines:      #iterating through each line of the file
                binuser, binpass = line.strip().split(',')      #splits the line into user and pass by comma seperator
                usr = b2s(binuser)       #convert binary to string
                pas = b2s(binpass)
                if y==usr:      #checks if username is in database
                    if x==pas:      #checks is password is correct  
                        print(GREEN+"Login Successful"+RESET)
                        file1.close()       #closing file pointer
                        user=usr        #updating global variable
                        file2.write(f"{tim}: {user} logged in\n")       #append to history
                        file2.close()       #closing file pointer
                        return True     #returns TRUE when login successful
                    else:
                        print("\nUsername or Password "+RED+"incorrect"+RESET)
                        if not cond():      #calls condition 
                            continue        #retry login 
            print("\nUsername "+RED+"NOT"+RESET+" Found in Database")
            return False        #returns FALSE when login un-successful        
        except:
            print("\nThere has been some "+RED+"issue"+RESET)  # exception for all cases
            file1.close()       #close file pointer nevertheless
            file2.close()       #close file pointer nevertheless
            return False        #returns FALSE when login un-successful        
#unction body end-----------------------


def rpass():     #function to read stored user data
#funtion body start-----------------------
    file1=open("pass.txt","r")      #opens file in read mode
    file2=open("history.txt","a")   #opens file in read mode
    tim=str(datetime.now())
    lines = file1.readlines()       #reads all the lines in the file
    file2.write(f"{tim}: {user} read all the stored passwords\n")
    for line in lines:      #iterating through each line of the file
        binuser, binpass = line.strip().split(',')      #splits the line into user and pass by comma seperator
        usr = b2s(binuser)       #convert binary to string
        pas = b2s(binpass)       #convert binary to string
        print("\nUsername: ", usr,"\nPassword: ",pas)
    file1.close()       #closing file pointer
    file2.close()       #closing file pointer
#function body end-----------------------
 

def adduser():      #fucntion to add a user to  the password list
#funtion body start-----------------------
    for i in range(lim):        #definite list to avoid crashes
        try:
            inp1=input("\nTo "+YELLOW+"ADD"+RESET+" a New User\n\nEnter the Username: ")      #recieve username
            inp2=input("Enter the Password: ")     #recieve password
            print("Before Commit, is this what you wanted:\nUsername: ",inp1,"\nPassword: ",inp2,"\n")
            ch3=int(input("If Yes:1 or No:2 or Cancel:3\n: "))
            if ch3==1:      #checks if the entered value is what user wanted
                file1=open("pass.txt","a")      #opens the file in append mode
                file2=open("history.txt","a")   #opens the file in append mode
                tim=str(datetime.now())     #find current time
                bin1=s2b(inp1)       #converts username to binary using function
                bin2=s2b(inp2)       #converts password to binary using function
                file1.write(f"{bin1},{bin2}\n")     #writes both binary seperated by comma, and moves cursor to new line
                file2.write(f"{tim}: {user} added new user, Username: {inp1}\n")
                print("Done")
                file1.close()       #close file
                file2.close()       #close file
                break     #terminates function
            elif ch3==2:
                continue        #allows user to change input
            else:
                break       #cancel adduser() operation
        except:     #exception for password not being integer
            print("There has been some "+RED+"error"+RESET)
            continue
#function body end-----------------------


#----------------------------------------------


print(BRIGHT_CYAN+"\nIDEKWIMTBIWN v1.4"+RESET)
global tim      #global variable to access current system time
for i in range(lim):
    try:
        ch4=int(input("\n1.Login\n2.Add User\n3.Read Accounts\n4.Read History\n0.Exit\n"+GREEN+": "+RESET))
        if ch4==1:
            if login():
                simply()        #calls main function
                continue
            else:
                print(RED+"Login Unsuccesful"+RESET)
                continue
        elif ch4==2:
            print("\nFirstly, Login with "+YELLOW+"existing username\n"+RESET)
            if login():
                adduser()       #calling function to add a user
                continue
            else:
                print(RED+"Login Unsuccesful"+RESET)
                continue
        elif ch4==3:
            print("\nFirstly, Login with "+YELLOW+"existing username\n"+RESET)
            if login():
                rpass()      #calling fucntion to read contents of pass.txt
                continue
            else:
                print(RED+"Login Unsuccesful"+RESET)
                continue
        elif ch4==4:
            print("\nFirstly, Login with "+YELLOW+"existing username\n"+RESET)
            if login():
                rhis()       #calling function to read contents of history.txt
                continue
            else:
                print(RED+"Login Unsuccesful"+RESET)
                continue
        else:
            break       #program terminates
    except:
        print("There Has Been Some Input Error,"+RED+" Retry"+RESET)
        continue

print(GREEN+"\nTerminating all current Processes\n\n"+RESET+"----------------------\n")


#end of code
#by Simply      https://simplysameen.netlify.app
