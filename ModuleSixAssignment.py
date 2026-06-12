# Trevon Mathis
# IT-140 Module Six Milestone
# Simplified Dragon Text Game

# Room layout dictionary
rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}

# Starting room
current_room = 'Great Hall'

# Show initial instructions
print("Welcome to the Dragon Text Game (Simplified)!")
print("Move commands: go North, go South, go East, go West")
print("Type 'exit' to quit the game.")

# Game loop
while True:
    print("\nYou are in the", current_room)
    command = input("Enter your move: ").strip().title()

    # Exit game
    if command == 'Exit':
        print("Thanks for playing the game. Hope you enjoyed it!")
        break

    # Parse command
    if command.startswith('Go '):
        direction = command[3:]  # Get direction part after "go "

        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
        elif direction in ['North', 'South', 'East', 'West']:
            print("You can't go that way.")
        else:
            print("Invalid direction. Try North, South, East, or West.")
    else:
        print("Invalid command. Use: go North, go South, go East, go West, or 'exit'.")

