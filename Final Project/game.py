# game.py

from player import Player
import os

class Game:
    """Manages the overall game flow."""

    def __init__(self):
        print("Welcome to Battleship!")
        self.player1 = Player(input("Player 1, enter your name: "))
        self.player2 = Player(input("Player 2, enter your name: "))
        self.current_turn = self.player1
        self.high_score = self.load_high_score()

    def load_high_score(self):
        """Loads the high score from the 'game_history.txt' file."""
        try:
            with open('game_history.txt', 'r') as file:
                scores = [int(line.strip().split(',')[1]) for line in file if ',' in line]
                if scores:
                    high_score = min(scores)
                    print(f"\nCurrent high score: {high_score} guesses.")
                    return high_score
        except FileNotFoundError:
            pass
        return None

    def save_game_statistics(self, winner, guesses):
        """Saves the game statistics to 'game_history.txt'."""
        with open('game_history.txt', 'a') as file:
            file.write(f"{winner},{guesses}\n")
        print("\nGame statistics have been saved.")

    def play(self):
        """Starts and manages the game."""
        # Display existing high score
        if self.high_score:
            print(f"\nThe current high score is {self.high_score} guesses.")
        else:
            print("\nThere is currently no high score.")

        # Players place their ships
        input(f"\n{self.player1.name}, press Enter to place your ships.")
        os.system('cls' if os.name == 'nt' else 'clear')
        self.player1.place_ships()
        input("\nPress Enter and pass to the next player.")
        os.system('cls' if os.name == 'nt' else 'clear')
        input(f"\n{self.player2.name}, press Enter to place your ships.")
        self.player2.place_ships()
        input("\nPress Enter to start the game.")
        os.system('cls' if os.name == 'nt' else 'clear')

        # Game loop
        while True:
            opponent = self.player2 if self.current_turn == self.player1 else self.player1
            self.current_turn.take_turn(opponent)
            if opponent.has_lost():
                print(f"\n{self.current_turn.name} wins the game!")
                total_guesses = self.current_turn.guesses
                self.save_game_statistics(self.current_turn.name, total_guesses)
                if self.high_score is None or total_guesses < self.high_score:
                    print(f"New high score set: {total_guesses} guesses!")
                break
            # Switch turns
            input("\nPress Enter to pass to the next player.")
            os.system('cls' if os.name == 'nt' else 'clear')
            self.current_turn = opponent

        # Display final boards
        print("\nFinal boards:")
        print(f"\n{self.player1.name}'s Board:")
        self.player1.board.display(show_ships=True)
        print(f"\n{self.player2.name}'s Board:")
        self.player2.board.display(show_ships=True)
