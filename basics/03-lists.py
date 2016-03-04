#! /usr/bin/pyhton3


##### > https://docs.python.org/3.4/tutorial/datastructures.html

#Lists


#### Python knows a number of compound data types, used to group together other values. The most versatile is the list, which can be written as a list of comma-separated values (items) between square brackets. Lists might contain items of different types, but usually the items all have the same type.

numbers = [1,2,3,4,5,6]

print(numbers[2])

## Slicing List , slicing return a new String
print(numbers[3:5])
print(numbers[:])

## Concatenate Lists
list1 = [5,"Srath",4]
list2 = [9,5.56,20]

print(list1+list2)

## Lists are mutable , we can change lists element value

list1[1] = "x"

print(list1)

## Adding new items at the en using append methos

list1.append("help")

print(list1)

# TODO https://docs.python.org/3.4/tutorial/datastructures.html
