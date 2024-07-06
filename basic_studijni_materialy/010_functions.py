# FUNKCE
# """Funkce Jak vytvorit vlastni funkci
# kdyz se opakuje kod vic jak jednou uklidim ho do funkce.
# def function_name_1():
#     instuction"""

# TODO - k cemu jsou funkce, oprava kodu
# def vypis_programu():
#     print("Zprava z programu Meteor.")        """radky funkce ktere zacinaji TAB!!"""
#     print("Aktualni datum: 29.5.2024.")
#     print("Dnesni teploty: 20˚C.")
#     print("." * 20)
# vypis_programu()   """radek ktery vola funkci"""

# """pozdrav podle jmena"""
# def greet_by_name(name):
#
#     print(f"hello", (name))
# greet_by_name("Jarda")

# TODO - funkce s parametrem (argumentem)
def secti(cislo1, cislo2):
    print(cislo1 + cislo2)


# secti(7, 5)

# TODO - keyword parametry

def predstaveni_cloveka(jmeno, prijmeni, titul):
    print(f"{titul}. {jmeno} {prijmeni}")


# predstaveni_cloveka("Zdenek", "Volny", "Mgr")     """pozicni umisteni"""
# predstaveni_cloveka(prijmeni="Omacka", titul="Ing", jmeno="Jan")
# predstaveni_cloveka("Dana", titul="Bc", prijmeni="Kovova")

# TODO - typovani funkci zadavam do programu jake data maji byt na kterem vstupu

def predstaveni_cloveka(jmeno: str, prijmeni: str, titul: str):
    print(f"{titul}. {jmeno} {prijmeni}")

"""Default parameters: preddefinovana hodnota"""

predstaveni_cloveka(1 , True, 5)

# TODO - defaultni volitelne parametry

def vypocet_mocniny(mocnenec: int, mocnitel: int=2):
    print(mocnenec ** mocnitel)


# vypocet_mocniny(7)
# vypocet_mocniny(4, 3)


def registrace_lajnera(jmeno: str, prijmeni: str, vek: int, pohlavi: str = "zena"):
    print(f"lajner: {jmeno} {prijmeni}. Vek: {vek}. Pohlavi: {pohlavi}.")

registrace_lajnera("Jarda", "Adam", 31)

# print(registrace_lajnera("Bozena", "Nova", 42))

# TODO - navratove hodnoty return values  posledni radek funkce!
"""pracuje vne programu (prostredi) takze v hlavnim programu zustane jen vysledek bez vypoctu"""

def calculate_square (a):
    return a * a

vysledek = calculate_square(5)
print(vysledek)
def spocti_rok_narozeni(vek: int):
    global aktualni_rok
    """nedoporucuje se delat! vytvori se az po spusteni funkce"""
    aktualni_rok = 2024
    return aktualni_rok - vek
# print("konec funkce")   # nikdy se neprovede


rok_narozeni = spocti_rok_narozeni(50)
# print(rok_narozeni)

# TODO - vice navratovych hodnot

def kalkulacka(cislo1: int, cislo2: int) -> tuple:
    return cislo1 + cislo2, cislo1 - cislo2, cislo1 / cislo2, cislo1 * cislo2


# print(kalkulacka(10, 7))
# print(kalkulacka(10, 5)[3])

"""promenliva kalkulacka"""


# TODO - vice parametru

def secti(list_cisel: list):
    vysledek = 0
    for cislo in list_cisel:
        vysledek += cislo

    return vysledek

# print(secti([1, 2]))
# print(secti([4, 5, 7]))
# TODO Add
"""ARGS  *args  pridavame vlastni hodnoty"""

def secti(*cisla) -> int:
    vysledek = 0
    for cislo in cisla:
        vysledek += cislo

    return vysledek

# print(secti(1, 2))
# print(secti(4, 5, 7))

# TODO - vlastni parametry
# """KWARGS    **kwargs  pridavame vlastni parametry
# vznika slovnik"""


def soucet_ingredienci(**ingredience):
    soucet = 0

    for polozka, pocet in ingredience.items():
        soucet += pocet

    return soucet


# print(soucet_ingredienci(banan=2, mleko=1, maslo=1, cokolada=1))

# TODO - pouziti vice druhu paramteru (kombinace)

def popis_rodiny(jmeno_rodiny, **cleni):
    print(f"Predstaveni rodiny: {jmeno_rodiny}")
    for role, jmeno in cleni.items():
        print(f"{role.capitalize()}: {jmeno}")


popis_rodiny("Novakovi", otec="Petr", matka="Lucie", syn="Tomas", dcera="Libuse")


#TODO - popisovani funkci - komentovani dulezite pro spolupraci v teamu a naslednemu vraceni k funkcim
# komentovani funkce  """komentar"""

def spocti_rok_narozeni(vek: int) -> int:
    """
    Spocitani roku narozeni podle veku uzivatele. Od 2024 se odecte vek na vstupu.
    :param vek: Aktualni vek uzivatele.
    :return: Vypocitany rok narozeni. (s presnosti +-1 rok)
    """
    return 2024 - vek


# print(spocti_rok_narozeni())

# TODO - stinove nazvy promennych/funkci -> pozor na prepisovani jiz zadanych veci!!!
# print = 1
# print("Ahoj")

# TODO - prejmenovani funkci
# vypocti_narozeni = spocti_rok_narozeni
# print(vypocti_narozeni(19))

# TODO - global promenna je volani ktere

a = 15

def spocti_rok_narozeni(vek: int):
    print(a)
    """"""
    global aktualni_rok
    aktualni_rok = 2024
    return aktualni_rok - vek
    print("konec funkce")   # nikdy se neprovede


# rok_narozeni = spocti_rok_narozeni(50)
# print(aktualni_rok)
# print(rok_narozeni)