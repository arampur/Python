fname = input('Enter the filename: ')
try:
    fhand = open(fname)
except:
    print('File cant be opened..', fname)
    exit()

count = 0
for line in fhand:
    if line.startswith('Subject'):
        count = count + 1
print('There were',count,'subject line in',fname)