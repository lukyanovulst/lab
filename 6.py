import math
import timeit
import matplotlib.pyplot as plt


# Рекурсивная функция F(n)
def F_rec(n):
    if n == 1:
        return 2
    else:
        return (-1) ** n * (F_rec(n - 1) - G_rec(n - 1) / math.factorial(2 * n))


def G_rec(n):
    if n == 1:
        return 1
    else:
        return F_rec(n - 1) + G_rec(n - 1)


# Итерационная функция F(n)
def F_iter(n):
    F = [0] * (n + 1)
    G = [0] * (n + 1)
    F[1] = 2
    G[1] = 1
    for i in range(2, n + 1):
        F[i] = (-1) ** i * (F[i - 1] - G[i - 1] / math.factorial(2 * i))
        G[i] = F[i - 1] + G[i - 1]
    return F[n]


def G_iter(n):
    F = [0] * (n + 1)
    G = [0] * (n + 1)
    F[1] = 2
    G[1] = 1
    for i in range(2, n + 1):
        F[i] = (-1) ** i * (F[i - 1] - G[i - 1] / math.factorial(2 * i))
        G[i] = F[i - 1] + G[i - 1]
    return G[n]


def measure_time(func, n):
    number = 100  # Начальное число повторений
    time = timeit.timeit(lambda: func(n), number=number)

    # Автоматическая регулировка числа повторений
    while time < 0.1 and number < 10000:
        number *= 10
        time = timeit.timeit(lambda: func(n), number=number)

    return time / number  # Возвращаем среднее время выполнения


def main():
    n = int(input("Введите натуральное число N: "))

    results = {
        'n': [],
        'F_rec': [],
        'F_iter': [],
        'time_rec': [],
        'time_iter': []
    }

    for i in range(1, n + 1):
        results['n'].append(i)

        try:
            time_rec = measure_time(F_rec, i) * 1000
            f_rec = F_rec(i)
        except Exception as e:
            print(f"Ошибка рекурсивного вычисления F для n={i}: {e}")
            time_rec = None
            f_rec = None

        try:
            time_iter = measure_time(F_iter, i) * 1000
            f_iter = F_iter(i)
        except Exception as e:
            print(f"Ошибка итерационного вычисления F для n={i}: {e}")
            time_iter = None
            f_iter = None

        results['F_rec'].append(f_rec)
        results['F_iter'].append(f_iter)
        results['time_rec'].append(time_rec)
        results['time_iter'].append(time_iter)

    print("\nРезультаты вычислений:")
    print(f"{'n':<5}{'F рекурсивно':<20}{'F итерационно':<20}{'Время рекурсии (мс)':<20}{'Время итерации (мс)':<20}")
    for i in range(n):
        print(f"{results['n'][i]:<5}"
              f"{results['F_rec'][i]:<20.6f}"
              f"{results['F_iter'][i]:<20.6f}"
              f"{results['time_rec'][i]:<20.4f}"
              f"{results['time_iter'][i]:<20.4f}")

    plt.plot(results['n'], results['time_rec'], 'r-', label='Рекурсия')
    plt.plot(results['n'], results['time_iter'], 'b-', label='Итерация')
    plt.title('время сравнения итерации и рекурсии')
    plt.xlabel('n')
    plt.ylabel('время')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
