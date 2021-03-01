def welcome():
    print("Welcome to ModuleA...")

    print("Import done, called functions:\n#1 Name\n#2 Age\n#3 College")


def working():
    welcome()
    
    s=int(input())
    if s == 1:
        print("Binayak Bishnu")
    
    elif s==2:
        print("18")
    
    elif s==3:
        print("Vellore Institute of Technology")

    else:
        print("Error")


if __name__ == '__main__':
    print("In module file")
    working()

else:
    print("need to call 'working' function from custom_module")