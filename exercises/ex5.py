# Variables for code to follow
name = 'Andrew T. James'
age = 35 # not a lie
height = 72 # inches
weight = 230 # lbs
kgs = weight / 2.2046
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

# print statments from variables above
print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d years old" % age
print "He's %d kilograms heavy." % kgs
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, tyr to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
