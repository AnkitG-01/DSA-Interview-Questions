'''
Given two integer arrays A and B of size N. There are N gas stations along a
circular route, where the amount of gas at station i is A[i].
You have a car with an unlimited gas tank and it costs B[i] of gas to travel 
from station i to its next station (i+1). You begin the journey with an empty 
tank at one of the gas stations.
Return the minimum starting gas station's index if you can travel around the
circuit once, otherwise return -1.
You can only travel in one direction. i to i+1, i+2, ... n-1, 0, 1, 2.. Completing
the circuit means starting at i and ending up at i again.

Example Input:
gas=[5,8,2,8]
cost=[6,5,6,6]

Example Output:
3

'''
def canCompleteCircuit(gas, cost):
        if sum(gas)<sum(cost): #if total gas is less than total cost of journey its not possible to finish the journey
            return -1
        total=0
        res=0
        for i in range(len(gas)):
            total+=(gas[i]-cost[i])
            if total<0:
                total=0
                res=i+1
        return res
gas=[5,8,2,8]
cost=[6,5,6,6]
print(canCompleteCircuit(gas,cost))