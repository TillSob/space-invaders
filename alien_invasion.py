import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self) -> None:
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")
        # Create a instance of the class Ship and pass the current instance of
        # the game
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Listens for KBM Inputs.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Update the screen's on each cycle of the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Makes the last drawn screen visible (update screen).
            pygame.display.flip()


if __name__ == "__main__":
    # Creates instance of AlienInvasion and run the game.
    ai = AlienInvasion()
    ai.run_game()
