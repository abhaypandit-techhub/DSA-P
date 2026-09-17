# Solution - 1

# print("Finding number of factor of given number")
# n=int(input("Enter a number : "))
# lst=[]
# for i in range(1,n+1):
#   if n%i==0 :
#     lst.append(i)

# print(lst)

# Optimise solution - 2

# print("Finding number of factor of given number")
# n=int(input("Enter a number : "))
# lst=[]
# for i in range(1,n//2+1):
#   if n%i==0 :
#     lst.append(i)
# lst.append(n)
# print(lst)

# Optimal solution -3
import math
lst=[]
print("Finding number of factor of given number")
n=int(input("Enter a number : "))
for i in range(1,int(math.sqrt(n))+1):
  if n%i==0 :
    lst.append(i)
    if n//i !=i :
     lst.append(n//i)

print(lst)
print(sorted(lst))