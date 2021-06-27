# coding=utf-8

ocenka = [] # создаем пустой список для оценок учащихся
new_file = open("E:/New_Task.txt", 'w') #Новый документ куда будем сохранять всех учеников с определенной отметкой
with open("E:/Task.txt", 'r') as f: # Открываем файл со всеми учениками и оценками
    text = f.readlines() # Читаем файл
    for i in text: # Открываем цикл for
        ocenka.append(int(i.replace("\n", "")[-1]))
        if i.replace("\n", "")[-1] == "3":  # в строке заменяем \n (Это показатель новой строки) на пустое место. Короче тупо убираем \n и сравниваем с искомой оценкой
            new_file.writelines(i) # Если условие совпадает со строкой - записываем ее в новый файл

middle = float(sum(ocenka)) / len(ocenka) # Находим среднюю оценку.  (sum(ocenka)) - сумма всех элементов списка, len(ocenka) - количество элементов списка
middle2 = float('{:.3f}'.format(sum(ocenka) / len(ocenka))) # Можно так - это мы указали сколько чисел оставить после запятой
middle3 = float(sum(ocenka)) / len(ocenka) # А это средняя оценка округленная к целому числу
new_file.writelines("Средняя оценка: " + str(middle)) # Записываем всё в файл
new_file.close() # закрываем новый файл


