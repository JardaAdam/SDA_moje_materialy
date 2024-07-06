# TODO - proc OOP


# TODO - Class definice - metody a atributy
class Zvire:

    vyskyt = "Evropa"

    # TODO - konstruktor init
    def __init__(self, jmeno_zvirete: str, vek_zvirete: int):
        self.jmeno = jmeno_zvirete
        self.vek = vek_zvirete

    def predstav_se(self):
        print(f"Moje jmeno je {self.jmeno} a je mi {self.vek} let.")

    def nakrm_se(self, jidlo: str = "granule"):
        print(f"Jim {jidlo}")


# TODO - vytvorit objekty
moje_kocka = Zvire("Alice", 10)
# moje_kocka.predstav_se()
moje_kocka.vek = 15
# moje_kocka.predstav_se()
# print(moje_kocka.jmeno)
# moje_kocka.nakrm_se()

# TODO - nezavislost objektu
muj_pes = Zvire("Hafik", 2)
# muj_pes.jmeno = "Hafik"
# muj_pes.vek = 2

# moje_kocka.predstav_se()
# muj_pes.predstav_se()
# muj_pes.nakrm_se()
# moje_kocka.nakrm_se("mleko")

# TODO - vnitrni promenne - _p
# class Zvire:
#
#     vyskyt = "Evropa"
#
#     # TODO - konstruktor init
#     def __init__(self, jmeno_zvirete: str, vek_zvirete: int):
#         self.jmeno = jmeno_zvirete
#         self._vek = vek_zvirete
#
#     def predstav_se(self):
#         print(f"Moje jmeno je {self.jmeno} a je mi {self._vek} let.")
#
#     def nakrm_se(self, jidlo: str = "granule"):
#         print(f"Jim {jidlo}")
#
#
# pes = Zvire("hafik", 2)
# print(pes._vek)
# pes._vek = -10
# pes.predstav_se()

# TODO - soukrome promenne - __p
# class Zvire:
#
#     vyskyt = "Evropa"
#
#     # TODO - konstruktor init
#     def __init__(self, jmeno_zvirete: str, vek_zvirete: int):
#         self.jmeno = jmeno_zvirete
#         self.__vek = vek_zvirete
#
#     def predstav_se(self):
#         print(f"Moje jmeno je {self.jmeno} a je mi {self.__vek} let.")
#
#     def nakrm_se(self, jidlo: str = "granule"):
#         print(f"Jim {jidlo}")
#
#     def vrat_vek(self):
#         return self.__vek
#
#     def nastav_vek(self, novy_vek):
#         if novy_vek > self.__vek:
#             self.__vek = novy_vek
#         else:
#             raise ValueError("Novy vek neni vetsi nez stavajici!")
#
#
# pes = Zvire("hafik", 2)
# # print(pes.__vek)
# # pes.__vek = -10
# # pes.nastav_vek(-5)
# pes.nastav_vek(10)
# pes.predstav_se()

# TODO - properties
class Zvire:

    vyskyt = "Evropa"

    # TODO - konstruktor init
    def __init__(self, jmeno_zvirete: str, vek_zvirete: int):
        self.jmeno = jmeno_zvirete
        # self.__vek = vek_zvirete
        if vek_zvirete >= 0:
            self.__vek = vek_zvirete
        else:
            raise ValueError("Novy vek neni vetsi nez stavajici!")

    def predstav_se(self):
        print(f"Moje jmeno je {self.jmeno} a je mi {self.__vek} let.")

    def nakrm_se(self, jidlo: str = "granule"):
        print(f"Jim {jidlo}")

    @property
    def vek(self):
        return self.__vek

    @vek.setter
    def vek(self, novy_vek):
        if novy_vek > self.__vek:
            self.__vek = novy_vek
        else:
            raise ValueError("Novy vek neni vetsi nez stavajici!")

    @vek.deleter
    def vek(self):
        del self.__vek


pes = Zvire("hafik", 2)
# print(pes.__vek)
# pes.vek = -10
pes.vek = 4
# print(pes.vek)
# pes.predstav_se()

# TODO - garbage collector
# TODO - odkazovani, kopie
a = Zvire("Hafik", 5)
b = a

b.vek = 10

# a.predstav_se()
# b.predstav_se()

# TODO - __dict__
# print(a.__dict__)

# TODO - magic methods
class Clovek:

    def __init__(self, jmeno, vek, pohlavi="zena"):
        self.jmeno = jmeno
        self.vek = vek
        self.pohlavi = pohlavi

    def __str__(self):
        return self.jmeno

    def __int__(self):
        return self.vek

    def __add__(self, other):
        return Clovek(other.jmeno, 0, other.pohlavi)

    def __eq__(self, other):
        return self.vek == other.vek

    def predstav_se(self):
        print(f"Moje jmeno je {self.jmeno} a je mi {self.vek} let.")


adam = Clovek("Adam", 15, "muz")
# print(str(adam))
# print(int(adam))

eva = Clovek("Eva", 20)

dite = eva + adam
# adam.predstav_se()
# dite.predstav_se()

# print(adam == eva)
# print(adam > eva)


# TODO - zapouzdreni metod


# TODO - odkazovani, kopie, garbage collector


# TODO - dedeni

class Zvire:

    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek


class Savec(Zvire):

    def dychej(self):
        print("Dycham")


class Pes(Savec):

    def stekej(self):
        print("Haf")


class Opice(Savec):

    def skakej(self):
        print("Skacu po strome")


class Zirafa(Savec):

    def __init__(self, jmeno, vek, delka_krku):
        super().__init__(jmeno, vek)
        self.delka_krku = delka_krku


pes = Pes("Alik", 3)
opice = Opice("Zofie", 7)
zirafa = Zirafa("Melmen", 15, 100)

# pes.stekej()
# opice.skakej()
# zirafa.dychej()


# TODO - dedeni ze dvou trid

class Netopyr:

    def let(self):
        print("Letim")


class Clovek:

    def bez(self):
        print("Bezim")


class Batman(Netopyr, Clovek):

    def chyt_zlocince(self):
        self.let()
        self.bez()
        print("Zneskodnuji zlocince")


bruce_wayne = Batman()
# bruce_wayne.chyt_zlocince()

# TODO - polymorfismus


# TODO - isinstance, type
# print(type(bruce_wayne))
# print(type(3.4))

# print(isinstance(bruce_wayne, Batman))
# print(isinstance(bruce_wayne, Netopyr))
# print(isinstance(bruce_wayne, Opice))


# TODO - doplnuji funkce
# print(sum([4, 1, 7, 6]))
# print(max([4, 1, 7, 6]))
# print(min([4, 1, 7, 6]))
