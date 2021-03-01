import moduleA
#import custom_module as cm

#print("Second module's name: {}".format(__name__))

#after adding if in moduleA:
print("Second module's name: {}".format(__name__))


moduleA.mm()
#cm.working()