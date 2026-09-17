lst=[9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5]
n=len(lst)
for i in range(1,n):
    key=lst[i]
    j=i-1
    while j>=0 and lst[j]>key:
        lst[j+1]=lst[j]
        j-=1
    lst[j+1]=key
print(lst)        