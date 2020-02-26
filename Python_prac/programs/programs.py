class Sorting():
    def __init__(self):
        pass

    def insertion_sorting(self):
        pass

    def bubble_sorting(self,arr=[]):
        """"Bubble sort, sometimes referred to as sinking sort,
        is a simple sorting algorithm that repeatedly steps through
        the list to be sorted, compares each pair of adjacent items and swaps
        them if they are in the wrong order.
        The pass through the list is repeated until no swaps are needed"""

        n = len(arr)
        for i in range(n):
            for j in range(0,n-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
        return arr

    def quick_sorting(self):
        pass

    def merge_sorting(self):
        pass

    def selection_sorting(self):
        pass

    def heap_sorting(self):
        pass


# if __name__=="__main__":
#     Obj = Sorting()
#     array=[2,4,1,5,8,-1]
#
#     print(Obj.bubble_sorting(arr=array))
import practise
print(practise)
    # print(practise.test())
    # print("djjjjjjjjjj")
if __name__ == practise:
    practise.test()