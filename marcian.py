import random

locations = [random.randint(0, 7) for _ in range(3)]
weights = [200,300,213]
total_weight = sum(weights)

while True:
    guesses = [int(input(f"Enter guess for box {i+1} (km): ")) for i in range(3)]
    if guesses == locations:
        print("Congrats, you found everything")
        print(f"Locations: {locations}")
        print("Total weight of packages is ",total_weight)
        break
    elif guesses != locations:
        locations = [random.randint(0, 7) for _ in range(3)]
        print("Error you typed something wrong, all packages are shafled, try again")
