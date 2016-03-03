#! /usr/bin/python

# Functions

def sayHello():
    print("Hello")

sayHello()

## Function arguments

def sayHello(name):
    print("Hello",name)

sayHello("Sarath")

### Function with default arguments

def sayHello(name="World!"):
    print("Hello",name)

sayHello()

## function return

def add(a,b):
    return a+b;

print(add(10,20));
