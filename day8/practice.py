rhand = open("romeo.txt","r")
rlist = rhand.read()
list = rlist.split()
result = []
for line in list:
    word = line.split()
    result = result + word

result.sort()
print(result)



fname = input("Enter file name:")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()
result = []
for line in list(fhand):
    words = line.split()
    for word in words:
        if word in result:
            continue
        result.append(word)

result.sort()
print(result)


fname = input("Enter file name:")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()
count = 0
for line in list(fhand):
    if line.startswith("From:"):
        count = count + 1
        words = line.split()
        print(words[1])
print("There were", count, "lines in the file with 'From' as the first word")