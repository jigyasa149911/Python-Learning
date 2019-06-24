salary=int(input('Enter your salary:'))
if(salary<1000):
    print("You don't have to pay the tax.")
elif(salary>=1000 and salary<2000):
    print("You have to pay 5% tax.")
elif(salary>=2000 and salary<4000):
    print("You have to pay 10% tax.")
else:
    print("You have to pay 12% tax.")
    
