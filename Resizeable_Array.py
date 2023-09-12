'''
Design Dynamic Array (Resizable Array):

Design a Dynamic Array (aka a resizable array) class, such as an ArrayList in Java or a vector in C++.

Your DynamicArray class should support the following operations:

DynamicArray(int capacity) will initialize an empty array with a capacity of capacity, where capacity > 0.
int get(int i) will return the element at index i. Assume that index i is valid.
void insert(int i, int n) will insert the element n at index i. Assume that index i is valid.
void pushback(int n) will push the element n to the end of the array.
int popback() will pop and return the element at the end of the array. Assume that the array is non-empty.
void resize() will double the capacity of the array.
int getSize() will return the number of elements in the array.
int getCapacity() will return the capacity of the array.
If we call void pushback(int n) but the array is full, we should resize the array first.

'''
class DynamicArray:
    
    def __init__(self, capacity: int):
        self.cap=capacity
        self.size=0
        self.array=[0]*capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def insert(self, i: int, n: int) -> None:    
        self.array[i]=n
    
    def pushback(self, n: int) -> None:
        if self.size==self.cap:
            self.resize()
        self.array[self.size]=n
        self.size+=1

    def popback(self) -> int:
        popped=self.array[self.size-1]
        self.size-=1
        return popped

    def resize(self) -> None:
        self.cap*=2
        arr=[0]*self.cap
        for i in range(self.size):
            arr[i]=self.array[i]
        self.array=arr

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.cap
