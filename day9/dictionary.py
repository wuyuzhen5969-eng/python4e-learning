#dictionary, a linear collection of key-value pairs, where each key is unique and maps to a value. Dictionaries are mutable, meaning they can be changed after creation. 

# dictionaries have an ordered structure over python 3.7, meaning that the order of items is preserved as they are added and the order is maintained when importing or iterating over the dictionary.

cabnet = dict()
cabnet['chair'] = 5
cabnet['table'] = 2
print(cabnet) # {'chair': 5, 'table': 2}
cabnet['chair'] = cabnet['chair'] + 1
print(cabnet) # {'chair': 6, 'table': 2}

x = dict()#function调用函数创建
y = { }#literal syntax 直接写出对象
print(x == y) # True, both are empty dictionaries
y = {'a': 10, 'b': 1, 'c': 22}
print(y) # {'a': 10, 'b': 1, 'c': 22}
x = dict(a=10, b=1, c=22) # function调用函数创建
print(x) # {'a': 10, 'b': 1, 'c': 22}
x = dict(zip(['a', 'b', 'c'], [10, 1, 22])) # function调用函数创建
#zip is a iterater creating ordered pair, the type is zip,use list() or dict() to transform it
print(x) # {'a': 10, 'b': 1, 'c': 22}
z = [('a', 10), ('b', 1), ('c', 22)]#list of tuples, each tuple is a key-value pair
print(type(z)) # <class 'list'>
print(dict(z)) # {'a': 10, 'b': 1, 'c': 22}list转换为dictionaries

counts = {'a': 10, 'b': 1, 'c': 22}
for key in counts:
    print(key, counts[key]) # a 10 b 1 c 22


#making histograms, a histogram is a collection of counters, one counter for each unique item. A histogram is a dictionary that maps from the item to the number of times it appears.
file = input('Enter the file name: ')
try:
    fhand = open(file)
except:
    print('File cannot be opened:', file)
    exit()

hist = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word not in hist:
            hist[word] = 1
        else:
            hist[word] = hist[word] + 1
print(hist)
# it is an error to try to access a key that is not in the dictionary. we can use the in operator to check whether a key is in the dictionary.

#the get method, which allows us to safely access a value for a key, returning a default value(such as 0) if the key is not found. if the key is found, get returns the value associated with the key.
file = input('Enter the file name: ')
try:
    fhand = open(file)
except:
    print('File cannot be opened:', file)
    exit()
hist = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        hist[word] = hist.get(word, 0) + 1
print(hist)

#retrieving list of keys and values, we can retrieve a list of the keys in a dictionary using the keys method, and a list of the values using the values method. we can also retrieve a list of key-value pairs using the items method.
hist = {'a': 10, 'b': 1, 'c': 22}
print(type(hist.values())) # <class 'dict_values'>
print(type(hist.keys())) # <class 'dict_keys'>
print(type(hist.items())) # <class 'dict_items'>
print(hist.keys()) # dict_keys(['a', 'b', 'c'])
print(hist.items()) # dict_items([('a', 10), ('b', 1), ('c', 22)])  
print(list(hist.keys())) # ['a', 'b', 'c']
print(list(hist.values())) # [10, 1, 22]
print(type(list(hist.items()))) # <class 'list'>

#Bonus: two iteration variables, we can use two iteration variables to retrieve both the key and the value when iterating over a dictionary using the items method.
hist = {'a': 10, 'b': 1, 'c': 22}
for key, value in hist.items():
    print(key, value) # a 10 b 1 c 22
# note that hist.items() returns a list of tuples, where each tuple is a key-value pair, corresponding to the two iteration variables.

file = input('Enter the file name: ')
try:
    fhand = open(file)
except:
    print('File cannot be opened:', file)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)


