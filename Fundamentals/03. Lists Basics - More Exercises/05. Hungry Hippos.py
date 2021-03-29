rows = int(input())
matrix = []
blocks = 0
for row in range(rows):
    matrix.append(input().split())
if matrix[0][0] == matrix[0][1]:
    blocks += 1
print(blocks)
print(matrix)