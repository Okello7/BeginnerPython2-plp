import math
#If statement
marks = int(input("Enter Marks: "))
if marks > 85 and marks <= 100:
    print("Congratulations! you score grade A...")
elif marks > 60 and marks <= 85:
    print("You scored grade B+")
elif marks > 40 and marks <=60:
    print("You scored grade B")
elif marks > 30 and marks <= 40:
    print("You scored grade C...")
elif marks >= 0 and marks <= 30:
    print("Heads up you Failed.^|^")
else:
    print("Err input  the correct marks.")
    
#For Loop
#The for loop in Python is used to iterate the statements
# or a part of the program several times.
names = ["John","Peter","Matthew","Paul","Jude","Mark"]
for i in names:
    print(i)

#Python break, continue and pass statements
for i in range(7):#break stops the loop
    if i == 4:
        break

    print("Hello " + str(i))

print()

for i in range(7):#continue skips the condition and executes the rest of the code.
    if i == 4:
        continue
    
    print("Hello " + str(i))

print("*" * 5)
#pass is used to ignore a code that  is not defined

for i in names:
    if i == "John":
        pass
    
    print("Hello " + i)

#Self Test
print("*")
print("* *")
print("* * *")
print("* * * *")
print("* * * * *")
print("* * * *")
print("* * *")
print("* *")
print("*")

for i in range(6):
    print("* " * i)
for i in range(6,0,-1):
    print("* " * i)

#Write a Python program to guess a number between 1 to 9.
guess = 7
numGuess = int(input("Guess a number between 1 t0 9: "))
while numGuess != guess:
    numGuess = int(input("Guess a number between 1 to 9: "))
print('Correct guess!')

num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]
#create a new for loop and print out each value on the list in sequential order.
for val in num_list:
    print(val)
print("////\\\\")
#look for all numbers that are greater than 45 and print out
for val in num_list:
    if val > 45:
        print(val)
    #else:
    #    pass

#Change the print statement to “Over 45”
# and add an else condition with a print statement of “Under 45”
for val in num_list:
    if val > 45:
        print(str(val) + " is over 45")
    else:
        print(str(val) + " is under 45")

#Update the for loop to use the enumerate function so you can get and use the index.
for val in enumerate(num_list):
    if 36 in val:
        print("Number found in position " + str(val[0]))

#create a new variable called count and assign it a value of 0 and place it outside the for loop.
#Inside the for loop increment the counter by 1.
#Add a print statement outside the for loop to print the value of the count variable.

count = 0

for val in enumerate(num_list):
    count += 1
    if 36 in val:
        print("Number found in position " + str(val[0]))
    


print(count)

#Finally, add a break statement directly after the print statement inside the if condition for finding the number.
count = 0

for val in enumerate(num_list):
    count += 1
    if 36 in val:
        print("Number found in position " + str(val[0]))
        break


print(count)

