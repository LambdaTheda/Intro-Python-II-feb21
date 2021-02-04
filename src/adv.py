from room import Room
from player import Player 

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
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


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
name = input('Welcome to the game! What is your name? ')

# Make a new player object that is currently in the 'outside' room.

player = Player(name, room['outside'])

direction = None
current_room = None
input('Press any key ')

#This is how we are reassigning

while direction != "q":
    if current_room != player.current_room:
        current_room = player.current_room
    print(f'{player.current_room.name }-- \n')    
    print(f"{player.current_room.description} \n")
    direction = input('Choose your direction. Type: n,s,e, or w ')
    if direction.lower() in ["n","s","e","w"]:
        if direction.lower() == "n":
            current_room = current_room.n_to
           
        elif direction.lower() == "s":
            current_room = current_room.s_to
           
        elif direction.lower() == "e":
            current_room = current_room.e_to
            
        elif direction.lower() == "w":
            current_room = current_room.w_to
            
    if current_room is None:
        print('Oh Noes, You can\'t go there! That is a wall. \n')
    else:
        player.current_room = current_room

# Write a loop that:
#
##* Prints the current room name
## * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

##Go play a mud, 
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
