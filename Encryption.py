#!/bin/python3

import sys
import math


string = input().strip()
#string = "if man was meant to stay on the ground god would have given us roots"
no_str = string.replace(" ","")
#print(no_str)
length = len(no_str)
#print(length)
num = math.sqrt(length)
k = int(num)
if(k*k < length):
    row = k
    col = k+1
    if(row*col < length):
        col = col+1
        if(col > k+1):
            row = row+1
            col = col-1
else:
    row = k
    col = k
#print("row = "+ str(row))
#print("col = "+ str(col))
#i =0
#newstr = []
newstr = no_str[0:col]
#print(newstr)
#print(no_str)
i = 0
list = []
while i<len(no_str):
    newstr = no_str[i:col+i]
    i = i+col
    list.append(newstr)
#print(list)
j = 0
i=0
fin =[]
l =  len(list[len(list)-1])
if l<col:
    z = list[len(list)-1]+(" "*(col-l))
    list[len(list)-1] = z
while j<col:
    i =0
    lisr =""
    while i< row:
        lisr = lisr + list[i][j]
#   fin.append(list[i][j])
        i = i+1
    fin.append(lisr)
    j  = j+1
#print(fin)
for idx, item in enumerate(fin):
    if ' ' in item:
        item = item.replace(" ","")
        fin[idx] = item
        #print(item)
#print(fin)
ans = " ".join(fin)
print(ans)