def longestcombo(a1,a2):
  x=[]
  for i in a1:
      for j in a2:
        if i not in x:
            x.append(i)
        if j not in x:
            x.append(j)
        
  x.sort()
  return ("".join(x))


#a1="ifvheieuheingeuhgnei"
a1=input()
#a2="fivgunhigdubhvg"
a2=input()
print(longestcombo(a1,a2))
