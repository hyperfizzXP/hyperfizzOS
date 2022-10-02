#Welcome to hyperfizzOS
#If you are reading this, hi!!!

#Import Libraries
from tkinter import messagebox
from datetime import datetime
from datetime import date
import time
import random
import os

Connected = False
TextFile1 = False
TextFile2 = False
TextFile3 = False

#Change Background Colour
if os.name == "nt":
    os.system("color 0f")

if os.name == "nt":
    Clear = os.system("cls")
else:
    Clear = os.system("clear")

#Starting Up
print("Starting Up")
time.sleep(1)
if os.name == "nt":
    Clear = os.system("cls")
else:
    Clear = os.system("clear")
print(".")
time.sleep(1)
if os.name == "nt":
    Clear = os.system("cls")
else:
    Clear = os.system("clear")
print(". .")
time.sleep(1)
if os.name == "nt":
    Clear = os.system("cls")
else:
    Clear = os.system("clear")
print(". . .")
time.sleep(1)
if os.name == "nt":
    Clear = os.system("cls")
else:
    Clear = os.system("clear")
print(". . . .")
time.sleep(1)
if os.name == "nt":
    Clear = os.system("cls")
else:
    Clear = os.system("clear")
print(". . . . .")
time.sleep(1)
if os.name == "nt":
    Clear = os.system("cls")
else:
    Clear = os.system("clear")

#Sign Up
Username = input("What would you like your username to be? ")
Password = input("What would you like your password to be? ")

if os.name == "nt":
    os.system("color 0a")

if os.name == "nt":
    Clear = os.system("cls")
else:
    Clear = os.system("clear")

#Log In
LogOut = False
LogIn = False
while LogIn == False:
    EnterPassword = input("Please enter your password: ")
    if EnterPassword == Password:
        if os.name == "nt":
            os.system("color 1f")
        LogIn = True
    else:
        print("The password is incorrect")
        time.sleep(1)
        LogIn = False

MainOS = True

#The Main OS
while MainOS == True:
    if os.name == "nt":
        Clear = os.system("cls")
    else:
        Clear = os.system("clear")
    print("Welcome,",Username)
    time.sleep(1)
    print("What would you like to do?")
    time.sleep(1)
    print("info, time, apps, games, settings, end session")
    time.sleep(1)
    UserChoice = input("Please enter your option (Use no punctuation or capital letters) ")

    #End Session
    if UserChoice == "end session":
        print("End Session?")
        EndSession = input("log off, shut down, cancel ")
        #Log Off
        if EndSession == "log off":
            print("Logging Off")
            time.sleep(1)
            if os.name == "nt":
                os.system("color 0a")
            if os.name == "nt":
                Clear = os.system("cls")
            else:
                Clear = os.system("clear")
            print("Hello",Username)
            LogOff = True
            while LogOff == True:
                LogInPassword = input("Please enter your password: ")
                if LogInPassword == Password:
                    if os.name == "nt":
                        os.system("color 1f")
                    LogOff = False
                    MainOS = True
                else:
                    print("The password is incorrect")
                    time.sleep(1)
                    LogOff = True
        #Shut Down
        elif EndSession == "shut down":
            print("Shutting Down")
            time.sleep(5)
            print("Bye :)")
            break
        elif EndSession == "cancel":
            MainOS = True
        else:
            print("That is not an option")
            time.sleep(1)
            MainOS = True

    #Settings
    elif UserChoice == "settings":
        print("")
        print("Please enter which settings you would like to change")
        Settings = input("user, internet ")
        #User Settings
        if Settings == "user":
            print("")
            print("Which would you like to change?")
            UserSettings = input("username, password ")
            if UserSettings == "username":
                EnterPassword = input("Please enter your password: ")
                if EnterPassword == Password:
                    Username = input("What would you like to change your username to? ")
                    MainOS = True
                else:
                    print("Password is incorrect")
                    time.sleep(1)
                    MainOS = True
            elif UserSettings == "password":
                EnterPassword = input("Please enter your current password: ")
                if EnterPassword == Password:
                    Password = input("What would you like to change your password to? ")
                else:
                    print("Password is incorrect")
                    time.sleep(1)
                    MainOS = True
        #Internet Settings
        elif Settings == "internet":
            print("")
            print("Let's establish a connection to the web!")
            EnterPassword = input("Please enter your password: ")
            if EnterPassword == Password:
                input("Press enter to connect to the internet ")
                time.sleep(2)
                print(".")
                time.sleep(3)
                print(".")
                time.sleep(2)
                print(".")
                time.sleep(4)
                Connected = True
                print("You are connected")
                time.sleep(1)
                input("Press enter to return home ")
                MainOS = True
            else:
                print("Password is incorrect")
                time.sleep(1)
                MainOS = True
        else:
            print("That is not an option")
            time.sleep(1)
            MainOS = True

    #Info
    elif UserChoice == "info":
        print("")
        print("hyperfizzOS Version 1.5.0")
        print("Created by hyperfizz XP")
        print("Made in Python")
        print("Subscribe to my YouTube channel at https://www.youtube.com/c/hyperfizzXP")
        print("Follow me on Twitter at https://twitter.com/hyperfizzXP")
        print("")
        time.sleep(1)
        input("Press enter to return home ")
        mainOS = True

    #Time
    elif UserChoice == "time":
        now = datetime.now()
        CurrentTime = now.strftime("%H:%M:%S")
        CurrentDate = date.today()
        print("")
        print("The current time is",CurrentTime)
        print("The current date is",CurrentDate)
        print("")
        time.sleep(1)
        input("Press enter to return home")
        mainOS = True

    #Apps
    elif UserChoice == "apps":
        print("")
        print("App List")
        print("file explorer, messagebox creator, keyboard tester, calculator, web browser, notepad, home")
        Application = input("Please enter the name of the application you would like to run (Use no punctuation or capital letters) ")
        print("")
        if Application == "home":
            MainOS = True
        #File Explorer
        elif Application == "file explorer":
            print("Welcome to the totally real files in hyperfizzOS.")
            time.sleep(1)
            print("Enter the name of a folder/file to open it.")
            time.sleep(1)
            print("Type anything else to return home.")
            time.sleep(1)
            print("Files:")
            FileExplorer = input("main drive ")
            if FileExplorer == "main drive":
                MainDriveFile = input("hyperfizzos ")
                if MainDriveFile == "hyperfizzos":
                    hyperfizzOSFile = input("hyperfizzxp, windows, totallynotvirus ")
                    if hyperfizzOSFile == "totallynotvirus":
                        TotallyNotVirus = input("goofyvirus.exe ")
                        if TotallyNotVirus == "goofyvirus.exe":
                            GoofyVirus = True
                            while GoofyVirus == True:
                                print("You have been virused by the goofy virus")
                                GoofyVirus = True
                    elif hyperfizzOSFile == "windows":
                        WindowsFile = input("windows sux.txt ")
                        if WindowsFile == "windows sux.txt":
                            print("")
                            print("Text File (Read Only)")
                            print("hyperfizz OS is better than Windows!!!")
                            time.sleep(1)
                            print("")
                            input("Press enter to return home ")
                        else:
                            print("Unknown File")
                            time.sleep(1)
                            MainOS = True
                    elif hyperfizzOSFile == "hyperfizzxp":
                        hyperfizzXPFile = input("system files, memes, bug report.txt ")
                        if hyperfizzXPFile == "bug report.txt":
                            print("")
                            print("Text File (Read Only)")
                            print("Woah, no bugs so far :)")
                            time.sleep(1)
                            print("")
                            input("Press enter to return home ")
                            MainOS = True
                        if hyperfizzXPFile == "memes":
                            MemesFile = input("therealfunny.txt ")
                            if MemesFile == "therealfunny.txt":
                                print("")
                                print("Text File (Read Only)")
                                print("*something funny*")
                                print("admit it, you laughed")
                                print("I know you did")
                                time.sleep(1)
                                print("")
                                input("Press enter to return home ")
                                MainOS = True
                        elif hyperfizzXPFile == "system files":
                            print("There are no files in this folder ¯\_(ツ)_/¯")
                            time.sleep(1)
                            input("Press enter to return home ")
                            MainOS = True
                    else:
                        print("Unknown File")
                        time.sleep(1)
                        MainOS = True
                else:
                    print("Unknown File")
                    time.sleep(1)
                    MainOS = True
            else:
                print("Unknown File")
                time.sleep(1)
                MainOS = True
        #Messagebox Creator
        elif Application == "messagebox creator":
            Header = input("What header would you like on your messagebox? ")
            MainBody = input("What would you like the main message to be on your messagebox? ")
            messagebox.showinfo(Header,MainBody)
        #Keyboard Tester
        elif Application == "keyboard tester":
            input("Type something here to test your keyboard: ")
            time.sleep(5)
            print("Yep! It works fine :)")
            time.sleep(1)
            print("")
            input("Press enter to go home ")
            MainOS = True
        elif Application == "home":
            print("Going home")
            time.sleep(1)
        elif Application == "calculator":
            print("")
            print("What operation would you like to do?")
            Calculator = input("addition, subtraction, multiplication, division ")
            if Calculator == "addition":
                CalculatorNumber1 = int(input("Please input your first number: "))
                CalculatorNumber2 = int(input("Please input your second number: "))
                CompletedCalculation = CalculatorNumber1 + CalculatorNumber2
                print(CalculatorNumber1,"+",CalculatorNumber2,"=",CompletedCalculation)
                print("")
                time.sleep(1)
                input("Press enter to return home ")
            elif Calculator == "subtraction":
                CalculatorNumber1 = int(input("Please input your first number: "))
                CalculatorNumber2 = int(input("Please input your second number: "))
                CompletedCalculation = CalculatorNumber1 - CalculatorNumber2
                print(CalculatorNumber1,"-",CalculatorNumber2,"=",CompletedCalculation)
                print("")
                time.sleep(1)
                input("Press enter to return home ")
            elif Calculator == "multiplication":
                CalculatorNumber1 = int(input("Please input your first number: "))
                CalculatorNumber2 = int(input("Please input your second number: "))
                CompletedCalculation = CalculatorNumber1 * CalculatorNumber2
                print(CalculatorNumber1,"x",CalculatorNumber2,"=",CompletedCalculation)
                print("")
                time.sleep(1)
                input("Press enter to return home ")
            elif Calculator == "division":
                CalculatorNumber1 = int(input("Please input your first number: "))
                CalculatorNumber2 = int(input("Please input your second number: "))
                CompletedCalculation = CalculatorNumber1 / CalculatorNumber2
                print(CalculatorNumber1,"÷",CalculatorNumber2,"=",CompletedCalculation)
                print("")
                time.sleep(1)
                input("Press enter to return home ")
            else:
                print("That's not an option")
                time.sleep(1)
        #Web Browser
        elif Application == "web browser":
            if Connected == True:
                print("Welcome to the internet")
                time.sleep(1)
                input("Please input a URL or search quiery: ")
                time.sleep(5)
                print("Unable to load webpage")
                print("Try getting better internet")
                time.sleep(1)
                print("")
                input("Press enter to return home ")
                MainOS = True
            else:
                print("")
                print("You are not connected to the internet.")
                time.sleep(1)
                print("Go to Settings to connect to the internet")
                time.sleep(1)
        #Notepad
        elif Application == "notepad":
            print("")
            print("Would you like to open an existing text file or create a new one?")
            print("You can create up to three text files")
            Notepad = input("open, new, cancel ")
            if Notepad == "new":
                if TextFile1 == False:
                    TextFile1 = input("Please type what you would like this text file to contain: ")
                    print("This file will be saved as 'file 1'")
                    time.sleep(1)
                    print("")
                    input("Press enter to return home ")
                    MainOS = True
                elif TextFile1 != False and TextFile2 == False:
                    TextFile2 = input("Please type what you would like this text file to contain: ")
                    print("This file will be saved as 'file 2'")
                    time.sleep(1)
                    print("")
                    input("Press enter to return home ")
                    MainOS = True
                elif TextFile1 != False and TextFile2 != False and TextFile3 == False:
                    TextFile3 = input("Please type what you would like this text file to contain: ")
                    print("This file will be saved as 'file 3'")
                    time.sleep(1)
                    print("")
                    input("Press enter to return home ")
                    MainOS = True
                else:
                    print("You have run out of available text files.")
                    time.sleep(1)
                    print("")
                    input("Press enter to return home ")
                    MainOS = True
            elif Notepad == "open":
                print("Which text file would you like to open?")
                OpenFile = input("file 1, file 2, file 3 ")
                if OpenFile == "file 1":
                    if TextFile1 == False:
                        print("This file does not exist")
                        time.sleep(1)
                        print("")
                        input("Press enter to return home ")
                        MainOS = True
                    else:
                        print("")
                        print("Text File")
                        print(TextFile1)
                        time.sleep(1)
                        print("")
                        input("Press enter to return home ")
                        MainOS = True
                elif OpenFile == "file 2":
                    if TextFile2 == False:
                        print("This file does not exist")
                        time.sleep(1)
                        print("")
                        input("Press enter to return home ")
                        MainOS = True
                    else:
                        print("")
                        print("Text File")
                        print(TextFile2)
                        time.sleep(1)
                        print("")
                        input("Press enter to return home ")
                        MainOS = True
                elif OpenFile == "file 3":
                    if TextFile2 == False:
                        print("This file does not exist")
                        time.sleep(1)
                        print("")
                        input("Press enter to return home ")
                        MainOS = True
                    else:
                        print("")
                        print("Text File")
                        print(TextFile3)
                        time.sleep(1)
                        print("")
                        input("Press enter to return home ")
                        MainOS = True
                else:
                    print("File not found")
                    time.sleep(1)
                    print("")
                    input("Press enter to return home ")
        else:
            print("That is not an option")

    #Games
    elif UserChoice == "games":
        print("")
        print("Game List")
        print("quiz, number guesser, home ")
        Game = input("Please enter your option (Use no puntuation or capital letters) ")
        print("")
        #Quiz
        if Game == "quiz":
            print("")
            print("Please answer questions using no puctuation or capital letters")
            QuizQuestion1 = input("What year did Windows XP release ")
            if QuizQuestion1 == "2001":
                print("You got it correct!!!")
                print("")
                time.sleep(1)
            else:
                print("That's incorrect >:(")
                time.sleep(1)
            QuizQuestion2 = input("Other than Steve Jobs and Steve Wozniak, who founded Apple? ")
            if QuizQuestion2 == "ronald wayne":
                print("Correct!")
                print("")
                time.sleep(1)
            else:
                print("Wrong!")
                print("")
                time.sleep(1)
            QuizQuestion3 = input("What is the name of the virtual dog that first appeared in Microsoft BOB in 1995? ")
            if QuizQuestion3 == "rover":
                print("Well done, you got it correct!!!")
                print("")
                time.sleep(1)
                input("Press enter to return home ")
            else:
                print("You didn't get it right :(")
                print("")
                time.sleep(1)
                input("Press enter to return home ")
        #Number Guesser
        elif Game == "number guesser":
            print("Hello, and welcome to the Number Guesser game!")
            time.sleep(1)
            print("So basically you just gotta guess the number between 1 and 100")
            time.sleep(1)
            RandomNumber = random.randint(1, 100)
            print("Ok, start guessing")
            Guess = True
            while Guess != False:
                Guess = int(input())
                if Guess == RandomNumber:
                    print("Well done, you got it correct!")
                    time.sleep(1)
                    Guess = False
                    MainOS = True
                elif Guess > RandomNumber:
                    print("Too high!")
                elif Guess < RandomNumber:
                    print("Too low!")
                else:
                    print("Invalid Number")
        elif Game == "home":
            print("Going Home")
            time.sleep(1)
        else:
            print("That is not an option.")
            time.sleep(1)
    else:
        print("That is not an option")
        time.sleep(1)
LogIn = False
