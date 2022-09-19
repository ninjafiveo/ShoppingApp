import sekol_code as sc
from time import sleep

sc.CLEAR_CONSOLE()

def The_Answer():
    password = input("What is the answer to life, the universe and everything? ")

    if(password == '42'):
        print("Welcome wise one. I see you've traveled the Galaxy. Let's begin. ")
        sleep(2)
        sc.CLEAR_CONSOLE()
        Level_1()
    elif(password != "bob"):
        print("This is no time for jokes.")
    elif(password == "tom"):
        print("Ah yes. The funny cat that chases that mouse.")
    else:
        print("I see you are new. Go get more experience and come back.")

def Level_1():
    print("The man opens the door.")
    sleep(2)
    sc.CLEAR_CONSOLE()
    print("An old wizard approaches you.")
    sleep(2)
    sc.CLEAR_CONSOLE()
    begin_quest = input("Are you ready to begin your adventures? y/n: ")
    sleep(1)
    sc.CLEAR_CONSOLE()
    if(begin_quest == "y"):
        print("The adventure begins...")
    else:
        print("You're correct. Best if you go get some sleep.")

The_Answer()

