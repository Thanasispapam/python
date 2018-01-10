import argparse
import sys
import os
import re
import users

parser = argparse.ArgumentParser(description='Something')

parser.add_argument('-a', '--action', type=str, help='The action to perform', required=True,choices=["create", "delete", "list", "read"], dest="action", action="store")
parser.add_argument('-i', '--id', type=int, help='The id of the user', required=False, dest="Id", action="store")
parser.add_argument('-e', '--email', type=str, help='The email of the user', required=False, dest="email", action="store")
parser.add_argument('-f', '--first-name', type=str, help='The first name of the user', required=False, dest="firstName", action="store")
parser.add_argument('-l', '--last-name', type=str, help='The last name of the user', required=False, dest="lastName", action="store")
parser.add_argument('--file', type=str, help='The name of the file', required=False, default='list.txt', dest="file", action="store")
args = parser.parse_args()

# MAIN CODE
if (os.path.isfile(args.file)):
    print ("file exists")
else:
    print ("does not exist will be created")

if (args.action == "create"):
    if (args.email == None or args.firstName == None or args.lastName == None):
        print ("Please check your arguments")
        sys.exit(1)

    users.create(args.file, args.email, args.firstName, args.lastName)

elif (args.action == "delete"):
    if (args.Id == None):
        print ("Please check your arguments")
        sys.exit(1)
        
    users.delete(args.file, args.Id)

elif (args.action == "list"):
    users.list(args.file)

else:
    if (args.Id==None):
        print ("Please check your arguments")
        sys.exit(1)
    users.read(args.file, args.Id)