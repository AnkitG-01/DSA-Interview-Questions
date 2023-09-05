def bubbleSort(arr):
    n=len(arr)
    swapped=False
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if swapped==False:
            break
l=[9,1,8,4,3,17,12]
bubbleSort(l)
print(l)