# Single line comment
"""
This is a 
multi
line
comment
"""
a = "World"
# print("Hello {}".format(a))
# print("Hey {a} {b}".format(a = "Planet", b="Earth"))
str1 = "hello world"
str2 = 'hello world'
num1 = 1    # integer
num2 = 2.0  # float
bool1 = True
bool2 = False
# STRING METHODS
str3 = "i am hendry"
# print(str3.upper())
str4 = "I AM PLUTO"
# print(str4.lower())
# print(str4.split())
str5 = "soccer,table tennis, badminton"
# print(str5.split(","))

# OPERATIONS
op1 = 2 + 5
op2 = 6 - 3
op3 = 7 * 5
op4 = 8 / 4
op5 = 3 ** 2
op6 = 5 % 2     # Check odd or even
op7 = (5 + 2) * 3
# LIST
# Lists are mutable
list1 = ['apple', 'banana', 'watermelon']
list1.append('papaya')
list1_item = list1[1]
list1.pop()
list1.pop(0)
print(list1)
# TUPLE
# Tuples are immutable
tup1 = ("dog", "cat", "horse")
tup1_item = tup1[2]
# Tuple unpacking
(item1, item2, item3) = tup1
print(item1)
# DICTIONARY
dict1 = { 'name': "Johnny", "age": 22}
dict1_item = dict1['age']
# SET
set1 = {1,1,2,2,2,3,4,5,6,6,6,7,7}  # Unique Values Only
# FUNCTIONS
def func1(arg1, arg2 = 20): # Using Default Argument
    return arg1 + arg2
res1 = func1(2)

def func2(arg1):
    if (arg1 > 5):
        print("Number greater than 5")
    if (arg1 < 5):
        print("Number less than 5")

def func3():
        for i in range(0, 20, 5):
                print("printing line {}".format(i))

def func4():
        for i in [1, 2, 3, 4,5, 6, 7, 8]:
                print(i ** 2)

def func5(arg1):
        i= 0
        while (i < arg1):
                print("printing {}".format(i))
                i += 1

x = [1, 2, 3, 4, 5]
out1 = []
out1 = [num**2 for num in x]

lam1 = lambda var1 : var1 ** 2

samp1 = [1,2,3,4,5,6,7,8,9]
test1 = list(filter(lambda var1 : var1 % 2 == 0, samp1))
#print('test1 {}'.format(test1))

test2 = list(map(lambda var1 : var1 ** 2, samp1))
#print('test2 {}'.format(test2))

# LIST COMPREHENSION
z1 = [1,2,3,4,5,6]
z2 = [x ** 2 for x in z1]   # 1,4,9,16,25,36

# CLASS
class Person:
    def __init__(self, name, school, age):
        # data types - String, Numbers, List, Tuple, Dictionary
        # variables
        self.name = name
        self.school = school
        self.age = age
        self.marks = []
        # list can be changed
        self.list = ['soccer', 'swimming', 'badminton', 'listening music', 'sleeping']
        # tuple cannot be changed
        self.number_list = [13,29,18,1,8,22,21]
        self.tuple = ('singaporean', 's8273737')
        # set unique and unordered
        self.set = {1,2,5,6,6,7,7,7,7,8,8}
        # dictionary
        self.dict = { 'country': 'SG', 'postal': 120202 }

        # function without parameter
    def showList(self):
        print(self.name, self.age, self.list, self.tuple, self.set, self.dict)

        # function with parameter
    def setName(self, name):
        print('Hi. My name is {}'.format(name))

        # if elif else conditional statement
    def if_func(self, name):
        if name == 'John':
            print('John is a bad match')
        elif name == 'Eric':
            print('Eric is a good match')
        else: 
            print('I got no idea')

        # function with *args
    def sumNumbers(self, *args):
        return sum(args)

        # function with **kwargs
    def showNames(self, **kwargs):
        print(kwargs)

    def countNumbers(self, numOne, numTwo = 10):
        return numOne + numTwo

    def friend(self, friend_name): 
        return Person(friend_name, self.school, self.age)

    @staticmethod
    def staticFunc():
        print('static method')

    @classmethod
    def cls_friend(cls, origin, friend_name):
        return cls(friend_name, origin.school, origin.age, origin.prefect)

   # KIV Lambda function
    def lambda_func(self):
        res = lambda x: x * 2, self.number_list
        print(res)

    # KIV Class Method
    @classmethod
    def classFunc(cls, person):
        # return Person(person.name + '- says Hi')
        return cls(person.name + '- says Hi')

# Inheritance
class Child(Person):
    def __init__(self, name, school, age, prefect):
        super().__init__(name, school, age)
        self.prefect = True

sally = Person('Sally', 'amkss', 22)
sally.if_func('Eric')
print(sally.countNumbers(52))
print(sally.sumNumbers(10,12,22,23,25,1000))
sally.showNames(title='manager', role='administrative')
sally.lambda_func()

ivy = sally.friend('Ivy')
print(ivy.name)
print(ivy.age)

# using class method
eric = Child("Eric", 'Tpyss', 18, True)
print(eric.school)

jack = Child.cls_friend(eric, "Jack")
print(jack.name)
print(jack.school)

my_list = [22, 25, 26, 12, 11, 33]

def less_than_twenty(x):
    return x < 20

# Lambda Function
print(list(filter(less_than_twenty, my_list)))

# List Comprehension 
print([x for x in my_list if x < 20])
