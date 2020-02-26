"""interchange first and last elements in a list"""
l =[1,2,4,6,1,6,10]
s=len(l)
l[0],l[s-1] = l[s-1],l[0]
print(l)

