t1=(101,'Ankit',23)
t2=('Apple','Banana','Mango')
t3=()
t4=45,
t5=(19,5,6,1)
l1=[4,5,6,7]
print(type(t4))

print(t1[:]) #indexing and slicing of tuples.
print(t1[0:])
print(t2[0:2])
print(t2[-1])
print(t1[:-1])

del(t4) #deletes the entire tuple.

print(t1*2) #Repetition operator: enables tuple items to be repeated multiple times.

print(t1+t2) #Concatenation operator : concatenates tuples mentioned on either sides of operator.

print('Ankit' in t1) #Memebrship operator : returns true if specified element is present in tuple.
print('Jigyasa' not in t1) #Memebrship operator : returns true if specified element is not present in tuple.

for i in t1:  #iteration of tuple.
    print(i)

print(len(t1)) # returns length of tuple.

print(max(t2)) #returns maximum element of tuple.
print(max(t5))

print(min(t2)) #returns minimum element of tuple.
print(min(t5))

print(tuple([2,5])) #converts any sequence into tuple.
print(tuple(l1))


Students=[(1,'Ayush',45),(2,'Ankita',19)] #Nesting of list and tuple.
for i in Students:
    print(i)

Students[1]=(3,'Beena',67)
for i in Students:
    print(i)


