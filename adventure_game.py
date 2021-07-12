import time  # using time module to slow down message output.
import random  # random module will be used to randomize fighters and outcomes

fighters = ["Ryu", "Goku", "Zuko", "Korra", "Toph"]


def print_pause(message):  # function for message outputs
    print(message)
    time.sleep(2)


def intro(fighter):  # intro messages
    print_pause("It has been a long time since you left your village.")
    print_pause("You've undertaken this pilgramage to discover yourself")
    print_pause("To find fighters who have strong technique and spirit.")
    print_pause(f"Rumor has it that there is a strong fighter in this town.")
    print_pause(f"Tales of {fighter}'s ability have spread across the land.")
    print_pause("Once you reached the town, a crowd was gathered around.")
    print_pause("They surrounded a wide platform.")
    print_pause(f"{fighter} stood at the center, calling for a new challenge.")
    print_pause("You also notice that down the street is an old woman.")
    print_pause("She matches the description of a legendary fighter.")
    print_pause("She's sitting alone and unbothered.")
    print_pause("While you think you are ready to fight,")
    print_pause("there is no guarantee of victory at this moment in time.")


def first_decision():
    print_pause("Enter 1 to walk over to the platform.")
    print_pause("Enter 2 to walk down the street.")
    print_pause("What would you like to do?")
    print_pause("(Please enter 1 or 2.)")


def choose_platform(fighter, ability):
    print_pause("You approach the platform.")
    print_pause(f"{fighter} spots you and challenges you to a match.")
    print_pause(f"You step up onto the platform.")
    print_pause(f"{fighter} moves with great speed to strike you!")
    fight_flight(fighter, ability)


def choose_street(fighter, ability):
    if "Spirit" not in ability:
        print_pause("You awkwardly approach the older woman.")
        print_pause("She's sitting on the ground, staring at nothing.")
        print_pause(f"She makes a comment that you would lose this fight.")
        print_pause("'You may still lose, but I can give you a chance,'")
        print_pause("She said.")
        print_pause("She places two fingers on your right temple.")
        print_pause("It was a feeling of tidal waves raging inside you.")
        print_pause("As if she gave you knowledge and power for a lifetime.")
        print_pause("'This is a lot to process but give it some time'")
        print_pause("You walk back towards the crowd.")
        ability.append("Spirit")
        first_decision()
        location_choice(fighter, ability)
    elif "Spirit" in ability:
        print_pause("'I\'ve done everything I can kid, it\'s up to fate now.'")
        print_pause("You walk back towards the crowd.")
        first_decision()
        location_choice(fighter, ability)


def location_choice(fighter, ability):
    response = input("")
    if response == str(1):
        choose_platform(fighter, ability)
    elif response == str(2):
        choose_street(fighter, ability)
    else:
        print_pause("Sorry that choice doesn't exist.")
        first_decision()
        location_choice(fighter, ability)


def fight_flight(fighter, ability):
    if "Spirit" not in ability:
        print_pause(f"You lost sight of {fighter}. You're in trouble!")
        print_pause("Would you like to (1) fight or (2) run away")
        response = input("")
        if response == str(1):
            defeat_KO(fighter)
        elif response == str(2):
            print_pause("You throw your hands up and yell 'WAIT!'")
            print_pause("You say you need to go to the bathroom and leave.")
            first_decision()
            location_choice(fighter, ability)
        else:
            print_pause("Sorry, that choice isn't valid.")
            fight_flight(fighter, ability)
    elif "Spirit" in ability:
        print_pause("Would you like to (1) fight or (2) run away")
        response = input("")
        if response == str(1):
            victory(fighter)
        elif response == str(2):
            print_pause("You throw your hands up and yell 'WAIT!'")
            print_pause("You say you need to go to the bathroom and leave.")
            first_decision()
            location_choice(fighter, ability)
        else:
            print_pause("Sorry, that choice isn't valid.")
            fight_flight(fighter, ability)


def play_again():
    print_pause("Would you like to play again?")
    print_pause("Please enter y/n")
    response = input("").lower()
    if response == "y":
        adventure()
    elif response == "n":
        print_pause("Thanks for playing! See you next time.")
    else:
        print_pause("Sorry, that was not a valid input.")
        play_again()


def defeat_KO(fighter):
    print_pause("All you could see was a fist flying towards you.")
    print_pause(f"It stops before your eyes and {fighter} says,")
    print_pause(f"'You\'re outmatched. Go home before you get hurt.'")
    print_pause("Defeat has never felt this bitter.")
    play_again()


def defeat_effort(fighter):  # Wanted to create a lose scenario from chance.
    print_pause("You react in time to dodge the first punch.")
    print_pause("Your spirit feels invigorated with power.")
    print_pause(f"{fighter} looks shocked, but continues to press on.")
    print_pause("The crowd's cheering is intense.")
    print_pause("They began to slam their hands on the platform.")
    print_pause("One of the platform tiles pops out.")
    print_pause(f"You were so focused on {fighter}, you trip on the tile.")
    print_pause(f"You fall flat on your back, with {fighter} looming over.")
    print_pause(f"'You almost had me there, but it's my win this time.'")
    print_pause("You did your best. But it wasn't enough. You lose.")
    play_again()


def victory(fighter):  # Random is used to determine victory.
    print_pause(f"{fighter} moves to strike.")
    if random.randint(1, 5) in range(3, 6):  # Add element of luck to game
        print_pause("You react in time to dodge the first punch.")
        print_pause(f"Your spirit feels invigorated with power")
        print_pause(f"{fighter} looks shocked at your skill")
        print_pause("You move with impressive agility, and dexterity.")
        print_pause(f"{fighter} trips due to a tile sticking out the ground.")
        print_pause(f"You sweep {fighter}'s legs and bring down your fist.")
        print_pause(f"You float your knuckles just before their eyes.")
        print_pause(f"'You win.' {fighter} says.")
        print_pause("You are victorious!")
        play_again()
    else:
        defeat_effort(fighter)


def adventure():
    ability = []
    fighter = random.choice(fighters)
    intro(fighter)
    first_decision()
    location_choice(fighter, ability)


adventure()
