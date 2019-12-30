# 2019/12/28
# Main python script
# Step 3: have a database to create and check existing users

import datetime
import ConditionMessages
import DataStorage
import os
import getpass

#Set variables
conPrompt   = False
setInput     = ""
#Set to false once database is created
inDataBase  = True
correctInfo = True
saveInfo    = ""
newInfo     = True
cmd         = True
currentTime = datetime.datetime.now()
user        = ConditionMessages.usermessages()
prgm        = ConditionMessages.appmessages()
db          = DataStorage.datastorage()


#I should add this into every class? Or simply whenever I need to clear the page
def clearScreen():
    os.system('clearScreen' if os.name == 'nt' else 'clear')

# Read from the array containing user's personal information
def reviewUserInfo():
    # Clear terminal space
    clearScreen()

    # Flesh out this fn using below code
    user.helloMsg()

# Confirm information is correct
#    print("Are the following pieces of personal information you've provided correct?")
# while(...) that goes through an array with the individual's personal information
#    correctInfo = raw_input("Entre y/n to confirm or deny your personal information: ")

# Save information?
 #   saveInput = raw_input("Entre y/n to confirm or deny saving your personal information: ")
 #   if (saveInput == "y" or saveInput == "Y" or saveInput == "Yes"):
 #       print("Personal information confirmed save.")
 #       saveInfo = True
 #   else:
 #       print("Personal information denied save.")
 #       saveInfo = False


def setUserInfo():
    # Clear terminal space
    clearScreen()

    # Enter personal information
    dateOfBirth = raw_input("Enter your year of birth: ")
    jobType = raw_input("Enter your job type/position: ")
    favColour = raw_input("Enter your favourite colour: ")
    favFood = raw_input("Enter your favourite food: ")

    # Calculated personal information
    age = currentTime.year - int(dateOfBirth)

    while cmd:
        # Confirm personal information
        setInput = raw_input("Satisfied with your entered information? Y/N: ")
        if (setInput == "y" or setInput == "Y" or setInput == "Yes"):
            userPrompt()
            break
        elif (setInput == "n" or setInput == "N" or setInput == "No"):
            setUserInfo()
            break
        else:
            user.deniedCmdMsg()

def userPrompt():
    # Confirm with user to review personal information
    while cmd:
        setInput = raw_input("Review pre-existing personal information? Y/N: ")
        if (setInput == "y" or setInput == "Y" or setInput == "Yes"):
            reviewUserInfo()
            break
        elif(setInput == "n" or setInput == "N" or setInput == "No"):
            break
        else:
            user.deniedCmdMsg()

    # Confirm with user to edit their information
    while cmd:
        setInput = raw_input("Edit pre-existing personal information? Y/N: ")
        if (setInput == "y" or setInput == "Y" or setInput == "Yes"):
            setUserInfo()
            break
        elif(setInput == "n" or setInput == "N" or setInput == "No"):
            break
        else:
            user.deniedCmdMsg()

    # Confirm to close the app
    while cmd:
        setInput = raw_input("Close app.py or list options again? Y/N: ")
        if (setInput == "y" or setInput == "Y" or setInput == "Yes"):
            closeApp()
            break
        elif (setInput == "n" or setInput == "N" or setInput == "No"):
            userPrompt()
            break
        else:
            user.deniedCmdMsg()

def userCreate():

    # Confirm to create new user in database
    while cmd:
        setInput = raw_input("Create new user? Y/N: ")
        if (setInput == "y" or setInput == "Y" or setInput == "Yes"):
            clearScreen()
            setUserInfo()
            break
        elif(setInput == "n" or setInput == "N" or setInput == "No"):
            break
        else:
            user.deniedCmdMsg()

    # Confirm that user already is in database but may have entered incorrect information
    while cmd:
        setInput = raw_input("Already a pre-existing user? Y/N ")
        if (setInput == "y" or setInput == "Y" or setInput == "Yes"):
            # Clear terminal screen
            clearScreen()
            userActive()
            break
        elif (setInput == "n" or setInput == "N" or setInput == "No"):
            userCreate()
            break
        else:
            user.deniedCmdMsg()

def userActive():
    # Prompt user
    name = raw_input("Name: ")
    nopass = getpass.getpass()

    # Store personal information into some sort of database or txt file
    # inDataBase = db.confirmUser(name,password)
    if (inDataBase):
        prgm.availableUser(name)
        user.acceptedAccessMsg()
        user.acceptedEntryMsg(name)
        userPrompt()
    else:
        prgm.unvailableUser()
        user.deniedEntryMsg()
        # Create user in database
        userCreate()

def startApp():
    #Open app.py
    print("Starting app.py...")
    print("-" * 100)
    print("")

    # Prompt for input by user
    userActive()

def closeApp():
    #No longer prompt user
    conPrompt = False

    #Closing app.py
    print("")
    print("-" * 100)
    print("Closing app.py...")

# Clear terminal screen
clearScreen()
# Start app
startApp()