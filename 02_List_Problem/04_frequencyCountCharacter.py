s="abhayalokkunal?/?@"
hash_list=[0]*128
q=['@','a','/','s']
for ch in s:
  index=ord(ch)
  hash_list[index]+=1
for chr in q:
  index=ord(chr)
  print(hash_list[index])   