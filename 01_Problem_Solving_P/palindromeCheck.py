print("Checking number is palindrome or not")
n=int(input("Enter a number :"))
num=n
sum=0
while num > 0 :
  rem=num%10
  sum=sum*10+rem
  num=num//10

if sum == n :
  print(f" The Given number is {n} is palindrome")  
else :
  print(f" The Given number is {n} is not palindrome")   
