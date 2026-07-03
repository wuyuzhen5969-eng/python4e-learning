#def that stands for defined function
def my_function(x):
    print("Hello from a function") 
    print("This is a function that prints a message")
    print(x*2)
my_function(5)

#these built-in functions are already defined and stored in python and we can reuse them whennever we want. We can also create our own functions and reuse them whenever we want.
big = max("Hello world")
print(big)
tiny = min("Hello world")
print(tiny)

#building our own function
def my_max(*items):
    if len(items) == 0:
        raise(ValueError("my_max() arg is an empty sequence"))
    elif len(items) == 1:
        args = items[0]   
    else:
        args = items
    it = iter(args)
    big = next(it)
    for item in it:
        if item > big:
            big = item
    return(big)
  
my_max(1,2,3)


def my_max(*items):
    try:
        big = items[0]
    except IndexError:
        raise(ValueError("my_max() arg is an empty sequence"))
    for item in items[1:]:
        if item > big:
            big = item
    return(big)
  
my_max()

def my_min(*items):
    if len(items) == 0:
        raise(ValueError("my_min() arg is an empty sequence"))
    elif len(items) == 1:
        args = items[0]
    else:
        args = items
    it = iter(args)
    small = next(it)
    for items in it:
        if items < small:
            small = items
        return(small)
my_min(1,2,8)
# an argument(arg) is a value that is passed to a function when it is called. The function can then use this value to perform some operation or calculation.

#return statement is used to exit a function and return a value to the caller. 写函数要输出结果给后面代码用，一律用 return statement, 不要 print. print 是输出结果给用户看的， return 是输出结果给后面代码用的。
def add(x,y):
    return x+y
result = add(3,4)
print(result)

def computepay(hrs,rate):
    if hrs > 40:
        pay = 40*rate +(hrs-40)*rate*1.5
    else:
        pay = hrs*rate
    return pay
hrs = input("Enter hours: ")
hrs = float(hrs)
rate = input("Enter rate: ") 
rate = float(rate)
pay = computepay(hrs,rate)
print(f"Pay: {pay:.2f}")