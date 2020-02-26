"""factorial of a number
  For example factorial of 6 is 6*5*4*3*2*1 which is 720.
 """
from functools import reduce
# with recursion
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
# print(factorial(6))#720

#without recursion
def factorial_without_recursion(n):
    res =1
    for i in range(1,n+1):
        res*=i
    return res
# print(factorial_without_recursion(6))
""" check Armstrong Number
Input : 153
Output : Yes
153 is an Armstrong number.
1*1*1 + 5*5*5 + 3*3*3 = 153
"""
def armstrong(n):
    num =len(str(n))
    l= sum([int(i)**num for i in str(n)])
    if n==l:
        return "{0} is armstrong".format(n)
    else:
        return "{0} is not armstrong".format(n)
# print(armstrong(153))
""" print all Prime numbers in an Interval """
def all_prime_num(start,end):
    for n in range(start,end):
        if n>1:
            for i in range(2,n):
                if n%i ==0:
                    break
            else:
                print("{0} is prime".format(n))
    # l = [n else break if n%i==0for i in range(2,n) for n in range(start,end) if n>1]
# all_prime_num(11,25)
""" check whether a number is Prime or not """
def check_prime_num(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                break
        else:
            print("{0} is prime".format(n))
# check_prime_num(11)
""" n-th Fibonacci number """
#with recursion
def n_th_fibonacci_number_with_recursion(n):
    if n<=0:
        return "incorrect input"
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return n_th_fibonacci_number_with_recursion(n-1)+n_th_fibonacci_number_with_recursion(n-2)
# print(n_th_fibonacci_number_with_recursion(9)) #21
def n_th_fibonacci_number_without_recursion(n):
    n1,n2 =0,1
    for i in range(n-1):
        n1,n2=n2,n1+n2
    return n1
# print(n_th_fibonacci_number_without_recursion(-6))
"""Fibonacci numbers
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……...
"""
def fibonacci_series(n):
    n1,n2 =0,1
    for i in range(n):
        print(n1)
        n1,n2=n2,n1+n2
# print(fibonacci_series(9))
def check_fibonacci_num(n):
    n1,n2=0,1
    for i in range(n):
        if n1==n:
            print("yes")
            # break
        n1,n2=n2,n1+n2
# print(check_fibonacci_num(5))
"""print ASCII Value of a character"""
# print(ord("g"))
"""
smallest value and largest value  in list
"""
lst=[-4,-3,-55,-2,-33]
min =lst[0]
max =lst[0]
for n in lst:
   if n > max:
       max =n
   if n < min:
       min=n
# print(max) #-2
# print(min)#2
""" find second largest number in a list"""
def second_largest(lst):
    first= lst[0]
    second= 0
    for i in lst:
        if i>first:
            first,second =i,first
        elif first > i > second:
            second= i
    return second
# print(second_largest([7,-4,1,-4,-5,2,-6]))#2
 # minimum = float('-inf')
    # first, second = minimum, minimum
    # for n in numbers:
    #     if n > first:
    #         first, second = n, first
    #     elif first > n > second:
    #         second = n
    # return second if second != minimum else None
"""find N largest elements from a list"""
def N_max_elements(lst,n):
    final=[]
    for i in range(n):
        max =0
        for ele in lst:
            if ele > max:
                max=ele
        lst.remove(max)
        final.append(max)
    return final
# print(N_max_elements([1,3,2,4,5,1,60,],3)) #[60,5,4]
""" duplicates from a list of integers?"""
def duplicates(lst):
    unique=[]
    duplicate =[]
    for i in lst:
        if i in unique:
            if i not in duplicate:
                duplicate.append(i)
        else:
            unique.append(i)
    return duplicate
# print(duplicates([1,1,3,3,4,1,2,2,4,5,7]))#[1,2,3,4]


"""find Cumulative sum of a list
Input : list = [10, 20, 30, 40, 50]
Output : [10, 30, 60, 100, 150]
"""
def cumulative(lst):
    l =[sum(lst[:i+1]) for i in range(len(lst))]
    return l
# print(cumulative([10,20,30,40,50]))


"""Break a list into chunks of size N in Python"""
def break_list(lst,n):
    return [lst[i:i+n] for i in range(0,len(lst),n)]
# print(break_list([1,2,3,4,5,6,7,8,9,10],2))#[[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]


""" Sort the values of first list using second list
Input : list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
Output :['a', 'd', 'h', 'b', 'c', 'e', 'i', 'f', 'g']

"""


"""check if a string is palindrome or not"""
def str_palindrome(s):
    r =s[::-1]
    if r==s:
        print("palindrome")
    else:
        print("not palindrome")
# print(str_palindrome("hah"))
"""Reverse words in a given String in Python
Input : str = "geeks quiz practice code"
Output : str = "code practice quiz geeks"
"""
def reverse_word(s):
    lst = s.split(" ")
    print(" ".join(lst[::-1]))#code practice quiz geeks
    res_s = " ".join([i[::-1] for i in lst])
    print(res_s) #skeeg ziuq ecitcarp edoc
# reverse_word("geeks quiz practice code")
"""check if a string contains any special character"""
# print(any([not c.isalnum() for c in " Geeks$For$Geeks"]))#True

"""removing i-th character from a string"""
st ="testing"
n=4
f_st =""
for i in range(len(st)):
    if i==n:
        continue
    f_st+=st[i]
# print(f_st)#testng

"""Execute a String of Code in Python
Given few lines of code inside a string variable and execute the code inside the string."""

def exec_code():
    LOC = """ 
def factorial(num): 
    fact=1 
    for i in range(1,num+1): 
        fact = fact*i 
    return fact 
print(factorial(5)) 
"""
    exec(LOC)
# exec_code()#120

"""
Linear Search------------
Linear search is one of the simplest searching algorithms, and the easiest to understand. We can think of it as a ramped-up version of our own implementation of Python's in operator.
The algorithm consists of iterating over an array and returning the index of the first occurrence of an item once it is found:"""

def leaner_search(lst,st):
    for i in range(len(lst)):
        if lst[i]==st:
            return i
    return -1
result = leaner_search([1,2,'a','b'],'a')
if(result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result);


"""
Bubble Sort --------------------
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order."""
# Python program for implementation of Bubble Sort

def bubbleSort(arr):
    n =len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return (arr)
arr = [64, 34, 25,12, 12, 22, 11, 90]
print(bubbleSort(arr))#[11, 12, 12, 22, 25, 34, 64, 90]

