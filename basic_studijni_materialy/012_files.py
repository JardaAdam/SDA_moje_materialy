# FILE
"""soubory delime na File a Package"""
"""File = obrazky textaky atd."""
"""Package = moduly s priponou [.py] """
# TODO - oteviraci metody
# basen = open("basen.txt")
# basen.close()

# TODO - metody cteni - bool(str)
# with open("basen.txt", encoding="utf-8") as basen:
    # print(basen.read(5))

    # print(basen.readline())
    # print(basen.readline())

    # print(basen.readlines())

    # radek = basen.readline()
    # while radek:
    #     print(radek, end="")
    #     radek = basen.readline()

    # seznam_radku = basen.readlines()
    # for radek in seznam_radku:
    #     print(radek, end="")

    # for radek in basen:
    #     print(radek, end="")

    # print(basen.read().split())       # TODO - cteni - split()

# TODO - zapis "w"
# with open("novy.txt", "w") as novy_soubor:
#     # for index in range(5):
#     #     novy_soubor.write(f"Radek s indexem {index}\n")
#
#     novy_soubor.writelines(["Ahoj\n", "dnes\n", "je\n", "pekny\n", "den"])

# TODO - prekopirovani souboru
# with open("basen.txt") as basen:
#     with open("novy.txt", "w") as novy_soubor:
#         novy_soubor.writelines(basen.readlines())


# TODO - create "x"
# with open("novy.txt", "x") as novy_soubor:
#     novy_soubor.write("Pracujeme s creation modem.")

# TODO - append "a"
# with open("novy.txt", "a") as soubor:
#     soubor.write("\nRadek pridany appendem.")

# TODO - bytes
with open("basen.txt", "rb") as basen:
    print(basen.read())

# with open("novy.txt", "wb") as novy_soubor:
#     novy_soubor.write(b"Ahoj, ucime se Python")

# TODO - rw +

# with open("basen.txt") as basen:
#
#     print(basen.tell())
#     print(basen.readline())
#     print(basen.tell())
#     print(basen.readline())
#     print(basen.tell())
#
#     basen.seek(0)
#     print(basen.readline())