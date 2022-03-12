def thesaurus_adv(*args):
    full_name = {}
    for name in args:
        name_n = name.split()[0][0]
        supername_s = name.split()[1][0]
        if supername_s not in full_name:
            full_name[supername_s] = {supername_s: [name]}
        elif name_n in full_name[supername_s]:
            full_name[supername_s][name_n].append(name)
        else:
            full_name[supername_s][name_n] = [name]
    return full_name
print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))

