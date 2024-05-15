print("--------------------------- WELCOME TO PYTHON ---------------------------")
import sys

#printing python version
print("Python Version:", sys.version)

#indentation
if 5 > 2:
    print("5 is greater than 2")

#variables
x=10
y="hello"
print("value of x :",x,'& y:',y)

#This is comment

''' #multiline string
This is comment 
written in more than 
one line
'''

a=2 #int value
print(a)
a='hi' #string value
print(a)

#casting
a=str(10)
#get the type
print(type(a),a)
b=float(2)
print(type(b),b)

#string var can be declared in single quote/ double quote
st='hellllo'
st1="heyyy"
print(type(st),st)
print(type(st1),st1)

#variable name case sensitive
a=3
A=2
print(a,A)

#assign many values to multiple variables
x, y, z = 'CAR', 'BIKE', 'TRUCK'
print(x,y,z)

#assign 1 value to multiple var
x=y=z='black'
print(x,y,z)

#unpack collection
cars=['BMW','AUDI','MERCEDES']
x,y,z=cars
print(x,y,z)

#can print output using , & +
print(x+" "+y+" "+z)

x,y =2,3
print(x+y)

#global variable
x=34

def fun():
    print ("value of x:", x)

fun()   

#local variable
x=34

def fun():
    x=43
    print ("value of x:", x)

fun()   

#global keyword
def myfunc():
    global x
    x='fantastic'
    print("value of x:", x)

myfunc()
print("value of global variable inside function:", x)

