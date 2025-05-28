def distribute_money(total_sum, num_banks):
  
    def distribute(current_bank, remaining_sum, current_distribution):
        if current_bank == num_banks - 1:
            distribution = current_distribution + [remaining_sum]
            print(distribution)
            return

        for i in range(remaining_sum + 1):
            distribute(current_bank + 1, remaining_sum - i, current_distribution + [i])

    print(f"Распределение {total_sum} по {num_banks} банкам:")
    distribute(0, total_sum, [])


total_sum = int(input("Введите общую сумму денег: "))
num_banks = int(input("Введите количество банков: "))

distribute_money(total_sum, num_banks)
