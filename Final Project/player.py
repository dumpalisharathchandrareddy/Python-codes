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
        """Allows the player to place all their ships."""
        ship_specs = [
            ('Destroyer', 3, 2),
            ('Cruiser', 5, 1),
            ('Battleship', 7, 1),
            ('Aircraft Carrier', 9, 1)
        ]

        print(f"\n{self.name}, it's time to place your ships.")
        for name, size, count in ship_specs:
            for _ in range(count):
                ship = Ship(name, size)
                while True:
                    try:
                        print(f"\nPlacing {name} (Size {size})")
                        print("Enter orientation ('H' for horizontal or 'V' for vertical).")
                        orientation = input("Orientation (H/V): ").strip().upper()
                        if orientation not in ['H', 'V']:
                            print("Invalid orientation. Please enter 'H' or 'V'.")
                            continue

                        print("Enter the middle coordinate (e.g., 'A,5').")
                        coord_input = input("Enter middle coordinate: ").strip().upper()
                        if ',' not in coord_input:
                            print("Invalid format. Please use 'Row,Column' like 'A,5'.")
                            continue

                        row_part, col_part = coord_input.split(',', 1)
                        if len(row_part) != 1 or not col_part.isdigit():
                            print("Invalid input. Please enter a valid row letter and column number.")
                            continue

                        row = ord(row_part) - 65
                        col = int(col_part) - 1  # Adjust for zero-based index

                        if row < 0 or row >= self.board.rows or col < 0 or col >= self.board.cols:
                            print(f"Coordinate out of bounds. Rows: A-{chr(self.board.rows + 64)}, Columns: 1-{self.board.cols}.")
                            continue

                        # Generate placement hint
                        hint_coords = self.board.get_hint_coords(size, (row, col), orientation)
                        if hint_coords is None:
                            print("Ship does not fit on the board at this position or overlaps with another ship.")
                            continue
                        hint_str = ', '.join([f"{chr(r + 65)},{c + 1}" for r, c in hint_coords])
                        print(f"The {name} will occupy: {hint_str}")

                        confirm = input("Do you want to place the ship here? (yes/no): ").strip().lower()
                        if confirm != 'yes':
                            continue

                        if self.board.place_ship(ship, (row, col), orientation):
                            # Display the board after placing each ship
                            print("\nYour board after placing the ship:")
                            self.board.display(show_ships=True)
                            break
                    except Exception as e:
                        print(f"An error occurred: {e}. Please try again.")

        # Confirm ship placements
        while True:
            print("\nYour final ship placements:")
            self.board.display(show_ships=True)
            confirm = input("Confirm ship placements? (yes/no): ").strip().lower()
            if confirm == 'yes':
                break
            elif confirm == 'no':
                self.board = Board()
                print("Let's start over with ship placements.")
                self.place_ships()
                return
            else:
                print("Please enter 'yes' or 'no'.")

    def take_turn(self, opponent):
        """Allows the player to take a turn."""
        print(f"\n{self.name} Turn")
        print("\nGuess Board:")
        self.display_guess_board()
        while True:
            guess = input("Enter your guess as row,column (e.g., A,1): ").strip().upper()
            if ',' not in guess:
                print("Invalid format. Please enter as 'Row,Column' (e.g., A,1).")
                continue
            row_part, col_part = guess.split(',', 1)
            if len(row_part) != 1 or not col_part.isdigit():
                print("Invalid input. Please enter a valid row letter and column number.")
                continue
            row = ord(row_part) - 65
            col = int(col_part) - 1  # Adjusting for zero-based index
            if row < 0 or row >= self.board.rows or col < 0 or col >= self.board.cols:
                print("Guess out of bounds. Please try again.")
                continue
            result = opponent.board.receive_attack((row, col))
            if result:
                self.guesses += 1
                if result == "HIT":
                    print("HIT!")
                    self.opponent_view[row][col] = 'X'
                elif result == "MISS":
                    print("MISS!")
                    self.opponent_view[row][col] = '0'
                elif result == "SHIP SUNK":
                    print("SHIP SUNK!")
                    self.opponent_view[row][col] = 'X'
                break
            else:
                print("You have already guessed that coordinate. Try again.")

    def display_guess_board(self):
        """Displays the player's guess board with hits and misses."""
        header = "     " + " ".join(str(c + 1) for c in range(self.board.cols))
        print(header)
        for r in range(self.board.rows):
            row_label = chr(r + 65) + "."
            row_cells = []
            for c in range(self.board.cols):
                cell = self.opponent_view[r][c]
                if cell == 'X':
                    row_cells.append('X')
                elif cell == '0':
                    row_cells.append('0')
                else:
                    row_cells.append('~')
            print(f"{row_label:<4}" + " ".join(row_cells))

    def has_lost(self):
        """Checks if all ships have been sunk."""
        return all(ship.is_sunk for ship in self.board.ships)
