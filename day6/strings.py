#string position is called index, and the first character has index 0. The second character has index 1, and so on. You can use square brackets to access individual characters in a string by their index. For example, if you have a string s = 'hello', you can access the first character with s[0], which will return 'h'. You can also use negative indices to access characters from the end of the string. For example, s[-1] will return 'o', which is the last character in the string.
s = 'hello'
print(s[0]) # h
print(s[1]) # e
print(s[2]) # l
print(s[3]) # l
print(s[4]) # o
print(s[-1]) # o
print(s[-2]) # l
print(s[-3]) # l
print(s[-4]) # e
print(s[-5]) # h
print(len(s)) # 5, the length of the string is 5, and the index of the last character is 4, which is len(s)-1.

len(123)# not working
len(str(123))#3

def my_len(s):
    count = 0
    for char in s:
        count = count + 1
    return count

# looping through a string
s = 'hello'
index = 0
while index < len(s):
    print(s[index])
    index = index + 1

#the iteration variable is the variable that takes on the value of each item in the sequence as the loop iterates through it. In a for loop, the iteration variable is defined in the loop header and is assigned the value of each item in the sequence during each iteration. For example, in the loop for char in s:, char is the iteration variable that takes on the value of each character in the string s as the loop iterates through it.

#slicing strings. we can use the slice operator (:) to extract a portion of a string. The syntax for slicing is: string[start:end], where start is the index of the first character to include in the slice, and end is the index of the second character to exclude from the slice. For example, if you have a string s = 'hello', you can extract the substring 'ell' with s[1:4], which will return 'ell'. If you omit the start index, it defaults to 0, and if you omit the end index, it defaults to the length of the string 5. For example, s[:3] will return 'hel', and s[2:] will return 'llo'.
print(s[1:4]) # ell
print(s[:3]) # hel
print(s[2:]) # llo
print(s[2:4]) # llo
print(s[:]) # hello

#string concatenation. when the + operator is used with strings, it concatenates them, which means it combines them into a single string. For example, if you have two strings s1 = 'hello' and s2 = 'world', you can concatenate them with s1 + s2, which will return 'helloworld'. You can also add a space between the two strings with s1 + ' ' + s2, which will return 'hello world'.
s1 = 'hello'
s2 = 'world'
print(s1 + s2) # helloworld
print(s1 + ' ' + s2) # hello world, a single string with a space in between
print(s1, s2) # hello world, two separate strings with a space in between

#using in as a logical operator. The in operator is used to check if a substring is present in a string. It returns True if the substring is found, and False otherwise. For example, if you have a string s = 'hello world', you can check if the substring 'world' is in s with 'world' in s, which will return True. You can also check if the substring 'python' is in s with 'python' in s, which will return False.
s = 'hello world'
if 'world' in s:
    print("found world")
else:
    print("world not found")
if 'python' in s:
    print("found python")
else:
    print("python not found")

# string comparison. When you compare two strings with the == operator, it checks if they are exactly the same, including the case of the letters. For example, 'hello' == 'hello' will return True, but 'Hello' == 'hello' will return False because of the difference in case. You can also use the != operator to check if two strings are not equal. For example, 'hello' != 'Hello' will return True.you can also use the <, >, <=, >= operators to compare strings lexicographically, which means they are compared based on the Unicode code point of each character. For example, 'apple' < 'banana' will return True because 'a' comes before 'b' in the alphabet.
word = input("enter a word: ")
if word == "hello":
    print("hi there!")
elif word > "hello":
    print("your word is greater than hello")
else:
    print("your word is less than hello")

# the string library provides a collection of string constants and functions that can be used to manipulate strings. For example, string.ascii_letters is a string constant that contains all the ASCII letters (both uppercase and lowercase), and string.digits is a string constant that contains all the digits from 0 to 9. You can use these constants to check if a character is a letter or a digit, or to generate random strings of letters and digits.
import string

print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits) # 0123456789
print(string.punctuation) # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
greet = "hello world"
upper_greet = greet.upper() # HELLO WORLD/ greet.lower() # hello world/ greet.title() # Hello World 每个单词首字母大写/ greet.capitalize() # Hello world 只有第一个字母大写/ greet.swapcase() # HELLO WORLD 大小写互换
print(upper_greet)

if greet in string.ascii_letters:
    print("greet is a letter")
else:    
    print("greet is not a letter")
#函数 function：通用工具，谁都能用 function（variable）
#方法 method：只有这种数据类型能用 string.method() 只有字符串才有 .title(); 数字就没有 .title(). dot means object oriented programming. string is an object, and it has methods that can be called on it. The dot operator is used to access the methods of an object. For example, greet.upper() calls the upper() method on the greet string object, which returns a new string with all the characters in uppercase.
# https://docs.python.org/3/library/stdtypes.html#string-methods

#searching a string. if xx in s; find() method returns the index of the first occurrence of the substring in the string, or -1 if the substring is not found. For example, s.find('world') will return 6, which is the index of the first character of 'world' in the string s. If you want to find all occurrences of a substring in a string, you can use a loop to repeatedly call find() with a starting index that is updated after each occurrence is found.
# .find('world', start) will start searching for 'world' from the index specified by start. If you want to find the last occurrence of a substring in a string, you can use the rfind() method, which works similarly to find() but searches from the end of the string instead of the beginning. For example, s.rfind('o') will return 7, which is the index of the last occurrence of 'o' in the string s.
s = 'hello world'  
print(s.find('world')) # 6
print(s.find('python')) # -1
print(s.rfind('d')) # 10

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos) # 21, the index of the @ symbol
sppos = data.find(' ', atpos) # find the first space after the @ symbol
print(sppos) # 31, the index of the first space after the @ symbol
host = data[atpos+1 : sppos] # extract the substring between the @ symbol and the first space after it
print(host) # uct.ac.za


#replace() method returns a new string with all occurrences of a substring replaced by another substring. For example, s.replace('world', 'python') will return 'hello python', which is a new string with 'world' replaced by 'python'. The original string s remains unchanged because strings are immutable in Python.count is an optional argument that specifies the maximum number of occurrences to replace. If count is not provided, all occurrences will be replaced. For example, s.replace('o', 'x', 2) will return 'hellx world', which replaces only the first 2 occurrences of 'o' with 'x'.
s = 'hello world'
new_s = s.replace('world', 'python')
print(new_s) # hello python
print(s) # hello world, the original string is unchanged
new2_s = s.replace('o', 'x',1) # hellx wxrld, all occurrences of 'o' are replaced by 'x'
print(new2_s)

#指定替换
import re

def replace_nth(s, old, new, n):
    # 1. 先把前 n-1 个 old 保留不变
    part1 = re.sub(old, old, s, count=n-1)
    # 2. 把第 n 个替换成 new
    result = re.sub(old, new, part1, count=1)
    return result

s = "hello world"
print(replace_nth(s, 'o', 'x', 2))  # hello wxrld

#stripping whitespace. The strip() method returns a new string with leading and trailing whitespace removed. For example, s.strip() will return 'hello world' if s is '  hello world  '. You can also use lstrip() to remove only leading whitespace and rstrip() to remove only trailing whitespace.
s = '  hello world  '
print(s.strip()) # 'hello world'
print(s.lstrip()) # 'hello world  '
print(s.rstrip()) # '  hello world'

# prefixes and suffixes. The startswith() method returns True if the string starts with a specified prefix, and False otherwise. For example, s.startswith('hello') will return True if s is 'hello world', but False if s is 'world hello'. The endswith() method returns True if the string ends with a specified suffix, and False otherwise. For example, s.endswith('world') will return True if s is 'hello world', but False if s is 'world hello'.
s = 'hello world'
print(s.startswith('hello')) # True
print(s.endswith('world')) # True

s = 'hello'
print(s.startswith('h')) # True
print(s.endswith('o')) # True

#每一个字符底层都是unicode数字，我们可以用 ord() 函数来获取一个字符的 Unicode 码点（整数表示），用 chr() 函数来获取一个 Unicode 码点对应的字符。例如，ord('a') 会返回 97，因为 'a' 的 Unicode 码点是 97，而 chr(97) 会返回 'a'。只是 Python 帮你自动显示成字符样子
# 查看字符的 Unicode 编号（用 ord()）
print(ord('A'))    # 65
print(ord('中'))   # 20013
print(ord('😊'))   # 128522

# 通过编号转回字符（用 chr()）
print(chr(65))     # A
print(chr(20013))  # 中
print(chr(128522)) # 😊