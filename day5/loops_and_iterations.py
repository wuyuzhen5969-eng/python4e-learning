x = 2
x = x + 2
print(x)

while x > 1:
    print('bigger' )
    x = x - 1
print('done')
#loops have itertation variables that change with each iteration of the loop. In this case, x is the iteration variable. The loop will continue to execute as long as the condition (x > 1) is true. With each iteration, x is decreased by 1, eventually leading to the termination of the loop when x is no longer greater than 1.

# while loops (indefinite loops) are useful when you want to repeat a block of code an unknown number of times, as long as a certain condition is met.so it icludes if statements.while condition is always true, the loop will continue to execute indefinitely, which is known as an infinite loop. To prevent this, you can use a break statement to exit the loop when a certain condition is met.

# break statement ends the current loop and jumps to the statement immediately follwing the loop.
while True:
    line = input("Enter a line of text (or 'quit' to exit): ")
    if line == 'quit':
        break#break 只作用于最近一层循环
    print("You entered:", line)
print('done!')

# continue statement ends the current iteration and jumps to the top of the loop and starts the next iteration.
for i in range(10):
    if i % 2 == 0:
        continue#continue 只作用于最近一层循环
    print(i)


# for loops (definte loops) are used to iterate over a sequence (like a list, tuple, or string) or other iterable objects. They are often used when the number of iterations is known beforehand. The syntax of a for loop is: for variable in sequence: block of code. The variable takes on the value of each item in the sequence, and the block of code is executed for each item.
for i in range(5):
    print(i)
for letter in 'hello':
    print(letter)
for item in ['apple', 'banana', 'cherry']:
    print(item) 



# loop idiom is a common pattern of using loops to process items in a sequence. The most common loop idiom is to use a for loop to iterate over a sequence and perform some operation on each item. For example, you can use a for loop to calculate the sum of a list of numbers:
numbers = [1, 2, 3, 4, 5] 
total = 0
for n in numbers:
    total = total + n
print(total)

#counting the number of items in a sequence is another common loop idiom. You can use a for loop to iterate over the items in a sequence and increment a counter variable for each item:
count = 0
for item in ['apple', 'banana', 'cherry']:
    count = count + 1
    print(item, count)

#summing the number of items in a sequence is another common loop idiom. You can use a for loop to iterate over the items in a sequence and add them to a total variable:
total = 0 
for n in [1, 2, 3, 4, 5]:
    total = total + n 
print(total)

#calculating the average of a sequence is another common loop idiom. You can use a for loop to iterate over the items in a sequence, add them to a total variable, and count the number of items to calculate the average:
total = 0
count = 0
for n in [1, 2, 3, 4, 5]:
    total = total + n
    count = count + 1
print('total:', total, 'count:', count, 'average:', total/count)
avarge = total / count
print('average:', avarge)

# filtering items in a sequence is another common loop idiom. You can use a for loop to iterate over the items in a sequence and use an if statement to filter out items that do not meet a certain condition:
for n in [1, 2, 3, 4, 5]:   
    if n % 2 == 0:
        print(n)

#众数 is another common loop idiom. You can use a for loop to iterate over the items in a sequence and use a dictionary to count the frequency of each item, then find the item with the highest frequency:
counts = {}
for item in ['apple', 'banana', 'cherry', 'apple', 'banana', 'apple']:
    if item not in counts:
        counts[item] = 1
    else:
        counts[item] = counts[item] + 1
print(counts)
max_count = None
max_item = None
for item, count in counts.items():
    if max_count is None or count > max_count:
        max_count = count
        max_item = item 
print('most common item:', max_item, 'count:', max_count)

#  A Boolean variable is a variable that can only take on two values: True or False. if we juest want to search and know if a value was found, we use a variable that starts at false and is set to true when the value is found.
found = False
for item in ['apple', 'banana', 'cherry']:
    if item == 'banana':
        found = True
        break
print('found:', item, found)

# finding the smallest value
smallest= None #None is a constant that represents the absence of a value or a null value. It is often used to indicate that a variable has not been assigned a value yet or to represent the end of a list or sequence.
for n in [3, 1, 4, 1, 5, 9]:
    if smallest is None or n < smallest:
        smallest = n
print('smallest:', smallest)
# true: 0 == 0.0 (value equal); false: 0 is 0.0 (value and type equal); you can use is on boolean(true or false) and none,but not on numbers and strings.
largest = None
smallest = None
while True:
    num = input("enter a integer:")
    if num == 'done':
        break
    try:
        num = int(num)
    except:
        print('invalid input')
        continue
    if largest is None or num > largest:
        largest = num
    if smallest is None or num < smallest:
        smallest = num
print('largest:', largest, 'smallest:', smallest)
        
        