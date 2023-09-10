class Min_Heap:

    def __init__(self,capacity): #default constructor
        self.heap=[0]*capacity
        self.capacity=capacity
        self.size=0
    
    def getParent(self,index): #returns the index of parent node of the given index
        return (index-1)//2
    
    def getLeftChild(self,index): #returns the index of left child of the given index
        return 2*index+1
    
    def getRightChild(self,index): #return the index of right child of the given index
        return 2*index+2
    
    def hasParent(self,index): #returns a boolean value of whether the given index has a parent or not
        return self.getParent(index)>=0
    
    def hasLeftChild(self,index): #returns a boolean value of whether the given index has a left child or not
        return self.getLeftChild(index)<self.size
    
    def hasRightChild(self,index): #returns a boolean value of whether the given index has a right child or not
        return self.getRightChild(index)<self.size
    
    def parent(self,index): #returns the parent node of the given index
        return self.heap[self.getParent(index)]
    
    def leftChild(self,index): #returns the left child of the given index
        return self.heap[self.getLeftChild(index)]
    
    def rightChild(self,index): #returns the right child of the given index
        return self.heap[self.getRightChild(index)]
    
    def isFull(self): #checks whether the heap is full or not 
        return self.size==self.capacity
    
    def swap(self,index1,index2): #swaps the elements of two given indices
        temp=self.heap[index1]
        self.heap[index1]=self.heap[index2]
        self.heap[index2]=temp

    def push(self,data): #inserts elements to heap
        if self.isFull():
            print("Heap is Full") #if heap is full, print the statement
            return
        self.heap[self.size]=data #enter data to next empty cell
        self.size+=1 #increment size
        self.heapifyUp() #heapify the new array to make sure the parent nodes are smaller than child nodes
    
    def heapifyUp(self):
        index=self.size-1
        while self.hasParent(index) and self.parent(index)>self.heap[index]: #if parent exists and parent greater than child
            self.swap(self.getParent(index),index) #swap the parent and child
            index=self.getParent(index)
    
    def pop(self):
        if not self.size: 
            print("Empty Heap")
            return
        data=self.heap[0]
        self.heap[0]=self.heap[self.size-1]
        self.size-=1
        self.heapifyDown()
        return data

    def heapifyDown(self):
        index=0
        while self.hasLeftChild(index):
            smallerChildIndex=self.getLeftChild(index)
            if self.hasRightChild(index) and self.rightChild(index)<self.leftChild(index):
                smallerChildIndex=self.getRightChild(index)
            if self.heap[index]<self.heap[smallerChildIndex]:
                break
            else:
                self.swap(index,smallerChildIndex)
            index=smallerChildIndex
    
    # recursive insert and heapifyUp methods

    def push_r(self,data):
        if self.isFull():
            print("Heap is Full")
            return
        self.heap[self.size]=data
        self.size+=1
        self.heapifyUp_r(self.size-1)
    
    def heapifyUp_r(self,index):
        if self.hasParent(index) and self.parent(index)>self.heap[index]:
            self.swap(self.getParent(index),index)
            self.heapifyUp_r(self.getParent(index))

    def pop_r(self):
        if not self.size:
            print("Empty Heap")
            return
        data=self.heap[0]
        self.heap[0]=self.heap[self.size-1]
        self.size-=1
        self.heapifyDown_r(0)
        return data

    def heapifyDown_r(self,index):
        smallest=index
        if self.hasLeftChild(index) and self.heap[smallest]>self.leftChild(index):
            smallest=self.getLeftChild(index)
        if self.hasRightChild(index) and self.heap[smallest]>self.rightChild(index):
            smallest=self.getRightChild(index)
        if smallest!=index:
            self.swap(index,smallest)
            self.heapifyDown_r(smallest)
