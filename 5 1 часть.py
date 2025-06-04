import time
from itertools import product

def generate_bank_deposits_algorithm(total_amount, num_banks):
    results = []
    def backtrack(remaining_amount, current_deposit, index):
        if index == num_banks:
            if remaining_amount == 0:
                results.append(current_deposit[:])
            return
        for amount in range(remaining_amount + 1):
            current_deposit[index] = amount
            backtrack(remaining_amount - amount, current_deposit, index + 1)
    backtrack(total_amount, [0] * num_banks, 0)
    return results

def generate_bank_deposits_python(total_amount, num_banks):
    results = []
    for deposit in product(range(total_amount + 1), repeat=num_banks):
        if sum(deposit) == total_amount:
            results.append(deposit)
    return results

def main():
    total_amount = int(input("Введите общую сумму денег: "))
    num_banks = int(input("Введите количество банков: "))

    # Алгоритмический вариант
    start_time = time.time()
    deposits_algorithm = generate_bank_deposits_algorithm(total_amount, num_banks)
    end_time = time.time()
    print(f"Время выполнения алгоритмического варианта: {end_time - start_time:.6f} секунд")

    # Вариант с использованием функций Python
    start_time = time.time()
    deposits_python = generate_bank_deposits_python(total_amount, num_banks)
    end_time = time.time()
    print(f"Время выполнения варианта с использованием функций Python: {end_time - start_time:.6f} секунд")

    # Вывод результатов
    print(f"\nВсе возможные варианты размещения суммы {total_amount} в {num_banks} банках:")
    for i, deposit in enumerate(deposits_python, 1):
        print(f"Вариант {i}: {deposit}")

if __name__ == "__main__":
    main()