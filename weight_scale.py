print("Добро пожаловать в программу 'Весы'!")
weight_1 = float(input("Введите вес первого объекта: "))
weight_2 = float(input("Введите вес второго объекта: "))

if weight_1 > weight_2:
    print("Первый объект тяжелее второго.")
elif weight_1 < weight_2:
    print("Первый объект легче второго.")
else:
    print("Объекты равны по весу.")
