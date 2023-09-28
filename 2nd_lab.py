#2.	Определить, является ли квадратный массив симметричным относительно своей главной диагонали.
def is_symmetric(matrix):
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            return False
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True
matrix = [
    (1, 2, 3),
    (2, 4, 5),
    (3, 5, 6)
]
result = is_symmetric(matrix)
print(result)