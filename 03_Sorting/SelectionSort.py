# Method - 1

# arr_1=[23,67,34,15,45,50,39,27]
# for i in range (0,len(arr_1)-1):
#   for j in range (1+i,len(arr_1)):
#     if (arr_1[i] > arr_1[j]) :
#       swap=arr_1[i]
#       arr_1[i]=arr_1[j]
#       arr_1[j]=swap
# print(f"Required sorted array using selection sort : {arr_1}")

# Method - 2 ( Best Recommended )

nums=[5,7,8,4,1,6,9,2]
for i in range(0,len(nums)-1):
  min_index=i
  for j in range(i+1,len(nums)):
    if nums[min_index]>nums[j]:
      min_index=j
  nums[i],nums[min_index]=nums[min_index],nums[i]
print(nums)