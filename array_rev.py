'''
Reverse an array/list

'''
def rev(arr):
    last=len(arr)
    for i in range(last//2):
        arr[i]=arr[i]+arr[last-1-i]
        arr[last-1-i]=arr[i]-arr[last-1-i]
        arr[i]=arr[i]-arr[last-1-i]
    return arr
list=[int(i) for i in input("Enter array: ").split()]
print(rev(list))