#! /usr/bin/python3


# Loops

## For Loop

names = ['sarath','billy','daou'];

for name in names:
    print(name)

### using range

for i in range(10):
    print(i)


for i in range(1,10):
    print(i)

#### range with steps

for j in range(120,150,2):
    print(j,"Increment by 2")

for j in range(170,150,-3):
    print(j,"Decrement by 3")


## While loop

x= 10;
while(x>5):
    x -=1
    print("Hey",x)

## Break and Continue

lessons = ['print','lists','loops','functions','classes']

for lesson in lessons:
    if(lesson == "loops"):
        print("Current lesson is loops")
        break;
    else:
        print("Lesson",lesson,"Not matching")


for lesson in lessons :
    if( not lesson == "functions"):
        continue;
    print("Next lesson is ",lesson)
