# Task 1
# Napis funkciu load_book_from_json(file_name), ktora nacita knihy do dataclassy
# Book (ktoru treba tiez vytvorit)
# Format jsonu:
"""
{
    "books": [
        {
            "title": "To Kill a Mockingbird",
            "author": "Harper Lee",
            "year": 1960,
            "isbn": "978-0061120084"
        },
        {
            "title": "1984",
            "author": "George Orwell",
            "year": 1949,
            "isbn": "978-0451524935"
        }
    ]
}
"""

# Task 2
# Napis funkciu print_books(books), ktora v peknom formate vypise vsetky knihy
# a na zaver vypise aj ich pocet

# Task 3
# Napis funkciu add_book(book), ktora upravi json file `books.json` tak, ze sa don
# prida nova kniha predana cez parameter `book` (typu `Book`)

# Task 4
# Napis funkciu remove_book(isbn), ktora vymaze knihu z .json suboru podla isbn cisla.

import json
from dataclasses import dataclass

@dataclass(frozen=True)
class Book:
    title: str
    author: str
    year: int
    isbn: str

    def __str__(self):
        return f'{self.title} by {self.author} from {self.year}. ISBN: {self.isbn}'

def load_books_from_json(file_name):
    loaded_books = []
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
            books_data = data.get('books', [])
            for book in books_data:
                loaded_books.append(Book(**book))
    except FileNotFoundError:
        print(f"File {file_name} not found.")
    return loaded_books

def print_books(books):
    for book in books:
        print(book)
    print(f'Book count: {len(books)}')

def add_book(book):
    try:
        with open('books.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            books = data.get('books', [])
    except FileNotFoundError:
        data = {'books': []}
        books = data['books']

    books.append(book.__dict__)  # Convert Book instance to dictionary

    with open('books.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    file_name = 'books.json'

    # Load and print existing books
    print("Task 2: Print Books")
    books = load_books_from_json(file_name)
    print_books(books)

    # Add a new book
    print("Task 3: Add Book")
    new_book = Book(
        title="Babička",
        author="Božena Němcová",
        year=1855,
        isbn="978-8000063370"
    )
    add_book(new_book)

    # Print books after adding the new one
    print("Books after adding new book:")
    books = load_books_from_json(file_name)
    print_books(books)