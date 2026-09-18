# M - 1

# sum=0
# def NaturalSum(n):
#   global sum
#   if n==0:
#     return 0
#   sum=sum+n
#   NaturalSum(n-1)
# NaturalSum(6)  
# print(sum)

# M - 2

def NaturalSum(n):
  if n==1:
    return 1
  return n + NaturalSum(n-1)
print(NaturalSum(6)) 
