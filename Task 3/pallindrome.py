def pallindrome(n):
    temp=n
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    if temp==rev:
        return 1
    else:
        return 0


n=int(input('Enter the number:'))
ans=pallindrome(n)
if ans==1:
    print('%d is pallindrome'%(n))
else:
    print('%d is not pallindrome'%(n))
    
