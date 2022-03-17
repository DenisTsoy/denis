import random
def get_jokes(n,m):
    """The function gets the value of the number of jokes and the quality of jokes"""
    NOUNS = ["автомобиль", "лес", "огонь", "город", "дом"]
    ADVERBS = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    ADJECTIVES = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = [] # создаем пустой список
    number_of_repetitions=0 # количество повторений
    if m == True: # Проверем условия на качество шуток
        while n > 0:
            jokes.append('{} {} {}'.format(random.choice(NOUNS),random.choice(ADVERBS),random.choice(ADJECTIVES))) # добавляем случайнуй шутку
            n-=1 # уменьшаем количество шуток
    else:
        while n > 0: # Пока количество шуток больше 0 выпоняем цикл
            random.shuffle(NOUNS) #перемешиваем список 1
            random.shuffle(ADVERBS) #перемешиваем список 2
            random.shuffle(ADJECTIVES) #перемешиваем список 3
            if n > 5: # проверям количество шуток уникальных шуток может быть только 5
                n = n // 5 # оставляем остаток от деления на 5
            while n > 0: # Пока количество шуток больше 0 выпоняем цикл
                jokes.append('{} {} {}'.format(NOUNS[n-1], ADVERBS[n-1], ADJECTIVES[n-1]))  # добавляем случайнуй шутку
                n-=1# уменьшаем количество шуток
    print(*jokes, sep ="\n") # Распечатываем шутки из списка
    print ("Шутки закончились")
number_of_jokes = int(input("Введите число попыток: ")) # Запрашиваем количество шуток
quality_request = input("Введите  True - будут поторяться шутки или False  - нет не будут:  ")  # Запрашиваем качество шуток
get_jokes(number_of_jokes,quality_request) # запрос функции
