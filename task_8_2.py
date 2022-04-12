import re


f_name='nginx_logs.txt'
with open(f_name, 'r', encoding='utf-8') as file:
    for row in file:
        pattern = re.compile(r'(?P<remote_addr>^\d+\.\d+\.\d+\.\d+).+')
        all_resultat = pattern.findall(row)
        if len(all_resultat):
            pattern = re.compile(r'(?P<remote_addr>^\d+\.\d+\.\d+\.\d+).+'
                             r'\[(?P<request_datetime>[\d\w/: \+]+)\] "'
                             r'(?P<request_type>[A-Z]+) '
                             r'(?P<requested_resource>/\w+/\w+) \w+/\d\.\d" '
                             r'(?P<response_code>\d+) '
                             r'(?P<response_size>\d+)')
            all_resultat = pattern.findall(row)
            print(all_resultat)
        else:
            pattern = re.compile(r'(?P<remote_addr>^\w+\:\w+\:\w+\:\w+\:\w+\:\w+\:\w+\:\w+).+'
                             r'\[(?P<request_datetime>[\d\w/: \+]+)\] "'
                             r'(?P<request_type>[A-Z]+) '
                             r'(?P<requested_resource>/\w+/\w+) \w+/\d\.\d" '
                             r'(?P<response_code>\d+) '
                             r'(?P<response_size>\d+)')
            all_resultat = pattern.findall(row)
            print(all_resultat)
