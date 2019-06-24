str="AMERICA"  #declaration of string
print(str)

str1='UNITED STATES OF '
print(type(str1))

print(str[:])
print(str[0:])
print(str[:6])
print(str[1:6])
print(str[1:7]) #this is slicing of string where [] is slicing operator.

print(str[-1])
print(str[:-1]) #this is negative indexing.

str='America' #reassignment of string
print(str)

str2=str1+str  #Concatenation operator
print(str2)


str2=2*str  #Repetition operator
print(str2)

print('A' in str) #Membership operator

print('S'not in str)  #Membership operator(works reverese of  memebership operator.

print('The string is :%s'%str)  # formatting operator '%'.

print('USA stands for %s%s'%(str1,str))


print(str.lower())  #lower() changes string into lower case only.

print(str.upper()) #upper() changes string into upper case only.

print(str.title()) #title() changes string into title case .

print(str.isalnum()) #returns true if string contains only alphanumeric characters and no symbols.

print(str.isalpha()) #returns true if string contains only alphateic charactersand no symbol.

print(str.islower()) # returns true if the string is in lowercase only.

print(str.isupper()) #returns true if the string is in uppercase only.

print(str.isnumeric()) #returns true if string characters consist only numeric characters.

print(str.isdecimal()) #it returns true if all charaters in string are decimals.

print(str.isdigit()) #it returns true if all characters are digit and there is at least one character.

print(str.isspace()) #returns true if string contains only whitespace character .

print(str.isidentifier()) #returns true if the string is an valid identifier.

print(str.isprintable()) #it returns true if all character of string are printable or string is empty.

print(str.swapcase()) #it inverts case of all characters in string.

str3=' '
print(str3.isspace())

print(str.istitle()) # returns true if string is in title case .

print(len(str))  #returns length of string.

print(str.capitalize()) #capitalise first character of the string.

print(" ".join(str)) #Adding whitespaces in string.

print("".join(reversed(str))) #string reverse using join function.

print(",".join(['ABC','DEF','GHI']))

print(str1.split()) #splits the string into a list of strings separated by whitespaces.
print(str1.split('A')) #remove a particular letter from string.

print(str1.replace('STATES','States')) #replace a substring from another substring.

print(str.casefold()) #returns a version suitable for case-less comparisons.







