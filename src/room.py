# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def describe(self):
        print(f'\n\n*** {self.name} ***')
        print(f'{self.description}')
        if len(self.items) > 0:
            print('\nAvailable items:')
            for item in self.items:
                print(f'* {item.name} - {item.description}')

    def place_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)
