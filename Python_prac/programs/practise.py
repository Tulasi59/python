# def func1(func):
#     def inner_funct():
#         print "inner function"
#         func()
#         print " innnnnnnnn"
#
#     return  inner_funct()
#
#
# def main_funcddt():
#     print "main functionnnnn"
#
# main_funcddt= func1(main_funcddt)
# main_funcddt()
#
#
# def hello_decorator(func):
#     def inner1():
#         print("Hello, this is before function execution")
#         func()
#         print("This is after function execution")
#     return inner1
#
# def function_to_be_used():
#     print("This is inside the function !!")
# function_to_be_used = hello_decorator(function_to_be_used)
# # calling the function
# function_to_be_used()

# import math,time
# def calculate_time(func):
#     def get_time(*args,**kwargs):
#
#         stime = time.time()
#         func(*args,**kwargs)
#         etime = time.time()
#         print ("total time:",func.__name__,stime-etime)
#
#     return  get_time()
# @calculate_time
# def factorial(num):
#     print math.factorial(num)
#
# factorial(10)

# def facto(num):
#     if num == 1:
#         return 1
#     else:
#         return num * facto(num - 1)
#
#
# print(facto(5))

#
# def memoize_factorial(f):
#     memory = {}
#
#     # This inner function has access to memory
#     # and 'f'
#     def inner(num):
#         if num not in memory:
#             memory[num] = f(num)
#         return memory[num]
#
#     return inner
#
#
# @memoize_factorial
# def facto(num):
#     if num == 1:
#         return 1
#     else:
#         return num * facto(num - 1)
#
#
# print(facto(5))

#
# myList = [['a:', 'b:', '4,80', 'c:', 'b:', '5,00', ':', '4,91', 'Pass'],['a:', 'b:', '1,45', 'c:', 'b:', '1,55', 'd:', '1,51', 'Pass'],['a:', 'b:', '-1,15', 'a:', 'b:', '-0,95', 'c:', '-1,07', 'Pass']]
# newList = []
# for f in myList:
#     nLis = []
#     for i in f:
#         if i.__contains__(','):
#             a =  i.replace(',','')
#             nLis.append(a)
#         #print (nLis)
#     newList.append(nLis)
# print (newList)

# test_dict = {'nikhil': 1, "akash": 2, 'akshat': 3, 'manjeet': 4}
# res = dict((k, test_dict[k]) for k in ['nikhil', 'akshat'] if k in test_dict)
#
# print (str(res))
#
# test_dict = {'Gfg' : 11, 'for' : 12, 'CS' : 11, 'geeks':8, 'nerd':112}
# temp = min(test_dict.values())
# print (temp)
# # res  = [ k for k in test_dict if test_dict[k]==temp]
# # print (res)

# Convert a nested list into a flat list
# l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
# out = []
# def remove_nestedList(l):
#     for i in l:
#         if type(i)== list:
#             remove_nestedList(i)
#         else:
#             out.append(i)
# remove_nestedList(l)
# print (out)

#
# #Find the sublist with maximum value in given nested list
# li = [['Paras', 90], ['Jain', 32], ['Geeks', 120],['for', 338], ['Labs', 532]]
# print (max(li,key=lambda x:x[1]))
#
# #find maximum value in each sublist
# a = [[10, 13, 454, 66, 44], [10, 8, 7, 23]]
# b = [max(b) for b in a]
# print (b)
#
# #Maximum Sum Sublist
# test_matrix = [[1, 3, 1], [4, 5, 3], [1, 2, 4]]
# res = max(test_matrix, key = sum)
# print ("Maximum sum sublist is : " + str(res))
#
# #multiply each  element in a sublist by index
# ini_list = [[3, 4, 7], [ 6, 7, 8], [ 10, 7, 5], [ 11, 12, 13]]
# res = [sum(i * j for i, j in enumerate(sublist))
#        for sublist in ini_list]
# print("result", res)
#
# from operator import itemgetter
# test_list = [['Rash', 4, 28], ['Varsha', 2, 20], ['Nikhil', 1, 20], ['Akshat', 3, 21]]
# res = sorted(test_list, key=itemgetter(1))
# print(res)

# from collections import OrderedDict
#
# li = [1, 3, 4, 4, 1, 5, 3, 1]
# for i in li:
#     res = (li.count(i))
#     print(list(OrderedDict(res).items()))
# #
#
# # jlis = [1, 2, 3, 4, 5]
# # jlis.insert(len(jlis), 6)
# # jlis[4] = 6
# # print(jlis)
#
# s = "hi give me a, missed call? when work completed!"
# import re
# patt = re.compile('(\w*\,)')
# re.split()
# print(re.findall(pattern=patt, string=s))


# ss = re.compile('\$')
# print(re.search(ss))
# s=max([len(i.split()) for i in ss])
# print(s)
#
# ======================================================
# with open(r'D:\samplesai.txt') as f:
#     s = (f.read()).split("\n")
#     for each in s:
#         try:
#             print(int(each))
#         except:
#             pass
#
# s = [1, 2, 3, 6, 5, 4, 1, 7, 8, 9]

# ===================================================
# Input : A = {1, 2, 3, 4, 5}
# Output : [48]
#          [20, 28]
#          [8, 12, 16]
#          [3, 5, 7, 9]
#          [1, 2, 3, 4, 5]
#
# Explanation :
# Here,   [48]
#         [20, 28] -->(20 + 28 = 48)
#         [8, 12, 16] -->(8 + 12 = 20, 12 + 16 = 28)
#         [3, 5, 7, 9] -->(3 + 5 = 8, 5 + 7 = 12, 7 + 9 = 16)
#         [1, 2, 3, 4, 5] -->(1 + 2 = 3, 2 + 3 = 5, 3 + 4 = 7, 4 + 5 = 9)

# def printData(A):
#     if (len(A)<1):
#         return A
#     temp = [0] * (len(A) - 1)
#     # print (temp,">>")
#     for i in range(0,len(A)-1):
#         # print (i)
#         x = A[i]+A[i+1]
#         temp[i] = x
#     printData (temp)
#     print (A)
# A = [ 1, 2, 3, 4, 5 ]
# printData(A)
# =================

# #Armstrong Number  153 = 1*1*1 +5*5*5 +3*3*3
# num = int(input("Enter a number: "))
# # initialize sum
# sum = 0
# # find the sum of the cube of each digit
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** 3
#    temp //= 10
# # display the result
# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")
# ===============
# num = 407
# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
# else:
#     print(num, "is a prime number")
#
# from itertools import izip
# A = [1, 2, 3, 4, 5, 6, 7, 8]
# b = [1, 2, 3, 4, 5, 6]
#
# print (dict(izip_longest(b, A)))

# #
# v = 1
# print type(v)
#
# print long(1)
#
# def search(arr,n,x):
#     i = 0
#     for i in range(i,n):
#         if (arr[i]==x):
#             return i
#
# arr = [2,35,10,15]
# x = 15
# n = len(arr)
# print (x ,"present at index",search(arr,n,x))
#
#
# class Person:
#     def __init__(self):
#         self.name = ''
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self,val):
#       self.__name = val
#
# p = Person()
# p.name = 'Prasanna'
# print (p.name)
#A pattern
# def print_pattern(n):
#     # Outer for loop for number of lines(rows)
#     for i in range(n):
#         # Inner for loop for printing *'s and  &nbsp's(columns)
#         for j in range((n // 2) + 1):
#             # prints two column lines
#             if ((j == 0 or j == n // 2) and i != 0 or
#                 # print first line of alphabet
#                                 i == 0 and j != 0 and j != n // 2 or
#                 # prints middle line
#                         i == n // 2):
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#         print()
#        # Size of the letter
# um = int(input("Enter the size: \t "))
# if num > 7:
#     print_pattern(num)
# else:
#     print("Enter a size minumin of 8")

import collections
from collections import namedtuple

# dd = namedtuple("Student",'name age')
# d1 = dd(name='vinod',age='10')
# print (type(dd))
# print (d1)



#Student = collections.namedtuple('Student',['name','age','DOB'])
# s = ['sandy','27','10']
# print (Student._make(s))
# # di = {'name': "Nikhil", 'age': 19, 'DOB': '1391997'}


#
# a = "{'a':'avishek', 'p':'prasanna'}"
#
# c = """
# print("Avishek")
# print("Prasanna")
# d = 10
# e = 50
# print(d+e)
# """
#
# exec(c)
# a = compile(c,"Z:/devspace/prasanna/testttt.py",'exec')
# print(exec(a))

# class Counter:
#
#     def __init__(self,num):
#         self.num = num
#         self.counter = 0
#
#     def __iter__(self):
#         pass
#
#     def __next__(self):
#         if self.counter<=self.num:
#             x = self.counter+1
#
#             #print (x)
#             return x
#         else:
#             raise StopIteration
#
# cnt = Counter(10)
# print(cnt.__next__())
# print(cnt.__next__())
# print(cnt.__next__())
# print(cnt.__next__())
# print(cnt.__next__())


# data = "My name is Prasanna"
#
# s =  ""
# new_s = ""
# for i in data:
#     if i== " ":
#         s += new_s[::-1]+ " "
#         new_s = ""
#     else:
#         new_s += i
# s+= new_s[::-1]
# print (s)

# s,ss = "",""
# p = "my name is prasanna"
# for i in p:
#     if i == " ":
#         ss+= s + " "
#         s=" "
#     else:
#         # pass
#         s = i + s
# ss += s
# print (ss)
#Iterator Ex
# class IterEx:
#     def __init__(self):
#         self.num = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.num<=10:
#             val =self.num
#             self.num+=1
#             return val
#         else:
#             raise StopIteration
# iterobj = IterEx()
# for i in iterobj:
#     print (i)

# list1=[1,3,[7,4],6]
# import copy
# list2 = copy.copy(list1)
# print (list1)
# print (list2)
# list2[2][0]=5
# print (list2)
# print (list1)
# # ==== deepcopy
# print ('----------')
# list1=[1,3,[7,4],6]
# list2 = copy.deepcopy(list1)
# # print (list1)
# # print (list2)
# list2[2][0]=5
# print (list2)
# print (list1)
# from itertools import cycle,repeat
# c=0
# for i in cycle(['prasanna','batchu']):
#     if c>7:
#         break
#     print (i)
#     c+=1
#
# li = ["man","nut","bag","rat","cat","dog","fog","cat","man"]
# from collections import Counter
# c = Counter(li)
# print (c)
#
# #Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor Sample value of n is 5 Expected Result : 615
# a = int(input("Input an integer : "))
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# print (n1+n2+n3)

#print the calendar of a given month and year.
# import calendar
# y = int(input("Input the year : "))
# m = int(input("Input the month : "))
# print (calendar.month(y,m))
#
# from datetime import date
# d1 = date(2014, 7, 2)
# d2 = date(2014, 7, 11)
# s = d2-d1
# print (s)

# x =3
# y=3
# z=3
# sum = (x+y+z)
# if x==y==z:
#     print ('sum:', 3*sum)

# #get count of 4 in a list
# li = [1,4,5,15,4,26,16,4]
# count =0
# for l in li:
#     if l==4:
#         count+=1
# print (count)

# li = ['a','e','i','o','u']
# s = input('enter letter:')
# if s in li:
#     print ('vowel')
# else:
#     print ('not vowel')

#Concatenate all elements in a list into a string and return it
# li = [15,12,1,4,6,8,7]
# s = " "
# for i in li:
#     s += str(i)
# print (s)
#
# #
# numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328,
#            615, 953, 345,399, 162, 758, 219, 918, 237, 412, 566,826, 248, 866, 950, 626, 949, 687, 217,815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527]
# for i in numbers:
#     if i == 237:
#         break
#     elif i%2 == 0:
#         print (i)
# import multiprocessing
# print (multiprocessing.cpu_count())
#
# import math
# print (dir(math))
# x=874.190867
# print (math.floor(x))
# print (math.fmod)
#


# num = int(input("enter a number: "))
#
# temp = num
# rev = 0
#
# while temp != 0:
#     rev = (rev * 10) + (temp % 10)
#     temp = temp // 10
#
# if num == rev:
#     print("number is palindrome")
# else:
#     print("number is not palindrome")

# def countdown(num):
#     print('Starting')
#     while num > 0:
#         yield num
#         num -= 1
# val = countdown(5)
# print (val)
# print (next(val))


# #Generator Expression
# my_list = ['a', 'b', 'c', 'd']
# gen_obj = (x for x in my_list)
# for val in gen_obj:
#     print(val)

# Usecases of Generators
#Generators are perfect for reading a large number of large files since they yield out data a single chunk at a time irrespective of the size of the input stream.
#  They can also result in cleaner code by decoupling the iteration process into smaller components.


# dossiers = ['The Contessa', 'Double Trouble', 'Eartha Brute', 'Kneemoi']
# list_iter = iter(dossiers)
# # print (list_iter,"vvv")
# while True:
#     try:
#         crook = next(list_iter)
#         print(crook)
#     except StopIteration:
#         break

# temps_f = [67.0, 72.5, 71.3]
# for f in temps_f:
#     f = round((f - 32) / 1.8, 1)
#
#     print (f)

# odd_remainders = {10 % n for n in range(1,10,2)}
# print(odd_remainders)
# #
# odd_remainders = [10 % n for n in range(1,10)]
# print(odd_remainders)
#
# for n in range(1,10):
#     #print (n,">>>")
#     print (10%n)

#
# line_list = ['  line 1\n', 'line 2  \n', 'line 3  \n', 'line 4  \n', 'line 5  \n']
# stripped_iter = (line.strip() for line in line_list)
# print (stripped_iter.__next__())
# print (stripped_iter.__next__())
# print (stripped_iter.__next__())
#
# stripped_list = [line.strip() for line in line_list]
# print (stripped_list)
#

# # Abstraction
# class Sample(ABC):
#     @abstractmethod
#     def sample(self):
#         pass

#
# class ATM():
#     def add(self):
#         pass
#     def sub(self):
#         pass
#     def money(self):
#         pass
# #
# class Sample(ATM):
#     def add(self):
#         print ("logic add")
# Sample().add()
#Encapsulation
# class MySample():
#     def __init__(self,a=0,b=0):
#         self.a = a
#         self.b = b
#         self.__message = "Addition Result Is "
#     def add(self):
#         c = str(self.a+self.b)
#         return c
#
#
# ob = MySample(a = 5,b = 5)
# print (ob.a)
# print (ob.b)
# ob.message = "Subtraction Result "
# print ()
# print (ob.add())
# print (ob.__dict__)



# class Person:
#     name = ""
#     age = 0
#
#     def __init__(self, personName, personAge):
#         self.name = personName
#         self.age = personAge
#
#     def __repr__(self):
#         return {'name':self.name, 'age':self.age}
#     # def __repr__(self):
#     #     return '{name:' + self.name + ', age:' + str(self.age) + '}'
#     def __str__(self):
#         return '(name='+self.name+', age='+str(self.age)+ ')'
#
# p = Person('prasanna','27')
# print (p.__str__())
# print (p.__repr__())
# #
# p = 'prasanna'
# print ((p.__repr__()))
# print ((p.__str__()))
# ============
# import datetime
# today = datetime.datetime.now()
# # Prints readable format for date-time object
# print (str(today))
#
# # prints the official format of date-time object
# print (repr(today))
# # Output:2016 - 02 - 22 19:32:04.078030
# datetime.date#time(2016, 2, 22, 19, 32, 4, 78030)

# class AddableDict(dict):
#
#     def __add__(self, otherObj):
#         self.update(otherObj)
#         print (otherObj)
#         return AddableDict(self)
#
#
# dict1 = AddableDict({1 : "ABC"})
# dict2 = AddableDict({2 : "EFG"})
#
# print (dict1 + dict2)
#
# class Sample():
#     cls_a = 'class var'  #class var which is declared within the class and outside func/method
#     def __init__(self,a=0,b=0):
#         self.a = 0  #instance var
#         self.b = 0
#
#     def tt(self): #instance method  is used by passing self keyword
#         asa = 0
#         print (self.cls_a)
#         #print (Sample.cls_a)
#     @classmethod
#     def tt_class(cls): #class method  is declared using @clasmethod and first arg must be cls and not self
#         print (cls.cls_a)
#
#     @staticmethod
#     def tt_static(): #static method  is declared using @staticmethod and which doesnot contains any argument
#         print ("FFf")
#
#
# ob = Sample()
# #ob.tt_class()
# ob.tt_static()


#Abstraction with Encapsulation
# class AbstractionDemo():
#     def __init__(self):
#         self.my_balance = 1000
#
#     def credit(self):
#         amount = input("please enter money")
#         self.my_balance = self.my_balance + int(amount)
#
#
#     def debit(self):
#         amount = input("please enter money")
#         self.my_balance = self.my_balance - int(amount)
#
#     def check_balance(self):
#         print (self.my_balance)
#
#
# ob = AbstractionDemo()
# ob.check_balance()
# ob.credit()
# ob.check_balance()
# #ob.debit()

# class Test:
#     def __init__(self):
#         self.name = 'Prasanna'
#         self._num = 9009090786
#     def _test_func(self):
#         print ("data")
#
# obj = Test()
# print (obj._test_func())
# # print (obj._num)

##Double Pre Underscores
# class Sample():
#
#     def __init__(self):
#         self.a = 1
#         self._b = 2
#         self.__c = 3
# obj1 = Sample()
# print (dir(obj1))
# print(obj1._Sample__c)


# a,b=0,1
# #a,b=1,0
# try:
#    print(a/b)
# except:
#    print("You can't divide by 0")
# else:
#     print ('Else block')
# finally:
#     print ('final')


# import array
# a = array.array('i',[1,2,3])
# print (a.__sizeof__())
# li = [1,2,3]
# print (li.__sizeof__())

#prime
# num = int(input("Enter a number: "))
# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")

# palindrome
# str = 'mom'
# # 'Palindrome' if str[::-1]==str else 'not a palindrome'
# if str[::-1] == str:
#     print ('palindrome')
# else:
#     print ('not palindrome')
#
# # even odd
# n = raw_input('enter num')
# mod = num % 2
# if mod > 0:
#     print('even')
# else:
#     print('odd')
#
# # armstrong
# num = int(input("Enter a number: "))
# sum = 0
# temp = num
#
# while temp > 0:
#     digit = temp % 10  # remainder
#     sum += digit ** 3
#     temp //= 10
#
# if num == sum:
#     print(num, "is an Armstrong number")
# else:
#     print(num, "is not an Armstrong number")

# class X(object):
#     def __init__(self, a):
#         self.num = a
#
#     def doubleup(self):
#         self.num *= 2
#
#
# class Y(X):
#     def __init__(self, a):
#         X.__init__(self, a)
#
#     def tripleup(self):
#         self.num *= 3
#
#
# obj = Y(4)
# print(obj.num)
#
# obj.doubleup()
# print(obj.num)
# class Car:
#     __maxspeed = 0
#     __name = ""
#
#     def __init__(self):
#         self.__maxspeed = 200
#         self.__name = "Supercar"
#
#     def drive(self):
#         print('driving. maxspeed ' + str(self.__maxspeed))
#
#     def setMaxSpeed(self, speed):
#         self.__maxspeed = speed
#
#
# redcar = Car()
# redcar.drive()
# redcar.setMaxSpeed(320)
# redcar.drive()

#decorator

# def sample(func):
#     def wrap():
#         print ("fFFF")
#         func()
#         print ('SSSS')
#     return wrap
#
# def saywrap():
#         print ('im called')
#
# new_sample = sample(saywrap)
# new_sample()

#iterator
# class Iterator:
#     def __init__(self):
#         self.num = 1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.num <= 10:
#             val = self.num
#             self.num+=1
#         return val
# obj = Iterator()
# a = iter(obj)
# print(a)
# print(next(a))
# print(next(a))

#generator
# def even(x):
#     while (x != 0):
#         if x % 2 == 0:
#             yield x
#         x -= 1
#
# for i in even(8):
#     print(i)
#
# num = [5,5,9,1,65]
# print ([lambda e:e*5,num])


# list sort
#bubble sort
#dict values sort
#using lambda get even nums
#get content from a url using bs4
#what all functions get executed
#in a given string tell the count of characters
#list comprehension
#re
#python debugging methods


# data_list = [25,10,6,3,89,1,14]
# new_list = []
#
# while data_list:
#     minimum = data_list[0]
#     # arbitrary number in list
#     for x in data_list:
#         if x < minimum:
#             minimum = x
#     new_list.append(minimum)
#     data_list.remove(minimum)
#
# print (new_list)

# import re
# strs = 'if this is method which got all methods of methods'
# search = 'methods'
# print (re.findall(r'\b' + search + r'\b',strs))


# s = 'aabbccccdddddddeeffa'
# print ({i:s.count(i) for i in set(s)})

# import collections
# res = collections.Counter(s)
# print (res)

# Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Geeks',
#         'A' : {1 : 'Geeks', 2 : 'For', 3 : 'Geeks'},
#         'B' : {1 : 'Geeks', 2 : 'Life'}}
# print (Dict)
# # s = Dict.copy()
# # print (s)
# print (Dict.items())

# s = {'saf':112,'b':25,'c':4,'d':8}
# # for k,v in s.items():
#     #print (k,v)
# s['e']= '85'
# print (s)
# # print (s['a'])
# print (s.get('b'))
# print (s.popitem())
# print (s)
# print(sorted(s))
# # print (list(sorted(s.keys())))

# s = {'dd':'R:/RH/asset_lib/assets/ep_102/sets/rig/rh1_102_set_village_market/split/village_market_grocery.ma','aa':'sailaja','bb':'prasanna'}
# for key in sorted(s.keys()):
#     print (key,s[key])

# from threading import Thread
# import time
# def thread1():
#         print ('LLLLL')
#         time.sleep(3)
#         print ('Thread1 is running')
# def thread2():
#         print ('Thread2')
# t1 = Thread(target=thread1)
# t2 = Thread(target=thread2)
# t1.start()
# t2.start()
# t1.join()
# t2.join()


# ex = 'aaabbbbbbcccdddddd'
# d = {}
# for i in ex:
#     d[i]=d.get(i,0)+1
# print (d)

# li = [15,2,145,56,89,78]
# for i in range(len(li)):
#     for  j in range(i,len(li)-i-1):
#         if li[j]>li[j+1]:
#             li[j],li[j+1]=li[j+1],li[j]
# print (li)


# li = [{'cc':'ccccc','ff':'fffffff','ddd':'ddddd'},{'ff':'sssssssss','cc':'lllllllll'},{'ddd':'rrrr','cc':'rrrrfggg'}]
# new_dict = {}
# for i in li:
#     new_dict.update(i)
# print (new_dict)


# from array import *
# li = [12,5,16,17,1,45,26]
# a = array('i',li)
# print (a[2:5])

# a={3,4,5}
# a.update([1,2,3])
# print (a)


# print ("abc DEF".capitalize())

# print ("abcdef".center(7,1))


# print ('1'.isnumeric()
# )
# a = {4,5,6}
# b={2,8,6}
# print (a+b)


# import math
# c = math.ceil(3.4)
# print (c)

#
# li = [1,2,[3,4],[5,6]]
# def sum(li):
#     for i in li:
#         if type(i) == "<class 'list'>":
#             print (i)

# s = array('i',range(10))
# print (s)

# li = [1, 3, 2, 4, 5]
# print (li[-3:][::-1])
#======================
#
# import json
# save_data = {'sel_input': ['{"week_start_date":{"unit":" ","monthly_plan":" ","week_one":"01/10/19","week_two":"14/10/19","week_three":"21/10/19","week_four":"28/10/19"},'
#                            '"week_end_date":{"unit":"","monthly_plan":" ","week_one":"11/10/19","week_two":"18/10/19","week_three":"25/10/19","week_four":"31/10/19"},'
#                            '"no_of_working_days":{"unit":"","monthly_plan":"23","week_one":"9","week_two":"5","week_three":"5",'
#                            '"week_four":"4"}"'],
#              'data': ['{"PROJECT":"power-players-series","PROCESSES":"ALL","MONTH":"April-2019"}']}
#
#
# for k,v in save_data.items():
#     print (v)
#     for r in v:
#         print (r)

# x = int(input())
# y = int(input())
# n = int(input())
# ar = []
# p = 0
# for i in range(x + 1):
#     print (i)
#     for j in range(y + 1):
#         print (i  + j,">>>")
#         print (n)
#         if i + j != n:
#             ar.append([])
#             ar[p] = [i, j]
#             p += 1
# print (ar)

#linear search

# li = [2, 3, 4, 10, 40]
# x=40
# n =len(li)
# for i in range(0,n):
#     if (li[i]==x):
#         print ("ele present",i)

def test():
    print("hello")
if __name__=="__main__":
    test()