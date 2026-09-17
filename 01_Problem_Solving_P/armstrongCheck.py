print("Checking armstrong number")
n=int(input("Enter a number : "))
num=n
sum=0
count=0
lst=list(str(n))
for i in lst :
  count+=1
# count  number M-2
# nod=len(str(n))
while num > 0 :
  rem=num%10
  sum=sum+rem**count
  num=num//10
if sum == n :
  print(f"{n} is armstrong number")  
else :  
  print(f"{n} is not armstrong number")  
