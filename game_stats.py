class GameStats:
    """Track stats of the game."""

    def __init__(self, ai_game):
        """initialise"""
        self.settings = ai_game.settings
        self.reset_stats()
        # Start Alien Invasion in an active state.
        self.game_active = True
    
    def reset_stats(self):
        """Initalise stats that can change during the game"""
        self.ships_left = self.settings.ship_limit
