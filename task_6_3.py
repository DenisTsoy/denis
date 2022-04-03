import requests
import pickle
from itertools import zip_longest
full_names = ()
users = []
hobbys = []
hobbys_h = []
response = requests.get("https://randomus.ru/name?type=0&sex=10&count=50")
content = response.text
rav_rov = content.split('data-numbers="')[-1]
rov =rav_rov.split('">')[0]
full_names = rov.split(',')
f1_name='users.csv'
with open(f1_name, 'w', encoding='utf-8') as f1:
    for index in full_names:
        print('{},{},{}'.format(index.split()[0],index.split()[1],index.split()[2]), file=f1)
response_h = requests.get("http://vatolin.info/texts/56-psychologist-client/391-giant-list-of-hobbies-and-pleasures")
content_h = response_h.text
rav_rov_h = content_h.split('<ol style="text-align: justify;">')[-1]
rov_h = rav_rov_h.split('</ol>')[0]
hobbys = rov_h.split(',')
f2_name='hobby.csv'
with open(f2_name, 'w', encoding='utf-8') as f2:
    for index in hobbys:
        hobby = index.split('<li>')[-1]
        print(hobby.split('<li>')[0], file =f2)
f3_name='resultat.csv'
with open(f3_name, 'wb') as f3:
    with open(f1_name, 'r', encoding='utf-8') as f1,  open(f2_name, 'r', encoding='utf-8') as f2:
        for rov1 in f1:
            users.append(rov1.strip())
        for rov2 in f2:
            hobbys_h.append(rov2.strip())
        if len(users) < len(hobbys_h):
            exit(1)
        hobbies_of_users = {user: hobby for (user, hobby) in zip_longest(users, hobbys_h)}
    pickle.dump(hobbies_of_users, f3)
with open(f3_name, 'rb') as f:
    content = pickle.load(f)

print(type(content))
for el in content.items():
    print(el)
