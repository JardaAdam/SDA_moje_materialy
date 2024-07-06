# TODO Control instructions
""" vzdycky se provede jenom prvni True podminka a potom pokracuje v programu dal

 if -> co se ma stat v pripade kladneho (True) vysledku

 elif -> pokud byl vysledek if (False) pokracuje se na elif podminku

 else -> co se ma stat v pripade zaporneho (False) vusledku

if condition:
![TAB]!instruction_1
    instruction_2
     instruction_3
instruction_4 tato podminka se provede nezavisle na podmince"""
# TODO - if
prsi = False
"""promena se kterou pracujou dalsi radky """

# if prsi:
#     print("Vezmu si destnik")
#     print("Vezmu si bundu")
#     print("Vezmu si nepromokave boty")
# print("Jdu nakupovat")
#
# if prsi:
#     print("Vem si destnik")
# else:
#     print("Vem si slunecni bryle")
# print("Jdi nakupovat")

# TODO - elif statement vetveni podminek provede se prvni True
cena = 150
vek_zakaznika = 15

# if vek_zakaznika <= 25:
#     typ_zakaznika = "student"
#     sleva = 0.2
# # #elif vek_zakaznika >= 90:
# #     typ_zakaznika = "senior vyherce"
# #     sleva = 2
# # elif 65 <= vek_zakaznika < 100:
# #     typ_zakaznika = "senior"
# #     sleva = 0.5# """ tento zapis se da nahradit dalsim if v elif viz. dalsi radky"""
# elif vek_zakaznika >= 65:
#     if vek_zakaznika >= 90:
#         typ_zakaznika = "senior vyherce"
#         sleva = 3
#     else:
#         typ_zakaznika = "senior"
#         sleva = 0.5
#
# elif vek_zakaznika == 50:
#     typ_zakaznika = "padesatnik"
#     sleva = 1
# else:
#     typ_zakaznika = "dospely"
#     sleva = 0
#
# print(f"Zakaznik je {typ_zakaznika}. Finalni cena listku je: {cena - cena * sleva} Kc.")


pocet_dni_dovolene = 15
volne_penize = 60000
jsem_nemocny = False

# if pocet_dni_dovolene >= 10 and volne_penize >= 50000 and not jsem_nemocny:
#     print("Jedu na dovolenou")
# else:
#     print("Nejedu na dovolenou")

mam_hlad = True
mam_chut = False

# if mam_chut or mam_hlad:
#     print("Jdu se najist")
# else:
#     print("Nejdu se najist")

# TODO - Zkraceny if

# print("Jdu se najist") if mam_chut or mam_hlad else print("Nejdu se najist")

# TODO trening
print("vypocet ceny listku")

"""vlozeni dat uzivatelem v prikazovem radku pres input"""

# jmeno_zakaznika = input("Ahoj jak se jmenujes? napis mi sve jmeno:")
# cena = 150
# vek_zakaznika = int(input("zadej svuj vek: "))

"""import dat pres Terminal (uzivatel zada data za script)"""

import sys
jmeno_zakaznika = (sys.argv[1])
vek_zakaznika = int(sys.argv[2])

if vek_zakaznika <= 25:
    typ_zakaznika = "student"
    sleva = 0.2
# #elif vek_zakaznika >= 90:
#     typ_zakaznika = "senior vyherce"
#     sleva = 2
# elif 65 <= vek_zakaznika < 100:
#     typ_zakaznika = "senior"
#     sleva = 0.5# """ tento zapis se da nahradit dalsim if v elif viz. dalsi radky"""
elif vek_zakaznika >= 65:
    if vek_zakaznika >= 90:
        typ_zakaznika = "senior vyherce"
        sleva = 3
    else:
        typ_zakaznika = "senior"
        sleva = 0.5

elif vek_zakaznika == 50:
    typ_zakaznika = "padesatnik"
    sleva = 1
else:
    typ_zakaznika = "dospely"
    sleva = 0

print(f"{jmeno_zakaznika} jsi {typ_zakaznika}. Finalni cena listku je: {cena - cena * sleva} Kc.")