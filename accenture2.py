#B4A1D3
'''

x=input()
s1=''
s2=''
for ch in x:
    if ch.isalpha():
        s1+=ch
    else:
        s2+=ch
# print(sorted(s1))
print("".join(sorted(s1)) +("".join(sorted(s2))))
 
'''

''' write a program for hte following requirement
input:a4b3c2
output:aaaabbbcc



x=input()
output=""
for ch in x:
    if ch.isalpha():
        output+=ch
        prev=ch
    else:
        output+=prev*(int(ch)-1)
print(output)
'''





# #a4k3b2
# x=input()
# output=''
# for ch in x:
#     if ch.isalpha():
#         output+=ch
#         prev=ch
#     else:
#         output+=chr(ord(prev)+int(ch))
# print(output)
"""
    write a python program to perform th efollowing activity:
    input:a4k3b2
    output:aeknbd
    
    
    input:A4K3W5
    output:AEKNWB
"""
    
x=input()
output=''
# prev=''
for ch in x:
    if ch.isalpha():
        output+=ch
        prev=ch
   
    else:
       if ord(prev)>=97 and ord(prev)<=122:
           if ord(prev)+int(ch)>122:
               d=ord(prev)+int(ch)-122
               output+=chr(96+d)
           else:
               output+=chr(ord(prev)+int(ch))
               
    
       elif ord(prev)>=65 and ord(prev)<=90:
           if ord(prev)+int(ch)>90:
               d=ord(prev)+int(ch)-90
               output+=chr(64+d)
           else:
               output+=chr(ord(prev)+int(ch))  
    
    
print(output)