class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (20, 20, 50)

        # Ship settings
        self.ship_speed = 0.8

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 6
        self.bullet_height = 30
        self.bullet_color = (200, 30, 30)
        self.bullets_allowed = 4