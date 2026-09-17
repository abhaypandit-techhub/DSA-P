def QuickSort(nums,low,high):
  if low < high :
    p_index=partision(nums,low,high)
    QuickSort(nums,low,p_index-1)
    QuickSort(nums,p_index+1,high)
def partision(nums,low,high):
  pivot=nums[low]
  i=low
  j=high
  while i<j:
    while nums[i]<=pivot and i<=high-1 :
      i+=1
    while nums[j]>=pivot and j>=low+1 :
      j-=1
    if i<j :
      nums[i],nums[j]=nums[j],nums[i] 
  nums[low],nums[j]=nums[j],nums[low]
  return j
nums=[1,3,5,7,2,0,4]
QuickSort(nums,0,len(nums)-1)
print(nums)
