def print_statment(*bargs):
    arg1, arg2 = bargs
    print "%r,  %r" % (arg1, arg2)

print_statment("this", "that")

# smaller code for above
def print_statment2(arg1, arg2):
    print "%r, %r" % (arg1, arg2)

print_statment2("That", "This")
