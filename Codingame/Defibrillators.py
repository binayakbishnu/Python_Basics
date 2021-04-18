import sys
import math

lon = input()
lat = input()
lon=lon.split(',')
lon=float('.'.join(lon))
lat=lat.split(',')
lat=float('.'.join(lat))
n = int(input())
s=""
L=[]
L2=[]
for i in range(n):
    defib = input().split(';')
    l=len(defib)
    # print(defib[l-1],defib[l-2])
    defib[l-1]=defib[l-1].split(',')
    defib[l-1]=float('.'.join(defib[l-1]))
    defib[l-2]=defib[l-2].split(',')
    defib[l-2]=float('.'.join(defib[l-2]))
    # print(defib[l-1],defib[l-2])
    x = (abs(defib[l-2]-lon))*math.cos((defib[l-1]+lat)/2)
    # print(x)
    y = abs(defib[l-1]-lat)
    # print(y)
    d = 6371 * (x**2 + y**2)**0.5
    # print(d)
    L.append(d)
    L2.append(defib[1])


# print(L)

x=L.index(min(L))
# print(x)
print(L2[x])
