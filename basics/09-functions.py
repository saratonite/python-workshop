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




## Functions with key word arguments

def keyfun(name="Sarath",action="Cool"):
    print(name+" is ",action);

keyfun(action="Awesome");

## Arbitrary Argument Lists


## Lambda Functions
