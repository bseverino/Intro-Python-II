from player import Player
from item import Item
from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! The only exit is to the south."""),
}

# Item population

room['foyer'].items.append(Item('sword', 'an old looking sword.'))
room['treasure'].items.extend([Item('coins', 'a pouch of shiny coins.'), Item(
    'gem', 'a brilliant red gemstome.'), Item('dagger', 'an exquisitely carved dagger.')])

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('outside')

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

action = ['']
current_room = room.get(player.current_room)

while action[0] != 'q':
    print(f'\n*** {current_room.name} ***')
    print(f'{current_room.description}')

    if len(current_room.items) > 0:
        print('\nAvailable items:')
        for item in current_room.items:
            print(f'* {item.name} - {item.description}')

    action = input(
        '\nPlease enter a command ([h] for help): ').split()

    if len(action) == 2:
        contains_item = False
        if action[0] == 'get' or action[0] == 'take':
            for item in current_room.items:
                if item.name == action[1]:
                    item.on_take()
                    current_room.items.remove(item)
                    player.items.append(item)
                    contains_item = True
        if action[0] == 'drop':
            for item in player.items:
                if item.name == action[1]:
                    item.on_drop()
                    player.items.remove(item)
                    current_room.items.append(item)
                    contains_item = True
        if contains_item == False:
            print("\nThere is no such item in the room.")

    elif action[0] == 'h':
        print(
            '\nCommands:\nMove: [n], [s], [w], [e]\nPick up item: [get ITEM] or [take ITEM]\nDrop item: [drop ITEM]\nInventory: [i] or [inventory]\nQuit game: [q]')

    elif action[0] == 'i' or action[0] == 'inventory':
        if len(player.items) > 0:
            print('\nInventory:')
            for item in player.items:
                print(f'* {item.name} - {item.description}')
        else:
            print('\nYou have no items.')

    elif action[0] == 'n':
        try:
            current_room = current_room.n_to
        except AttributeError:
            print('\nYou cannot go north')

    elif action[0] == 'e':
        try:
            current_room = current_room.e_to
        except AttributeError:
            print('\nYou cannot go east')

    elif action[0] == 's':
        try:
            current_room = current_room.s_to
        except AttributeError:
            print('\nYou cannot go south')

    elif action[0] == 'w':
        try:
            current_room = current_room.w_to
        except AttributeError:
            print('\nYou cannot go west')

    elif action[0] != 'q':
        print('\nPlease enter a valid command')
