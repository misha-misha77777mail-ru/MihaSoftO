

strings_1 = []
result = 0
first_result = []
_list = []

# Открываем файл для Excel, который записан в виде строк
file = open('9.csv', 'r')
read_strings = file.readlines()

# У всех полученных строк отрезаем символы переноса (\n)
for i in range(0, 1000):
    read_strings = [line.rstrip() for line in read_strings]

# Реформатируем строки так, чтобы они выглядели как списки
for i in read_strings:
    strings_1.append('[' + i.replace(';', ',') + ']')

# Превращаем строки в списки и заполняем ими другой список
for i in strings_1:
    mass = eval(i)
    first_result.append(mass)

# Записываем результат в файл, т. к. иначе он не сохраняется (?)
f = open('temp.txt', 'w')
f.write(str(first_result))

# С помощью цикла находим в каждом списке дубликаты и копируем их в новые списки, добавляемые в ещё один список
for i in first_result:
    ints_list = i
    temp = []
    for x in ints_list:
        if x not in temp:
            temp.append(x)
    for z in temp:
        ints_list.remove(z)
    _list.append(ints_list)  # => Список списков с дубликатами

# Возвращаем сохранённый исходник
new_array = eval(open('temp.txt', 'r').read())

# Цикл проверки наличия только одной пары дубликатов
# Если в списке с дубликатами видно, что их не было или было больше 2-ух
# Соответствующие списки из new_array превращаются в нули
for i in range(6400):
    if not _list[i]:
        new_array[i] = 0
    else:
        # Если в списке несколько дубликатов (не двойных), они также удаляются
        if len(_list[i]) != 1:
            ff = []
            for j in range(len(_list[i])):
                if _list[i][j] not in ff:
                    ff.append(j)
                else:
                    _list[i][j] = 0
            while 0 in _list[i]:
                _list[i].remove(0)
            # Финальная проверка наличия только двух дубликатов
            if len(_list[i]) != 1:
                new_array[i] = 0

# Очистка от нулей
while 0 in new_array:
    new_array.remove(0)

last_result = []
exceptions = []

# Удаление двойных дубликатов из всех списков
for i in new_array:
    k = []
    exception = 0
    for j in i:
        if j not in k:
            k.append(j)
        else:
            exception = j
            break
    i.remove(exception)
    i.remove(exception)
    # Список со списками без дубликатов
    last_result.append(i)
    # Список дубликатов
    exceptions.append(exception)

absolute_result = 0
# Проверка второго условия
for i in range(len(last_result)):
    if sum(last_result[i])/4 <= exceptions[i]*2:
        absolute_result += 1
# Вуаля
print(absolute_result)  # 2241
