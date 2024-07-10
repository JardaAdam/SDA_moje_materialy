# Task 1
# Napis generator `even_numbers()`, ktory bude generovat donekonecna parne (sude) cisla

# Task 2
# Napis generator `my_range(start, stop=None, step=1), ktory sa sprava rovnako
# ako funkcia range


def even_number():
    num = 0
    while True:
        yield num
        num +=2


for i in even_number():
    print(i)
    if i >100:
        break


def my_range():
    num = 0