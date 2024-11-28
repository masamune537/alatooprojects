import random
import os

class BattleshipGame:
    def __init__(self):
        self.size = 7
        self.player_name = ""
        self.field = [[" " for _ in range(self.size)] for _ in range(self.size)]
        self.ships = []
        self.hits = 0
        self.shots = 0
        self.high_scores = []

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def display_field(self, revealed=False):
        print("   " + " ".join(str(i + 1) for i in range(self.size)))
        for i, row in enumerate(self.field):
            print(f"{i + 1:2} " + " ".join(
                self.reveal_cell(i, j, revealed) for j in range(self.size)
            ))

    def reveal_cell(self, x, y, revealed):
        if self.field[x][y] == "X":  # Hit
            return "X"
        elif self.field[x][y] == "M":  # Miss
            return "M"
        elif self.field[x][y] == "S":  # Sunk
            return "S"
        elif revealed and self.field[x][y] == "O":  # Reveal ships after victory
            return "O"
        return "."  # Unrevealed cells

    def place_ships(self):
        ship_sizes = [3, 2, 2, 1, 1, 1, 1]
        for size in ship_sizes:
            while True:
                x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
                direction = random.choice([(0, 1), (1, 0)])  # Horizontal or vertical
                if self.can_place_ship(x, y, size, direction):
                    self.add_ship(x, y, size, direction)
                    break

    def can_place_ship(self, x, y, size, direction):
        dx, dy = direction
        for i in range(size):
            nx, ny = x + i * dx, y + i * dy
            if not (0 <= nx < self.size and 0 <= ny < self.size):
                return False
            if not self.is_cell_empty(nx, ny):
                return False
        return True

    def is_cell_empty(self, x, y):
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.size and 0 <= ny < self.size:
                    if self.field[nx][ny] != " ":
                        return False
        return True

    def add_ship(self, x, y, size, direction):
        ship = []
        dx, dy = direction
        for i in range(size):
            nx, ny = x + i * dx, y + i * dy
            self.field[nx][ny] = "O"
            ship.append((nx, ny))
        self.ships.append(ship)

    def take_turn(self):
        while True:
            try:
                coords = input("Enter your shot (row column): ").split()
                x, y = int(coords[0]) - 1, int(coords[1]) - 1
                if not (0 <= x < self.size and 0 <= y < self.size):
                    raise ValueError("Coordinates out of bounds!")
                if self.field[x][y] in {"X", "M", "S"}:
                    raise ValueError("You already shot there!")
                break
            except ValueError as e:
                print(e)

        self.shots += 1
        if self.field[x][y] == "O":
            self.field[x][y] = "X"
            self.hits += 1
            self.check_sink()
        else:
            self.field[x][y] = "M"

    def check_sink(self):
        for ship in self.ships:
            if all(self.field[x][y] == "X" for x, y in ship):
                for x, y in ship:
                    self.field[x][y] = "S"

    def is_victory(self):
        return all(self.field[x][y] == "S" for ship in self.ships for x, y in ship)

    def play(self):
        self.clear_screen()
        self.player_name = input("Enter your name: ")
        self.field = [[" " for _ in range(self.size)] for _ in range(self.size)]
        self.ships = []
        self.hits = 0
        self.shots = 0

        self.place_ships()
        while not self.is_victory():
            self.clear_screen()
            self.display_field()
            self.take_turn()

        self.clear_screen()
        self.display_field(revealed=True)
        print(f"Congratulations {self.player_name}, you won in {self.shots} shots!")
        self.high_scores.append((self.player_name, self.shots))
        self.high_scores.sort(key=lambda x: x[1])

    def main_menu(self):
        while True:
            self.play()
            again = input("Do you want to play again? (yes/no): ").strip().lower()
            if again != "yes":
                break

        print("\nHigh Scores:")
        for i, (name, shots) in enumerate(self.high_scores, 1):
            print(f"{i}. {name}: {shots} shots")
        print("Thanks for playing!")

if __name__ == "__main__":
    game = BattleshipGame()
    game.main_menu()
