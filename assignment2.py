import sys
import os.path
import crypt


def getArguments():
   return sys.argv[1], sys.argv[2]


def openFile(filename):
   if os.path.isfile(filename):
      if os.access(filename, os.R_OK):
         return open(filename, 'r')
      else:
         sys.exit("Error: You do not have permission to access this file.")
   else:
      sys.exit("Error: File Does Not Exist.")


def getHashedPassword(username, shadow):
   for line in shadow:
      line = line.split(":")

      if line[0] == username:
         if line[1] == "*":
            sys.exit("Warning: User Does Not Have A Password.")
         else:
            return line[1]
   sys.exit("Warning: User Does Not Exist.")


def crackPassword(hash, dictPath, ctype, salt):
   insalt = '${}${}$'.format(ctype, salt)

   dict = openFile(dictPath)

   for password in dict:
      if crypt.crypt(password.strip(), insalt) == hash:
         sys.exit("Success: Password is " + password)
   sys.exit("Warning: Password Not Found In Dictionary.")




### MAIN SCRIPT ###

if len(sys.argv) < 3:
   sys.exit("Error: Invalid Arguments.")
else:
   # GET REQUIRED ARGUMENTS
   username, shadowfile = getArguments()

   # SELECT DICTIONARY FILE
   dictPath = "./dict.txt"

   if len(sys.argv) > 3:
      if sys.argv[3] == "-d" and len(sys.argv) > 4:
         dictPath = sys.argv[4]
      else:
         sys.exit("Error: Invalid Arguments.")


   # OPEN SHADOW FILE AND GET HASHED PASSWORD
   shadow = openFile(shadowfile)
   hash = getHashedPassword(username, shadow)
   enc = hash.split("$")

   # GET HASH PROPERTIES
   ctype = enc[1]
   salt = enc[2]
   insalt = '${}${}$'.format(ctype, salt)

   # CRACK THE PASSWORD
   crackPassword(hash, dictPath, ctype, salt)
