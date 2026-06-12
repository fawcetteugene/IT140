# Trevon Mathis

print("🧠 Welcome to the Tech-Hacker Adventure Game!")
print("Your mission: Collect 6 cyber tools to defeat the Villain Hacker and secure the system.")
print("🔁 Commands: go North/South/East/West | get [item] | exit")
print("⚔️ Tools needed: Laptop, Firewall Token, USB Drive, Encrypted Key, Toolkit, Admin Badge")
print("--------------------------------------------------")

# Room layout and items
rooms = {
    'Lobby': {'North': 'Server Room', 'East': 'Office', 'West': 'Break Room'},
    'Server Room': {'South': 'Lobby', 'East': 'Security Room', 'item': 'Laptop'},
    'Security Room': {'West': 'Server Room', 'item': 'Firewall Token'},
    'Office': {'West': 'Lobby', 'North': 'Lab', 'item': 'USB Drive'},
    'Lab': {'South': 'Office', 'East': 'Control Room', 'item': 'Encrypted Key'},
    'Control Room': {'West': 'Lab', 'North': 'Data Vault', 'item': 'Toolkit'},
    'Data Vault': {'South': 'Control Room', 'item': 'Villain Hacker'},
    'Break Room': {'East': 'Lobby', 'item': 'Admin Badge'}
}

# Hints for each room
room_hints = {
    'Lobby': "💡 Tip: This is the hub. Explore East, West, or North to begin your mission.",
    'Server Room': "💡 You sense a critical tool is nearby. Maybe it's techy and portable?",
    'Security Room': "💡 This place looks highly guarded. Something firewall-related might be here.",
    'Office': "💡 Desks and drawers... Sounds like a good place to find storage devices.",
    'Lab': "💡 This room feels encrypted. Could there be a key to unlock hidden secrets?",
    'Control Room': "💡 Tools of all sorts are lined up. Grab what you need!",
    'Data Vault': "💡 Final confrontation ahead. Be sure you're fully geared up.",
    'Break Room': "💡 It's not all snacks here... look around for something with authority."
}

required_items = ['Laptop', 'Firewall Token', 'USB Drive', 'Encrypted Key', 'Toolkit', 'Admin Badge']
current_room = 'Lobby'
inventory = []

# Game loop
while True:
    print(f"\n📍 You are in the: {current_room}")
    print(f"🎒 Inventory: {inventory}")
    
    # Show hint
    if current_room in room_hints:
        print(room_hints[current_room])

    print("--------------------------------------------------")

    # Item in the current room
    if 'item' in rooms[current_room] and rooms[current_room]['item'] not in inventory:
        item = rooms[current_room]['item']
        if item == 'Villain Hacker':
            if len(inventory) == len(required_items):
                print("😎 You confront the Villain Hacker with all your tools...")
                print("💥 You launch your cyber defense and defeat the villain!")
                print("🏆 YOU WIN! The system is now safe. Mission accomplished.")
            else:
                print("💀 You encounter the Villain Hacker...")
                print("🧨 You don’t have all the tools to stop them.")
                print("🔥 SYSTEM BREACHED. GAME OVER.")
            break
        else:
            print(f"🧱 You spot a {item} here.")

    # Get user input
    command = input("\n🕹️  What do you want to do? ").strip().title()

    # Quit game
    if command.lower() == 'exit':
        print("👋 Thanks for playing! See you next hackathon 😎")
        break

    # Move command
    elif command.startswith("Go "):
        direction = command[3:]
        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
        else:
            print("🚧 You can't go that way. Try another direction.")

    # Get item command
    elif command.startswith("Get "):
        if 'item' in rooms[current_room]:
            item_in_room = rooms[current_room]['item']
            user_item = command[4:]
            if user_item.lower() == item_in_room.lower():
                if item_in_room not in inventory:
                    inventory.append(item_in_room)
                    print(f"✅ {item_in_room} collected and added to your tools.")
                else:
                    print("⚠️ You already have this tool.")
            else:
                print(f"❌ No '{user_item}' found here.")
        else:
            print("🚫 There's nothing here to pick up.")

    # Invalid input
    else:
        print("❗ Unknown command. Use 'go [direction]' or 'get [item]'.")

    # Final check before villain encounter
    if current_room == 'Data Vault' and len(inventory) == len(required_items):
        print("💪 You've collected all cyber tools. You're ready to confront the Villain Hacker!")

