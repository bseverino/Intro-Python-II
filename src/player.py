# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, current_room):
        self.current_room = current_room
        self.items = []

    def move(self, room):
        self.current_room = room

    def inventory(self):
        if len(self.items) > 0:
            print('\nInventory:')
            for item in self.items:
                print(f'* {item.name} - {item.description}')
        else:
            print('\nYou have no items.')

    def take_item(self, item):
        self.items.append(item)

    def drop_item(self, item):
        self.items.remove(item)
