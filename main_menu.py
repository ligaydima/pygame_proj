import pygame

import constants


class MainMenu:
    def __init__(self, top5):
        self.font_object = pygame.font.SysFont("Comic Sans MS", 35, False, True)
        self.font_main = pygame.font.SysFont("Comic Sans MS", 72, False, True)
        self.text1 = self.font_main.render("Snakee", 0, (0, 180, 0))
        self.text2 = self.font_object.render("Start", 0, (0, 180, 0))
        self.freq_text = self.font_object.render("Current frequency:", 0, (0, 180, 0))
        self.speed_text = self.font_object.render("Current speed:", 0, (0, 180, 0))
        self.freq_display = self.font_object.render("3", 0, (0, 180, 0))
        self.speed_display = self.font_object.render("5", 0, (0, 180, 0))
        self.top5 = []
        for i in range(len(top5)):
            self.top5.append(self.font_object.render(f"{i + 1}. {top5[i][0]}, {top5[i][1]}", 0, (0, 180, 0)))
        for i in range(len(top5), 5):
            self.top5.append(self.font_object.render(f"{i + 1}. -------", 0, (0, 180, 0)))
        self.is_changed = False
        self.settings = dict()
        self.settings["frequency"] = 3
        self.settings["speed"] = 5

    def draw(self, screen):
        screen.fill(constants.WHITE)
        screen.blit(self.text1, (constants.WIDTH // 2 - 100, 100))
        screen.blit(self.text2, (constants.WIDTH // 2 - 100, 300))
        screen.blit(self.freq_text, (constants.WIDTH // 2 - 100 + 90, 300))
        screen.blit(self.speed_text, (constants.WIDTH // 2 - 100 + 90, 380))
        screen.blit(self.freq_display, (constants.WIDTH // 2 - 100 + 90 + 230, 300))
        screen.blit(self.speed_display, (constants.WIDTH // 2 - 100 + 90 + 230, 380))
        for i in range(5):
            screen.blit(self.top5[i], (10, constants.WIDTH // 2 + 50 + i * 30))
        pygame.draw.rect(screen, (0, 180, 0), [constants.WIDTH // 2 - 100, 290, 80, 35], 1)

    def event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 5:  # scroll down
                self.settings["speed"] = max(1, self.settings["speed"] - 1)

                self.speed_display = self.font_object.render(str(self.settings["speed"]), 0, (0, 180, 0))
                return
            if event.button == 4:  # scroll up
                self.settings["speed"] += 1
                self.speed_display = self.font_object.render(str(self.settings["speed"]), 0, (0, 180, 0))
                return
            x, y = event.pos
            if constants.WIDTH // 2 - 100 <= x <= constants.WIDTH // 2 - 100 + 80 and 290 <= y <= 290 + 35:
                self.is_changed = True
                return self.settings
        if event.type == pygame.KEYDOWN:
            k = pygame.key.name(event.key)
            if k.isdigit():
                self.settings["frequency"] = int(k)
                self.freq_display = self.font_object.render(str(self.settings["frequency"]), 0, (0, 180, 0))

    def logic(self):
        pass
