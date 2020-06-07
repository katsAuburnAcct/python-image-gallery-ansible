import psycopg2

db_host = "development-db.c4xkuoec7dni.us-east-2.rds.amazonaws.com"
db_name = "image_gallery"
db_user = "image_gallery"

# Notice that this file location is not part of the git repo
password_file = "/home/ec2-user/.image_gallery_config"

connection = None

def get_password():
    f = open(password_file, "r")
    result = f.readline()
    f.close()
    # remove the new line at the end of the line
    return result[:-1]

# Maintain a single connection to our db
def connect():
    global connection
    #DO NOT commit the password here, since it'll be pushed up to github!
    connection = psycopg2.connect(host=db_host, dbname=db_name, user=db_user, password=get_password())

#allows user to execute their query. Returns a cursor
def execute(query, args=None):
    cursor = connection.cursor()
    if not args:
        cursor.execute(query)
    else:
        cursor.execute(query, args)
    return cursor

def listUsers():
    #see all users
    res = execute('select * from users;')
    for row in res:
        print(row)

def isUsernameExist(username):
    res = execute("select count(username) from users where username=%s;", (username,))
    countRow = res.fetchone()
    return int(countRow[0]) > 0

def addUser(username, password, fullname):
    res = execute("insert into users(username, password, full_name) values (%s,%s,%s);", (username, password, fullname))
    connection.commit()

def editUser(username, newPassword, newFullname):
    if newPassword and newFullname:
        res = execute("update users set password=%s, full_name=%s where username=%s;", (newPassword, newFullname, username))
        connection.commit()
    elif not newPassword and newFullname:
        res = execute("update users set full_name=%s where username=%s;", (newFullname, username))
        connection.commit()
    elif newPassword and not newFullname:
        res = execute("update users set password=%s where username=%s;", (newPassword, username))
        connection.commit()
    else:
        return None

def deleteUser(username):
    res = execute("delete from users where username=%s;", (username,))
    connection.commit()

def closeConnection():
    connection.close()

