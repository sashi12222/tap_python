"""
#Dictionary:
   ->We can use list,tuple and set to represent a group of infividual objects as a single entity.
   ->if we want to represent a group of objects as key-value pairs then awe should go for Dictionary.
             
             rollno->name
             phonen number->address
             ipaddress->domain name
    -> duplicates keys are not allowed but values can be duplicated.
    =>Heterogeneous objects are allowed for both key and vlues.
    =>Insetion order is not preserved
    =>Dictionaries are mutable
    =>Dictionaries are dynamic
    =>Indexing and slicing concepts are not applicable
NOTE: In c++ and java Dictionaries are known as "Map" whre as in perl an Ruby it is known as"Hash"

#How to create Dictionary?
  => d={} OR d=dict()
   We are creating empty dictionary. We can add entries as follows
       
       d[100]="sai"
       d[200]="ravi"
       d[300]="shiva"
    print(d)
    
  => If we know data in advance then we can create dictionary as follows:
      d={key:value,key:value}
   ex:
    d={100:"sai",200:"ravi"}


#How to access Data fom the dictionary?
  =>We can access data by using keys.
       d={100:'sai',200:'ravi',300:'shiva'}
       print(d[100])  //sai
       print(d[300])    //shiva
       
       if we specified key is not availalble then we will get KeyError
    print(d[400])   //KeyError:400
    
    =>We can prevent this by checking whether key is already available or not by using in operator.
          if 400 in d:
           print(d[400])   
    Ex:
       x={100:"kumar",200:"sai",300:"boby",400:"Balu",200:"vijay",500:"Balu"}
       n=int(input("Enter the key value:))
       if n in x:
         print(x[n])
       else:
         print(n,"is not available in x")


#How to update Dictionaries?
  d[key]=value
  =>If the key is not availabe then a new entry will be added to the dictioanry with the specified key-value pair
  =>if the key is already available then old value will be replaced with new value.
  
  d={100:'sai',200:'ravi',300:'shiva'}
  print(d)   //{100:'sai',200:'ravi,300:'shiva'}
  d[400]="sashi"
  print(d)  //{100:'sai',200:'ravi',300:'shiva',400:'pavan'}
  d[100]='pandey'
  print(d)  //{100:'padney',200:'ravi',300:'shiva',400:'pavan'}
#update():
     d.update(x)
    => All items present in the dictioanry x will be added to dictionary 
    ex1:
     x={100:'A',200:'B',300:'C'}
     y-{400:'D',500:'E',600:'F'}
     print(x)
     print(y)
     x.update(y)
     print(x)
     print(y)
    ex2:
    x={100:'A',200:'B',300:'C'}
    y={100:'D',400:'E',500:'F'}
    x.update(y)
    print(x)
  
#How to Delete Elements from Dictionary?
    del d[key]: It deletes entry associated withe the specified key.
    If the key is not available then we will get KeyError.
    
    d={100:'sai',200:'ravi',300:'shiva'}
    print(d)
    del d[100]  {100:'sai',200:'ravi',300:'shiva'}
    print(d)  {200:'ravi',300:'shiva'}
    del d[400]  KeyError:400
    
    d.clear()=> To remove all entries frome the dictionary. 
       d={100:'sai',200:'ravi',300:'shiva'}
       print(d)   {100:'sai',200:'ravi',300:'shiva'}
       d.clear()  {}
       print(d)
     del d => To delete total dictionary. Now we cannot access d.
        d={100:'sai'.200:'ravi',300:'shiva'}
        print(d)
        del d
        print(d) //NameError:name 'd' is not defined 
              
                              Important functions of Dictionary:
               d=dict([(100,'sai'),(200,'shiva'),(300,'ravi')])
                it creates dictionary with the given list of tuple elements
                x=dict([(100,'sai',),(200,'sashi',),(300,'ram','shyam'),(400,'raju')])
                print(x)
                
    x=[10,20,30,40]
    y=['python','java','C++','oracle']
    a=dict(zip(x,y))
    print(a)
    
    x=[10,20,30,40]
    y=['python','java','C++','oracle']
    rec={}
    for i in range(len(x)):
      rec.upadate({x[i]:y[i]})
    print(rec)
    
    
    name=['sai','pandey']
    default={'desg':'desingner','sal':4000,'addr':'hyd'}
    rec=dict.fromkeys(name, default)
    print(rec)
    print(rec['sai']['addr'])
    rec['sai']['addr']='gntr'
    print(rec)
    
#get():To get the value associated with the key
   d.get(key)
=>If the key is available then retuns the corresponding value otherwise retuns None. It won't raise any error.

     d.get(key,defaultValue)=>If the  key is available then returns the corresponding value otherwise reutns the default value
     
     d={100:'sai',200:'ravi',300:'shiva'}
     print(d[100])
     print(d[400])  //keyError:400
     print(d.get(100))  //sai
     print(d.get(400)) //none
     print(d.get(100,'abc'))//sai
     print(d.get(400,'abc')) //abc 
"""
'''Write a program to Enter Name and Percntage Marks in a Dictionary and Display informaton on the screen'''

n=int(input("Enter the no of records:"))
rec={}

for  i in range(n):
    name=input("Name:")
    marks=input("Marks:")
    rec[name]=marks
print("-"*36)
print("| {:^15} | {:^15}|".format("NAME","MARKS"))
print("-"*36)
for key in rec:
   print("| {:^15} | {:^15}|".format(key,rec[key]))
   print("-"*36)
# import pandas as pd
# a=pd.DataFrame(rec)
# print(a)