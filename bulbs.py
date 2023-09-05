'''
N light bulbs are connected by a wire.
Each bulb has a switch associated with it, however due to faulty wiring, a
switch also changes the state of all the bulbs to the right of current bulb.
Given an initial state of all bulbs, find the minimum number of switches you
have to press to turn on all the bulbs.
You can press the same switch multiple times.
Note: 0 represents the bulb is off and 1 represents the bulb is on.

Example Input:
a=[1,0,1,0,1]
n=5

Example Output:
4

'''
def countFlips(a,n):
    count=0
    for i in range(n):
        if a[i]==0:
            a[i]=1
            for j in range(i+1,n,1):
                if a[j]==1:
                    a[j]=0
                else:
                    a[j]=1
            count+=1
    return count

arr=[1,0,1,0,1]
print(countFlips(arr,len(arr)))
