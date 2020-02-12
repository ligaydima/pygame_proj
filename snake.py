import constants


def convert_cell_to_pixels(pos):
    return [(pos[0] * constants.CELL_SIDE, pos[1] * constants.CELL_SIDE), (constants.CELL_SIDE, constants.CELL_SIDE)]


class SnakeBlock:
    def __init__(self, pos):
        """
        constructor
        :type pos: tuple
        :param pos: initial coordinates of block
        """
        self.pos = pos

    def update(self, new_pos):
        self.pos = new_pos


class Snake:
    def __init__(self, size, colors, start_pos):
        """
        constructor
        :param size: initial length of snake
        :param colors: array of snake colors
        :param start_pos: array of initial snake blocks positions
        """
        self.size = size
        self.colors = colors
        self.snake = []
        self.is_dead = False
        self.ind = 0
        self.direction = -1  # -1 left clockwise
        self.ind = 0
        self.cur_color = colors[0]
        for i in range(len(start_pos)):
            self.snake.append(SnakeBlock(start_pos[i]))

    def change_color(self):
        self.ind = (self.ind + 1) % len(self.colors)
        self.cur_color = self.colors[self.ind]

    def change_direction(self, direction):
        self.direction = direction

    def update(self):
        """
        moves snake for 1 block
        """
        if self.direction == -1:
            self.snake.insert(0, SnakeBlock((self.snake[0].pos[0] - 1, self.snake[0].pos[1])))
        if self.direction == 1:
            self.snake.insert(0, SnakeBlock((self.snake[0].pos[0] + 1, self.snake[0].pos[1])))
        if self.direction == 0:
            self.snake.insert(0, SnakeBlock((self.snake[0].pos[0], self.snake[0].pos[1] - 1)))
        if self.direction == 2:
            self.snake.insert(0, SnakeBlock((self.snake[0].pos[0], self.snake[0].pos[1] + 1)))
        self.snake.pop()
        self.check_death()

    def check_food_collision(self, pos):
        for i in self.snake:
            if pos == i.pos:
                return 1
        return 0

    def check_death(self):
        for i in self.snake:
            if i.pos[1] < 0 or i.pos[0] < 0 or i.pos[0] >= constants.FIELD_WIDTH or i.pos[1] >= constants.FIELD_HEIGHT:
                self.is_dead = True
                return
        if len(list(map(lambda a: a.pos, self.snake))) != len(set(list(map(lambda a: a.pos, self.snake)))):
            self.is_dead = True

    def add_block(self):
        self.snake.append(self.snake[-1])

    def get_rects(self):
        """
        get rectangles of snake blocks
        :return: array of rectangles [(left, top), (width, height)
        """
        res = []
        for i in self.snake:
            res.append(convert_cell_to_pixels(i.pos))
        return res
