src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
resultat = set()
for index in src:
    if index in resultat:
        resultat.discard(index)
        continue
    resultat.add(index)
print([index for index in src if index in resultat])
