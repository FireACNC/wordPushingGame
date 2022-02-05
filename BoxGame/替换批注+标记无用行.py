# -*- Coding:UTF-8 -*-
"""
#Main module
"""

import os
import sys
import time
import pyautogui as gui
from game_sprites import *

pygame.init()

# Load Music
pygame.mixer.init()
pygame.mixer.music.load(GAME_MUSIC)

# Get computer's resolution
screen_width, screen_height = gui.size()
game_x = (screen_width - SCREEN_RECT.width) / 2
game_y = (screen_height - SCREEN_RECT.height) / 2
# Set up for the window
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (game_x, game_y)

game_maps = {
    ice_map: [
        [0, W, A, L, L, S, A, N, D, W, A, L, L, S, 0],
        [W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W],
        [A, 0, M, Y, 0, H, E, A, R, T, 0, I, S, 0, A],
        [L, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, L],
        [L, 0, L, I, K, E, 0, F, R, O, Z, E, N, 0, L],
        [S, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, S],
        [0, W, A, L, L, S, I, C, E, W, A, L, L, S, 0],
    ],
    1: [
        [9, 9, 1, 1, 1, 9, 9, 9],
        [9, 9, 1, 4, 1, 9, 9, 9],
        [9, 9, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 2, 0, 2, 4, 1],
        [1, 4, 0, 2, 3, 1, 1, 1],
        [1, 1, 1, 1, 2, 1, 9, 9],
        [9, 9, 9, 1, 4, 1, 9, 9],
        [9, 9, 9, 1, 1, 1, 9, 9]
    ],
    2: [
        [9, 9, 1, 1, 1, 1, 9, 9],
        [9, 9, 1, 4, 4, 1, 9, 9],
        [9, 1, 1, 0, 4, 1, 1, 9],
        [9, 1, 0, 0, 2, 4, 1, 9],
        [1, 1, 0, 2, 3, 0, 1, 1],
        [1, 0, 0, 1, 2, 2, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]
    ],
    3: [
        [9, 9, 1, 1, 1, 1, 9, 9],
        [9, 1, 1, 0, 0, 1, 9, 9],
        [9, 1, 3, 2, 0, 1, 9, 9],
        [9, 1, 1, 2, 0, 1, 1, 9],
        [9, 1, 1, 0, 2, 0, 1, 9],
        [9, 1, 4, 2, 0, 0, 1, 9],
        [9, 1, 4, 4, 6, 4, 1, 9],
        [9, 1, 1, 1, 1, 1, 1, 9]
    ],
    4: [
        [1, 1, 1, 1, 1, 9, 9, 9, 9],
        [1, 0, 0, 0, 1, 1, 1, 1, 1],
        [1, 2, 1, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 3, 0, 0, 2, 0, 1],
        [1, 4, 5, 1, 2, 1, 2, 1, 1],
        [1, 4, 2, 0, 0, 0, 0, 1, 9],
        [1, 4, 4, 0, 0, 1, 1, 1, 9],
        [1, 1, 1, 1, 1, 1, 9, 9, 9]
    ],
    5: [
        [9, 1, 1, 1, 1, 1, 1, 9],
        [9, 1, 0, 0, 0, 0, 1, 9],
        [9, 1, 0, 2, 2, 0, 1, 9],
        [9, 1, 1, 6, 3, 0, 1, 9],
        [9, 1, 0, 4, 0, 1, 9, 9],
        [9, 1, 0, 6, 0, 1, 9, 9],
        [9, 1, 0, 6, 0, 1, 9, 9],
        [9, 1, 0, 4, 0, 1, 9, 9],
        [9, 1, 1, 1, 1, 1, 9, 9]
    ],

    6: [
        [9, 1, 1, 1, 1, 1, 1, 9, 9],
        [9, 1, 0, 0, 0, 0, 1, 1, 9],
        [1, 1, 4, 1, 1, 3, 0, 1, 9],
        [1, 0, 6, 5, 0, 0, 0, 1, 9],
        [1, 0, 0, 1, 2, 2, 0, 1, 9],
        [1, 0, 0, 0, 0, 1, 1, 1, 9],
        [1, 1, 1, 1, 1, 1, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9]

    ],
    7: [
        [9, 1, 1, 1, 1, 1, 9, 9, 9],
        [9, 1, 0, 3, 0, 1, 1, 1, 9],
        [1, 1, 0, 1, 2, 0, 0, 1, 9],
        [1, 0, 6, 4, 0, 4, 0, 1, 9],
        [1, 0, 0, 2, 2, 0, 1, 1, 9],
        [1, 1, 1, 0, 1, 4, 1, 9, 9],
        [9, 9, 1, 0, 0, 0, 1, 9, 9],
        [9, 9, 1, 1, 1, 1, 1, 9, 9]

    ],
    8: [
        [1, 1, 1, 1, 1, 1, 1, 9],
        [1, 4, 4, 2, 4, 4, 1, 9],
        [1, 4, 4, 1, 4, 4, 1, 9],
        [1, 0, 2, 2, 2, 0, 1, 9],
        [1, 0, 0, 2, 0, 0, 1, 9],
        [1, 0, 2, 2, 2, 0, 1, 9],
        [1, 0, 0, 1, 3, 0, 1, 9],
        [1, 1, 1, 1, 1, 1, 1, 9]

    ],
    9: [
        [1, 1, 1, 1, 1, 1, 9, 9],
        [1, 0, 0, 0, 0, 1, 9, 9],
        [1, 0, 4, 6, 0, 1, 1, 1],
        [1, 0, 4, 2, 4, 2, 0, 1],
        [1, 1, 0, 2, 0, 0, 0, 1],
        [9, 1, 1, 1, 1, 0, 3, 1],
        [9, 9, 9, 9, 1, 1, 1, 1],
        [9, 9, 9, 9, 9, 9, 9, 9]
    ],
    10: [
        [9, 9, 1, 1, 1, 1, 1, 9, 9],
        [9, 1, 1, 0, 3, 0, 1, 1, 9],
        [9, 1, 0, 0, 6, 2, 0, 1, 9],
        [9, 1, 2, 0, 4, 0, 2, 1, 9],
        [9, 1, 4, 4, 1, 4, 4, 1, 9],
        [1, 1, 2, 0, 6, 0, 0, 1, 1],
        [1, 0, 2, 0, 1, 0, 2, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
}


class BoxGame(object):

    def __init__(self, game_level=1):
        ##############################
        # Whether begin to record time
        self.is_first_time_count = True
        ##############################

        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.game_name = pygame.display.set_caption(GAME_NAME)
        self.game_clock = pygame.time.Clock()

        # Default Level 1
        self.game_level = game_level
        self.game_map = game_maps[self.game_level]
        self.is_first = True
        # Character's moving direction
        self.move_direction = None

        ###########################
        # 记录游戏开始时间
        self.start_time = None
        # 记录游戏当前时间
        self.current_time = None

        # 记录游戏移动
        self.step_count = 0
        ###########################

        # Initial Setup
        self.__init_game_map()
        self.__create_sprite()

    def start_game(self):
        """Game Start"""
        while True:
            # Play music
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play()
            self.game_clock.tick(FRAME_PRE_SEC)
            self.__event_handle()
            self.current_time = time.process_time()
            self.__check_collision()
            self.__update_sprite()
            self.__update_game_level()
            pygame.display.update()
            pass

    def __event_handle(self):
        """Keep tracking"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # print(pygame.key.name(event.key))
                self.__move_event(event)
                self.__time_step_count(event)
            elif event.type == pygame.KEYUP:
                print("keyup")
            elif event.type == pygame.MOUSEMOTION:
                # Mouse movement
                x, y = event.pos  # Get coordinates
                # print("Mouse_Move:%s---%s" % (x, y))

                if self.__is_on_reset_img(x, y):
                    # Switch pictures
                    self.reset_sprite_group.sprites()[0].image = pygame.image.load(BLUE_RESET_IMG)
                else:
                    # Reset
                    self.reset_sprite_group.sprites()[0].image = pygame.image.load(RED_RESET_IMG)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Mouse click
                x, y = event.pos  # Get mouse position
                print("Mouse_Click:%s---%s" % (x, y))
                if self.__is_on_reset_img(x, y):
                    # Restart
                    self.__reset_game()

    @staticmethod
    def __is_on_reset_img(x, y):
        #if the player click in the range of reset image
        if (RESET_IMG_POS.x <= x <= RESET_IMG_POS.x + RESET_IMG_POS.width) and \
                (RESET_IMG_POS.y <= y <= RESET_IMG_POS.y + RESET_IMG_POS.height):
            return True
        else:
            return False

    def __create_sprite(self):

        #backgroup
        game_bg_sprite = GameSprite(GAME_BACKGROUND, self.game_map)
        self.game_bg_group = pygame.sprite.Group(game_bg_sprite)

        #player
        self.game_person_sprite = GamePerson(PERSON_IMAGE, self.game_map)
        self.game_person_group = pygame.sprite.Group(self.game_person_sprite)

        #level
        level_sprite = TextSprite(text="Level: " + str(self.game_level))
        level_sprite.set_rect(LEVEL_DISPLAY_POS)
        self.level_sprite_group = pygame.sprite.Group(level_sprite)

        #reset
        reset_sprite = GameSprite(RED_RESET_IMG, self.game_map)
        reset_sprite.set_pos(RESET_IMG_POS.x, RESET_IMG_POS.y)
        self.reset_sprite_group = pygame.sprite.Group(reset_sprite)

        #################################################
        self.box_group = pygame.sprite.Group()
        for box_count in range(self.box_counts):
            box_sprite = Box(BOX_IMAGE, self.game_map)
            box_sprite.set_sprite_pos(box_count, BOX_FLAG)
            self.box_group.add(box_sprite)

        self.wall_group = pygame.sprite.Group()
        for wall_count in range(self.wall_counts):
            wall_sprite = GameSprite(GAME_WALL, self.game_map)
            wall_sprite.set_sprite_pos(wall_count, WALL_FLAG)
            self.wall_group.add(wall_sprite)

        self.box_terminal_group = pygame.sprite.Group()
        for terminal_count in range(self.terminal_counts):
            box_terminal_sprite = GameSprite(TERMINAL_IMAGE, self.game_map)
            box_terminal_sprite.set_sprite_pos(terminal_count, TERMINAL_FLAG)
            self.box_terminal_group.add(box_terminal_sprite)

        # 创建显示时间精灵
        time_sprite = TextSprite(text="Time: 0")
        time_sprite.set_rect(TIME_DISPLAY_POS)
        self.time_sprite_group = pygame.sprite.Group(time_sprite)

        # 创建显示移动步数精灵
        step_sprite = TextSprite(text="Step: 0")
        step_sprite.set_rect(STEP_DISPLAY_POS)
        self.step_sprite_group = pygame.sprite.Group(step_sprite)
        #################################################


    def __update_sprite(self):
        #keep updating the sprite
        self.game_bg_group.update()
        self.game_bg_group.draw(self.screen)

        self.game_person_group.update()
        self.game_person_group.draw(self.screen)

        self.box_group.update()
        self.box_group.draw(self.screen)

        self.wall_group.update()
        self.wall_group.draw(self.screen)

        #################################################
        self.box_terminal_group.update()
        self.box_terminal_group.draw(self.screen)

        if self.current_time is not None and self.start_time is not None:
            self.time_sprite_group.update("Time: " + str(self.current_time - self.start_time))
        self.time_sprite_group.draw(self.screen)

        self.step_sprite_group.update("Step: " + str(self.step_count))
        self.step_sprite_group.draw(self.screen)
        #################################################

        self.level_sprite_group.draw(self.screen)

        self.reset_sprite_group.draw(self.screen)

    def __check_collision(self):
        # when collision happen between player and moveable blocks, push them
        box_sprite = pygame.sprite.spritecollide(self.game_person_sprite, self.box_group, False)
        if box_sprite:
            if self.move_direction is not None:
                if self.move_direction == "up":
                    box_sprite[0].rect.y = box_sprite[0].rect.y - box_sprite[0].rect.height
                    self.__box_wall_box_collide(box_sprite)
                elif self.move_direction == "down":
                    box_sprite[0].rect.y = box_sprite[0].rect.y + box_sprite[0].rect.height
                    self.__box_wall_box_collide(box_sprite)
                elif self.move_direction == "left":
                    box_sprite[0].rect.x = box_sprite[0].rect.x - box_sprite[0].rect.width
                    self.__box_wall_box_collide(box_sprite)
                elif self.move_direction == "right":
                    box_sprite[0].rect.x = box_sprite[0].rect.x + box_sprite[0].rect.width
                    self.__box_wall_box_collide(box_sprite)
                    
        #collide with wall, went back one space
        wall_sprite = pygame.sprite.spritecollide(self.game_person_sprite, self.wall_group, False)
        if wall_sprite:
            self.__back_person()
    
    def __box_wall_box_collide(self, box_sprite):
        #when box collide with other stuff, remove box and went back player
        result = pygame.sprite.groupcollide(self.box_group, self.wall_group, False, False)
        self.box_group.remove(box_sprite[0])
        box_collide_result = pygame.sprite.spritecollide(box_sprite[0], self.box_group, False)
        print(box_collide_result)
        if result or box_collide_result:
            print("test")
            if self.move_direction == "up":
                box_sprite[0].rect.y = box_sprite[0].rect.y + box_sprite[0].rect.height
            elif self.move_direction == "down":
                box_sprite[0].rect.y = box_sprite[0].rect.y - box_sprite[0].rect.height
            elif self.move_direction == "left":
                box_sprite[0].rect.x = box_sprite[0].rect.x + box_sprite[0].rect.width
            elif self.move_direction == "right":
                box_sprite[0].rect.x = box_sprite[0].rect.x - box_sprite[0].rect.width
            self.__back_person()
        #add back box
        self.box_group.add(box_sprite[0])


        ##################################################################
        # 游戏箱子与箱子的目的地发生碰撞,目的地图片更换成星星
        result = pygame.sprite.groupcollide(self.box_group, self.box_terminal_group, False, False)
        if result:
            for box_sprite, terminal_sprite in result.items():
                terminal_sprite[0].image = pygame.image.load(STAR_IMAGE)
                terminal_sprite[0].is_success = True

        # 游戏角色与目的地发生碰撞，目的地更换图片为t_man.png
        terminal_sprite = pygame.sprite.spritecollide(self.game_person_sprite, self.box_terminal_group, False)
        if terminal_sprite:
            # 把没有变成星星的图片还原,然后在更换
            for t_sprite in self.box_terminal_group.sprites():
                if not t_sprite.is_success:
                    t_sprite.image = pygame.image.load(TERMINAL_IMAGE)
            terminal_sprite[0].image = pygame.image.load(TERMINAL_PERSON_IMAGE)
            terminal_sprite[0].is_success = False
        else:
            # 没有发生碰撞时记得把没有变成星星的图片还原
            for t_sprite in self.box_terminal_group.sprites():
                if not t_sprite.is_success:
                    t_sprite.image = pygame.image.load(TERMINAL_IMAGE)
        
        ##################################################################
        

    def __back_person(self):
        #go back one person
        self.step_count -= 1
        if self.move_direction == "up":
            self.game_person_sprite.move_down()
        elif self.move_direction == "down":
            self.game_person_sprite.move_up()
        elif self.move_direction == "left":
            self.game_person_sprite.move_right()
        elif self.move_direction == "right":
            self.game_person_sprite.move_left()

    def __move_event(self, event):
        if event.key == pygame.K_w or pygame.key.name(event.key) == "up":
            #move direction
            self.move_direction = "up"
            self.game_person_sprite.move_up()
        elif event.key == pygame.K_s or pygame.key.name(event.key) == "down":
            self.move_direction = "down"
            self.game_person_sprite.move_down()
        elif event.key == pygame.K_a or pygame.key.name(event.key) == "left":
            self.move_direction = "left"
            self.game_person_sprite.move_left()
        elif event.key == pygame.K_d or pygame.key.name(event.key) == "right":
            self.move_direction = "right"
            self.game_person_sprite.move_right()

    def __init_game_map(self):
        self.is_first = True
        box_count = 0
        terminal_count = 0
        wall_count = 0
        for x in range(len(self.game_map)):
            for y in range(len(self.game_map[x])):
                if self.game_map[x][y] == BOX_FLAG:
                    box_count += 1
                elif self.game_map[x][y] == TERMINAL_FLAG:
                    terminal_count += 1
                elif self.game_map[x][y] == WALL_FLAG:
                    wall_count += 1
        self.box_counts = box_count
        self.wall_counts = wall_count
        self.terminal_counts = terminal_count


    #################################################

    def __update_game_level(self):
        count = 0
        for terminal_sprite in self.box_terminal_group.sprites():
            if terminal_sprite.is_success:
                count += 1
        # 如果目的地全部变成星星图片则下一关卡
        if count == self.terminal_counts:
            # 由于while速度太快，加个是否第一次的标志来更新关卡
            if self.is_first:
                self.game_level += 1
                self.is_first = False
                level = self.game_level
                print("游戏关卡:" + str(self.game_level))
                # 释放内存
                del self
                BoxGame(game_level=level).start_game()

    def __time_step_count(self, event):
        """游戏时间和移动步数计时"""
        if event.key == pygame.K_w or pygame.key.name(event.key) == "up" or \
                event.key == pygame.K_s or pygame.key.name(event.key) == "down" or \
                event.key == pygame.K_a or pygame.key.name(event.key) == "left" or \
                event.key == pygame.K_d or pygame.key.name(event.key) == "right":
            if self.is_first_time_count:
                self.start_time = time.process_time()
                self.is_first_time_count = False
            self.step_count += 1

    #################################################

    def __reset_game(self):
        game_level = self.game_level
        # if self.step_count == 0:
        #     # 如果玩家没有走动则重置无效
        #     print("玩家没有走动则重置无效")
        #     return
        del self #release ram
        BoxGame(game_level=game_level).start_game()


if __name__ == '__main__':
    BoxGame().start_game()
    pass
