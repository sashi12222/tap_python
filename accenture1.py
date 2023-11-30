 
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
# A function to check the password validity
def checkPassword(str, n, min):
  # Check if the password has at least min characters
  if n < min:
    return 0 # invalid
  
  # Check if the password starts with a number
  if str[0].isdigit():
    return 0 # invalid
  
  # Initialize flags for other criteria
  has_digit = False
  has_upper = False
  has_special = False
  has_space_or_plus = False
  
  # Define a list of special characters
  special_chars = ['$', '@', '#', '%']
  
  # Loop over the password characters
  for ch in str:
    # Check if the character is a digit
    if ch.isdigit():
      has_digit = True
    
    # Check if the character is an uppercase letter
    if ch.isupper():
      has_upper = True
    
    # Check if the character is a special character
    if ch in special_chars:
      has_special = True
    
    # Check if the character is a space or a plus
    if ch == ' ' or ch == '+':
      has_space_or_plus = True
  
  # Check if the password meets all the criteria
  if has_digit and has_upper and has_special and not has_space_or_plus:
    return 1 # valid
  else:
    return 0 # invalid

# Example
password = input("Enter the password")
length = len(password)
min_length = 6
result = checkPassword(password, length, min_length)
if result == 1:
  print("Valid Password")
else:
  print("Invalid Password")


'''
Input: A stirng of comma separated numbers are given such that numbers 4 and 7 are already available in the list
Assumption:7 always comes after 4 in the given string
number1:
Add all numbers which do not lie between 4 and 7(i.e excluding 4 and 7) in the given input.

number2:
Numbers formed by concatenating all numbers from 4 to 7(i.e including 4 and 7).
output=sum of number1 and number2

Example:2,5,1,4,3,2,7,8
number1:2+5+1+8=16
number2='4'+'3'+'2'+'7'=4327
output=16+4327=4343

'''