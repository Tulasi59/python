"""1)  l=[k1:v1,k2:v2,k3:v3]
can use a=[1,2,4] as a key :ans NO
can use b=(1,2,3) :ans YES
"""

""" 2) reverse string 
Ex: s =globaldata
ans : s[::-1]

ex: s[::2] 
ans : goadt

ex: s[2::]
ans: obaldata

https://docs.python.org/2.3/whatsnew/section-slices.html
"""

"""3)
l1 =[1,2,3,4,5,6,7,8,9,10]
output =[[1,2],[3,4],[5,6],[7,8],[9,10]]
"""
l1 =[1,2,3,4,5,6,7,8,9,10]
l2 =[l1[i:i+2]for i in range(0,len(l1),2)]
print(l2) #[[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]

"""
4)
l =[1,2,4,6,8,10,12]
find missing elements
output =3,5,7,9,11
"""
l = [1,2,4,6,8,10,12]
m_l =[i for i in range(1,max(l)) if i not in l]
# print(m_l) #[3, 5, 7, 9, 11]
"""https://www.aspsnippets.com/Articles/jQuery-AJAX-call-with-parameters-example-Send-parameters-to-WebMethod-in-jQuery-AJAX-POST-call.aspx
just refer for ajax
"""
"""5)
l=[1,2,3,4,5,6,7]
find gt 2 and lt 7 values in list using lambda and comprehension
"""
l=[1,2,3,4,5,6,7]
#comprehension
l2 =[x for x in l if 2<x<7]
# lambda
l2 = list(filter(lambda x:2<x<7,l))
# print(l2) #[3, 4, 5, 6]

"""
6)class based views and function based views in django
7)how render data in font end get data from back end 
8)ajax calling 
9)static files in django
10)how to render bluk data from database
11)differnece between filter and get in ORM queries
12)how to deployment your project
https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-uwsgi-and-nginx-on-ubuntu-14-04

13)which server you are using
14)how to create app in djnago project
15)can we use multiple databases in django
16)can u use different database host in django
17)what are varibles in database in settings.py
18)i have one table in my database ..how can connect with this table to django with command
19)how to add app to project
20)how render data in jinja template
21)diff b/w list and tuple
22)diff b/w list and set
23) diff b/w append and extend
24)l=[1,2,1,2,3] counting of elements
output={1:2,2:2,3:1}

l1 =[1,1,23,2,3,2,2,3,1]
from collections import Counter
print(dict(Counter(l1)))# {1: 3, 2: 3, 3: 2, 23: 1}

without built in functions

d ={}
for i in l1:
    if i in d:
        d[i]+=1
    else:
        d.update({i:1})
print(d)

25) diff b/w threading and multi threading
26)how to pass variables in url

27)what is url reverse
28)context processors
29)staticroot and templete dir in django
30)what is middlewares
31)type of django response
32)diff b/w render ,http response and redirect 
33)django authencations
34)what is @login_required
35)pass data form views to template
36)which one is excuted function or decorator
37)count the number of conscutive pairs in list
    input=[1,1,2,2,3,4,5,6,6]
    output =[1,2,6]
38)max num of list..list contains only -ve values 
39)searching and sorting list without inbluit functions

"""

"""
a =2. # print(a) :2.0
a,b =x,y #print(a,b)  :x,y
a =x,y # print(a) :(x,y) tuple packing
a,b,c =x,y,z #print(a,b,c) :(x,y,z)
a,b,c =x,y #need more than 2 values to unpack
a,b = x,y,z #too many values to unpack
"""
"""
reverse list 
list = ["11", "12", "11ddasa"]
i =0
j = len(list)-1
while i<j:
    list[i],list[j] =list[j],list[i]
    i+=1
    j-=1
print(list) #['11ddasa', '12', '11']
"""


# l = [1, 2, 3]
#
# k = [1, 2, 3, 4, 5]
#
# print zip(l, k)
#
# print set(l)  # what it will return

# write main datatypes in python

# write default import modules in python

# write amstrong number

# write lambda function

# write syntax of map

# Remove duplicates in list (l = [1,2,3,4,1,5,6,7,1]) without using predefined methods

# write syntax of list comprehension

# update {'a':2} to {'b':1} # {b:2}
"""l1 ={'a':2}
l2={'b':1}
l2['b'] =l1['a']
print(l2) #{"b":2}"""
# update {'a':1} to {'a':1, 'b':1}
"""
l1={'a':1}
l2={'b':1}
l1.update(l2)
print(l1) #{'a':1, 'b':1}"""

#differnece between python 2.7 and 3

#differnece between xrange and range

#differnece between list and tuple

#is it possible to give key as a tuple in dictionary, why?

#what is scraping

#reverse a string "sai ram" using predefined method and logic

#what is threading and multithreding

"""
smallest value and largest value  in list
"""
lst=[-4,-3,-55,-2,-33]
min =lst[0]
max =lst[0]
for i in range(len(lst)):
    if lst[i]<min:
        lst[i],min =min,lst[i]
    if lst[i]>max:
        lst[i],max =max,lst[i]
print(max) #-2
# print(min)#2

"""
sorting list
"""
lst=[4,3,55,2,33,1]
for i in range(len(lst)):
    for j in range(i,len(lst)):
        if lst[i]>lst[j]:
            lst[i],lst[j] =lst[j],lst[i]
# print(lst) #[1, 2, 3, 4, 33, 55]
""" find N(3)largest elements from a list"""
# print(lst[:3]) #[1, 2, 3]
""" find second largest number in a list"""
# print(lst[-2]) #33


"""list is sortedor not """
def check_list_sorted(list):
    flag=0
    i=1
    while i<len(list):
        if list[i]<list[i-1]:
            flag =1
        i+=1
    if flag:
        print("list is not sorted")
    else:
        print("list is sorted")
# print(check_list_sorted([10,1,2,3,4]))


"""Program to print duplicates from a list of integers
Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
Output : output_list = [20, 30, -20, 60]
"""

def duplicate_elements(lst):
    new_list=[]
    duplicate=[]
    for i in lst:
        if i in new_list:
            if i not in duplicate:
                duplicate.append(i)
        else:
            new_list.append(i)
    return duplicate
# print(duplicate_elements(lst = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]))







