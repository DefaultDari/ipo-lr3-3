month = int(input("Введите месяц (от 1 до 12) : ")) #Ввод месяца
day = int(input("Введите число: ")) #Ввод дня
# Определеям время года с if/elif/else:
if (month == 3 and day >= 1) or (month == 4) or (month == 5) or (month == 6 and day <= 31):
    time = "Весна"
elif (month == 6 and day >= 1) or (month == 7) or (month == 8) or (month == 9 and day <= 31):
    time = "Лето"
elif (month == 9 and day >= 1) or (month == 10) or (month == 11) or (month == 12 and day <= 30):
    time = "Осень"
else:
    time = "Зима"
print(f"Время года : {time}") #Выводим результат на экран
