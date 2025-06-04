import itertools

def distribute_money_with_max(total_sum, num_banks, max_per_bank):

    if total_sum < 0 or num_banks <= 0 or max_per_bank < 0:
        return []

    if total_sum > num_banks * max_per_bank:
        print("Невозможно распределить сумму по банкам с таким ограничением на максимальную сумму.")
        return []

    distributions = []
    possible_amounts = range(min(total_sum + 1, max_per_bank + 1))
    for combination in itertools.combinations_with_replacement(possible_amounts, num_banks):
        if sum(combination) == total_sum:
            distributions.append(list(combination))
    return distributions

def find_optimal_distribution(distributions):

    if not distributions:
        return None

    optimal_distribution = None
    max_min_amount = -1

    for distribution in distributions:
        min_amount = min(distribution)
        if min_amount > max_min_amount:
            max_min_amount = min_amount
            optimal_distribution = distribution

    return optimal_distribution

total_sum = int(input("Введите общую сумму денег: "))
num_banks = int(input("Введите количество банков: "))
max_per_bank = int(input("Введите максимальную сумму в банке: "))

distributions = distribute_money_with_max(total_sum, num_banks, max_per_bank)

if distributions:
    print(f"Распределение {total_sum} по {num_banks} банкам (максимум {max_per_bank} в банке):")
    for distribution in distributions:
        print(distribution)

    optimal_distribution = find_optimal_distribution(distributions)
    print(f"\nОптимальное распределение: {optimal_distribution}")
else:
    print("Нет вариантов распределения.")