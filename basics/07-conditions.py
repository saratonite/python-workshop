#!/usr/bin/python3



# Conditions
x = 10

## equality

if(x==10):
    print("X is 10")

## Inequality
if(x!=11):
    print("X is Not 11")
## Greater then

if(x>5):
    print("X is greater than 5")

## Lesst than

if(x<15):
    print("X is Less than 15")

## IN operator

name = "Sarath"
if name in ['Sarath','Billy']:
    print("You are in the list, Great!!")


## IS operator

#### Checking the instance equality

y = [1,2,3]
z = [1,2,3]
g = y
if y is g :
    print("Same instance")
else:
    print("Not same Instance")


## Else part

if name == "Billy":
    print("Your are Billy")
else:
    print("You may be Sarath")

## Elif part

if(name == "Billy"):
    print("Hey Billy")
elif name=="Sarath":
    print("Hey Sarath , You are so kind")
else:
    print("Ooops , I dont  know you!@@#")

## Not operator

if not name == "Billy":
    print("You are not Billy")
