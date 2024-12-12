# board.py

from ship import Ship

class Board:
    """Represents a player's game board."""

    def __init__(self):
        self.rows = 26                  # Number of rows (A-Z)
        self.cols = 10                  # Number of columns (0-9)
        self.grid = [['~' for _ in range(self.cols)] for _ in range(self.rows)]
        self.ships = []                 # List of ships on the board

    def display(self, show_ships=False):
        """Displays the board. Shows ships if show_ships is True."""
        print("   " + " ".join(str(i) for i in range(self.cols)))
        for r in range(self.rows):
            row_label = chr(r + 65)
            row_display = []
            for c in range(self.cols):
                cell = self.grid[r][c]
                if cell == 'S' and not show_ships:
                    row_display.append('~')
                else:
                    row_display.append(cell)
            print(f"{row_label}  " + " ".join(row_display))

    def is_valid_placement(self, ship_size, middle_coord, orientation):
        """Checks if a ship can be placed at the given position and orientation."""
        row, col = middle_coord
        coords = []
        half_size = ship_size // 2

        if orientation == 'horizontal':
            start_col = col - half_size
            end_col = col + half_size
            if start_col < 0 or end_col >= self.cols:
                return False
            for c in range(start_col, end_col + 1):
                if self.grid[row][c] != '~':
                    return False
                coords.append((row, c))
        elif orientation == 'vertical':
            start_row = row - half_size
            end_row = row + half_size
            if start_row < 0 or end_row >= self.rows:
                return False
            for r in range(start_row, end_row + 1):
                if self.grid[r][col] != '~':
                    return False
                coords.append((r, col))
        else:
            return False

        return coords

    def place_ship(self, ship, middle_coord, orientation):
        """Places a ship on the board."""
        coords = self.is_valid_placement(ship.size, middle_coord, orientation)
        if coords:
            for coord in coords:
                r, c = coord
                self.grid[r][c] = 'S'
            ship.place(coords)
            self.ships.append(ship)
            return True
        else:
            print("Invalid placement. Please try again.")
            return False

    def receive_attack(self, coord):
        """Processes an attack and returns the result."""
        row, col = coord
        cell = self.grid[row][col]
        if cell == 'S':
            self.grid[row][col] = 'X'
            for ship in self.ships:
                if coord in ship.coordinates:
                    ship.take_hit()
                    if ship.is_sunk:
                        return "SHIP SUNK"
                    else:
                        return "HIT"
            return "HIT"
        elif cell == '~':
            self.grid[row][col] = 'O'
            return "MISS"
        else:
            print("Already guessed this coordinate.")
            return None
