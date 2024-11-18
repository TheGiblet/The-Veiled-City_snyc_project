# game_mechanics.py

class SyncProfile:
    def __init__(self):
        self.strength = 5
        self.intelligence = 5
        self.negotiation = 5
        self.charisma = 5
        self.clues = []

    def update_sync(self, attribute, value):
        if attribute == "strength":
            self.strength += value
        elif attribute == "intelligence":
            self.intelligence += value
        elif attribute == "negotiation":
            self.negotiation += value
        elif attribute == "charisma":
            self.charisma += value
        else:
            print(f"Error: Invalid attribute '{attribute}'")

        # Optional: Keep values within a range (e.g., 0-10)
        self.strength = max(0, min(10, self.strength))
        self.intelligence = max(0, min(10, self.intelligence))
        self.negotiation = max(0, min(10, self.negotiation))
        self.charisma = max(0, min(10, self.charisma))

        print(f"SYNC updated: {attribute} changed by {value}")  # Print statement

    def get_dominant_attribute(self):
        dominant = max(self.strength, self.intelligence, self.negotiation,
                        self.charisma)
        if dominant == self.strength:
            return "Strength"
        elif dominant == self.intelligence:
            return "Intelligence"
        elif dominant == self.negotiation:
            return "Negotiation"
        else:
            return "Charisma"

    def add_to_inventory(self, item):  # Add this method
        """Adds an item to Anya's inventory."""
        self.clues.append(item)
        print(f"{item} added to your inventory.")


def combat_encounter():
    # This is a placeholder for the combat system
    print("You are ambushed by a shadowy figure!")
    # ... (Implement your combat logic here) ...
    pass  # Remove this when you implement the combat logic


def start_dialogue(character):
    # This is a placeholder for the dialogue system
    print(f"\n{character['portrait']}")
    print(f"{character['name']}:")
    for line in character['dialogue']['greeting']:
        print(f"  {line}")
    # ... (Implement your dialogue logic here) ...
    pass  # Remove this when you implement the dialogue logic