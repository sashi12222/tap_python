'''
   * * *
*         *
*          *
*  * * *   *
*          *
*          *

write the program to print the above pattern
'''


for r in range(7):
  for c in range(5):
      if r not in {0} and c in{0,4}:
        print("*",end=" ")
      elif r in {0,3} and c in {1,2,3}:
          print("*",end=" ")
      else:
          print(" ",end=" ")
  print()
