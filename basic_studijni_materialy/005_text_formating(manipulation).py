# 1 Text manipulation
# TODO - len, index (find), count
#Funkce ve stringu
# index zacina !0!

veta = "chodime na lajnach rychle"          # string
#       0123456789
# TODO Funkce-len pocita pismena ve stringu
# print(len(veta))    # 25
# TODO Funkce-index udava kde zacina slovo
# print(veta.index("lajnach"))      # kde slovo zacina pocitano od 0
# print(veta.index(" "))              # kde je prvni mezera
# TODO Funkce- count pocita kolik je ceho v
# print(veta.count(" "))              # kolik je ve stringu mezer

# print(veta[15])                     # jake pismeno je na teto pozici

# TODO - string slicing vysec z textu
veta = "chodime na lajnach rychle"
# print(veta[5:13])            # vypise [ pismeno na kterem zacina : pismeno po kterem konci ] vysec
# print(veta[2:15:4])            # vypise [ prvni pismeno : pismeno po poslednim vypsanem : ob kolik pismen ]
# print(veta[:5])              # [ automaticky (defaultne) 0 : na kterem konci ]
# print(veta[5:])           # [ prvni pismeno ktere vypise : defaultne konec ]
# print(veta[::-3])           # [ 0 : posledni pismeno : vypisuje kazde 3 a znamenko - takze vypisuje od konce ]

# print(veta[len(veta) - 10])     # pismeno od konce
# print(veta[3:-3])                   # [ prvni pismeno : posledni pismeno cislovane od konce ]

# TODO - funkce nad stringy - lower,upper, replace, split..
# print(veta.upper())               # vsechny pismena zmeni na velke
# print(veta.lower())               # vsechny pismena zmeni na male
# print(veta.split())                 # udela z listu stringi
# print(veta.isspace())               # odpoved bool -> pokud je string jenom mezera vypise True jinak napise False
# print(veta)
# TODO - retezeni funkci - lower, islower

print(veta[2:15].upper().split())  # zvetsi pismena urcena v [] a rozdeli na stringy

