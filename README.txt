### RUNNING THE PROGRAM ###

Run the program using the following command

> python shadowcrack.py [username] [path of shadow file]


There is an optional parameter to specify the location of the dictionary file.

> python shadowcrack.py [username] [path of shadow file] -d [path of dictionary file]


If this option is not included, the program will use the default dictionary file named "dict.txt" located in the same folder as this file.

If any specified file is located in a protected folder such as '/etc/shadow', you may need to run the program with the 'sudo' command.

> sudo python shadowcrack.py [username] [path of shadow file]


### ERRORS ###

If you run the program with less than 2 parameters, or if you use the optional -d flag without specifying the path, the program will exit with an error for invalid arguments.
If any specified file does not exist, the program will exit with an error.
If you specify a file that you do not have permission to access, the program will exit with an error.


### WARNINGS ###

If the specified user does not exist, the program will quit with a warning.
If the user exists, but does not have a password, the program will quit with a warning.
If the user exists and has a password, but the password is not in the dictionary, the program will quit with a warning.

### TESTING ###

1) Create a new user using the linux shell using the following command.
> sudo adduser test

2) Give the user a password that you know is in the dictionary and follow the on-screen instructions.

3) Run the program using the following command. The password should be found.
> sudo python shadowcrack.py test /etc/shadow
