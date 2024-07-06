# 2 Loops
# TODO - While stejne jako If ale na konci cyklu se vraci zase na zacatek dokud neni vysledek False
# jedno opakovani cyklu while je jedna Iterace.
# Brake ukoncuje celi cuklus a pokracujeme v programu
# continue ukonci aktualni iteraci a vracime se na zacatek cyklu
# n = 0
# while n < 5:
#     n += 1    # dulezita cast aby nebezel while do nekonecn
#     # print(n)

# cislo = 10

# while cislo > 0:
#
#     cislo -= 1
#     print(cislo)

# TODO - nekonecny cyklus ! nenechat nezakomentovany !!!
n = 0
# while 1:
#     print(f"Nekonecny cyklus - {n}")
#     n += 1

# TODO - continue
# TODO - break
# cislo = 10

# while cislo > 0:
#
#     cislo -= 1
#
#     if cislo in [8, 7, 2]:
#         continue
#
#     if cislo == 4:
#         break
#
#     print(cislo)

# cislo = 90
#
# while cislo <= 990:
#     cislo += 10
#
#     if 500 <= cislo <= 700:
#         continue
#
#     print(cislo)

# TODO - For defined iteration
# definovana iteration je jasne dany pocet opakovani (for)
# for loop pouzivame k nemu kolekce napr. list
list_jmen = ["Lubos", "Jarmila", "Josef", "Eva"]

# for jmeno in list_jmen:
#     print(jmeno)

list_cisel = [1, 2, 3, 4]
vysledek = 0

# for cislo in list_cisel:
#     vysledek += cislo
#
# print(vysledek)

# TODO - for - dve polozky
seznam = {
    "mamka": 12345,
    "tata": 23456,
    "bracha": 34567
}
# seznam = {
#     "mamka": {"cislo": 12345, "email": "email"},
#     "tata": 23456,
#     "bracha": 34567
# }

# print(seznam.items())
# for kontakt in seznam:
#     print(kontakt)
#     print(seznam[kontakt])

# for kontakt in seznam.items():
#     print(kontakt)
# for jmeno, cislo in seznam.items():
#     # jmeno, cislo = kontakt
#     print(f"Kontakt {jmeno} ma cislo {cislo}")

# nejkratsi verze

# for jmeno, cislo in phonebook.items():

    # print(f"kontakt {jmeno} ma cislo {cislo}")

# TODO - for break, continue
# for jmeno in list_jmen:
#
#     if jmeno == "Josef":
#         break
#
#     if jmeno == "Lubos":
#         continue
#
#     print(jmeno)

# TODO - for range()  (start, stop, step) vytvari listy cisel podle zadanych parametru
                   """(aut.0,pov. , aut.1)"""
# for cislo in range(100):
#     print(cislo)

# TODO - Enumerate() vytvari index k prvkum ( od 0 )
poradi_bezcu = ("Tomas", "Lukas", "Jan")

# for poradi, jmeno in enumerate(poradi_bezcu, start=1):
#     print(f"Bezec {jmeno} se umistil na poradi {poradi}.")

# TODO - for zkraceny (priklad s chr()) #zkraceny list jak rychle zapsat dlouhy list
# list_cisel = []
# for cislo in range(1000):
#     list_cisel.append(cislo)

# """zrychlene"""
# list_cisel = [cislo for cislo in range(1000)]
# print(list_cisel)

# list_mocnin = []
# for cislo in range(1, 101):
#     list_mocnin.append(cislo ** 2)

# list_mocnin = [cislo ** 2 for cislo in range(1, 101)]
# list_celych_cisel = [1, 2, 3, 4, 5, 6]
# list_mocnin = [cislo ** 2 for cislo in list_celych_cisel]
# print(list_mocnin)

# list_asci = [chr(cislo) for cislo in range(1, 101)]
# print(list_asci)

# """zkraceny slovnik dics"""
slovnik_mocnin = {cislo: cislo ** 2 for cislo in range(1, 101)}
# print(slovnik_mocnin)

# TODO - else

# TODO - vnoreny cyklus
matice_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for radek in matice_2d:
#     for cislo in radek:
#         print(cislo)