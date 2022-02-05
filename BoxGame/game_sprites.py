# -*- Coding:UTF-8 -*-

import pygame

# Game Music
GAME_MUSIC = "image/卡农.mp3"
# Game size
SCREEN_RECT = pygame.Rect(0, 0, 700, 480)
# Game Name
GAME_NAME = "BoxGame"
# Refresh rate
FRAME_PRE_SEC = 60
# Background
GAME_BACKGROUND = "image/white_bg.png"
# The image of "I"
PERSON_IMAGE = "image/human.png"
# The game boxes
BOX_IMAGE = "image/box.png"
# After the box arrive the location 
##############################
STAR_IMAGE = "image/star.png"
# The pictures of the end point
TERMINAL_IMAGE = "image/terminal.png"
# 目的地与游戏重叠的图片
TERMINAL_PERSON_IMAGE = "image/t_man.png"
##############################
# Game walls
GAME_WALL = "image/wall.png"
# Reset picture
RED_RESET_IMG = "image/red_reset.png"
BLUE_RESET_IMG = "image/blue_reset.png"

# Font Size
TEXT_FONT_SIZE = 25

# Level display position
LEVEL_DISPLAY_POS = pygame.Rect(520, 50, 100, 50)
# timing
TIME_DISPLAY_POS = pygame.Rect(520, 150, 100, 50)
# steps
STEP_DISPLAY_POS = pygame.Rect(520, 250, 100, 50)
# remake button
RESET_IMG_POS = pygame.Rect(520, 350, 64, 64)

# 0	# Null
WALL_FLAG = 1  # Wall
BOX_FLAG = 2  # Box
PERSON_FLAG = 3  # ?
TERMINAL_FLAG = 4  # shows the end block 
FINISH_BOX_FLAG = 5  # finished boxes

I_BOX='I'
C_BOX='C'
E_BOX='E'




RED = pygame.color.Color("RED")
YELLOW = pygame.color.Color("YELLOW")
BLUE = pygame.color.Color("#70f3ff")
GREEN = pygame.color.Color("GREEN")
WHITE = pygame.color.Color("WHITE")
ORANGE = pygame.color.Color("ORANGE")
PINK = pygame.color.Color("#ff4777")


class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image, game_map):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.game_map = game_map
        # 标识游戏箱子到达目的地
        self.is_success = False

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def set_sprite_pos(self, sprite_counts, sprite_flag):
        count = 0
        for x in range(len(self.game_map)):
            for y in range(len(self.game_map[x])):
                if self.game_map[x][y] == sprite_flag:
                    if count == sprite_counts:
                        self.rect.x = self.rect.width * x
                        self.rect.y = self.rect.height * y
                        return
                    count += 1


class GamePerson(GameSprite):
    def __init__(self, image, game_map):
        super().__init__(image, game_map)
        self.person_x = self.rect.x
        self.person_y = self.rect.y
        #set character position
        super().set_sprite_pos(0, PERSON_FLAG)

    def move_left(self):
        self.rect.x = self.rect.x - self.rect.width
        pass

    def move_right(self):
        self.rect.x = self.rect.x + self.rect.width
        pass

    def move_up(self):
        self.rect.y = self.rect.y - self.rect.height
        pass

    def move_down(self):
        self.rect.y = self.rect.y + self.rect.height
        pass


class Box(GameSprite):
    def __init__(self, image, game_map):
        super().__init__(image, game_map)

##############################
class TextSprite(pygame.sprite.Sprite):
    def __init__(self, text):
        super().__init__()
        self.text = text
        # 创建系统字体
        self.sys_font = pygame.font.SysFont("simsunnsimsun", TEXT_FONT_SIZE)
        # 根据字体创建显示对象(文字)    render(self,text,antialias,color,background = None)
        self.image = self.sys_font.render(str(self.text), True, RED)
        self.rect = self.image.get_rect()

    def set_rect(self, s_rect: pygame.Rect):
        self.rect = s_rect

    def update(self, text):
        self.text = text
        self.image = self.sys_font.render(str(self.text), True, RED)
 ##############################
