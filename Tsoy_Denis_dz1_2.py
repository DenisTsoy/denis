def num_translate(y):
    if y.istitle() == True:
        y=y.lower()
        f = 1
    else:
        f = 0
    if user.get(y) != True:
        if f == 1:
            x = user.get(y).title()
        else:
            x = user.get(y)
    else:
        x = user[y]
    return x
user = {'one' : 'один', 'two' : 'два', 'three' : 'три', 'four' : 'четыре', 'five': 'пять', 'six' : 'шесть', 'seven' : 'семь', 'eight' : 'восемь', 'nine' : 'девять', 'ten' : 'десять'}
y=input("Введите число: ")
print(num_translate(y))


