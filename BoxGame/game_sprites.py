# -*- Coding:UTF-8 -*-
"""
游戏精灵模块
author:David
version:1.0
"""

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
STAR_IMAGE = "image/star.png"
# The pictures of the end point
TERMINAL_IMAGE = "image/terminal.png"
# 目的地与游戏重叠的图片
TERMINAL_PERSON_IMAGE = "image/t_man.png"
# Game walls
GAME_WALL = "image/wall.png"
# Reset picture
RED_RESET_IMG = "image/red_reset.png"
BLUE_RESET_IMG = "image/blue_reset.png"


A_IMG="image/A.png"
B_IMG="image/B.png"
C_IMG="image/C.png"
D_IMG="image/D.png"
E_IMG="image/E.png"
F_IMG="image/F.png"
G_IMG="image/G.png"
H_IMG="image/H.png"
I_IMG="image/I.png"
J_IMG="image/J.png"
K_IMG="image/K.png"
L_IMG="image/L.png"
M_IMG="image/M.png"
N_IMG="image/N.png"
O_IMG="image/O.png"
P_IMG="image/P.png"
Q_IMG="image/Q.png"
R_IMG="image/R.png"
S_IMG="image/S.png"
T_IMG="image/T.png"
U_IMG="image/U.png"
V_IMG="image/V.png"
W_IMG="image/W.png"
X_IMG="image/X.png"
Y_IMG="image/Y.png"
Z_IMG="image/Z.png"



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
        """设置位置"""
        self.rect.x = x
        self.rect.y = y

    def set_sprite_pos(self, sprite_counts, sprite_flag):
        """
        the sprite position
        :param sprite_counts
        :param sprite_flag
        :return:
        """
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
    """游戏角色精灵"""

    def __init__(self, image, game_map):
        super().__init__(image, game_map)
        self.person_x = self.rect.x
        self.person_y = self.rect.y
        # 设置游戏角色位置
        super().set_sprite_pos(0, PERSON_FLAG)

    def move_left(self):
        """向右移动"""
        self.rect.x = self.rect.x - self.rect.width
        pass

    def move_right(self):
        """向左移动"""
        self.rect.x = self.rect.x + self.rect.width
        pass

    def move_up(self):
        """向上移动"""
        self.rect.y = self.rect.y - self.rect.height
        pass

    def move_down(self):
        """向下移动"""
        self.rect.y = self.rect.y + self.rect.height
        pass


class Box(GameSprite):
    """游戏箱子精灵"""

    def __init__(self, image, game_map):
        super().__init__(image, game_map)


class TextSprite(pygame.sprite.Sprite):
    """显示文本的精灵"""

    def __init__(self, text):
        super().__init__()
        self.text = text
        # 创建系统字体
        self.sys_font = pygame.font.SysFont("simsunnsimsun", TEXT_FONT_SIZE)
        # 根据字体创建显示对象(文字)    render(self,text,antialias,color,background = None)
        self.image = self.sys_font.render(str(self.text), True, RED)
        self.rect = self.image.get_rect()

    def set_rect(self, s_rect: pygame.Rect):
        """设置精灵的显示位置及大小"""
        self.rect = s_rect

    def update(self, text):
        """更新精灵显示文本"""
        self.text = text
        self.image = self.sys_font.render(str(self.text), True, RED)
