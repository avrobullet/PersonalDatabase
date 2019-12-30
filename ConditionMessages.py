# 2019/12/29
# Python script that responds to user and program actions and respond in kind
#

# State messages prompted by the user
class usermessages:

    def helloMsg(self):
        print("I'm over here in UserInteraction!")

    def acceptedEntryMsg(self, userName):
        print("Welcome " + userName + ".")

    def deniedEntryMsg(self):
        print("Invalid entry...")

    def acceptedCmdMsg(self):
        print("Valid command entered.")

    def deniedCmdMsg(self):
        print("Unvalid command entered...")

    def acceptedAccessMsg(self):
        print("Access accepted.")

    def deniedAccessMsg(self):
        print("Access denied...")

# State messages prompted by the program (Will need to redo for appropriate messages)
class appmessages:

    def availableUser(self, userName):
        print("User found under name " + userName + ".")

    def unvailableUser(self, userName):
        print("No user found under name " + userName + "...")

    def availableInfo(self, userName):
        print("Information found for " + userName + ".")

    def unvailableInfo(self, userName):
        print("Information missing for " + userName + "...")