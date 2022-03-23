import requests
import decimal
def currency_rates(n):
    response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    exchange_rate = {}
    content = response.text
    data_line = content.split('<ValCurs Date="')[-1]
    data = data_line.split('" name')[0]
    for el in content.split('<CharCode>')[1:]:
        working_line = el.split('</Name>'[0])
        char_code = el.split('</CharCode>')[0]
        nominal_line = el.split('</Nominal>')[0]
        nominal =int(nominal_line.split('<Nominal>')[-1])
        name_line = el.split('</Name>')[0]
        name =  name_line.split('<Name>')[-1]
        course_line =el.split('</Value>')[0]
        course= course_line.split('<Value>') [-1]
        course=decimal.Decimal(course.replace(',','.'))
        exchange_rate[char_code] = course / nominal
    if exchange_rate.get(n, True) != True:
        print(data, n.upper()  ,exchange_rate[n.upper()])
    else:
        print(None)
currency_rates(input('Введите валюту: '))
