print('This is first file..')

#Counting numbner of lines in file
fhand = open(readme)
count = 0
for line in fhand:
    count = count + 1
print('number of lines in file', count)
