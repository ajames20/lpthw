#imprort and argv containing the arguments passed to the
#python interpreter when called from a command line.
from sys import argv
# names to be used for arguments by argv
script, filename = argv

# open filename

txt = open(filename)

#print statement and read the text

print "Here's your file %r:" % filename
print txt.read()

#print statement and file_again input from user in commmad line

print "Type the filename again:"
file_again = raw_input("> ")

#opens file

txt_again = open(file_again)

#prints files contents

print txt_again.read()
txt_again.close()
