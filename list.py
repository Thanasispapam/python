import argparse
import sys
import os
import re

parser = argparse.ArgumentParser(description='Something')

parser.add_argument('-a', '--action', type=str, help='The action to perform', required=True,
    choices=["create", "delete", "list", "read"], dest="action", action="store")
parser.add_argument('-i', '--id', type=int, help='The id of the user', required=False, dest="Id", action="store")
parser.add_argument('-e', '--email', type=str, help='The email of the user', required=False, dest="email", action="store")
parser.add_argument('-f', '--first-name', type=str, help='The first name of the user', required=False, dest="firstName", action="store")
parser.add_argument('-l', '--last-name', type=str, help='The last name of the user', required=False, dest="lastName", action="store")
parser.add_argument('--file', type=str, help='The name of the file', required=False, default='list.txt', dest="file", action="store")
args = parser.parse_args()


# Util methods for reading file
def getLinePart(line, part):

    m = re.search('^(.*):(.*):(.*):(.*)$', line)
    if m:
        return m.group(part)
    else:
        return None

def getId(line):
    return getLinePart(line, 1)

def getEmail(line):
    return getLinePart(line, 2)

def getFirstName(line):
    return getLinePart(line, 3)

def getLastName(line):
    return getLinePart(line, 4)

def printUser(line):
    line = line.strip()
    Id = getId(line)
    email = getEmail(line)
    firstName = getFirstName(line)
    lastName = getLastName(line)
    print "Id: %s\t" % Id, "Email: %s\t" % email, "First Name: %s\t" %firstName, "Last Name: %s\n" %lastName


def create(file, email, firstName, lastName):
    with open(file,"a")as f:
        lines_of_text=["%s:" % email,"%s:" % email,"%s:" % firstName,"%s\n" % lastName]
        f.writelines(lines_of_text)

    print ("Successfuly created user %s %s %s", email, firstName, lastName)

# Connect to database and create user

def delete(userId):
    print ("Deleted user with :")
    print "Id: %s" % userId

def list(file):
    with open("list.txt","r")as f:
        for line in f:
            printUser(line)
            
    

def read(userId):
    with open("list.txt","r")as f:
        for line in f:
            line = line.strip()
            Id = getId(line)
            if (userId == int(Id)):
                printUser(line)
                return
    
    print "User with id: %s not found\n" %userId






# MAIN CODE
if (os.path.isfile(args.file)):
    print ("file exists")
else:
    print ("does not exist will be created")


if (args.action == "create"):
    if (args.email == None or args.firstName == None or args.lastName == None):
        print ("Please check your arguments")
        sys.exit(1)

    create(args.file, args.email, args.firstName, args.lastName)

elif (args.action == "delete"):
    if (args.Id == None):
        print ("Please check your arguments")
        sys.exit(1)
        
    delete(args.Id)

elif (args.action == "list"):
    list("The list is")

else:
    if (args.Id==None):
        print ("Please check your arguments")
        sys.exit(1)
    read(args.Id)