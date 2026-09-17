n=4567
num=n
print(f"The reverse of the number {n} is")
while(num>0):
  digit=num%10
  print(digit,end="")
  num=num//10
