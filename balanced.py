#!/usr/bin/env python3.4
""""""
# This program is for checking the balance of braces
""""""
count1 = 0
count2 = 0
str1 = input()
for x in str1:
    if x == '(':
        x.append(x)
    if x == ')':
        x.pop(x)

if x.find("(") or x.find(")")
    print("F")
else:
    print("T")
