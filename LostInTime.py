# %%
import pygame
import threading
import time
import pyfiglet
from colorama import Fore

# %%
#1914_WW1
airforce = {
    "name": "airforce",
    "type": "room element",
}

time_machine_a = {
    "name": "time machine a",
    "type": "door",
}

key_time_machine_a = {
    "name": "key for time machine a",
    "type": "key",
    "target": time_machine_a,
}

soldier = {
    "name": "soldier",
    "type": "room element",
}

WW1_1914 = {
    "name": "World War 1 - 1914",
    "type": "room",
}

note_1 = {
    "name": "a mysterious note",
    "type": "note",
    "content": "To move forward, you need to trust in those around you. What they carry may open doors."
}

#1969_Apollo11
Apollo11_1969 = {
    "name": "Apollo 11 - 1969",
    "type": "room"
}

time_machine_c = {
    "name": "time machine c",
    "type": "door",
}

time_machine_b = {
    "name": "time machine b",
    "type": "door",
}

astronaut = {
    "name": "astronaut",
    "type": "room element"
}

helmet = {
    "name": "helmet",
    "type": "room element"
}

key_time_machine_b = {
    "name": "key for time machine b",
    "type": "key",
    "target": time_machine_b,
}

note_2 = {
    "name": "a mysterious note",
    "type": "note",
    "content": "To reach new worlds, pay attention to those who have traveled far."
}

#2150_future
Future_2150 = {
    "name": "Future - 2150",
    "type": "room"
}

saturn = {
    "name": "saturn",
    "type": "room element"
}

key_time_machine_c = {
    "name": "key for time machine c",
    "type": "key",
    "target": time_machine_c,
}

note_3 = {
    "name": "a mysterious note",
    "type": "note",
    "content": "Remember the rings that shine so bright, they may help you find a way."
}

time_machine_d = {
    "name": "time machine d",
    "type": "door",
}

space_shuttle = {
    "name": "space shuttle",
    "type": "room element"
}

key_time_machine_d = {
    "name": "key for time machine d",
    "type": "key",
    "target": time_machine_d,
}

#stone_age
Stone_age = {
    "name": "Stone Age",
    "type": "room"
}

fire_pit = {
    "name": "fire pit",
    "type": "room element"
}

pile_of_stones = {
    "name": "pile of stones",
    "type": "room element"
}

time_machine_e = {
    "name": "time machine e",
    "type": "door",
}

Cave = {
    "name": "Cave",
    "type": "room"
}

hand_axe= {
    "name": "hand axe",
    "type": "room element"
}

spears_and_arrows= {
    "name": "spears and arrows",
    "type": "room element"
}

bear = {
    "name": "bear",
    "type": "room element"
}

key_time_machine_e = {
    "name": "key for time machine e",
    "type": "key",
    "target": time_machine_e,
}

note_4 = {
    "name": "a mysterious note",
    "type": "note",
    "content": "Look closely where warmth brought comfort and stories came to life."
}

Present = {
  "name": "Present"
}


all_rooms = [WW1_1914, Apollo11_1969, Future_2150, Stone_age, Cave]

all_doors = [time_machine_a, time_machine_b, time_machine_c, time_machine_d, time_machine_e]

all_notes = [note_1, note_2, note_3, note_4]

# define which items/rooms are related

object_relations = {
    "World War 1 - 1914": [airforce, soldier, time_machine_a],
    "airforce": [note_1],
    "helmet": [note_2],
    "space shuttle": [note_3],
    "pile of stones": [note_4],
    "soldier": [key_time_machine_a],
    "Present": [time_machine_e],
    "time machine a": [WW1_1914, Apollo11_1969],
    "Apollo 11 - 1969": [astronaut, helmet, time_machine_a, time_machine_b],
    "astronaut": [key_time_machine_b],
    "time machine b": [Apollo11_1969, Future_2150],
    "Future - 2150":[saturn, space_shuttle, time_machine_b, time_machine_c],
    "saturn": [key_time_machine_c],
    "fire pit": [key_time_machine_d],
    "Stone Age": [pile_of_stones, time_machine_c, time_machine_d, fire_pit],
    "time machine c": [Future_2150, Stone_age],
    "time machine d": [Stone_age, Cave],
    "time machine e": [Cave, Present],
    "Cave": [hand_axe, time_machine_d,time_machine_e, spears_and_arrows, bear],
    "hand axe": [key_time_machine_e]
}

# define game state. Do not directly change this dict.
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This
# way you can replay the game multiple times.


INIT_GAME_STATE = {
    "current_room": WW1_1914,
    "keys_collected": [],
    "target_room": Present,
}

# %%
def linebreak():
    """
    Print a line break
    """
    print("\n\n")


def background_song(first_song):
    """
    Plays the chosen song in the background
    """
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(first_song)
    pygame.mixer.music.play(0)

    def play_background_song():
        """
        Allows the backgroud song to play while the game continues.
        """
        song_thread = threading.Thread(target = first_song)
        song_thread.start()


def custom_print(text):
    """
    Prints the desired text into the selected color
    """
    print(Fore.RED + text)


def start_game():
    """
    Start the game
    """
    styled_text = pyfiglet.figlet_format("Lost in Time", font='dos_rebel',width = 200)
    custom_print(styled_text)

    global user_name
    user_name = input("Player's name:").capitalize()

    first_song = r"C:\Users\biave\Documents\IronHack\Quests\1stProject\initialsong.mp3"
    background_song(first_song)
          
    custom_print(f"{user_name}, you're waking up with a strange feeling, in a new dimension which you have never been to before.")
    time.sleep(4)
    custom_print("You don't remember why you are here and what had happened before.")
    time.sleep(4)
    custom_print("You feel some unknown danger approaching. You must find your way back to the present, NOW!")
    time.sleep(4)
    play_room(game_state["current_room"])

def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either
    explore (list all items in this room) or examine an item found here.
    """
    game_state["current_room"] = room

    if (game_state["current_room"] == game_state["target_room"]):
        first_song = r"C:\Users\biave\Documents\IronHack\Quests\1stProject\initialsong.mp3"
        background_song(first_song)
        time.sleep(3)
        custom_print("As you step through the portal, you look around and start preparing your return to the present.")
        time.sleep(4)
        custom_print("Congrats, you made it into the real world!")
        time.sleep(4)
        styled_text = pyfiglet.figlet_format(f"Welcome Back to the Present, {user_name}", font='dos_rebel',width = 300)
        custom_print(styled_text)
    else:
        custom_print(f"{user_name}, you are now in " + room["name"])

        intended_action = input("What would you like to do? Type 'explore' or 'examine'? ").strip().lower()

        if intended_action == "explore":
            explore_room(room)
            play_room(room)
        elif intended_action == "examine":
            examine_item(input("What would you like to examine? ").strip().lower())
        else:
            custom_print("Not sure what you mean. Type 'explore' or 'examine'.")
            play_room(room)
        linebreak()

def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    items = [i["name"] for i in object_relations[room["name"]]]
    custom_print("You just finished exploring this new dimension. \nYou found " + ", ".join(items) + ".")

def get_next_room_of_door(door, current_room):
    """
    From object_relations, find the two rooms connected to the given door.
    Return the room that is not the current_room.
    """
    connected_rooms = object_relations[door["name"]]
    for room in connected_rooms:
        if (not current_room == room):
          return room

def examine_item(item_name):
    """
    Examine an item which can be a door or room element.
    First make sure the intended item belongs to the current room.
    Then check if the item is a door. Tell player if key hasn't been
    collected yet. Otherwise ask player if they want to go to the next
    room. If the item is not a door, then check if it contains keys.
    Collect the key if found and update the game state. At the end,
    play either the current or the next room depending on the game state
    to keep playing.
    """
    current_room = game_state["current_room"]
    next_room = ""
    output = []

    for item in object_relations[current_room["name"]]:
        if (item["name"] == item_name):
            output = "You examine " + item_name + ". "
            if (item["type"] == "door"):
                have_key = False
                for key in game_state["keys_collected"]:
                    if key.get("target") == item:
                        have_key = True
                if (have_key):
                    output += "You unlock it with the key you have."
                    next_room = get_next_room_of_door(item, current_room)
                else:
                    output += "It is locked but you don't have the key."
            else:
                if (item["name"] in object_relations and len(object_relations[item["name"]]) > 0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    output += "You find " + item_found["name"] + "."
                    """
                    Adding the note to let it read out a note's content right away
                    """
                    if item_found["type"] == "note":
                        second_song = r"C:\Users\biave\Documents\IronHack\Quests\1stProject\papercrackle.mp3"
                        background_song(second_song)
                        time.sleep(1)
                        output += " The note reads: \n" + item_found["content"]
                else:
                   output += "You examine it closely but it holds no secrets."
            custom_print(output)
            break

    if (output is None):
        custom_print("The item you requested is not found in the current dimension.")

    if next_room:
        user_input = input("Would you like to go to the next dimension? Enter 'yes' or 'no': ").strip().lower()
        third_song = r"C:\Users\biave\Documents\IronHack\Quests\1stProject\portalsound.mp3"
        fourth_song = r"C:\Users\biave\Documents\IronHack\Quests\1stProject\tryagain.mp3"
        
        if user_input == 'yes':
            background_song(third_song)
            play_room(next_room)
        elif user_input == 'no':
            background_song(fourth_song)
            custom_print("Remember: there might be something better waiting for you out there!")
            time.sleep(3)
            custom_print("Let's try again!")
            time.sleep(2)
            play_room(current_room)
    else:
      play_room(current_room)

# %%
game_state = INIT_GAME_STATE.copy()

start_game()


