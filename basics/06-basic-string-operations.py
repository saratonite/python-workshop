#! /usr/bin/python3


# String Operations
str1 = "Hello World"

## String Length
print(len(str1))

## Index
print(str1.index('l'))

## Count number of occurance

print(str1.count('l'))

## To uppercase and lowercase

print(str1.upper())
print(str1.lower())

## This is used to determine whether the string starts with something or ends with something, respectively

print(str1.startswith("Hello"))
print(str1.endswith("Foo"))

## Split String using a specified character

print(str1.split("o"))
print(str1.split(" "));
