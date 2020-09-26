import pygame
import neat
import time
import os
import random

black = (0, 0, 0)

pygame.font.init()

img_dict = {
    "2": pygame.image.load("2.png"),
    "4": pygame.image.load("4.png"),
    "8": pygame.image.load("8.png"),
    "16": pygame.image.load("16.png"),
    "32": pygame.image.load("32.png"),
    "64": pygame.image.load("64.png"),
    "128": pygame.image.load("128.png"),
    "256": pygame.image.load("256.png"),
    "512": pygame.image.load("512.png"),
    "1024": pygame.image.load("1024.png"),
    "2048": pygame.image.load("2048.png"),
    "background": pygame.image.load("Background.png")
}

WIN_WIDTH = 500
WIN_HEIGHT = 500


class Box:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.val = val
        self.clock = pygame.time.Clock()
        self.width = 125
        self.height = 125
        self.switch = {
            "2": "4",
            "4": "8",
            "8": "16",
            "16": "32",
            "32": "64",
            "64": "128",
            "128": "256",
            "256": "512",
            "512": "1024",
            "1024": "2048",
        }

    def my_pos(self):
        return [self.x, self.y]

    def my_val(self):
        return self.val

    def remove(self):
        print(self.x)
        print(self.y)
        self.x = 500
        self.y = 500

    def upgrade(self):
        self.val = self.switch[self.val]

    def draw(self, win):
        self.win.blit(img_dict[self.val], (self.x, self.y))


def move_right(box_list):
    box_listt = []
    for box in box_list:
        current_pos = box.my_pos()
        current_val = box.my_val()
        i = 125
        flag = True
        count = 0
        while current_pos[0] != 375:
            for boxx in box_list:
                if boxx.my_pos() == [current_pos[0]+i, current_pos[1]]:
                    flag = False
                    break
            if flag:
                current_pos[0] = current_pos[0] + i
            # print(flag)
            count = count + 1
            if count >= 6:
                break
        box_listt.append(
            Box(current_pos[0], current_pos[1], current_val))
    box_list = box_listt.copy()
    # print(box_list)
    box_listt.clear()
    return box_list


def move_up(box_list):
    box_listt = []
    for box in box_list:
        current_pos = box.my_pos()
        current_val = box.my_val()
        i = 125
        flag = True
        count = 0
        while current_pos[1] != 0:
            for boxx in box_list:
                if boxx.my_pos() == [current_pos[0], current_pos[1]-i]:
                    flag = False
                    break
            if flag:
                current_pos[1] = current_pos[1] - i
            # print(flag)
            count = count + 1
            if count >= 6:
                break
        box_listt.append(
            Box(current_pos[0], current_pos[1], current_val))
    box_list = box_listt.copy()
    # print(box_list)
    box_listt.clear()
    return box_list


def move_down(box_list):
    box_listt = []
    for box in box_list:
        current_pos = box.my_pos()
        current_val = box.my_val()
        i = 125
        flag = True
        count = 0
        while current_pos[1] != 375:
            for boxx in box_list:
                if boxx.my_pos() == [current_pos[0], current_pos[1]+i]:
                    flag = False
                    break
            if flag:
                current_pos[1] = current_pos[1] + i
            # print(flag)
            count = count + 1
            if count >= 6:
                break
        box_listt.append(
            Box(current_pos[0], current_pos[1], current_val))
    box_list = box_listt.copy()
    # print(box_list)
    box_listt.clear()
    return box_list


def move_left(box_list):
    box_listt = []
    for box in box_list:
        current_pos = box.my_pos()
        current_val = box.my_val()
        i = 125
        flag = True
        count = 0
        while current_pos[0] != 0:
            for boxx in box_list:
                if boxx.my_pos() == [current_pos[0]-i, current_pos[1]]:
                    flag = False
                    break
            if flag:
                current_pos[0] = current_pos[0] - i
            # print(flag)
            count = count + 1
            if count >= 6:
                break
        box_listt.append(
            Box(current_pos[0], current_pos[1], current_val))
    box_list = box_listt.copy()
    # print(box_list)
    box_listt.clear()
    return box_list


def add_horizontal_L(box_list, box_count):
    for box in box_list:
        current_pos = box.my_pos()
        current_val = box.my_val()
        for boxx in box_list:
            if boxx.my_pos() == [current_pos[0]-125, current_pos[1]]:
                if boxx.my_val() == current_val:
                    # ........................
                    boxx.upgrade()
                    box.remove()
                    # box_max = box_max + 1
                    box_count = box_count - 1
                    # for boxxx in box_list:
                    #     if boxxx.my_pos() == [current_pos[0], current_pos[1]]:
                    #         boxxx.remove()
    return box_count


def add_horizontal_R(box_list, box_count):
    for box in box_list:
        current_pos = box.my_pos()
        current_val = box.my_val()
        for boxx in box_list:
            if boxx.my_pos() == [current_pos[0]+125, current_pos[1]]:
                if boxx.my_val() == current_val:
                    # ........................
                    boxx.upgrade()
                    box.remove()
                    # box_max = box_max + 1
                    box_count = box_count - 1
    return box_count


def add_horizontal_U(box_list, box_count):
    for box in box_list:
        current_pos = box.my_pos()
        current_val = box.my_val()
        for boxx in box_list:
            if boxx.my_pos() == [current_pos[0], current_pos[1]-125]:
                if boxx.my_val() == current_val:
                    # ........................
                    boxx.upgrade()
                    box.remove()
                    # box_max = box_max + 1
                    box_count = box_count - 1
    return box_count


def add_horizontal_D(box_list, box_count):
    for box in box_list:
        current_pos = box.my_pos()
        current_val = box.my_val()
        for boxx in box_list:
            if boxx.my_pos() == [current_pos[0], current_pos[1]+125]:
                if boxx.my_val() == current_val:
                    # ........................
                    boxx.upgrade()
                    box.remove()
                    # box_max = box_max + 1
                    box_count = box_count - 1
    return box_count


def gen_rand_box(box_list, box_count):
    pos_val = [0, 125, 250, 375]
    box_val = ["2", "4"]
    randVal = box_val[random.randint(0, 1)]
    if len(box_list) == 0:
        box_list.append(
            Box(pos_val[random.randint(0, 3)],
                pos_val[random.randint(0, 3)],
                "2")
        )

    while box_count > len(box_list) and box_count <= 16:
        Match = False
        randX = pos_val[random.randint(0, 3)]
        randY = pos_val[random.randint(0, 3)]
        # box_list.my_pos
        for box in box_list:
            if box.my_pos() == [randX, randY]:
                Match = True
                break
        if not Match:
            box_list.append(Box(randX, randY, randVal))
        # print(Match)


def main():
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    box_count = 2
    box_list = []
    joke = []
    # box_max = 16
    clock = pygame.time.Clock()
    run1 = True
    # box = Box(375, 375, "2")
    # box_list.append(box)
    while run1:
        clock.tick(5)
        gen_rand_box(box_list, box_count)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run1 = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    for b in range(0, 3, 1):
                        box_list = move_left(box_list)

                    box_count = add_horizontal_L(box_list, box_count)

                    for b in range(0, 3, 1):
                        box_list = move_left(box_list)
                    # print("__________________")
                    box_count = box_count + 1
                elif event.key == pygame.K_RIGHT:

                    for b in range(0, 3, 1):
                        box_list = move_right(box_list)

                    box_count = add_horizontal_R(box_list, box_count)

                    for b in range(0, 3, 1):
                        box_list = move_right(box_list)
                    box_count = box_count + 1
                elif event.key == pygame.K_UP:
                    for b in range(0, 3, 1):
                        box_list = move_up(box_list)

                    box_count = add_horizontal_U(box_list, box_count)

                    for b in range(0, 3, 1):
                        box_list = move_up(box_list)
                    # print("__________________")
                    box_count = box_count + 1

                elif event.key == pygame.K_DOWN:
                    for b in range(0, 3, 1):
                        box_list = move_down(box_list)

                    box_count = add_horizontal_D(box_list, box_count)

                    for b in range(0, 3, 1):
                        box_list = move_down(box_list)
                    # print("__________________")
                    box_count = box_count + 1
        # print(len(box_list))
        # print(box_max - len(box_list))
        pygame.draw.rect(win, black, (0, 0, 500, 500))
        for box in box_list:
            if box.my_pos()[0] >= 0 and box.my_pos()[0] <= 375 and box.my_pos()[1] >= 0 and box.my_pos()[1] <= 375:
                joke.append(box)
        print(len(joke))
        # box_count = len(joke) + 1
        box_list = joke.copy()
        joke.clear()

        for box in box_list:
            box.draw(win)
            # box_list.remove(box)
            pygame.display.update()
        # pygame.display.update()


main()
