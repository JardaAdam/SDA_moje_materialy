
# Napis funkciu append_text(filename, text), ktora doplni text `text` do suboru s nazvom `filename`.
# Ak je subor readonly, osetri tento pripad tak, ze vypises na vystup "Cannot write to file <filename>"
# Pre windows userov, ako nastavit, aby bol subor readonly:
# https://adamtheautomator.com/how-to-make-a-file-read-only/

with open("file_readonly.txt", "w") as new_file:
    new_file.writelines("learn how to create folder readonly")

    