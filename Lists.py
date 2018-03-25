#List demonstration
list1 = ['Amith','Akshath','Appaji','mummy','Rishika','Anvika']
for myelement in list1:
    #traversing the list elements
    print(myelement)

#to add every element by two in the lists
list2 = [30,20,30,46,6567]
for i in range(len(list2)):
    list2[i] = list2[i] + 2
list2.sort()
print(list2)

#to calculate the average of elements in a list
numlist = list()
while(True):
    myinput = input('Enter number:')
    if myinput == 'done': break
    value = float(myinput)
    numlist.append(value)
average = sum(numlist)/len(numlist)
print('Average is: ',average)

#trying something for the string joins using lists
mystring = ['Amith', 'Akshath', 'Appaji', 'mummy', 'Rishika', 'Anvika']
delimiter = ' '
delimiter.join(mystring)
print(mystring)

#Testing on aliases
mystring = list1
mystring[0] = 'AmithRampur'
print(mystring is list1)
print(list1)
