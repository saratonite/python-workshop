#! /usr/bin/python3

# Types

## Number

### The integer numbers (e.g. 2, 4, 20) have type int, the ones with a fractional part (e.g. 5.0, 1.6) have type float

print(2+5)

print(5.6+5)


#### Integer type
myint = 5;

#### float type
myfloat = 7.5


print(myint*myfloat)



## String <str>

mystring1 = 'Hello World'

mystring2 = "Hello universe"

### Escaping
print('Escaping single \' quotes') # Escaping by using \'

print("Escaping Double quotes by \"  ")

#### New line
print("Hey \nThis is a new line ")

#### If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote:
print(r"C:\new\musics")

### Multiline Strings
#### String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''

print("""\
First line
Second line
Third line
"""
);

#### Prevent new lines using \

print("""
 First line \
Continue First line
Second line"""
);

### String Concatenation
####Strings can be concatenated (glued together) with the + operator, and repeated with *:

print("Hello "+ "World")
print("->Sarath"*5)
#### This feature is particularly useful when you want to break long strings
text = (
'Hello World Whats up?'
'Fooo Bar')
print(text)


### Accessing Sctring Positions Characters

sample = "Goodbye WorlD"

print("at first position",sample[0])
print("Last postion",sample[-1])
print("Second Last postion",sample[-2])
print("Last postion",sample[-1])
print("from right to postion",sample[-13]) # is equal to [0]

### Slicing
#### slicing allows you to obtain substring:
print("slice from 0 to 7", sample[0:7]) # 0-6

print("max"[0:3])
print("max"[:2])
print("max"[1:])
