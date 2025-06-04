import copy

def read_matrix_from_file(filename):
    with open(filename, 'r') as file:
        matrix = [list(map(int, line.split())) for line in file]
    return matrix

def extract_submatrix(matrix, n):
    return [row[:n] for row in matrix[:n]]

def print_matrix(m, title):
    print(f"\n{title}:")
    for row in m:
        print(" ".join(f"{x:4}" for x in row))

def count_zeros_in_odd_columns_area4(matrix, n):
    count = 0
    for i in range(n//2 + 1):
        for j in range(i + 1, n - i):
            if j % 2 == 1 and matrix[i][j] == 0:
                count += 1
    return count

def sum_in_odd_rows_area1(matrix, n):
    total = 0
    for i in range(n):
        for j in range(n - i, n):
            if i % 2 == 0:
                total += matrix[i][j]
    return total

def swap_areas_1_2_symmetrically(matrix, n):
    for i in range(n):
        for j in range(n):
            if i >= j and i + j >= n - 1:
                ii, jj = n - 1 - j, n - 1 - i
                matrix[i][j], matrix[ii][jj] = matrix[ii][jj], matrix[i][j]

def swap_areas_2_3_asymmetrically(matrix, n):
    for i in range(n):
        for j in range(n):
            if i > j and i + j < n - 1:
                ii, jj = n - 1 - j, n - 1 - i
                matrix[i][j], matrix[ii][jj] = matrix[ii][jj], matrix[i][j]

k = int(input('Введите число k: '))
n = int(input('Введите число n: '))

try:
    file_matrix = read_matrix_from_file('matrix.txt')
    if len(file_matrix) < n or any(len(row) < n for row in file_matrix):
        raise ValueError("Файл содержит матрицу меньшего размера, чем требуется")
    A = extract_submatrix(file_matrix, n)
except Exception as e:
    print(f"Ошибка при чтении матрицы из файла: {e}")
    exit()

print_matrix(A, "матрица A")

F = copy.deepcopy(A)

zeros_area4 = count_zeros_in_odd_columns_area4(F, n)
sum_area1 = sum_in_odd_rows_area1(F, n)

if zeros_area4 > sum_area1:
    swap_areas_1_2_symmetrically(F, n)
else:
    swap_areas_2_3_asymmetrically(F, n)

print_matrix(F, "Матрица F")

AF = [[sum(A[i][m] * F[m][j] for m in range(n)) for j in range(n)] for i in range(n)]
print_matrix(AF, "A*F")

K_AF = [[k * x for x in row] for row in AF]
print_matrix(K_AF, "K*(A*F)")

AT = [[A[j][i] for j in range(n)] for i in range(n)]
print_matrix(AT, "A^T")

K_AT = [[k * x for x in row] for row in AT]
print_matrix(K_AT, "K*A^T")

result = [[K_AF[i][j] - K_AT[i][j] for j in range(n)] for i in range(n)]
print_matrix(result, "K*(A*F) - K*A^T")
