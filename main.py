month = int(input("Введите месяц (от 1 до 12) : ")) #Ввод месяца
day = int(input("Введите число: ")) #Ввод дня
# Определеям время года с if/elif/else:
if (month == 3 and day >= 1 and day<=31) or (month == 4 and day>=1 and day<=30) or (month == 5 and day>=1 and day <=31): #Проверка на весну
    time = "Весна"
    print(f"Время года : {time}") #Выводим результат на экран
elif (month == 6 and day >= 1 and day <= 30) or (month == 7 and day>=1 and day<=31) or (month == 8 and day >= 1 and day <= 31): #Проверка на лето
    time = "Лето" 
    print(f"Время года : {time}") #Выводим результат на экран
elif (month == 9 and day >= 1 and day <= 30) or (month == 10 and day>=1 and day<=31) or (month == 11 and day >= 1 and day <=30): #Проверка на осень
    time = "Осень"
    print(f"Время года : {time}") #Выводим результат на экран
elif (month == 12  and day >= 1 and day <= 31) or (month == 1 and day >= 1 and day < 31) or (month == 2 and day >= 1 and day <= 28): #Проверка на зиму
    time = "Зима"
    print(f"Время года : {time}") #Выводим результат на экран
else:
    print("Неверный ввод")  #Неверный ввод
