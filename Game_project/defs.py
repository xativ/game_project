def start_new_game():
    print("Starting a new game...")
    # Add logic to initialize a new game here
    health = 100
    inventory = []

    return health, inventory
def check_health(health):
    if health <= 0:
        print("You have died. Game over.")
        return False
    return True

def check_inventory(inventory):
    if not inventory:
        print("Your inventory is empty.")
    else:
        print("Your inventory contains:")
        for item in inventory:
            print(f"- {item}")