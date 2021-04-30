# -*- coding: utf-8 -*-
"""
Created on Sat May  1 00:32:20 2021

@author: gaurav
"""

#Number divisible by 7 and not multiple of 5
list(range(2000,3200))
m = []
for i in list(range(2000,3200)):
    if (i%7==0) and (i%5!=0):
        m.append(i)
print(m)

#first name and last name in reverse order
a = "Gaurav Jagtap"
a[:: -1]


#volumne of the sphere
pi = 3.1415
d = 12
r = d/2
v = 4/3*(pi*(r**3))
print("the volumne of the sphere is",v)