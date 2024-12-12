# ship.py

class Ship:
    """Represents a ship in the Battleship game."""

    def __init__(self, name, size):
        self.name = name                # Ship's name (e.g., Destroyer)
        self.size = size                # Number of grid spaces the ship occupies
        self.hits = 0                   # Number of hits taken
        self.coordinates = []           # Coordinates the ship occupies
        self.is_sunk = False            # Status of the ship (sunk or not)

    def take_hit(self):
        """Registers a hit and updates the ship's status."""
        self.hits += 1
        if self.hits >= self.size:
            self.is_sunk = True
            print(f"SHIP SUNK! You sunk the {self.name}!")

    def place(self, coordinates):
        """Assigns coordinates to the ship."""
        self.coordinates = coordinates
