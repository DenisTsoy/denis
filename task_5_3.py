from itertools import zip_longest
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Виктория', 'Денис']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
journal = ((tutor, klass) for tutor, klass in zip_longest(tutors, klasses) if tutor)
print(journal)
print(*journal)

