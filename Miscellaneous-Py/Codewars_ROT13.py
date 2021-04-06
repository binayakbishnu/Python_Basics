def rot13(message):
    L=[]
    for i in message:
        L.append(i)
    print(L)
    
    for i in range(len(L)):
        if L[i].isalpha():
            if L[i].isupper():
                if ord(L[i])+13>90:
                    L[i] = chr(64+(13-(90-ord(L[i]))))
                else:
                    L[i] = chr(ord(L[i])+13)
            elif L[i].islower():
                if ord(L[i])+13>122:
                    L[i] = chr(96+(13-(122-ord(L[i]))))
                else:
                    L[i] = chr(ord(L[i])+13)
    
    message =  "".join(L)
    return message
