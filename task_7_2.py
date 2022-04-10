import os

def check(line_number):
    folder = line_number.find(':') # определяем папка или файл
    cursor_position = line_number.find('-') #положение курсора
    if folder > 0:
        a = line_number.partition(':')[0]
        name = a.split('- ')[-1]        #название папки
    if folder < 0:
        name = line_number.split('- ')[-1] #название фаила
    return  folder, cursor_position, name

f1_name='./config.yaml'
dict_adress = {}
with open(f1_name , 'r', encoding='utf-8') as f:
    for line in f:
        raw_row = line.rstrip()
        if check(raw_row)[1] in dict_adress:
            if check(raw_row)[0] > 0:
                os.mkdir('{}\{}'.format(dict_adress[(check(raw_row)[1] - 3)], check(raw_row)[2]))
                dict_adress[check(raw_row)[1]] = ('{}\{}'.format(dict_adress[(check(raw_row)[1] - 3)], check(raw_row)[2]))
        else:
            if check(raw_row)[1] == 0 and check(raw_row)[0] > 0:
                os.mkdir(check(raw_row)[2])
                n_course = check(raw_row)[1]
                dict_adress[check(raw_row)[1]] = ('{}\{}'.format(os.getcwd(), check(raw_row)[2]))
            elif check(raw_row)[1] == 0 and check(raw_row)[0] < 0:
                f_name = ('{}\{}'.format(dict_adress[check(raw_row)[1]], check(raw_row)[2]))
                f = open(f_name, "a")
            elif check(raw_row)[1] > n_course and check(raw_row)[0] > 0:
                os.mkdir('{}/{}'.format(dict_adress[n_course] , check(raw_row)[2]))
                n_course = check(raw_row)[1]
                dict_adress[check(raw_row)[1]] = ('{}\{}'.format(dict_adress[(check(raw_row)[1] - 3)], check(raw_row)[2]))
            elif check(raw_row)[1] > n_course and check(raw_row)[0] < 0:
                f1_name = ('{}\{}'.format(dict_adress[(check(raw_row)[1] - 3)], check(raw_row)[2]))
                f = open(f1_name, "a")
