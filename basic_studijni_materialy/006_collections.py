# 2 Collections
# uschovna vice hodnot najednou ruzne typi atd.
# TODO - List ohranicen (definition square brackets) [] sekvence prvku
# abeceda = ["a"]

# TODO - Naplneni pres append, extend
# append pridavani jednotlivich prvku
# abeceda.append("b")
# abeceda.append("c")
#
# print(abeceda)
# print(len(abeceda))
# extend pridani vice prvku najednou
# abeceda.extend(["x", "f", "e"])
# print(abeceda)
# print(len(abeceda))
# TODO - List - ostatni metody
#sorted- seradi poradi upravi kopii a nezmeni original
# print(sorted(abeceda))
# print(abeceda)
#sort- seradi poradi navzdy
# print(abeceda.sort())
# print(abeceda)
# print(abeceda.count(True))
# Index -> hleda prvek
# print("index")
# print(abeceda.index("x"))                           # vypise umisteni prvku v listu !(pocitano od 0)!
# abeceda.insert(3, False)            # vklada objekty
# print(abeceda)
# print("pop")
# abeceda.pop()           # odebira prvky kdyz jsou zavorky prazdne odebira posledni
# abeceda.pop(3)            # odebira prvek na pozici v zavorkach
# print(abeceda)

# abeceda.remove("x")         # odebira definovany prvek
# print(abeceda)

# abeceda.reverse()           # obraci poradi v listu
# print(abeceda)
# print("clear")
# abeceda.clear()             # maze celi list
# print(abeceda)
"""tuple jsem zkoncil"""
# TODO Slicing list
users = ["Alice", "Bob", "Chris", "John"]
# print(users)
# print(users[0:3])       # vypise od [ nulteho : do druheho]
# print(users[1:2])       # vypise pouze [ prvni pozici ]
# print(users[1:])        # vypise od [ prvni pozice : defaultne do konce ]

# TODO - matice -> list listu
matice_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matice_2d)        # vypise kompletni list listu
# print(matice_2d[1])     # vypise list [index listu]  !! ( pocitame od nuli ) !!
# print(matice_2d[1][2])  # vypise cislo ([index listu][index cisla]
# print(len(matice_2d))   # zpocita pocet listu v listu
# matice_2d.append([10, 11, 12])
# print(matice_2d)
# TODO - string split
veta = "Ucime se v Pythonu"
# print(veta.split())         # rozdeli vetu na stringy
# print(veta.count(" "))      # zpocita mezery ve vete
# TODO - Dict - slovnik {} sam si priradim k prvku vlastni klic  { key : value }
# priklad telefoni seznam
# print("slovnik")
seznam = {"mamka": 12345,
          "tata": 23456,
          "bracha": 34567,
          "sestra": 56789}

# print(seznam)
# print(seznam["sestra"])             # vypise hodnotu pro klic -> ["sestra"]

# TODO - pristup
# seznam.pop("bracha")                # odstrani key "bracha"
# del seznam["sestra"]                  # odstrani key "sestra"
#
# print(seznam)

# print(seznam.get("bracha", "Nemohl jsem nic najit"))  # hleda ve slovniku key "bracha" za , je udano co
# ma napsat jako vysledek

# TODO - Tuple  neprepsatelny list  definuje ho , viz tupple1
# tuple po vytvoreni nelze upravovat!!! muze obsahovat prvky ruznych datovych typu
# v pripade tuplu s jednin prvkem je nutne za prvek dat , !!
# print("tuple")
# tupple = ("pes", "kocka", 2000, 5.0, True)
# tupple1 = "lajna", "wblock", 350, 4.5, False
# print(tupple[3])
# print(tupple1[4])
# print(len(tupple1))
# TODO - unpacking
tuple_cisla = (25, 30, 49, 87)

# w, y, z, x = tuple_cisla        # postup prirarezi pismen k cislum v taplu

# print(y - w)                    # rovnou pocita vysledek


# TODO - Set neusporadana colekce prvku ktera nema pevne poradi a neobsahuje duplicity lze prepisovat a odstranovat prvky
# definice : slozene zavorky (curly brackets) {} nebo konstruktorem set()
farma = {"pes", "kocka", "prase", "kun"}        # vytvoreni skupinu set
print(farma)                                    # kazdy print se meni poradi

# TODO - Set - pridavani, odebirani
farma.add("pes")                            # add -> pridava jednotlive prvky ("pes" uz je ve skupine takze se neprida
print(farma)
farma.update(["papousek", 25])              # update -> pridava vice prvku najednou
print(farma)

farma.remove(25)                       # odstrani prvek pokud prvek neni v kolekci vyhodi error
farma.discard("hovno")                 # odstrani prvek ale pokud se prvek nenachazi v colekci nevyhodi error!!
print(farma)
# TODO - operace nad kolekcemi
print("operace")
print("hovno" in farma)                   # ptam se zda je prvek "pes" v kolekci odpoved je True nebo False


# TODO - Pretypovani pomoci pretipuvani lze pridat do tuplu
print("pretypovani")
staly_tuple = 1, 2, 3
print(staly_tuple)
pomocny_list = list(staly_tuple)            # pretipovani tuplu na list
print(pomocny_list)
pomocny_list.append("shackel")              # pridani prvku v listu
novy_tuple = tuple(pomocny_list)            # zpetne pretipovani na tuple
print(novy_tuple)