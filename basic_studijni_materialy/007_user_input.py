# User input
#TODO - input  vsechny data od uzivatele prevadi Python na string -> cisla je treba pretipovat do int!!
# input() pri zadani program ceka na vlozeni dat od uzivatele
# lepsi pro mensi programy

# print("Spustil se program na vypocet roku narozeni.")
# jmeno_uzivatele = input("Zadej sve jmeno: ")
# """ inputem si vyzadam data od uzivatele """
# print(f"Ahoj {jmeno_uzivatele}, vitej v tomto programu!")
# """ v {} jsou data od uzivatele """
# vek_uzivatele = int(input("Zadej svuj vek: "))
# """ int -> natipuju si co od uzivatele chci za typ dat ( chci cislo ) kontrolni mechanismus """
# print(f"Tvuj rok narozeni je {2024 - vek_uzivatele}")


#TODO - argumenty - prikazovy radek, pycharm
# command line parameters
# vstupi pro program napisu programu vstupi za nazev souboru
# tento ukon zacina : import sys (knihovna)
# tyto data zadavam v prikazovem radku!! a spoustim je v Terminalu NE! -> Run !!
# tento zpusob preda data programu na zacatku a program neceka na uzivatelske vstupi jako v pripade nad timto psanim

# 07_user_input.py Jarda 31 -> """ script """

import sys              # import knihovny
print(sys.argv)         # vypis kompletnich argumentu ( argv jsou tipovane jako str ) !!!
print(sys.argv[0])      # nulty argv = nazev skriptu ktery spoustime
print(sys.argv[1])      # vypis prvniho argv ( v tomto pripade jmeno )

print("Spustil se program na vypocet roku narozeni.")
jmeno_uzivatele = (sys.argv[1])
""" urcuji ktery argv bude vlozen do dalsiho radku -> aby mohl program zpracovat data """
print(f"Ahoj {jmeno_uzivatele}, vitej v tomto programu!")

vek_uzivatele = int(sys.argv[2])
""" argv[2] musim pretipovat na !int! kvuli dalsimu vypoctu, pozice 2 je snad jasna ze zapisu ( scriptu )"""
print(f"Tvuj rok narozeni je {2024 - vek_uzivatele}")

print(type(vek_uzivatele))