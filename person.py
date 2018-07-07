import string
class Person(object):
    """ Person class representation """
    def __init__(self,name,age,dob):
        self.name = name
        self.age = age
        self.dob = dob
    
    def printname(self):
        """"printing the details"""
        print("My name is " + self.name.title() + " and my age is " + str(self.age) + " and my date of birth " + str(self.dob))

    def walking(self):
        """walking method"""
        print("My name is " + self.name.title() + " and i am walking...")

    def updateage(self,newage):
        """Updating age"""
        self.age += newage

myself = Person('Amith',28,'06261989')
myself.printname()
myself.walking()
myself.updateage(2)
myself.printname()

class newperson(Person):
    def __init__(self,name,age,dob):
        super(newperson,self).__init__(name,age,dob)

my_person = newperson('akshath',31,'04251985')
print(my_person.printname())

mystr = 'aMbsdasfMwewweKsd assdas qwedsa asdas asdas'
print(mystr)
print(string.capwords(mystr))

