num=int(input('Enter the number:'))
sum=0
temp=num

while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10


if num==sum:
    print('%d is an armstrong number'%(num))
else:
    print('%d is not an armstrong number'%(num))
