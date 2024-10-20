first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторная сборка для высчитывания разницы длин строк из списков first и second
first_result = (abs(len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s))

# Генераторная сборка для сравнения длин строк в одинаковых позициях из списков first и second
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

# Вывод результата
print(list(first_result))
print(list(second_result))
