numbs=[3,5,6,4,8,9,10,7,1]
n=len(numbs)
for i in range(0,n):
  for j in range(0,n-i-1):
    if numbs[j]>numbs[j+1]:
      numbs[j],numbs[j+1]=numbs[j+1],numbs[j]
print(numbs)      
