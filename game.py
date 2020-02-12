import pygame

import constants
from gameover import GameOver
from main_menu import MainMenu
from play import Play
from db_interaction import Interactor

class Game:
    def __init__(self):
        self.gameover = False
        self.screen = pygame.display.set_mode(constants.SIZE)
        self.phase = 0
        self.phases = [MainMenu, Play, GameOver]
        self.inter = Interactor()
        self.cur_phase = MainMenu(self.inter.get_top_5())

    def process_drawing(self):
        self.cur_phase.draw(self.screen)
        pygame.display.flip()

    def process_logic(self):
        if self.cur_phase.is_changed:
            self.phase = (self.phase + 1) % 3
            if self.phase == 1:
                self.cur_phase = self.phases[self.phase](self.cur_phase.settings["speed"],
                                                         self.cur_phase.settings["frequency"])
            elif self.phase == 2:
                pygame.time.wait(10 ** 3)
                self.inter.write(self.cur_phase.score * self.cur_phase.speed)
                self.cur_phase = self.phases[self.phase](self.cur_phase.score * self.cur_phase.speed)
            else:
                self.cur_phase = self.phases[self.phase](self.inter.get_top_5())
        self.cur_phase.logic()

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameover = True
                self.inter.close()
            self.cur_phase.event(event)

    def main_loop(self):
        clock = pygame.time.Clock()
        while not self.gameover:
            self.process_events()
            self.process_logic()
            self.process_drawing()
            clock.tick(constants.FPS)
