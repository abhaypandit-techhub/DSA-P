def recursionBubbleSort(arr,i):
  n=len(arr)
  if i==n-1:
     return
  for j in range(n-i-1):
      if arr[j]>arr[j+1]:
        arr[j],arr[j+1]=arr[j+1],arr[j]
  i=i+1
  return recursionBubbleSort(arr,i)
arr=[3,7,5,2,1,8]
recursionBubbleSort(arr,0)
print(arr)
      