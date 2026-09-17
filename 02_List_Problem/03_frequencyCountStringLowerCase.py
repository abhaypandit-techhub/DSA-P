# using hashing

s="abhaykumarmy"
q=['a','q','p','b','y']
hash_list=[0]*27
for ch in s:
  index=ord(ch)-97
  hash_list[index]+=1

for ch in q:
  index=ord(ch)-97
  print(hash_list[index])  