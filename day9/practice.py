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
    if len(words) < 2 or words[0] != 'From':
        continue
    hist[words[1]] = hist.get(words[1], 0) + 1
bigname = None
bigcount = None
for name, count in hist.items():
    if bigcount is None or count > bigcount:
        bigname = name
        bigcount = count
print(bigname, bigcount)