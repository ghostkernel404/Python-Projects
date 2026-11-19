'''slice= 'Good Morning good Afternoon'
print(slice[-14:-10])
print(slice[-17:-21-1:-2])
print(slice[-14:-22-1:-2])'''

#Check whether the given input is tuple or not
'''s=eval(input("Enter the elements:"))
if type(s)==tuple:
    print("Yes")
else:
    print("Noo")'''

#Check whether the given string is palindrome or not
'''s=input("Enter the string:")
if s==s[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")'''
    
#Check whether the string has exactly 5 characters or not
'''s=input("Enter the string:")
if len(s)==5:
    print("yes")
else:
    print("No")'''
    
#Check whether the given number is 2 digit or not
'''n=int(input("Enter the numbers:"))
if 10<=n<=99:
    print("Yes")
else:
    print("No")'''
    
#Check whether the relation between to numbers
'''a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
if a>b:
    print("The first number is greater")
elif b>a:
    print("The second number is greater")
else:
    print("Both are equal")'''
    
#Check whether the given character is upper,lower,number or special character
'''n=input("Ente the character:")
if 'A'<=n<='Z':
    print("It is upper case character")    
elif 'a'<=n<='z':
    print("It is lower case character")
elif '0'<=n<='9':
    print("It is a digit")
else:
    print("It is a special character")'''
    
#Check whether given alphabet is ovel or consonant
'''ch=input("Enter the character:")
if ch=="aeiouAEIOU":
    print("It is a vowel")
else:
    print("It is a consonant")'''
    
#check whether given list is even or odd
'''list=eval(input("Enter the list:"))

if len(list)%2==0:
        print(list,"is even")
else:
    print(list,"is odd")'''

'''i=1
while i<=10:
     print("Hello")
     i+=1'''
     
#print all the elements inside the list using while loop
'''list=eval(input("Enter the list:"))
i=0
while i<len(list):
    print(list[i])
    i+=1
'''
#Reverse the number using while loop
'''n=int(input("Enter the number:"))
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print("The reversed number is:", rev)
'''
#Convert uppercase to lowercase using for loop
'''s=input("Enter the string:")
for ch in s:
    if 'A'<=ch<='Z':
        print(chr(ord(ch)+32),end='')
    else:
        print(ch,end='')'''

#Covert lowercase to uppercase using for loop
'''s=input("Enter the string:")
for ch in s:
    if 'a'<=ch<='z':
        print(chr(ord(ch)-32),end='')
    else:
        print(ch,end='')'''
        
'''for i in range(1,6):
    for j in range(1,6):
        print('*',end='')
    print() '''

'''def convert():
    s=input('enter:')
    output=''
    for ch in s:
        if 'A'<=ch<='Z':
            output+=chr(ord(ch)+32)
        else:
            output+=ch
    print(output)
convert()'''