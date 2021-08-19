# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 21:05:24 2021

@author: HP
"""
from joy import *

r1=rectangle(w=240,h=240,fill="#fa7a02",stroke="none")
r2=rectangle(w=200,h=200,fill="#25ff0d",stroke="none")|rotate(45)
r3=rectangle(w=180,h=180,fill="#fffb0d",stroke="none")|rotate(45)

c1=circle(x=66,y=66,r=20,fill="#b12bff",stroke="none")
c2=circle(x=66,y=66,r=30,fill="#fa7a02",stroke="none")
c3=circle(x=66,y=66,r=40,fill="#fff82b",stroke="none")
c4=circle(x=66,y=66,r=50,fill="#ffffff",stroke="none")
c=combine([c4,c3,c2,c1])|repeat(4,rotate(90))

s1=circle(r=150,fill="#fc0f17",stroke="none")
s2=circle(r=145,fill="#fff42b",stroke="none")
s3=circle(r=139,fill="#a72bff",stroke="none")
s=combine([s1,s2,s3])

b1=circle(r=5,fill="#051eff",stroke="none")
b2=circle(r=10,fill="#a72bff",stroke="none")
b3=circle(r=15,fill="#051eff",stroke="none")
b4=circle(r=20,fill="#ff2bf4",stroke="none")

a1=rectangle(w=50,h=50,fill="#fff305",stroke="none")|repeat(36,rotate(10))
a2=rectangle(w=70,h=70,fill="#ff05da",stroke="none")|repeat(36,rotate(10))

e1=circle(r=60,fill="#ffffff",stroke="none")

f1=circle(x=0,y=50,r=20,fill="#4130fc",stroke="none")
f2=circle(x=0,y=50,r=30,fill="#fc30eb",stroke="none")
f3=circle(x=0,y=50,r=40,fill="#ffffff",stroke="none")
f=combine([f3,f2,f1])|repeat(36,rotate(60))

show(s,r1,c,r2,r3,f,e1,a2,a1,b4,b3,b2,b1)

