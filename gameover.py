import pygame

import constants


class GameOver:
    def __init__(self, score):
        self.font_object = pygame.font.SysFont("Comic Sans MS", 35, False, True)
        self.gameover_text = self.font_object.render("Game over!", 0, (0, 180, 0))
        self.score_text = self.font_object.render(f"Score:{score}", 0, (0, 180, 0))
        self.is_changed = False

    def draw(self, screen):
        screen.fill(constants.BLACK)
        screen.blit(self.gameover_text, (constants.WIDTH // 2, constants.HEIGHT // 3))
        screen.blit(self.score_text, (constants.WIDTH // 2, constants.HEIGHT // 2))

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.is_changed = True

    def logic(self):
        pass
