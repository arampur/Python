fname = input('enter your filename: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ',fname)
count = 0
for line in fhand:
    if line.startswith('Subject'):
        count = count + 1
print('There were', count, 'subject lines in ',fname) 