class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an active state.
        self.game_active = False
        try:
            with open("All_Time_High_Score.txt") as f:
                self.high_score = int(f.read())
        except FileNotFoundError:
            print(f"Sorry, the file {filename} does not exist.")
        # self.high_score = 0

    def reset_stats(self):
        """Initializze statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1