from db import connect, listUsers, isUsernameExist, addUser, editUser, deleteUser, closeConnection

def setupDBConnection():
    connect()

def showAddUserPrompts():
    username = input('Username> ').rstrip()
    password = None
    fullname = None
    if isUsernameExist(username):
        return print('Error: user with username ' + username + ' already exists')
    else:
        password = input('Password> ').rstrip()
        fullname = input('Full Name> ').rstrip()
        addUser(username, password, fullname)

def showEditUserPrompts():
    username = input('Username to edit> ').rstrip()
    password = None
    fullname = None
    if isUsernameExist(username):
        password = input('New password (press enter to keep current)> ').rstrip()
        fullname = input('New full name (press enter to keep current)> ').rstrip()
        editUser(username, password, fullname)
    else:
        return print('No such user.')

def isPositiveConfirmation(confirmation):
    formattedConfirmation = confirmation.lower()
    if confirmation == 'yes' or confirmation == 'y':
        return True
    return False

def showDeleteUserPrompts():
    username = input('Enter username to delete> ').rstrip()
    if isUsernameExist(username):
        confirmation = input('Are you sure that you want to delete '+ username + '?'+ '(Yes/No) ').rstrip()
        if isPositiveConfirmation(confirmation):
            deleteUser(username)
            print('Deleted')
    else:
        return print('No such user.')

def exitProgram():
    print('Bye.')
    closeConnection()

def showMenu():
    print('1)   List Users')
    print('2)   Add User')
    print('3)   Edit User')
    print('4)   Delete Users')
    print('5)   Quit')
    selection = input('Enter command> ').rstrip()

    if selection == '1' :
        listUsers()
    elif selection == '2':
        showAddUserPrompts()
    elif selection == '3':
        showEditUserPrompts()
    elif selection == '4':
        showDeleteUserPrompts()
    elif selection == '5':
        return exitProgram()
    else:
        print('Invalid entry! Please try again')
    showMenu()

def main():
    setupDBConnection()
    showMenu()

if __name__ == '__main__':
    main()
