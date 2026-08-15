List=[34,56,19,29,45,16,37]
target=37
found=0

for i in range(0,len(List)):
  if(List[i]==target):
    found=1
    break

if(found==1):
    print(f"Element are found in array that is {target} at index {i}")
else :
    print(f"Element are not found in array that is {target}")