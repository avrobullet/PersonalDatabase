import os
# File class to confirm that userdata.txt exists

# Linked list node to store user information while app is active
class Node:
    def __init__(self, userdata=None, next_node=None):
        self.username = userdata.name
        self.userpassword = userdata.password
        self.next_node = next_node
# Confirms which users have access to the database
class Users:
    def __init__(self, head=None):
        self.head = head
        self.node_amount = 1
        self.getUsers()
        # Retrieve existing users
        print("Retrieving users...")
        # First confirm that the userdata.txt exists
        #try:hm
            #filename = os.getDirectory(this_project/userdata)
            #file = FileLocation.checkLocation(filename, filename_location)
            #while lines_file_present:
                #userdata_file(get_data)
        #except FileNotFound:
            #print("No user data found. Need admin key to create new userdata file")
    # Check eligible users
    def checkUser(self, new_userdata):
        current = self.head
        while current:
            if current.username == new_userdata[0] and current.userpassword == new_userdata[1]:
                print("User found...")
                # Return boolean to continue with user's access to the app
                #return boolean
            else:
                current = current.next_node
    # Create users
    def createUser(self):
        print("Creating account for ", this.name, ".")
        #write_in_a_file(this.name, this.passowrd)
    # Delete user and their data
    #def deleteUser
    # Edit user data
    #def editUser
# Command function to determine what user wants to do
def confirmUser(command, new_userdata):
    if command:
        user = Users()
        # Determine if new user is existing user
        # return user.checkUser(new_userdata)
        user.checkUser(new_userdata)
