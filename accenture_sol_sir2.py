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

x="2,5,1,4,3,2,7,8".split(",")

number1=0
number2=""
for i in range(len(x)):
    if i<x.index('4')or i>x.index('7'):
        number1+=int(x[i])
    else:
        number2+=x[i]
        
print(number1+int(number2))
    
        