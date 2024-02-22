#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        assert isinstance(size, int), "size must be an integer"
        self.brand = brand
        self.size = size
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

shoe1 = Shoe("Puma", 10)
shoe1.cobble()
print(shoe1.condition)