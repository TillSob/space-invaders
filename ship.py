import pygame


class Ship:
    """A class to manage the players's ship."""

    def __init__(self, ai_game) -> None:
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load image of the ship and get its border rect.
        self.image = pygame.transform.scale(
            pygame.image.load("images/ship.png"), (50, 70)
        )
        pygame.transform.scale(self.image, (30, 50))
        self.rect = self.image.get_rect()

        # Place ship in the middle on the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Save a float value for the center of the ship
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""

        # Update the value for the ship's center, instead the rect
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        # Update the rect-object via self.x
        self.rect.x = self.x

    def blitme(self) -> None:
        """Draw the ship at its current position."""
        self.screen.blit(self.image, self.rect)
