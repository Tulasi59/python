""" Find length of list without using loop and built in functions or with Recursion function"""
def len_of_list(lst):
    if lst==[]:
        return 0
    return 1+len_of_list(lst[:-1])
    # or
    # return 0 if lst == [] else 1 + len_of_list(lst[:-1])
print(len_of_list(lst=[1,2,4]))

"""
Qns:why change list inside tuple?
 Ans :mutable objects stored in a tuple do not lose their mutability 
 e.g. you can still modify inner lists using list methods
 
 You cannot modify the elements in a tuple but 
 you are allowed to modify the list which will reflect in the tuple.
 By this way you can modify the elements in a tuple
"""



