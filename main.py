# main.py

from game_data import scene_office
from game_functions import (check_for_events, display_scene, get_player_input,
                            update_game_state)
from game_mechanics import SyncProfile  # Import the scene_office variable


def game_loop():
    """Main game loop that drives the game flow."""
    current_scene = scene_office  # Now scene_office is accessible
    anya = SyncProfile()
    first_time_in_scene = True  # Flag to track first time in a scene

    try:
        while True:
            display_scene(current_scene,
                          first_time_in_scene)  # Pass the flag to display_scene
            choice = get_player_input()
            update_game_state(choice, current_scene, anya)
            check_for_events(current_scene, anya)

            # Transition to the next scene (after update_game_state)
            if "next_scene" in current_scene:  # Check for next_scene after updating
                current_scene = globals()[current_scene["next_scene"]]
                first_time_in_scene = True  # Reset the flag for the new scene
            else:
                first_time_in_scene = False  # Set to False if staying in the same scene

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Game over, display SYNC evaluation
        print("\n--- Game Over ---")
        print("\nSYNC Evaluation:")
        print(f"  - Strength: {anya.strength}")
        print(f"  - Intelligence: {anya.intelligence}")
        print(f"  - Negotiation: {anya.negotiation}")
        print(f"  - Charisma: {anya.charisma}")
        print(f"\nYour dominant attribute: {anya.get_dominant_attribute()}")
        # Add more detailed evaluation and personalized feedback based on SYNC profile


if __name__ == "__main__":
    game_loop()