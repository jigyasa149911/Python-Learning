num=int(input('Enter the number:'))

if num>0:
    for i in range(2,num):
        if (num%i)==0:
            print(num,'is not a prime number')
            print(i,'times',num//i,'is',num)
            break
    else:
        print('%d is a prime number'%(num))
else:
    print('%d is not a prime number'%(num))
    
