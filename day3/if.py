print (list(range(10)))

#nested if statement
x = 10
if x > 5:
    print("x is greater than 5")
    if x > 8:
        print("x is also greater than 8")
print('Done')

# if-elif-else statement, or if-else statement, or if-elif statement, if elif else 在同一个缩进下层级相同，只会执行第一个满足条件的语句块，后续即使再满足也不会执行
y = -3
if y > 10:
    print("y is greater than 10")
elif y > 5:
    print("y is greater than 5 but not greater than 10")
elif y > 0:
    print("y is greater than 0 but not greater than 5")
else:
    print("y is not greater than 0")  

# the try/except structure is used to handle exceptions, which are errors that occur during the execution of a program. The code inside the try block is executed, and if an exception occurs, it is caught and handled in the except block. This allows the program to continue running even if an error occurs, instead of crashing.
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input. Please enter a valid number.")   
except KeyboardInterrupt:
    print("Input interrupted by user.")
# any lines of code that may raise an exception can be placed inside the try block, and the error line is the last line to be executed in the try block. 

num = input("Enter a positive number: ")
try:
    num = int(num)
except ValueError:
    num = -1
if num < 0:
    print("Invalid input. Please enter a valid number.")
else:
    print("You entered:", num)

hrs = input("Enter hours: ")
hrs = float(hrs)
rate = input("Enter rate: ")
rate = float(rate)
if hrs > 40:
    pay = 40*rate +(hrs-40)*rate*1.5
else:
    pay = hrs*rate
print(f"Pay: {pay:.2f}")



Grade = input("Enter grade: ")
try:
    Grade = float(Grade)
except ValueError:
    raise ValueError("Invalid input. Please enter a valid number.")
else:#只有没报错才会执行这里
     if 0 <= Grade <= 1.0:
        if Grade >= 0.9:
            print("A")
        elif Grade >= 0.8:
            print("B")
        elif Grade >= 0.7:
            print("C")
        elif Grade >= 0.6:
            print("D")
        else:
            print("F")
     else:
         print("Invalid input. Please enter a number between 0 and 1.")