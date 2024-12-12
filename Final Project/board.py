# board.py

from ship import Ship

class Board:
    """Represents the game board for a player."""

    def __init__(self):
        self.rows = 26  # Number of rows (A-Z)
        self.cols = 9   # Number of columns (1-9)
        self.grid = [['~' for _ in range(self.cols)] for _ in range(self.rows)]
        self.ships = []  # List of ships placed on the board

    def display(self, show_ships=False):
        """Displays the board with hits and misses."""
        header = "     " + " ".join(str(c + 1) for c in range(self.cols))
        print(header)
        for r in range(self.rows):
            row_label = chr(r + 65) + "."
            row_cells = []
            for c in range(self.cols):
                cell = self.grid[r][c]
                if cell == 'S':
                    if show_ships:
                        row_cells.append('S')
                    else:
                        row_cells.append('~')
                elif cell == 'X':
                    row_cells.append('X')
                elif cell == 'O':
                    row_cells.append('0')
                else:
                    row_cells.append('~')
            print(f"{row_label:<4}" + " ".join(row_cells))

    def is_valid_placement(self, ship_size, middle_coord, orientation):
        """
        Checks if a ship can be placed at the given position and orientation.

        Returns:
            tuple(bool, str, list): (is_valid, error_message, coords)
        """
        row, col = middle_coord
        coords = []
        half_size = ship_size // 2

        orientation = orientation.upper()
        if orientation not in ['H', 'V']:
            return False, "Invalid orientation. Enter 'H' for horizontal or 'V' for vertical.", coords

        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return False, "Starting coordinate is out of bounds.", coords

        if orientation == 'H':
            start_col = col - half_size
            end_col = col + half_size

            if start_col < 0 or end_col >= self.cols:
                return False, "Ship does not fit horizontally on the board at this position.", coords

            for c in range(start_col, end_col + 1):
                if self.grid[row][c] != '~':
                    return False, "Ship overlaps with another ship.", coords
                coords.append((row, c))
        elif orientation == 'V':
            start_row = row - half_size
            end_row = row + half_size

            if start_row < 0 or end_row >= self.rows:
                return False, "Ship does not fit vertically on the board at this position.", coords

            for r in range(start_row, end_row + 1):
                if self.grid[r][col] != '~':
                    return False, "Ship overlaps with another ship.", coords
                coords.append((r, col))

        return True, "", coords

    def place_ship(self, ship, middle_coord, orientation):
        """Places a ship on the board."""
        is_valid, error_message, coords = self.is_valid_placement(
            ship.size, middle_coord, orientation)
        if is_valid:
            for coord in coords:
                r, c = coord
                self.grid[r][c] = 'S'
            ship.place(coords)
            self.ships.append(ship)
            return True
        else:
            print(error_message)
            return False

    def receive_attack(self, coord):
        """Processes an attack and returns the result."""
        row, col = coord
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            print("Attack coordinate is out of bounds.")
            return None
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
        elif cell in ['X', 'O']:
            print("Already attacked this coordinate.")
            return None

    def get_hint_coords(self, ship_size, middle_coord, orientation):
        """Generates coordinates that the ship will occupy for hint purposes."""
        is_valid, error_message, coords = self.is_valid_placement(
            ship_size, middle_coord, orientation)
        if is_valid:
            return coords
        else:
            return None
