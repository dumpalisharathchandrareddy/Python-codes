# player.py

from board import Board
from ship import Ship

class Player:
    """Represents a player in the game."""

    def __init__(self, name):
        self.name = name
        self.board = Board()
        self.guesses = 0
        self.opponent_view = [['~' for _ in range(self.board.cols)] for _ in range(self.board.rows)]

    def place_ships(self):
        """Allows the player to place their ships."""
        ship_specs = [
            ('Destroyer', 3, 2),
            ('Cruiser', 5, 1),
            ('Battleship', 7, 1),
            ('Aircraft Carrier', 9, 1)
        ]

        print(f"\n{self.name}, place your ships.")
        for name, size, count in ship_specs:
            for _ in range(count):
                ship = Ship(name, size)
                while True:
                    try:
                        print(f"\nPlacing {name} (Size {size})")
                        orientation = input("Orientation (horizontal/vertical): ").strip().lower()
                        coord_input = input("Enter middle coordinate (e.g., A5): ").strip().upper()
                        row = ord(coord_input[0]) - 65
                        col = int(coord_input[1:])
                        if self.board.place_ship(ship, (row, col), orientation):
                            break
                    except (IndexError, ValueError):
                        print("Invalid input. Please try again.")

        # Confirm ship placement
        while True:
            print("\nYour ship placements:")
            self.board.display(show_ships=True)
            confirm = input("Confirm ship placements? (yes/no): ").strip().lower()
            if confirm == 'yes':
                break
            elif confirm == 'no':
                self.board = Board()
                self.place_ships()
                break
            else:
                print("Please enter 'yes' or 'no'.")

    def take_turn(self, opponent):
        """Allows the player to take a turn."""
        print(f"\n{self.name}'s Turn")
        print("\nYour guess board:")
        self.display_guess_board()
        while True:
            try:
                guess = input("Enter attack coordinate (e.g., B7): ").strip().upper()
                row = ord(guess[0]) - 65
                col = int(guess[1:])
                result = opponent.board.receive_attack((row, col))
                if result:
                    self.guesses += 1
                    if result == "HIT":
                        print("HIT!")
                        self.opponent_view[row][col] = 'X'
                    elif result == "MISS":
                        print("MISS!")
                        self.opponent_view[row][col] = 'O'
                    elif result == "SHIP SUNK":
                        print("SHIP SUNK!")
                        self.opponent_view[row][col] = 'X'
                    break
            except (IndexError, ValueError):
                print("Invalid input. Please try again.")

    def has_lost(self):
        """Checks if all ships have been sunk."""
        return all(ship.is_sunk for ship in self.board.ships)

    def display_guess_board(self):
        """Displays the player's guess board."""
        print("   " + " ".join(str(i) for i in range(self.board.cols)))
        for r in range(self.board.rows):
            row_label = chr(r + 65)
            row_display = self.opponent_view[r]
            print(f"{row_label}  " + " ".join(row_display))
