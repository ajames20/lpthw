# import
from sys import argv

# arguments for argv
script, filename = argv

# print statments
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# input for user
raw_input("?")

# print statment and target for opening and naming file,  'w' allows for writing to a file
print "Opending the file..."
target = open(filename, 'w')

# print turncate statment and turncate file
print "Truncating the file.  Goodbye!"
target.truncate()

# print statment
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file"

target.write(line1,)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
