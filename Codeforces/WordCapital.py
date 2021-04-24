word = input()

wordC=word[0].upper()

for i in range(1,len(word)):
    wordC+=word[i]
    
    
print(wordC)
