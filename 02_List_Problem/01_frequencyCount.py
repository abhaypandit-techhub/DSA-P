# M - 1 TC : O(n^2)

# n=[2,4,6,7,8,8,2,1,6,6]
# m=[1,2,3,4,5,6,7]
# for i in range(len(m)):
#   count=0
#   for j in range(len(n)):
#     if m[i]==n[j]:
#       count=count+1
#   print(f"The number of {m[i]} is {count}")    

# M - 2 TC : O(n+m) Better solution ( Using Hashing )

hash_lst=[0]*11
lst_1=[1,1,2,3,2,4,5,3,3,1,9,7,7]
lst_2=[1,10,15,3,2,34,7,8,45]

for num in lst_1:
  hash_lst[num]+=1

for num in lst_2:
  if num < 1 or num > 10:
    print(0)
  else :  
    print(hash_lst[num])   