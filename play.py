import os
import random

import pygame

import constants
from snake import Snake, convert_cell_to_pixels


class Play:
    def __init__(self, speed, freq):
        self.speed = speed
        self.freq = freq
        self.snake = Snake(constants.INITIAL_SNAKE_SIZE, constants.SNAKE_COLORS,
                           constants.INITIAL_SNAKE_POS)
        self.is_changed = False
        self.logic_ticks = 0
        self.anim_ticks = 0
        self.new_dir = -3
        self.cur_food_coords = self.gen_food_coords()
        self.score = 0
        pygame.mixer.music.load(os.path.join('res', "music.mp3"))
        pygame.mixer.music.play(-1)
        self.is_epileptic = 0
        print(self.cur_food_coords)

    def gen_food_coords(self):
        coords = []
        x = set()
        for i in self.snake.snake:
            x.add(tuple(i.pos))
        for i in range(constants.FIELD_WIDTH):
            for j in range(constants.FIELD_HEIGHT):
                if (i, j) not in x:
                    coords.append((i, j))
        return random.choice(coords)

    def draw(self, screen):
        # screen.fill(255, 255, 255)
        screen.fill((255 - self.snake.cur_color[0], 255 - self.snake.cur_color[1], 255 - self.snake.cur_color[2]))
        for i in self.snake.get_rects():
            pygame.draw.rect(screen, self.snake.cur_color, i)
        pygame.draw.rect(screen, (100, 100, 100), convert_cell_to_pixels(self.cur_food_coords))

    def logic(self):
        self.logic_ticks += 1
        self.anim_ticks += 1
        if self.anim_ticks >= constants.FPS * self.freq and self.freq != 0:
            self.snake.change_color()
            if not self.is_epileptic:
                self.anim_ticks = 0
        if self.logic_ticks * self.speed // constants.FPS >= 1:
            if self.new_dir != -3:
                self.snake.change_direction(self.new_dir)
                self.new_dir = -3
            self.snake.update()
            self.logic_ticks = 0
            if self.snake.check_food_collision(self.cur_food_coords):
                self.score += 1
                self.cur_food_coords = self.gen_food_coords()
                self.snake.add_block()
        if self.snake.is_dead:
            self.is_changed = True
            pygame.mixer.music.stop()

    def check_new_direction(self, d):
        return (d + self.snake.direction) % 2

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and self.check_new_direction(0):
                self.new_dir = 0
            if event.key == pygame.K_a and self.check_new_direction(-1):
                self.new_dir = -1
            if event.key == pygame.K_s and self.check_new_direction(2):
                self.new_dir = 2
            if event.key == pygame.K_d and self.check_new_direction(1):
                self.new_dir = 1
            if event.key == pygame.K_BACKSPACE:
                self.is_epileptic = (self.is_epileptic + 1) % 2
