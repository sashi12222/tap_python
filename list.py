"""
#List Data type:
if we want to represent a group of values as a single entity
  ->Insertion order is preserved
  ->Heterogeneous objects are allowed 
  ->Duplicates are allowed 

=>List is dynamic because based on our requirement we can increase the size and decrease the size
=>In list the elements will be placed within square brackets[]
=>list objects are mutable i.e we can change the content. 
   [10,"a","B",20,30,40]
   
#creation of list objects:
  ->we can create empty list object as follows...
   list=[]
   print(list,type(list))
  ->if we know elements already then we can create list as follows
    list=[10,20,30,40]
  =>With list() function:
      l=list(range(20,30,3))
      print(l,type(l))
   -> with dynamic input:
   list=eval(input("Enter the list:"))
   print(list,type(list))

eg:
s="twinkle"
l=list(s)
print(l)  

#traversing the elements of list:
#Example:
#how to read the list values
z=eval(input("Enter teh list values"))
print(z,type(z))
y=[10,20,30,40,50,30,60]
x=list()
print(x,type(x))
print(y,type(y))
print(y,end='',sep=",")    

#by using the indexing
for i in range(len(y)):
  print(y[i])
print()
#by using value wise
for ele in y:
    print(ele,end=" ")
print()
i=0
while i<len(y):
    print(y[i],end=" ")
    i+=1
print()
print(*y)


#Accesing Elements of list:
  => We can access elements of the list either by using index or by using slice
      operator(:)
      
    eg:
    list=[10,20,30,40]
    list[0]
    list[-1]
    list[1:3]
    list[0]=100
    print(l)
    print(list[10]) //IndexError:list index out of range
NOTE:Sometimes we can take list inside another list, such type of list are called nested lists.add()
     l=[10,20,[30,40]]
    print(l[0])
      print(l[1])
      print(l[2])   //[30,40]
      print(l[2][0])  //30
      print(l[2][1]) // 40

#By using the slice operator:
   syntax:list2=list1[start:stop:step]
   
   n=[1,2,3,4,5,6,7,8,9,10]
   print(n[2:7:2])
   print(n[4::2])
   print(n[3:7])
   print(n[8:2:-2])  //[9,7,5]
   print(n[4:100]) //[5,6,7,8,9,10]
   
NOTE:
   ->Mutablitiy:
        Once we creates a list object, we can modify its content. Hence list objects are mutable

                           #IMPORTANT FUNCTIONS OF LIST:
                    =>To get information about list:
                    
    1.len():Returns the number of elements present in the list
         n=[10,20,30,40]
         print(len(n))
    2.index():Returns the  index of first occurence of the specified item.
        ex: 
        n=[1,2,2,2,2,3,3]
        print(n.index(1))
        print(n.index(2))
        print(n.index(4))  //Value Error: 4 is not in list
        
    3.count():It  returns the  number of occurences of specified item in the list
        ex:
        n=[1,2,2,2,2,3,,3]
        print(n.count(1))
        print(n.count(2))
        print(n.count(4))//0
"""
#Example:
#how to read the list values
z=eval(input("Enter teh list values"))
print(z,type(z))
y=[10,20,30,40,50,30,60]
x=list()
print(x,type(x))
print(y,type(y))
print(y,end='',sep=",")    

#by using the indexing
for i in range(len(y)):
  print(y[i])
print()
#by using value wise
for ele in y:
    print(ele,end=" ")
print()
i=0
while i<len(y):
    print(y[i],end=" ")
    i+=1
print()
print(*y)