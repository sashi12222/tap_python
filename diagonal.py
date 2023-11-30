
def diagonal_difference(matrix):

  left_to_right_sum = 0
  right_to_left_sum = 0
  # Get the size of the matrix
  size = len(matrix)
 
  for i in range(size):
    left_to_right_sum += matrix[i][i]   
    right_to_left_sum += matrix[i][size - i - 1] 
  
  return abs(left_to_right_sum - right_to_left_sum)

size = int(input("Enter the size of the matrix: "))

matrix = []

for i in range(size):
  row = list(map(int, input(f"Enter row {i + 1} of the matrix: ").split()))

  matrix.append(row)
#   printing the matrix
for i in range(size):
 for j in range(size):
    print(matrix[i][j],end=" ")
print()

print(f"The diagonal difference of the matrix is {diagonal_difference(matrix)}")
