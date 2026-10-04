#file processing, a text file can be thought of as a sequence of lines, and each line is a sequence of characters.
stuff = open('day7/mbox-short.txt', 'r')
print(type(stuff))
inp=stuff.read() 
print(type(inp))

print(len(inp))
for line in stuff:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
print(line)
stuff.close()

f = open('day7/file.txt','w')
l = list(range(1,39,4))
f.write(str(l))
f.close() #instead of .close, we can use ith

with open('day7/file.txt','w') as f
l = list(range(1,39,4))
f.write(str(l))


stuff = 'x\ny'
print(stuff)
print(len(stuff))
#a text file has newlines(\n) at the end of each line, so the length of a text file is the number of characters in the file, including the newlines.

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
for line in fhand:
    if not line.startswith('Subject:'):
        continue
    count = count + 1
print('There were', count, 'subject lines in', fname)


fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
num = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        floatnum = float(line[20:])
        num = num + floatnum
print('Average spam confidence:', num / count)

