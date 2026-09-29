#list is a mutable data structure in python which is used to store multiple items in a single variable. It is one of the most commonly used data structures in python. Lists are ordered, changeable, and allow duplicate values. They are defined by enclosing elements in square brackets []. 

# a list is a kind of collection, a collection is a data structure that can hold mutiple items.
numbers = [1,2,3,4,5]

# a list element can be of any data type, including another list.
lists = [1, "hello", 3.14, [1,2,3]]

# a list can be empty, and it can be created by using empty square brackets [].
empty_list = []

#Look inside lists, just like strings, lists are ordered, and each element has an index. The first element has index 0.
numbers = [1,2,3,4,5]
print(numbers[0]) # 1
print(numbers[-1]) # 5

#Lists are mutable, which means you can change their elements. You can change the value of an element by accessing it with its index and assigning a new value to it.
numbers = [1,2,3,4,5]
numbers[3] = 10
print(numbers) # [1, 2, 3, 10, 5]

#len() function can be used to get the number of elements in a list.
numbers = [1,2,3,4,5]
length = len(numbers)
print(length) # 5

#range() function can be used to create a list of numbers. It takes three arguments: start, stop, and step. The start argument is the first number in the list, the stop argument is the last number in the list (exclusive), and the step argument is the difference between each number in the list. For example, range(1, 10, 2) will create a list of odd numbers from 1 to 9.
print(range(5))
print(list(range(5)))
print(range(1, 10, 2))
print(list(range(1, 10, 2)))
#range and list both are iterable, but range is a generator, which means it generates the numbers on the fly and does not store them in memory. This makes it more memory efficient than a list, especially for large ranges.list(range(1, 1000000)) will create a list of 1 million numbers, which will take up a lot of memory.

friends = ["Alice", "Bob", "Charlie", "David"]
for friend in friends:
    print(friend)

for i in range(len(friends)):
    print(friends[i])

#concatenation of lists can be done using the + operator. It combines two lists into a single list.
a = [1, 2, 3]
b = [4, 5, 6]
c = a+b
print(c) # [1, 2, 3, 4, 5, 6]

#Lists can be sliced just like strings. The syntax for slicing is: list[start:end]
c = [1, 2, 3, 4, 5]
print(c[1:3]) # [2, 3]

#List methods are built-in functions that can be used to perform various operations on lists. Some commonly used list methods are:
# append() - adds an element to the end of the list
# extend() - adds multiple elements to the end of the list
# insert() - adds an element at a specific index
# remove() - removes the first occurrence of an element
# pop() - removes and returns the element at a specific index
# clear() - removes all elements from the list
# index() - returns the index of the first occurrence of an element
# count() - returns the number of occurrences of an element
# sort() - sorts the elements of the list in ascending order
# reverse() - reverses the order of the elements in the list
lists = [1, 2, 3, 4, 5]
lists.reverse()
print(lists)
lists.sort()
print(lists)
print(lists.append(6))
print(lists.extend([7, 8, 9]))
print(lists.insert(2, 10))
print(lists.index(2))
print(lists.count(2))
lists.reverse()
print(lists)
lists.sort()
print(lists)
print(lists.remove(3))
print(lists.pop(3))
print(lists.clear())

#Built-in functions that can be used with lists are:
# len() - returns the number of elements in the list
# min() - returns the smallest element in the list
# max() - returns the largest element in the list
# sum() - returns the sum of all elements in the list
numbers = [1, 2, 3, 4, 5]
print(len(numbers)) # 5
print(min(numbers)) # 1
print(max(numbers)) # 5
print(sum(numbers)) # 15
print(sum(numbers)/len(numbers)) # 3.0, average of the numbers in the list

numlist = []
while True:
    num = input("Enter a number:")
    if num == "done":
        break
    value = float(num)
    numlist.append(value)

print(numlist)
print("average:", sum(numlist)/len(numlist))

#Best Friends: Strings and Lists
#split breaks a string into parts and returns a list of those parts. The default separator is whitespace, but you can specify a different separator if you want. For example, if you have a string s = "hello world", you can split it into a list of words with s.split(), which will return ['hello', 'world']. You can also split a string by a specific character, such as a comma, with s.split(',').we can access a particular element of the list by using its index.
abc = "hello world"
abc2 = abc.split()
print(abc2)
for word in abc2:
    print(word[1])

abc = "hello;world"
abc3 = abc.split(';')
print(abc3)
for word in abc3:
    print(word[1])

help(list)

#Filter
#[expression for x in ls, if x]
names = ['Ally', 'Richard','Lily','April']
A_names = [name for name in names if 'il' in name]
print(A_names)
z_names = [0 for name in names]#same size,or range()

a = [1,2,3]
b = a[:]
a[1] = 42
print(b)
#slices, get elements to create a new list(shallow copy), so a and b are different list.

a = [1,2,3]
b = a
a[1] = 42
print(b)
#the nature of list, b = a means that b and a are related to the same list, so  the change of a implies b and conversely. 

a = [[1,2],[2,3]]
b = a[:]
a[1][0] = 42
print(b)
#deep copy, though list a and b are not the same list, their sublist are the same list.b = [[1,2],[42,3]]

print(4*'2'+'2')#eat space

print('2','2','2','2')

a = [1,2,3,4,5]
b = [0::2]#b=[1,3,5]
#the range of slices can over the index
