# game_functions.py

from inventory import display_inventory  # Import the display_inventory function
import time
import random


def typewrite_text(text):
    """Prints text with a typewriter effect."""
    for char in text:
        print(char, end='', flush=True)  # Print each character with the effect
        time.sleep(random.uniform(0.01, 0.05))  # Random typing speed
    print()  # Print a newline after the text


def display_scene(scene, first_time=True):  # Add first_time parameter
    """Displays the scene description and interactive elements."""

    if first_time:  # Only print the description if first_time is True
        try:
            typewrite_text(scene["description"])  # Use the typewriter effect
        except KeyError:
            print("Error: Missing scene description.")
            return

    if "interactive_elements" in scene:
        typewrite_text("\nYou see:")  # Use the typewriter effect
        for element in scene["interactive_elements"]:
            typewrite_text(f"- {element['name']}")  # Use the typewriter effect


def get_player_input():
    """Gets player input and validates it."""
    choice = input("\nWhat do you do? ")
    return choice.lower()  # Convert input to lowercase for easier comparison


def update_game_state(choice, scene, anya):
    """Updates the game state based on player choice."""

    found_match = False  # Flag to track if any event or exit was triggered

    # Check events first
    for event in scene.get("events", []):
        if choice == event["trigger"]:  # Use exact match for event triggers
            try:
                action = event["action"]  # Get the action string

                # Check if the action string contains 'display_inventory'
                if "display_inventory" in action:
                    display_inventory(anya)  # Call the function directly
                elif "ascii_art" in action:  # Check if the action involves ASCII art
                    exec(
                        action
                    )  # Execute the action to print the ASCII art  # This is the fix
                else:
                    exec(action)  # Execute other actions normally

                # Highlight the clue and add to inventory (if applicable)
                if "anya.clues.append" in event["action"]:
                    clue_name = event["action"].split("'")[1]  # Extract clue name
                    typewrite_text(f"\n**You found a clue: {clue_name}!**\n")  # Highlight
                    anya.add_to_inventory(clue_name)  # Add to inventory

            except Exception as e:
                print(f"Error executing event action: {e}")
            found_match = True  # Mark that an event was triggered
            break  # Exit the loop after executing the event

    # Check for interactions with interactive elements (only if no event was triggered)
    if not found_match and "interactive_elements" in scene:
        for element in scene["interactive_elements"]:
            # More robust matching for interactive elements
            element_name = element["name"].lower()
            if choice == element_name:  # Use exact match for element names
                if "description" in element:
                    typewrite_text(element["description"])  # Display the description

                if "actions" in element:
                    typewrite_text("You can:")
                    for action in element["actions"]:
                        typewrite_text(f"- {action}")

                found_match = True
                break  # Stop checking after finding a match

    # Check exits
    for exit in scene["exits"]:
        if choice in exit["direction"]:
            if all(clue in anya.clues
                   for clue in scene.get("required_clues", [])):
                scene["next_scene"] = exit["destination"]
                typewrite_text(
                    f"You're heading {exit['direction']}...")  # Print statement
            else:
                typewrite_text(
                    "You feel like you're missing something important. "
                    "Maybe you should investigate further.")
                # Provide hints
                missing_clues = set(scene["required_clues"]) - set(anya.clues)
                if "cigarette butt" in missing_clues:
                    typewrite_text(
                        "- Perhaps a closer look at your desk would be helpful."
                    )
                if "enchanted bullets" in missing_clues:
                    typewrite_text(
                        "- You might want to check if you have any useful tools hidden somewhere."
                    )
            found_match = True  # Mark that an exit was triggered
            break  # Exit the loop after finding a matching exit

    # If no event or exit is triggered, provide hints
    if not found_match:
        typewrite_text(
            "Hmm, that doesn't seem to work here.  Maybe try:")  # More helpful message

        # Hint at interactive elements
        if "interactive_elements" in scene:
            for element in scene["interactive_elements"]:
                typewrite_text(f"- Interacting with the {element['name']}")

        # Hint at exits
        if "exits" in scene:
            for exit in scene["exits"]:
                typewrite_text(f"- Going {exit['direction']}")

        # Additional hints based on game state or progress could be added here


def check_for_events(scene, anya):
    """Checks for and handles events based on game state."""
    # Placeholder for more complex event handling
    pass