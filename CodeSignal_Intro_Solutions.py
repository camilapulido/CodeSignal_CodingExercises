# -*- coding: utf-8 -*-
"""
Author: Camila Pulido
Code Signal -- Arcade --
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
def matrixElementsSum(matrix):
    matrix2 = matrix
    if len(matrix2)>1:
        for floor in range(1,len(matrix2)):
            for room in range(0,len(matrix2[floor])):
                if matrix2[floor-1][room] == 0:
                    matrix2[floor][room] = 0
    
    availability = 0
    for floor in matrix2:
           availability+=sum(floor)              
    return (availability, matrix2)

#%%

def allLongestStrings(inputArray):
    LongestString =max(len(i) for i in inputArray)
    outputArray =[i for i in inputArray if len(i) == LongestString]
    return outputArray

#%%
def countcaracter(s1,s2):
    total = 0
    for i in set(s1):
        if i in s2:
            total += min(s1.count(i),s2.count(i))
    return total

#%%
def luckynumber(n):
    m = str(n)
    f = [int(m[i]) for i in range(0,int(len(m)/2))] 
    s = [int(m[i]) for i in range(int(len(m)/2),len(m))] 
    return sum(f) == sum(s)

#%%
def sortyHeight(a):
    b = [x for x in sorted(a) if x>=0]
    n =0
    for i in range(0,len(a)):
        if a[i] >=0:
           a[i] = b[n]
           n+=1
        else:
            continue
    return a

#%%

def reverseParenthesis(inputString):
    Output = inputString
    for i, e in reversed(list(enumerate(Output))):
        if  e =='(':
            c = Output.index(")",i,)
            Output = Output.replace(Output[i:c+1],Output[c-1:i:-1])
    return Output


#%%

def reverseParenthesis2(s):
    print (s)
    for i in range(len(s)):
        if s[i] == "(":
            start = i
        if s[i] == ")":
            end = i
            
            return reverseParenthesis2(s[:start] + s[start+1:end][::-1] + s[end+1:])
            
    return s


#%%

def addborder(picture):
   l = len(picture[0])+2
   return ['*'*l]+[x.center(l,'*') for x in picture]+['*'*l]
    
#%%
def AlmostSimilar(a,b):
    notinloc = [i for i,x in enumerate(b) if x != a[i]]
   
    if len(notinloc) != 2:
       return False

    if not notinloc:
       return False
    
    return a[notinloc[0]]==b[notinloc[1]] and a[notinloc[0]]==b[notinloc[1]]
#%%%
def arrayChange(inputArray):
    outputArray = inputArray.copy()
    for i in range(1,len(inputArray)):
        if inputArray[i] <= outputArray[i-1]:
            outputArray[i] = (outputArray[i-1] + 1)
    return (sum(outputArray)-sum(inputArray))

#%%
def arrangePalindrome(a):
    return sum([a.count(i)%2 for i in set(a)]) <= 1

#%%
def jumpObstacles2(inputArray):
    step =2
    while True:
        if all(x%step!=0 for x in inputArray):
            return step
        step=step+1
#%%
def BoxBlur(image):
    imageWidth = len(image[0])
    imageheight = len(image)
    
    blurimage = []
       
    for y in range(1,imageheight-1):
        test=[]
        for x in range(1,imageWidth-1):
            Top = sum(image[y-1][x-1:(x-1)+3])
            Bottom = sum(image[y+1][x-1:(x-1)+3])
            Center = (image[y][x-1] + image[y][x]+image[y][x+1])
            test.append((Top+Bottom+Center)//9)
        blurimage.append(test)    
    return blurimage
#%%
