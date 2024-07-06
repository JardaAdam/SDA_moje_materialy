# MODULES
# Modul index -> knihovny ktere jsou ke stazeni
# Na strankach Doc.Python.org je prehled predinstalovanych knihoven
# pro volbu knihovny je dobre pouzivat Chatgpt a jine AI
# TODO CTRL odkazuje na funkce

"""muzu si vytvorit vlastni modul ktery vytvorim jako soubor .py -> modul_A.py ve kterem budu mit napsanou nejakou
funkcionalitu kterou pak pouzivam v hlavnim programu [main.py]"""
"""!!import jeden modul na jeden radek!!"""
"""druhy modulu: vestavene       !! v tomto poradi je i vypisujeme import do main.py souboru !! (pomuze nam s tim Pycharm)
                 externi
                 vlastni """
"""vlastni moduli ukladam primo do projektu tedy do stejne slozky kde je main.py"""
"""PYTHONPATH"""
# 4 tipy importu modulu
# Factorial(6) -> nasobeni po sobe jsoucich cisel ( 1*2*3*4*5*6)
# Math print (math.pi) pomoci CTRL otevru napovedu
# TODO - moduly - ruzne druhy importu a volani funkci (math)
"""1 nejbezpecnejsi import kvuli pouzivani vice funkci najednou"""
# import math
#
# print(math.factorial(5))
# print(math.pi)
"""2 moc se nepouziva prejmenovavani funkci ( pouziva se kdyz ma funkce dlouhy nazev"""
# import math as matematika

# print(matematika.factorial(10))
# print(matematika.sqrt(16))
"""3 import casti knihovny ( setreni operacni pameti ) pouziva se kdyz potrebuju jen malou cast knihovny"""
# from math import factorial, pi
# print(factorial(4))
# print(pi)
# print(math.sqrt(16))
"""4 import cele knihovny pomoci * moc se nepouziva protoze v kodu neni pouziti prehledne"""
# from math import *
# print(sqrt(25))
# print(pi)
# print(factorial(2))

# TODO - dir() vypisuje nazvy ze souboru
# import math
# print(dir(math))

# a = 5
# b = 1
# print(dir())

# TODO - random modul, google, modul index
# import random
#
# print(random.randint(1, 100))
# print(random.choice(["Ondra", "Lukas", "Petr"]))

# TODO - os  Prace s moduly
# import os
#
# print(os.getpid())
# print(os.cpu_count())
# TODO - string
# import string
#
# print(string.printable)

# TODO - logging vypisovani na vystup podobne jako print ale komplexneji
import logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Spoustim funkci f')
logging.info('Prihlasil se uzivatel Tonda')
logging.warning('Dochazi nam misto v pameti')
logging.error('Nefunkci odkaz na stranku')
logging.critical('Spadnul cely web')

# TODO - prohlidka implementace funkce nejake knihovny


# TODO - codewars