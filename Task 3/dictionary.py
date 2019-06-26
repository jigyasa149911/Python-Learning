employee={'Name':'Ayush','Age':29,'salary':25000,'company':'tcs'}

print(type(employee))
print(employee)

#accessing ditionary items.

print('Name:%s'%(employee['Name']))
print('company:%s'%(employee['company']))
print('Age:%d'%(employee['Age']))
print('Salary:%d'%(employee['salary']))


#updating dictionary values.

'''employee['Name']=input('Name:')
employee['Age']=int(input('Age:'))
employee['salary']=int(input('Salary:'))
employee['company']=input('Company:')
print(employee)'''

#deleting dictionary elements.

del employee["Name"]
del employee['company']
del employee['Age']
del employee['salary']
print(employee)
del employee

employee={'Name':'Ayush','Age':29,'salary':25000,'company':'tcs'}
# for loop to print all keys of dict.
for i in employee:
    print(i)

# for loop to print all values of dict.
for i in employee:
    print(employee[i])

#for loop for printing values of dict using values().
for i in employee.values():
    print(i)

#for loop for printing keys of dict using keys().
for i in employee.keys():
    print(i)

#for loop for printing items of dict using items().
for i,j in employee.items():
    print(i,j)

print(len(employee)) #returns length of the dict.

x=str(employee) # converts dict. into printable string representation.
print(x)

y=employee.items() #returns dict. items.
print(y)

z=employee.keys() #returns keys of dict.
print(z)

a=employee.values() #returns values of dict.
print(a)

employee.update({'Rank':3}) #update dict. by adding key-value pair of dict. in argument to this dict.
print(employee)

x=employee.copy() #returns copy of dict.
print(x)

p=employee.popitem() #removes last pair of dict. and returns the pair.
print('Removed',p)

p=employee.pop('salary') #removes item associated to specified key.
print(employee)
p=employee.pop('salary',100) #returns default value if specified item associated to key is not present.
print(p)

employee.clear() #used to delete all items of dict.
print(employee)

employee={'Name':'Ayush','Age':29,'salary':25000,'company':'tcs'}
c=employee.setdefault('Age',100) #returns the value of key if key is present otherwise return defaut which is none for python.
print(c)
c=employee.setdefault('Rank',)
print(c)






                    
