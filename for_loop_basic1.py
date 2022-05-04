# Basic - Print all integers from 0 to 150.
for i in range(0, 150):
    print(i)
# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for x in range(0, 150, 5):
    print(x)
# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for y in range(1, 100):
    if y % 5 != 0 and y % 10 != 0:
        print(y)
    elif y % 5 == 0 and not y % 10 == 0 :
        print("Coding")
    elif y % 10 == 0:
        print("Coding Dojo")
# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
counter = 0
for x in range(0,500000):
    if x % 2 != 0:
        counter += x
        x += 1
    else:
        x += 1
print(counter)
#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
empty_list = []
for x in range(0,2018,4):
    empty_list.append(x)
empty_list.reverse()
for x in empty_list:
    print(x)
#Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 0
highNum = 21
mult = 3
for x in range(lowNum, highNum):
    if x % mult == 0:
        print(x)
