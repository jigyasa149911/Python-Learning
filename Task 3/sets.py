set1={'apple','banana','cherry'}
set2={'english','spanish','french','apple'}
set3={'a','b','c'}
set4={'apple','f','g','a','b','c'}

print(set1)

for i in set1: #iterating the set.
    print(i)
print('banana' in set1) #checking if an item is present in the set or not.

#Changing items.

set1.add('orange') #add() is used to add one item in set.
print(set1)

set3.update(['e','f','g']) # update() is used to add more than one item in the set.
print(set3)

print(len(set1)) #returns the length of the set.

#Removing an item.

set1.remove('orange') #remove specified element from the set.
print(set1)

set1.discard('fruit') #remove specified element from the set,doesn't generate error if item is not present in set.
print(set1)

x=set3.pop() #removes item from last of set and returns the popped item.
print(x)

set3.clear() #empties the set.
print(set3)

del set3 #deletes the set.

set3=set(('a','b','c','d','e')) #set constructs set from any given sequence .
print(set3)

y=set2.union(set3) #returns a set containing union of two sets.
print(y)

z=set1.difference(set2) #returns a set containing items of only set1 and not set2.
print(z)

set3.difference_update(set4) #deletes the items that are common in other set ,from original set.
print(set3)

a=set1.intersection(set2) #returns a new set containing common elements of both set.
print(a)

set1.intersection_update(set2) # removes uncommon items from original set.
print(set1)

b=set1.isdisjoint(set3) #returns true if two sets doesn't contains similar items.
print(b)

c=set3.issubset(set4) #returns true if all items of set 3 is in set4.
print(c)

d=set4.issuperset(set3) #returns true if items of set 3 are all present in set4.
print(d)

set1={'apple','banana','cherry'}
set2={'english','spanish','apple'}

e=set1.symmetric_difference(set2) #returns a set with symmetric difference of two sets.
print(e)

set1.symmetric_difference_update(set2) # inserts symmetric difference from this set or another in original set.
print(set1)












