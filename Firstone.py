print('This is first file..')

#Counting numbner of lines in file
# fhand = open(Readme)
# count = 0
# for line in fhand:
#     count = count + 1
# print('number of lines in file', count)
fhand = open('Readme')
inp = fhand.read()
for line in fhand:
    if line.startswith('Python'):
        print(line)