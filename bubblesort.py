"""aList=[3,5,6,3,1,22,34]
n=len(aList)
print(aList)
for i in range(1,n):
    for j in range(n-i-1):
        if aList[j]<aList[j+1]:
            aList[j],aList[j+1]=aList[j+1],aList[j]
print(aList, 'descending order')
"""
'For ascending order:'
aList=[3,5,6,3,1,22,34]
n=len(aList)
print(aList)
for i in range(1,n):
    for j in range(n-i-1):
        if aList[j]>aList[j+1]:
            aList[j],aList[j+1]=aList[j+1],aList[j]
print(aList)
