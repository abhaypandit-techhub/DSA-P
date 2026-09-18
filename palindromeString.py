
# WITHOUT RECURSION PALINDROME STRING
          
# def palindromeString(stri,left,right):
#    while left<right:
#       if stri[left]!=stri[right]:
#          return False
#       return True
# stri="nitin"
# print(palindromeString(stri,0,len(stri)-1))  


# RECURSION SOLVING PALINDROME STRING M-1

# def palindromeString(stri,left,right):
#    while left<right:
#       if stri[left]!=stri[right]:
#          return False
#       palindromeString(stri,left+1,right-1)
#       return True
# stri="niti0"
# print(palindromeString(stri,0,len(stri)-1))  


# USING RECURSION SOLVING PALINDROME STRING M-2

def palindromeString(stri,left,right):
   if left>=right:
      return True
   if stri[left]!=stri[right]:
      return False
   return palindromeString(stri,left+1,right-1)
stri="nitin"
print(palindromeString(stri,0,len(stri)-1))  