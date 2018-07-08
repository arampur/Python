filename = 'TextFiles/firsttext.txt'
with open(filename) as fileobject:
    lines = fileobject.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

mynumber = input("enter the number you want to search :")
if mynumber in pi_string:
    print("your number is found in the file..")
else:
    print("sorry entered text not found..try something else..")

with open('blankfile.txt','w') as writefile:
    writefile.write(mynumber,'\n')