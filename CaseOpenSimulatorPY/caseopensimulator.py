import random
items = {
    "P2000 Handgun - 0.5$": 60,
    "P-250 Steel Disruption - 1.49$": 16.5,
    "Five-SeveN Case Hardened - 6.48$": 7.5,
    "Glock-18 Steel Disruption - 2.11$": 10,
    "Shadow Daggers Case Hardened - 165$": 0.928,
    "AK-47 Case Hardened - 326$": 0.5,
    "Hydra Gloves Case Hardened - 84$": 0.5
}
def open_case():
    random_number = random.randint(1, 100)
    cumulative_percentage = 0
    for item, percentage in items.items():
        cumulative_percentage += percentage
        if random_number <= cumulative_percentage:
            print("You received:", item)
            return
# Main loop
while True:
    user_input = input("Do you want to open a case? (y/n)")
    if user_input.lower() == "y":
        open_case()
    elif user_input.lower() == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")