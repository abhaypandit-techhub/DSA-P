# def reverseArray(lst,i):
#   if i == len(lst) :
#     return
#   reverseArray(lst,i+1)
#   rev_lst.append(lst[i])
# rev_lst=[]
# lst=[5,7,3,2,6,1,5,9]
# reverseArray(lst,0)
# print(rev_lst)

# M - 2
def reverseArray(lst,left,right):
  if left >= right:
    return lst
  lst[left],lst[right]=lst[right],lst[left]
  return reverseArray(lst,left+1,right-1)
lst=[1,2,3,4,5,6,7,8,9]
print(reverseArray(lst,2,5))
# reverseArray(lst,0,len(lst)-1)