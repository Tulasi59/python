"""
============================================================
Complexity			:	O(n2)
============================================================
"""


class Sorting():
	def __init__(self):
		pass

	def selection(self, arr=[]):
		for i in range(len(arr)):
			min_num = i
			for j in range(i+1,len(arr)):
				if arr[min_num]>arr[j]:
					min_num = j
			arr[min_num],arr[i] = arr[i], arr[min_num]
		return arr

	def insertion(self,arr=[]):
		for i in range(len(arr)):
			for j in range(i+1,len(arr)):
				if arr[i]>arr[j]:
					arr[i], arr[j] = arr[j],arr[i]
		return arr

	def quicksort(self, arr=[]):
		for i in range(len(arr)):
			for j in range(0, len(arr)-i-1):
				if arr[j]>arr[j+1]:
					arr[j],arr[j+1] = arr[j+1],arr[j]
		return arr



if __name__ == '__main__':
	test_array_unsorted = [2,7,9,4,1,5,3,89,4,7,54,87,52,17]
	obj = Sorting()
	print(obj.selection(arr=test_array_unsorted))
	print(obj.insertion(arr=test_array_unsorted))
	print(obj.quicksort(arr=test_array_unsorted))
	print(obj.bubblesort(arr=test_array_unsorted))

	# a = {'a':7,'b':3,'c':2,'d':1}
	# print(obj.selection(arr=list(a.values())))
	#


'''insertion sort
bubble sort
quick sort
merge sort
selection sort

binary search
linear search

linked list'''