import pygame


class Ship:
    """A class to manage the players's ship."""

    def __init__(self, ai_game) -> None:
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load image of the ship and get its border rect.
        self.image = pygame.transform.scale(
            pygame.image.load("images/ship.png"), (50, 70)
        )
        pygame.transform.scale(self.image, (30, 50))
        self.rect = self.image.get_rect()

        # Place ship in the middle on the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current position."""
        self.screen.blit(self.image, self.rect)
