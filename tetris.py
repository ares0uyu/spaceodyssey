import sys
import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, Rect, KEYUP
import random


class Block:
    def __init__(self):
        self.position = {
            'x' : 5,
            'y' : 5
        }
        self.blocks = []

    def init_position(self):
        self.position = {
            'x' : 5,
            'y' : 5
        }
        self.blocks = []

    def move_left(self):
        self.position['x'] -= 1

    def move_right(self):
        self.position['x'] += 1

    def move_down(self):
        self.position['y'] += 1

    def change(self):
        temp = self.blocks[0]
        self.blocks[0] = self.blocks[1]
        self.blocks[1] = self.blocks[2]
        self.blocks[2] = temp

def get_initialized_board():
    board = []

    for i in range(0, 20):
        board.append([0,0,0,0,0,0,0,0,0,0])
    return board

def can_move_left(now_block):
    x = now_block.position['x']
    y = now_block.position['y']
    if x <= 0:
        return False
    elif board[y][x-1] != 0:
        return False
    return True

def can_move_right(now_block):
    x = now_block.position['x']
    y = now_block.position['y']
    if x >= 9:
        return False
    elif board[y][x+1] != 0:
        return False
    return True

def can_move_down(now_block):
    x = now_block.position['x']
    y = now_block.position['y']
    if y >= 19:
        return False
    elif board[y + 1][x] != 0:
        return False
    return True

def set_value_on_board(x, y, value):
    global board
    board[y][x] = value


block_color = [
    (64, 64, 64),
    (255, 255, 255),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (128, 0, 0),
    (0, 128, 0),
    (0, 0, 128),
    (255, 0, 255),
    (0, 255, 255)
]

screen_size = {
    'width': 240,
    'height': 400
}

pygame.init()
screen = pygame.display.set_mode((screen_size['width'], screen_size['height']))
pygame.display.set_caption('HEXA')

now_block = Block()
next_block = Block()
board = get_initialized_board()

now_block.blocks = [
    random.randint(1, len(block_color) - 1),
    random.randint(1, len(block_color) - 1),
    random.randint(1, len(block_color) - 1)
]

next_block.init_position()
next_block.blocks = [
    random.randint(1, len(block_color) - 1),
    random.randint(1, len(block_color) - 1),
    random.randint(1, len(block_color) - 1)
]

delay = 1000
level = 0
score = 0
while True:
    update_game(board, now_block, next_block, score)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
                break
            elif event.key == pygame.K_UP:
                now_block.change()
                break
            elif event.key == pygame.K_LEFT:
                if canmove_left(now_block):
                    now_block.move_left()
                break
            elif event.key == pygame.K_DOWN:
                if canmove_down(now_block):
                    now_block.move_down()
                break
            elif event.key == pygame.K_RIGHT:
                if canmove_right(now_block):
                    now_block.move_right()
                break
            elif event.key == pygame.K_SPACE:
                for y in range(now_block.position['y'], 20):
                    b = Block()
                    b.position['x'] = now_block.position['x']
                    b.position['y'] = y
                    if can_move_down(b) == False:
                        now_block.position['y'] = y
                        break
                break
        if can_move_down(now_block):
            level += 1
            if level > delay:
                level = 0
                now_block.move_down()
            continue
        else:
            for i, block in enumerate(now_block.blocks):
                x = now_block.position['x']
                y = (now_block.position['y'] - i)
                set_value_on_board(x, y, block)

            while True:
                point = ckeck_board(board)
                if point <= 0: break
                score += point

            now_block.init_position()
            now_block.blocks = next_block.blocks

            next_block.blocks = [
                random.randint(1, len(block_color) - 1),
                random.randint(1, len(block_color) - 1),
                random.randint(1, len(block_color) - 1)
            ]

            delay -= 1

        if gameover(board):
            sys.exit()


