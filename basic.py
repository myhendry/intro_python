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
# TUPLE
# Tuples are immutable
tup1 = ("dog", "cat", "horse")
tup1_item = tup1[2]
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


