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
    print(f"\n{title}:\n" + "\n".join(" ".join(f"{x:4}" for x in row) for row in m))

def swap_C_B_symmetrically(matrix, n):
    half = n // 2
    for i in range(half, n):
        for j in range(half):
            matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]

def swap_C_E_asymmetrically(matrix, n):
    half = n // 2
    for i in range(half):
        for j in range(half):
            matrix[i][j+half], matrix[i + half][j] = matrix[i + half][j], matrix[i][j+half]

def create_lower_triangular(matrix):
    n = len(matrix)
    return [[matrix[i][j] if j <= i else 0 for j in range(n)] for i in range(n)]

def plot_matrices(matrices, titles):
    plt.figure(figsize=(15, 5))
    for i, (matrix, title) in enumerate(zip(matrices, titles), 1):
        plt.subplot(1, 3, i)
        plt.imshow(matrix, cmap='viridis')
        plt.colorbar()
        plt.title(title)
    plt.tight_layout()
    plt.show()

def count_numbers_greater_than_k_in_odd_cols_C(matrix, k, n):
    count = 0
    half = n // 2
    for i in range(half, n): # C
        for j in range(half):
            if (j + 1) % 2 != 0 and matrix[i][j] > k:
                count += 1
    return count

def product_in_odd_rows_C(matrix, n):
    product = 1
    half = n // 2
    for i in range(half, n):
        for j in range(half):
            if (i + 1) % 2 != 0:
                product *= matrix[i][j]
    return product

k_input = int(input('Введите число k: '))
n = int(input('Введите число n: '))

try:
    A = extract_submatrix(read_matrix_from_file('matrix.txt'), n)
except Exception as e:
    print(f"Ошибка при чтении матрицы из файла: {e}")
    exit()

A_np = np.array(A)
print_matrix(A, "Матрица A")

F = copy.deepcopy(A)
count_greater_than_k = count_numbers_greater_than_k_in_odd_cols_C(F, k_input, n)
product_in_odd_rows = product_in_odd_rows_C(F, n)

print(f"\nКоличество чисел > {k_input} в нечетных столбцах C: {count_greater_than_k}")
print(f"Произведение чисел в нечетных строках C: {product_in_odd_rows}")

if count_greater_than_k > product_in_odd_rows:
    print("\nУсловие: количество чисел > K в нечетных столбцах C > произведения чисел в нечетных строках C")
    swap_C_B_symmetrically(F, n)
    print("\nПоменяли местами C и B симметрично")
else:
    print("\nУсловие: количество чисел > K в нечетных столбцах C <= произведения чисел в нечетных строках C")
    swap_C_E_asymmetrically(F, n)
    print("\nПоменяли местами C и E асимметрично")

F_np = np.array(F)
print_matrix(F, "Матрица F после преобразований")

det_A = np.linalg.det(A_np)
det_A = int(det_A)
sum_diag_F = np.trace(F_np)

print(f"\nОпределитель матрицы A: {det_A}")
print(f"Сумма диагональных элементов матрицы F: {sum_diag_F}")

if det_A > sum_diag_F:
    print("\nУсловие: det(A) > sum(diag(F))")
    try:
        A_inv = np.linalg.inv(A_np)
        term1 = np.dot(A_np, A_np.T)
        term2 = k_input * np.linalg.inv(F_np)
        result = term1 - term2

        print("\nA*A^T:")
        print(term1)
        print("\nF^(-1):")
        print(term2 / k_input)
        print("\nРезультат A*A^T - K*F^(-1):")
        print(result)

    except np.linalg.LinAlgError:
        print("Матрица A или F сингулярна, невозможно вычислить обратную матрицу.")
        result = None
else:
    print("\nУсловие: det(A) <= sum(diag(F))")
    A_T = A_np.T
    G = create_lower_triangular(A)
    G_np = np.array(G)
    F_T = F_np.T

    term = A_np + G_np - F_T
    result = k_input * term

    print("\nA:")
    print(A_np)
    print("\nG (нижняя треугольная из A):")
    print(G_np)
    print("\nF^T:")
    print(F_T)
    print("\nРезультат (A + G - F^T)*K:")
    print(result)

if result is not None:
    plot_matrices([A_np, F_np, result],
                  ["Матрица A", "Матрица F", "Результат вычислений"])
else:
    plot_matrices([A_np, F_np],
                  ["Матрица A", "Матрица F"])
