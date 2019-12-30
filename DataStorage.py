# 2019/12/29
# Data base storage logic for personal information
#

# Database functions (Will have to redo for appropriate functions
class datastorage:

    def helloMsg(self):
        print("I'm over here in UserInteraction!")

    def acceptedEntryMsg(self, userName):
        print("Welcome " + userName + ".")

    def failedEntryMsg(self):
        print("Invalid entry...")

    def deniedAccessMsg(self):
        print("Access denied.")

    def acceptedAccessMsg(self):
        print("Access accepted.")