l1=[1,2,3,4]
l2=[5,6,7,8]
l3=['Jigyasa',102,'xyz']

print(l1[:])  #indexing of list
print(l1[0:])
print(l1[1:3])
print(l1[-1])
print(l1[:-1])

l1[2]=10 #updating list
print('New list is',l1) 
l1[1:3]=[15,19]
print('New list is',l1)

for i in l2:  #iterating a list
    print(i)

print(l2+l3) #concatenation operator conacatenates the list mentioned.

print(l1*2) #repetition operator : repeates the list for multiple times.

print(1 in l1)  #membership operator: returns true if mentioned item is present in list.

print(5 not in l1) #membership operator: returns true if mentioned item is not present in list.

print(len(l1)) #returns the length of list.

print(max(l1)) #returns maximum item of list.

print(min(l1)) #returns minimum item of list.

print(list((1,2,6,8))) #converts any sequence into list.

l1.append(46) #Elements inside append() is added to list.
print(l1)

l2.clear()  #Removes all elements fromt the list.
print(l2)

l3.remove('xyz') #remove specified object from list.
print(l3)

print(l3.copy()) #return a copy of list.

print(l1.count(1)) #returns the number of occurence of specified object in list.

print(l3.index('Jigyasa')) #returns the lowest index in list that when object appears.

l3.extend('Jigyasa') #sequence in extend is extended into the list.
l3.extend('1')
print(l3)

l1.insert(0,45)  # adds the specified element at specified index in string.
print(l1)

print(l1.pop()) #removes and return the last object of list.
print(l1)

l3.reverse() #reverses the list.
print(l3)

l1.sort() #sorts the list.
print(l1)



