#print (__name__)

#print("first module name is: {}".format(__name__))

print("Outside if statement")

if __name__ == '__main__':
    # print("First module's name: {}".format(__name__))
    print("Run directly") 
    # true only if this file is itself run and not as an import
    # in another file where it's __name__ will be "moduleA not __main__"

else:
    print("Run from import")

#funtions from moduleA can be called by moduleB after import
#even if inside if __name__...

def mm():
    print("Running function of moduleA")