import tkinter as tk
from tkinter import ttk, messagebox
import time
from itertools import combinations_with_replacement
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter.scrolledtext import ScrolledText

def distribute_recursive(amount, banks, current_distribution=[], all_distributions=[]):
    if banks == 1:
        current_distribution.append(amount)
        all_distributions.append(current_distribution.copy())
        current_distribution.pop()
        return

    for i in range(amount + 1):
        current_distribution.append(i)
        distribute_recursive(amount - i, banks - 1, current_distribution, all_distributions)
        current_distribution.pop()

def algorithmic_distribution(amount, num_banks):
    all_distributions = []
    distribute_recursive(amount, num_banks, all_distributions=all_distributions)
    return all_distributions

def python_distribution(amount, num_banks):
    distributions = []
    for c in combinations_with_replacement(range(amount + 1), num_banks):
        if sum(c) == amount:
            distributions.append(c)
    return distributions

def calculate_distributions():
    """Функция, вызываемая при нажатии кнопки. Запускает расчеты и выводит результаты."""
    try:
        amount = int(amount_entry.get())
        num_banks = int(num_banks_entry.get())

        if amount < 0 or num_banks <= 0:
            output_text.insert(tk.END, "Ошибка: Некорректные входные данные.\n")
            return
    except ValueError:
        output_text.insert(tk.END, "Ошибка: Введите целые числа.\n")
        return

    output_text.delete("1.0", tk.END)  # Очищаем поле вывода

    output_text.insert(tk.END, "Вычисление...\n")
    output_text.see(tk.END) # Автоматическая прокрутка

    # Алгоритмический подход
    start_time_alg = time.time()
    distributions_alg = algorithmic_distribution(amount, num_banks)
    end_time_alg = time.time()
    time_alg = end_time_alg - start_time_alg

    output_text.insert(tk.END, "\nАлгоритмический подход:\n")
    output_text.insert(tk.END, f"  Количество вариантов: {len(distributions_alg)}\n")
    output_text.insert(tk.END, f"  Время выполнения: {time_alg:.4f} секунд\n")
    # Вывод всех вариантов (или части)
    output_text.insert(tk.END, "  Варианты:\n")
    for dist in distributions_alg:
        output_text.insert(tk.END, f"    {dist}\n") #  Вывод каждого варианта


    # itertools
    start_time_itertools = time.time()
    distributions_itertools = python_distribution(amount, num_banks)
    end_time_itertools = time.time()
    time_itertools = end_time_itertools - start_time_itertools

    output_text.insert(tk.END, "\nС использованием itertools:\n")
    output_text.insert(tk.END, f"  Количество вариантов: {len(distributions_itertools)}\n")
    output_text.insert(tk.END, f"  Время выполнения: {time_itertools:.4f} секунд\n")
    # Вывод всех вариантов (или части)
    output_text.insert(tk.END, "  Варианты:\n")
    for dist in distributions_itertools:
        output_text.insert(tk.END, f"    {dist}\n") #  Вывод каждого варианта

    output_text.insert(tk.END, "Готово!\n")
    output_text.see(tk.END)

    # Обновление графика
    update_graph(amount,num_banks,time_alg,time_itertools)

def update_graph(amount,num_banks,time_alg,time_itertools):
     # Создаем данные для графика
    labels = ['Алгоритмический', 'itertools']
    times = [time_alg, time_itertools]

    # Очищаем предыдущий график
    plt.clf()  # Очистка графика
    # Создаем столбчатую диаграмму
    plt.bar(labels, times, color=['blue', 'green'])
    plt.ylabel('Время выполнения (секунды)')
    plt.title('Сравнение времени выполнения алгоритмов')
    plt.grid(True)
    # Обновляем canvas
    canvas.draw()

# Создание главного окна
window = tk.Tk()
window.title("Распределение денег по банкам")

# Настройка расширения ячеек для адаптивного интерфейса
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(4, weight=1)

# Элементы ввода
amount_label = ttk.Label(window, text="Сумма денег:")
amount_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
amount_entry = ttk.Entry(window)
amount_entry.grid(row=0, column=1, sticky=tk.E, padx=5, pady=5)

num_banks_label = ttk.Label(window, text="Количество банков:")
num_banks_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
num_banks_entry = ttk.Entry(window)
num_banks_entry.grid(row=1, column=1, sticky=tk.E, padx=5, pady=5)

# Кнопка
calculate_button = ttk.Button(window, text="Рассчитать", command=calculate_distributions)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Вывод результатов (текстовое поле со скроллингом)
output_text = ScrolledText(window, width=50, height=15)
output_text.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew") # sticky="nsew"

# График
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=window)  # root instead of window
canvas.get_tk_widget().grid(row=5, column=0, columnspan=2, sticky="nsew", padx=5, pady=5) #row 5 - отдельная строка для графика

# Запуск главного цикла
window.mainloop()