print('Домашнее задание 4 урок 2 задание:')
price = [57.8, 46.51, 97, 13.12, 5.02, 11.11, 18.21, 10.12, 4.6, 6.15]
for pri in price:
        print(''.join(f'{round(pri*100//100)} руб {int((pri*100)-round(pri*100//100)*100):02d} коп,'),end=" ")
print()
print(price)
price.sort(reverse=True)
print(price)
price_1 = sorted(item for item in price if item.__float__)
price_1.reverse()
i = 4
while i >= 0:
    print(''.join(f'{round(price_1[i]*100//100)} руб {int((price_1[i]*100)-round(price_1[i]*100//100)*100):02d} коп,'),end=" ")
    i -=1
