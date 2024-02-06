# -*- coding: utf-8 -*-
"""
Author: Camila Pulido
Code Signal -- Arcade -- Level-1
"""

#%%
def CenturyFromYear(year):
    Century = int(year/100)  
    if(year/100) == Century:
        return Century
    if(year/100)>= Century+0.01:
        return Century + 1

#%%
def checkPalindrome(inputString):
    reverStrg = inputString[::-1]
    return reverStrg == inputString

#%%
def adjacentElementsProduct(inputArray):
    value = inputArray[0]*inputArray[1]
    for i in range(len(inputArray)-1):
        if value < (inputArray[i]*inputArray[i+1]):
            value = inputArray[i]*inputArray[i+1]
    return value
        
#%%
def MakeArrayConsecutive2(statues):
    result = [i for i in statues if i >= 0 and isinstance(i, int)] or None
    result= list(set(result))
    result.sort()
    return ((result[len(result)-1]-result[0])+1)-len(result)

#%%

def almostIncreasingSquence(sequence):
    counter = 0
    for idx in range(1, len(sequence)):
        if sequence[idx] <= sequence[idx-1]:
            counter += 1
            if idx - 2 >= 0 and idx + 1 <= len(sequence)-1:
                if sequence[idx] <= sequence[idx-2] and sequence[idx+1] <= sequence[idx-1]:
                    counter += 1
    return counter <= 1  

#%%