import sys
import pygame


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self) -> None:
        """Initialize the game, and create game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        # Sets background color.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Listens for KBM Inputs.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Update the screen's background color.
            self.screen.fill(self.bg_color)

            # Makes the last drawn screen visible (update screen).
            pygame.display.flip()


if __name__ == "__main__":
    # Creates instance of AlienInvasion and run the game.
    ai = AlienInvasion()
    ai.run_game()
