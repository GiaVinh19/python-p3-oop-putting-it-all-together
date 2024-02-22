#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        assert isinstance(page_count, int), "page_count must be an integer"
        self.title = title
        self.page_count = page_count
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

book1 = Book("Made in Abyss", 100)
book1.turn_page()

