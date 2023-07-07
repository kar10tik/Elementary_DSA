a=[1,2,4,3,2,2,14,93]
print('Ornl list', a)
for i in range(1,len(a)):
    key=a[i]
    j=i-1
    while j>=0 and key>a[j]: '''reverse comparison sign for ascending'''
        a[j+1]=a[j]
        j=j-1
    else:
        a[j+1]=key
print('Sorted list, descending', a)
