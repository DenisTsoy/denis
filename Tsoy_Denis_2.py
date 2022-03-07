print('Домашнее задание 2 урок 2 задание:')
weather_forecasts = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for weather_forecast in weather_forecasts:
    j = weather_forecast.find('+')
    k = weather_forecast.find('-')
    if weather_forecast.isdigit() or j == 0 or k ==0:
        i = int(weather_forecast)
        if i < 10 and j == 0:
            print('"+0{}"'.format(i), end =" ")
        elif i < 10 and k ==0:
            print('"-0{}"'.format(i), end =" ")
        elif i < 10:
            print('"0{}"'.format(i), end =" ")
        elif i > 10 and j == 0:
            print('"+{}"'.format(i), end =" ")
        elif i > 10 and k == 0:
            print('"-{}"'.format(i), end =" ")
        elif i > 10:
            print('"{}"'.format(i), end =" ")
    else:
        print(weather_forecast , end =" ")
