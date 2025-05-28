import copy
import numpy as np
import matplotlib.pyplot as plt

def read_matrix_from_file(filename):
    with open(filename, 'r') as file:
        matrix = [list(map(int, line.split())) for line in file]
    return matrix

def extract_submatrix(matrix, n):
    return [row[:n] for row in matrix[:n]]

def print_matrix(m, title):
    print(f"\n{title}:")
    for row in m:
        print(" ".join(f"{x:7.1f}" for x in row))

def count_numbers_greater_than_k_in_odd_columns_C(matrix, n, k):
    half = n // 2
    count = 0
    for i in range(half):
        for j in range(half, n):
            if (j + 1) % 2 != 0 and matrix[i][j] > k:
                count += 1
    return count

def product_of_numbers_in_odd_rows(matrix, n):
    half = n // 2
    product = 1
    for i in range(1, n, 2):  # Только нечетные строки
        for j in range(n):
            product *= matrix[i][j]
    return product

def swap_C_B_symmetrically(matrix, n):
    half = n // 2
    print("Симметричный обмен C и B")
    for i in range(half):
        for j in range(half):
            matrix[i][j], matrix[i][j + half] = matrix[i][j + half], matrix[i][j]
    print_matrix(matrix, "F после обмена")

def swap_C_E_asymmetrically(matrix, n):
    half = n // 2
    print("Асимметричный обмен C и E")
    for i in range(half):
        for j in range(half):
            matrix[i][j + half], matrix[i + half][j + half] = matrix[i + half][j + half], matrix[i][j + half]
    print_matrix(matrix, "F после обмена")

def create_lower_triangular(matrix):
    n = len(matrix)
    G = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            G[i][j] = matrix[i][j]
    return G

def plot_matrices(matrices, titles):
    plt.figure(figsize=(15, 5))
    for i, (matrix, title) in enumerate(zip(matrices, titles), 1):
        plt.subplot(1, 3, i)
        plt.imshow(matrix, cmap='viridis')
        plt.colorbar()
        plt.title(title)
    plt.tight_layout()
    plt.show()

k = int(input('Введите число k: '))
n = int(input('Введите число n: '))

file_matrix = read_matrix_from_file('matrix.txt')
A = extract_submatrix(file_matrix, n)

A_np = np.array(A)
print_matrix(A, "Матрица A")

F = copy.deepcopy(A)
F_np = np.array(F)

# Правильные вычисления для 18 варианта
count_greater_k = count_numbers_greater_than_k_in_odd_columns_C(F, n, k)
product_odd_rows = product_of_numbers_in_odd_rows(F, n)

print(f"\nКол-во чисел > {k} в нечетных столбцах C: {count_greater_k}")
print(f"Произведение чисел в нечетных строках: {product_odd_rows}")

if count_greater_k > product_odd_rows:
    print("\nУсловие: Кол-во чисел > K в нечетных столбцах C > Произведения чисел в нечетных строках")
    swap_C_B_symmetrically(F, n)
else:
    print("\nУсловие: Кол-во чисел > K в нечетных столбцах C <= Произведения чисел в нечетных строках")
    swap_C_E_asymmetrically(F, n)

F_np = np.array(F)
print_matrix(F, "Матрица F после преобразований")

det_A = np.linalg.det(A_np)
sum_diag_F = np.trace(F_np)

print(f"\nОпределитель матрицы A: {det_A:.1f}")
print(f"Сумма диаг. эл-тов матрицы F: {sum_diag_F:.1f}")

if det_A > sum_diag_F:
    print("\nУсловие: det(A) > sum(diag(F))")
    A_AT = A_np @ A_np.T
    F_inv = np.linalg.inv(F_np)
    result = A_AT - k * F_inv

    print("\nA * AT:")
    print_matrix(A_AT.tolist(), "A * AT")
    print("\nF^(-1):")
    print_matrix(F_inv.tolist(), "F^(-1)")
    print("\nРезультат A*AT - K*F^(-1):")
    print_matrix(result.tolist(), "Результат")

else:
    print("\nУсловие: det(A) <= sum(diag(F))")
    A_inv = np.linalg.inv(A_np)
    G = create_lower_triangular(A)
    G_np = np.array(G)
    F_T = F_np.T
    result = (A_inv + G_np - F_T) * k

    print("\nA^(-1):")
    print_matrix(A_inv.tolist(), "A^(-1)")
    print("\nG (нижняя треугольная из A):")
    print_matrix(G_np.tolist(), "G")
    print_matrix(F_T.tolist(), "F^T")
    print_matrix(result.tolist(), "Результат (A^(-1) + G - F^T) * K:")

plot_matrices([A_np, F_np, result],
              ["Матрица A", "Матрица F", "Результат вычислений"])