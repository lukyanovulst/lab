dc={'0':'ноль','1':'один','2':'два','3':'три','4':'четыре','5':'пять','6':'шесть','7':'семь','8':'восемь','9':'девять'}
with open("1.txt",'r',encoding='utf-8') as f: data=f.read().split()
num_counter = 1
for i,num in enumerate(data,1):
    if not num.isdigit(): print(f"'{num}' не  является числом"); continue
    print(f"\nИсходное число (№{num_counter}): {num}"); num_counter +=1
    if len(num)>1 and num[0]=='7' and num[-1]=='7' or num=='7': print(f"'{num}' начинается и заканчивается на 7")
    if i%2==0:
        even=''.join([i for i in num if int(i)%2==0])
        odd=' '.join([dc[i] for i in num if int(i)%2!=0])
        if even: print(f"Четное число: {even}")
        else: print("Все цифры нечетные.")
        if odd: print(f"Удаленные нечетные цифры: {odd}")
        else: print("Не было удалено ни одной нечетной цифры")