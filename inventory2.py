class Inventory:
    def __init__(self):
        self.slots = []

    def add_item(self, item):
        self.slots.append(item)

class SortedInventory(Inventory):
    def add_item(self, item):
        super().add_item(item)
        self.item = item
        self.slots.sort()
    pass


# https://teamtreehouse.com/community/super-inventorypy-part2-i-dont-think-i-understand-what-the-question-is-asking-me-to-do




