 
'''
You are given a function 
   int checkPassword(char str[],int n,min)
The function will accept a sting and its length n and another argument min which dnotes minimum length
of the password . You are supposed to  print valid. If the passowrld meets criteria below or invalid if the password doesn't
meet the criteria mentioned below.

1.At least min characters
2.At least one numeric digit  
3.At least one capital letter
4.At least one special character
5.Must not have spaxe or +
6.Starting character must not be a number
'''

def checkPassword(s,n,m):
    u=d=sp=0
    if m<=n:
        for i in range(n):
            if i==0 and s[i].isdigit():
                return "Invalid, First character is digit"
            elif s[i].isupper():
                u=1
            elif s[i].isdigit():
                d=1
            elif s[i] in {'@','_','#','$','*'}:
                sp=1
            elif s[i].isspace() or s[i]=='+':
                return "invalid , + or space character "
    if u==d==sp==1:
        return "valid password"
    elif u==0 and sp==0:
        return "invalid password, upper aand special characteres are missing"
    elif u==0 and d==0:
        return"Invalid, upper and digit are missing"
    elif u==0:
        return"Invalid uppercharacteris missing"
    elif d==0 and sp==0:
        return"Invalid,digit and specaial characters are missing"
    elif d==0:
        return "Invalid digit character is missing"
    elif sp==0:
        return "Invalid specaial character is missing"
    else:
      return "Invalid , please provide min length of the characters"

s=input("Enter teh passowrd:")
m=int(input("Enter the password min length"))
print(checkPassword(s,len(s),m))