# inventory.py

def display_inventory(anya):
    """Displays Anya's current inventory."""
    print("\n--- Inventory ---")
    if anya.clues:
        for item in anya.clues:
            print(f"- {item}")
    else:
        print("Your inventory is empty.")