'''write a program to pritn character at odd postion and even positon for the given string
input:twinkle tech solutions
output: characters at Even positions:tiktc ouin
characters at odd positons:wnl ehsltos

'''
str=input("Enter a string:")
even_str=""
odd_str=""
for i in range(len(str)):
    if i%2==0:
        even_str+=str[i]
    else:
        odd_str+=str[i]
print("character at even string:",even_str)
print("characters at odd str",odd_str)
'''
program to merge characters of 2 strings inot a string by taking characters alternatively
input: s1:"ravi"
s2"teja"
output:rtaevjia

'''

s1=input("Enter the first string:")
s2=input("Enter the second string:")
output=""
min_len=min(len(s1),len(s2))

for i in range(min_len):
    output+=s1[i]+s2[i]
if len(s1) > len(s2):
    output+=s1[min_len:]
elif len(s2)>len(s1) :
    output+=s2[min_len]
    
print("the merged string is:",output)
    
    