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
    half_n = n // 2
    for i in range(half_n):
        for j in range(half_n):
            if j % 2 != 0 and matrix[i][j] == 0:
                count += 1
    return count

def product_in_odd_rows_area1(matrix, n):
    product = 1
    half_n = n // 2
    for i in range(half_n):
        if i % 2 != 0:
            for j in range(half_n, n):
                product *= matrix[i][j]
    return product

def swap_areas_1_2_symmetrically(matrix, n):
    half_n = n // 2
    for i in range(half_n):
        for j in range(half_n):
            matrix[i][j + half_n], matrix[i + half_n][j + half_n] = \
                matrix[i + half_n][j + half_n], matrix[i][j + half_n]

def swap_areas_2_3_asymmetrically(matrix, n):
    half_n = n // 2
    for i in range(half_n):
        for j in range(half_n):
            matrix[i + half_n][j + half_n], matrix[i + half_n][j] = \
                matrix[i + half_n][j], matrix[i + half_n][j + half_n]

def matrix_multiply(A, F, n):
    AF = [[sum(A[i][k] * F[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    return AF

def matrix_transpose(matrix, n):
    AT = [[matrix[j][i] for j in range(n)] for i in range(n)]
    return AT

def matrix_scalar_multiply(matrix, scalar):
    return [[scalar * x for x in row] for row in matrix]

def matrix_addition(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1))] for i in range(len(matrix1))]


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

print_matrix(A, "Матрица A")

F = copy.deepcopy(A)

zeros_area4 = count_zeros_in_odd_columns_area4(F, n)
product_area1 = product_in_odd_rows_area1(F, n)

if zeros_area4 * k > product_area1:
    swap_areas_1_2_symmetrically(F, n)
else:
    swap_areas_2_3_asymmetrically(F, n)

print_matrix(F, "Матрица F")

AF = matrix_multiply(A, F, n)
print_matrix(AF, "A*F")

FT = matrix_transpose(F, n)
print_matrix(FT, "F^T")

K_FT = matrix_scalar_multiply(FT, k)
print_matrix(K_FT, "K * F^T")

Result = matrix_addition(AF, K_FT)
print_matrix(Result, "A * F + K * F^T ")