# M = 1 O(n*m)


# lst_1=[1,1,2,3,2,4,5,3,3,1,8,9,7,7]
# lst_2=[1,10,15,3,2,34,7,45]
# dict={}
# for i in lst_2:
#   count=0
#   for j in lst_1:
#     if i == j :
#      count+=1
#   dict[i]=count
# print(dict)


# M = 2 O(n+m) Better solution

       # lst_1=[1,1,2,3,2,4,5,3,3,1,8,9,7,7]
# lst_2=[1,10,15,3,2,34,7,45]
# dict={}
# dict1={}
# for j in lst_1:
#   dict[j]=dict.get(j,0)+1
# for k in lst_2:
#   dict1[k]=dict.get(k,0)
# print(dict1)


lst_1=[1,1,2,3,2,4,5,3,3,1,8,9,7,7]
lst_2=[1,10,15,3,2,34,7,45]
dict={}
for j in lst_1:
  dict[j]=dict.get(j,0)+1
print(dict)  
print(dict[10])  
# freq={num : dict.get(num,0) for num in lst_2 }
# print(freq)


  




