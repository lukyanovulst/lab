import itertools

def distribute_money(total_sum, num_banks):
    """
    Генерирует все возможные варианты распределения суммы денег по банкам (с использованием itertools).
    """
    if num_banks == 0:
        if total_sum == 0:
            print([0]*num_banks)
        return
    if num_banks == 1:
        print([total_sum])
        return

    positions = list(range(total_sum + num_banks - 1))
    combinations = itertools.combinations(positions, num_banks - 1)

    print(f"Распределение {total_sum} по {num_banks} банкам:")
    for comb in combinations:
        distribution = []
        last_position = 0
        for position in comb:
            distribution.append(position - last_position)
            last_position = position + 1
        distribution.append(total_sum + num_banks - 1 - last_position) # остаток
        print(distribution)

total_sum = int(input("Введите общую сумму денег: "))
num_banks = int(input("Введите количество банков: "))

distribute_money(total_sum, num_banks)