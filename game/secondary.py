import pygame
from random import randint as ri

pygame.init()
time = pygame.time.Clock()
screen = pygame.display.set_mode((1296, 768))
pygame.display.set_caption("George and dinos")
labal_font = pygame.font.SysFont(None, 36)


score = 0
bg = pygame.image.load("images/Basic_forest_resized_1296x786.png")
bg_2 = pygame.image.load("images/forest_bg_1296x768.png")
bg_3 = pygame.image.load("images/snow_forest_1296x768.png")
bg_4 = pygame.image.load("images/desert.png")
bg_5 = pygame.image.load("images/castle_right_gate_1296x768.png")
portal = pygame.image.load("images/portal.xcf")
portal_1 = pygame.image.load("images/portal_1.xcf")
portal_2 = pygame.image.load("images/portal_2.gif")
portal_3 = pygame.image.load("images/portal_3.png")
death = pygame.image.load("images/death-small.gif")
heart = pygame.image.load("images/heart.xcf")
potion_blue = pygame.image.load("images/potion_blue.xcf")
potion_red = pygame.image.load("images/potion_red.xcf")
potion_green = pygame.image.load("images/potion_green.xcf")
Boss = pygame.image.load("images/Boss.xcf")
Boss_red = pygame.image.load("images/red_boss.xcf")
shield = pygame.image.load("images/shield.xcf")
shield_icon = pygame.image.load("images/shield_icon.xcf")
Boss_3 = pygame.image.load("images/boss_3.xcf")
boss_4_frames = [
    pygame.image.load("images/boss_4(1).xcf"),
    pygame.image.load("images/boss_4(2).xcf")
]
boss_5 = pygame.image.load("images/boss_5.xcf")
shaman_boss = pygame.image.load("images/shaman_boss.xcf")
boss_7 = pygame.image.load("images/boss_7.xcf")
boss_8 = pygame.image.load("images/boss_8.xcf")
fireball_img = pygame.image.load("images/fireball.xcf")
boss_9 = pygame.image.load("images/boss_9.xcf")
ice_chunk_img = pygame.image.load("images/ice_chunk.xcf")
boss_10 = pygame.image.load("images/Ice_qween_boss_10.xcf")
mummy_king_image = pygame.image.load("images/mummy_king_boss_13.xcf").convert_alpha()
sand_hand_image = pygame.image.load("images/sand_hand.xcf").convert_alpha()
icicle_img = pygame.image.load("images/icicle.xcf")
settings = pygame.image.load("images/settings_button1.xcf")
menu = pygame.image.load("images/green_lobby_background_1296x768.png")
button = pygame.image.load("images/button.xcf")
Jump_icon = pygame.image.load("images/jump_boost.xcf")
m16 = pygame.image.load("images/m16.xcf")
bullet = pygame.image.load("images/bullet.xcf")
hero_ultra_right = pygame.image.load("images/hero_ultra.xcf")
hero_ultra_left = pygame.transform.flip(hero_ultra_right, True, False)

warrior_img_right = pygame.image.load("images/warrior.xcf")
warrior_img_left = pygame.transform.flip(warrior_img_right, True, False)

voodoo_img_right = pygame.image.load("images/voodoo.xcf")
voodoo_img_left = pygame.transform.flip(voodoo_img_right, True, False)

snowman_img_right = pygame.image.load("images/snowman.xcf")
snowman_img_left = pygame.transform.flip(snowman_img_right, True, False)

yeti_img_right = pygame.image.load("images/Yeti.xcf")
yeti_img_left = pygame.transform.flip(yeti_img_right, True, False)

mummy_img_left = pygame.image.load("images/mimmy.xcf")
mummy_img_right = pygame.transform.flip(mummy_img_left, True, False)

bittle_img_left = pygame.image.load("images/bittle.xcf")
bittle_img_right = pygame.transform.flip(bittle_img_left, True, False)

rider_img_left = pygame.image.load("images/rider.xcf")
rider_img_right = pygame.transform.flip(rider_img_left, True, False)

knight_img_left = pygame.image.load("images/knight.xcf")
knight_img_right = pygame.transform.flip(knight_img_left, True, False)

skin_button = pygame.image.load("images/skins_button.xcf")

bg_x = 0
icon = pygame.image.load("images/icon.png")

labal_lose = labal_font.render("Game Over", False, (200, 200, 200))
bg_lose = pygame.image.load("images/bd_lose.jpeg")
skin_menu_bg = pygame.image.load("images/green_hex_skin_background_1296x768.png")

# Загрузка и повороты героя и скины
hero_img_right = pygame.image.load("images/hero.png")
hero_img_left = pygame.transform.flip(hero_img_right, True, False)
hero = hero_img_right  # начальное положение
hero_img_right_m16 = pygame.image.load("images/hero_m16.xcf")
hero_img_left_m16 = pygame.transform.flip(hero_img_right_m16, True, False)
default_george = pygame.image.load("images/hero.png")
beach_george = pygame.image.load("images/beach_george.xcf")
gentelman_george = pygame.image.load("images/gentleman_george.xcf")
king_george = pygame.image.load("images/king_george.xcf")
pegion = pygame.image.load("images/голубь.xcf")
austronaft_1 = pygame.image.load("images/austronaft_1.xcf")
# Загрузка и повороты динозавра
dino_img_left = pygame.image.load("images/dinosaurs.gif")
dino_img_right = pygame.transform.flip(dino_img_left, True, False)
stone = pygame.image.load("images/stone1.png")

# Вместо загрузки из файла создаём прозрачный чёрный фон
pause_overlay_img = pygame.Surface((1296, 768))
pause_overlay_img.set_alpha(1)  # Прозрачность (0 - полностью прозрачный, 255 - полностью непрозрачный)
pause_overlay_img.fill((0, 0, 0))  # Чёрный цвет
pause_continue_img = pygame.image.load("images/button_continue.xcf").convert_alpha()
pause_settings_img = pygame.image.load("images/button_settings.xcf").convert_alpha()
pause_back_img = pygame.image.load("images/button_Back to Menu.xcf").convert_alpha()

pause_continue_rect = pause_continue_img.get_rect(center=(648, 330))
pause_settings_rect = pause_settings_img.get_rect(center=(648, 430))
pause_back_rect = pause_back_img.get_rect(center=(648, 530))


# кнопки
skin_button_rect = pygame.Rect(500, 600, 300, 60)
back_from_skins_rect = pygame.Rect(50, 680, 150, 50)
skin1_rect = pygame.Rect(200, 250, 100, 100)
skin2_rect = pygame.Rect(500, 250, 100, 100)
skin3_rect = pygame.Rect(800, 250, 100, 100)
selected_skin = "default"  # текущий выбранный скин
in_skin_menu = False  # активировано ли меню скинов

class SafeList(list):
    def pop(self, i=-1):
        if not self:
            return None
        # поддержим отрицательные индексы и обычные
        if -len(self) <= i < len(self):
            return super().pop(i)
        return None

stone_list = SafeList()
stone_speed = 15
max_stones = 1

ultra_active = False
ultra_start_time = 0

clock = pygame.time.Clock()

hero_direction = "right"

hero_speed = 2
hero_life = 3


hero_height = 64
ground_y = 690
hero_y = ground_y - hero_height

is_jump = False         # активен ли прыжок
jump_count = 10       # счётчик прыжка
jump_boost = 1.0


dino_list = []
dino_speed =12

dino_kills = 0
has_m16 = False

pause = False

bullet_speed = 10
bullet_count = 1

dino_spawn_rate = 1.0  # в секундах
dino_timer = 0  # таймер спавна

hero_x = 200



dino_spawn_delay = 70

in_settings_menu = False
button_rect = button.get_rect(topleft=(550, 500))  # кнопка "Назад"

power_value = 0
max_power = 100


shield_hits = 0
shield_active = False
shield_timer = 0
shield_duration = 1000

potion_blue_timer = 0
potion_blue_spawn_delay = 800
potion_blue_active = False
potion_blue_rect = potion_blue.get_rect(topleft=(-100, -100))

potion_red_active = False
potion_red_timer = 0
potion_red_spawn_delay = 600
potion_red_rect = potion_blue.get_rect(topleft=(-100, -100))

potion_green_active = False
potion_green_timer = 0
potion_green_spawn_delay = 900
potion_green_effect_active = False
potion_green_effect_time = 0
potion_green_rect = potion_green.get_rect(topleft=(-100, -100))

boss_4_active = False
boss_4_life = 60
boss_4_speed = 2
boss_4_rect = boss_4_frames[0].get_rect(topleft=(1296, 530))
boss_4_anim_index = 0
boss_4_anim_timer = 0
boss_4_anim_speed = 10  # чем меньше, тем быстрее переключение кадров

portal_active = False
portal_entered = False
portal_rect = portal.get_rect(topleft=(-100, -100))  # изначально вне экрана

portal_1_active = False
portal_1_entered = False
portal_1_rect = portal.get_rect(topleft=(-100, -100))  # изначально вне экрана

portal_2_active = False
portal_2_entered = False
portal_2_rect = portal.get_rect(topleft=(-100,-100))

portal_3_active = False
portal_3_entered = False
portal_3_rect = portal.get_rect(topleft=(-100,-100))

boss_red_active = False
boss_red_life = 30
boss_red_speed = 3
boss_red_rect = Boss.get_rect(topleft=(1296, 680))

boss_3_active = False
boss_3_life = 45
boss_3_speed = 2
boss_3_rect = Boss.get_rect(topleft=(1296, 680))


boss_5_active = False
boss_5_life = 60
boss_5_speed = 2
boss_5_rect = Boss.get_rect(topleft=(1296, 680))

shaman_boss_active = False
shaman_boss_life = 40
shaman_boss_speed = 1
shaman_boss_rect = boss_5.get_rect(topleft=(1296, 500))  # или другое изображение
fireballs = []  # список снарядов
fireball_timer = 0
fireball_delay = 70  # чем меньше — тем чаще стреляет


boss_active = False
boss_life = 15
boss_speed = 5
boss_rect = Boss.get_rect(topleft=(1296, 680))  # появляется с правого края

boss_7_active = False
boss_7_life = 70
boss_7_speed = 2
boss_7_rect = Boss.get_rect(topleft=(1296, 680))  # появляется с правого края

boss_8_active = False
boss_8_life = 80
boss_8_speed = 1
boss_8_rect = boss_8.get_rect(topleft=(1296, 680))

boss_9_active = False
boss_9_life = 60
boss_9_speed = 0.7
boss_9_rect = boss_9.get_rect(topleft=(1296, 500))

boss_10_active = False
boss_10_life = 50
boss_10_speed = 1.5
boss_10_rect = boss_5.get_rect(topleft=(1296, 500))  # или другое изображение
icicle = []
icicle_list = []

# список снарядов
icicle_timer = 0
icicle_delay = 81  # чем меньше — тем чаще стреляет

ice_chunks = []  # список глыб
ice_chunk_timer = 0
ice_chunk_delay = 90  # каждые 90 тиков



sand_djinn = pygame.image.load("images/djinn_boss_11.xcf").convert_alpha()
boss_11_active = False
boss_11_life = 85
boss_11_speed = 1.4
boss_11_rect = sand_djinn.get_rect(topleft=(1296, 520))

tornado_img = pygame.image.load("images/sand_tornado.xcf").convert_alpha()
tornadoes = []
tornado_timer = 0
tornado_delay = 90

djinn_burrow_timer = 0
djinn_burrow_cd = 300
djinn_burrowed = False
djinn_burrow_time = 0
djinn_burrow_duration = 55

scorpion_emperor = pygame.image.load("images/scorpion_emperor_boss_12.xcf").convert_alpha()
boss_12_active = False
boss_12_life = 100
boss_12_speed = 1.2
boss_12_rect = scorpion_emperor.get_rect(topleft=(1296, 560))

venom_img = pygame.image.load("images/venom.xcf").convert_alpha()
venoms = []
venom_timer = 0
venom_delay = 65

mini_scorpion_img = pygame.image.load("images/mini_scorpion_img.xcf").convert_alpha()
mini_scorpions = []
summon_timer = 0
summon_delay = 60

phase2 = False



# Царь-Мумия
mummy_king_active = False
mummy_king_life = 60
mummy_king_speed = 1
mummy_king_timer = 0
mummy_king_rect = pygame.Rect(1296, 430, 120, 120)  # размеры под спрайт
sand_hands = []
sand_hand_delay = 90
sand_hand_timer = 0
sand_hands = []


warrior_list = []
warrior_speed = 5
warrior_spawn_rate = 2.5
warrior_timer = 0


voodoo_list = []
voodoo_speed = 3
voodoo_spawn_rate = 4.0
voodoo_timer = 0

snowman_list = []
snowman_speed = 3
snowman_spawn_rate = 3
snowman_timer = 0

yeti_list = []
yeti_speed = 2.5
yeti_spawn_rate = 4.5
yeti_timer = 0

bittle_list = []
bittle_speed = 4.5
bittle_spawn_rate = 3
bittle_timer = 0

mummy_list = []
mummy_speed = 3
mummy_spawn_rate = 5
mummy_timer = 0

knight_list = []
knight_speed = 3
knight_spawn_rate = 3.2
knight_timer = 0

rider_list = []
rider_speed = 5
rider_spawn_rate = 2.5
rider_timer = 0

# --- Переменные для меню паузы ---
in_pause_menu = False
pause_continue_rect = pygame.Rect(500, 300, 300, 60)
pause_settings_rect = pygame.Rect(500, 400, 300, 60)
pause_back_rect = pygame.Rect(500, 500, 300, 60)




skin_dict = {
    "default": pygame.image.load("images/hero.png"),
    "beach": pygame.image.load("images/beach_george.xcf"),
    "gentleman": pygame.image.load("images/gentleman_george.xcf"),
    "king": pygame.image.load("images/king_george.xcf"),
    "pegion": pygame.image.load("images/голубь.xcf"),
    "austranaft 1": pygame.image.load("images/austronaft_1.xcf")
}


def draw_pause_menu():
    # Всегда заново заполняем фон игры, чтобы прозрачность не накапливалась
    if portal_3_entered:
        screen.blit(bg_5, (bg_x, 0))
    elif portal_2_entered:
        screen.blit(bg_4, (bg_x, 0))
    elif portal_1_entered:
        screen.blit(bg_3, (bg_x, 0))
    elif portal_entered:
        screen.blit(bg_2, (bg_x, 0))
    else:
        screen.blit(bg, (bg_x, 0))

    # Накладываем полупрозрачный чёрный фон
    pause_overlay_img.set_alpha(90)  # 0=полностью прозрачный, 255=непрозрачный
    screen.blit(pause_overlay_img, (0, 0))

    # Кнопки паузы
    screen.blit(pause_continue_img, pause_continue_rect)
    screen.blit(pause_settings_img, pause_settings_rect)
    screen.blit(pause_back_img, pause_back_rect)

    # (по желанию) текст "PAUSE"
    screen.blit(pause_text, (600, 200))  # можешь подвинуть куда удобно

def reset_game():
    global player_rect, hero_life, score, boss_1_active, enemy_list, stone_list
    global portal_entered, portal_1_entered, portal_2_entered, portal_3_entered, portal_active, portal_1_active, portal_2_active, portal_3_active
    global boss, boss_1_active, boss_2_active, boss_3_active, boss_4_active, boss_5_active
    global boss_6_active, boss_7_active, boss_8_active, boss_9_active, boss_10_active
    global boss_11_active, boss_12_active, boss_13_active
    global boss_fight, rider_list, knight_list, hand_list
    global power_value, super_mode, power_bar_visible, hero_x
    global bg_lose, bg_2, bg_3, bg_4, bg_5
    global hero_img, hero_rect, shield_active


    # Сброс позиции и очков
    shield_active = False
    hero_rect.topleft = (100, 500)
    hero_life = 5
    score = 0
    hero_x = 200


    # Сброс врагов и снарядов
    dino_list.clear()
    warrior_list.clear()
    voodoo_list.clear()
    snowman_list.clear()
    yeti_list.clear()
    bittle_list.clear()
    mummy_list.clear()
    stone_list.clear()
    rider_list.clear()
    knight_list.clear()


    # Сброс порталов и боссов
    portal_active = False
    portal_1_active = False
    portal_2_active = False
    portal_3_active = False

    portal_entered = False
    portal_1_entered = False
    portal_2_entered = False
    portal_3_entered = False

    boss_1_active = False
    boss_2_active = False
    boss_3_active = False
    boss_4_active = False
    boss_5_active = False
    boss_6_active = False
    boss_7_active = False
    boss_8_active = False
    boss_9_active = False
    boss_10_active = False
    boss_11_active = False
    boss_12_active = False
    boss_13_active = False

    boss_fight = False

    # Сброс супер-режима
    power_value = 0
    super_mode = False
    power_bar_visible = False





paused = False
pause_text = labal_font.render("PAUSE", True, (255, 255, 255))

start_button_rect = button.get_rect(center=(648, 500))  # Кнопка по центру экрана
game_started = False

menu = pygame.image.load("images/green_lobby_background_1296x768.png")



# === Главное меню ===
# === Список скинов и имён
skins = [default_george, beach_george, gentelman_george, king_george,pegion, austronaft_1]
skin_names = ["default", "beach", "gentelman", "king","pegion", "austronaft 1"]

# === Позиции 4-х сот
skin_positions = [
    (79, 32),
    (301, 32),
    (523, 32),
    (745, 32),
    (967, 32),
    (1189,35)
]
skin_rects = [pygame.Rect(x, y, 64, 64) for x, y in skin_positions]

# === Кнопка "Назад"
back_from_skins_rect = pygame.Rect(50, 700, 150, 40)

# === Скин по умолчанию
selected_skin = "default"
game_started = False  # ← ключ

hero_img = skin_dict[selected_skin]
hero_rect = hero_img.get_rect(topleft=(hero_x, 500))

# === Меню до старта игры
while not game_started:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            game_started = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not in_skin_menu:
                if start_button_rect.collidepoint(event.pos):
                    game_started = True
                elif skin_button_rect.collidepoint(event.pos):
                    in_skin_menu = True
            else:
                for i, rect in enumerate(skin_rects):
                    if rect.collidepoint(event.pos):
                        selected_skin = skin_names[i]
                if back_from_skins_rect.collidepoint(event.pos):
                    in_skin_menu = False

    # === Отрисовка меню
    if in_skin_menu:
        screen.blit(skin_menu_bg, (0, 0))

        for i, rect in enumerate(skin_rects):
            screen.blit(skins[i], rect)

            # Название скина (над скином)
            name_surface = labal_font.render(skin_names[i].capitalize(), True, (220, 220, 220))
            name_x = rect.centerx - name_surface.get_width() // 2
            name_y = rect.top - 20
            screen.blit(name_surface, (name_x, name_y))

            # Подпись Selected / Select (под скином)
            label = "Selected" if selected_skin == skin_names[i] else "Select"
            label_color = (255, 255, 0) if label == "Selected" else (200, 200, 200)
            label_surface = labal_font.render(label, True, label_color)
            label_x = rect.centerx - label_surface.get_width() // 2
            label_y = rect.bottom + 5
            screen.blit(label_surface, (label_x, label_y))


    else:
        screen.blit(menu, (0, 0))
        screen.blit(button, start_button_rect)
        pygame.draw.rect(screen, (100, 200, 100), skin_button_rect)
        screen.blit(labal_font.render("Skins", True, (0, 0, 0)), (skin_button_rect.x + 90, skin_button_rect.y + 10))

    pygame.display.update()


# === Применение выбранного скина ===
if selected_skin == "beach":
    hero_img_right = beach_george
elif selected_skin == "gentelman":
    hero_img_right = gentelman_george
elif selected_skin == "king":
    hero_img_right = king_george
elif selected_skin == "pegion":
    hero_img_right = pegion
elif selected_skin == "austronaft 1":
    hero_img_right = austronaft_1
else:
    hero_img_right = pygame.image.load("images/hero.png")  # стандартный скин

hero_img_left = pygame.transform.flip(hero_img_right, True, False)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # === Главное меню ===
        if not game_started:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not in_skin_menu:
                    if start_button_rect.collidepoint(event.pos):
                        reset_game()
                        game_started = True
                    elif skin_button_rect.collidepoint(event.pos):
                        in_skin_menu = True
                else:
                    for i, rect in enumerate(skin_rects):
                        if rect.collidepoint(event.pos):
                            selected_skin = skin_names[i]
                    if back_from_skins_rect.collidepoint(event.pos):
                        in_skin_menu = False

        # === Меню паузы ===
        elif in_pause_menu:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pause_continue_rect.collidepoint(event.pos):
                    in_pause_menu = False
                elif pause_settings_rect.collidepoint(event.pos):
                    in_settings_menu = True
                elif pause_back_rect.collidepoint(event.pos):
                    in_pause_menu = False
                    game_started = False
                    reset_game()

        # === Игра ===
        elif game_started:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    in_pause_menu = not in_pause_menu
                elif event.key == pygame.K_u:
                    if power_value == max_power and not ultra_active:
                        ultra_active = True
                        ultra_start_time = pygame.time.get_ticks()
                        power_value = 0
                        hero_life = 10

    # === Отрисовка ===
    if not game_started:
        if in_skin_menu:
            screen.blit(skin_menu_bg, (0, 0))
            for i, rect in enumerate(skin_rects):
                screen.blit(skins[i], rect)
                name_surface = labal_font.render(skin_names[i].capitalize(), True, (220, 220, 220))
                name_x = rect.centerx - name_surface.get_width() // 2
                name_y = rect.top - 20
                screen.blit(name_surface, (name_x, name_y))

                label = "Selected" if selected_skin == skin_names[i] else "Select"
                label_color = (255, 255, 0) if label == "Selected" else (200, 200, 200)
                label_surface = labal_font.render(label, True, label_color)
                label_x = rect.centerx - label_surface.get_width() // 2
                label_y = rect.bottom + 5
                screen.blit(label_surface, (label_x, label_y))
        else:
            screen.blit(menu, (0, 0))
            screen.blit(button, start_button_rect)
            pygame.draw.rect(screen, (100, 200, 100), skin_button_rect)
            screen.blit(labal_font.render("Skins", True, (0, 0, 0)), (skin_button_rect.x + 90, skin_button_rect.y + 10))
        pygame.display.update()
        continue

    elif in_pause_menu:
        draw_pause_menu()
        pygame.display.update()
        continue

    if not paused:

        killed_dinos = labal_font.render(str(score), False, (155, 155, 155))
        labal_life = labal_font.render(str(hero_life), False, (155, 155, 155))
        keys = pygame.key.get_pressed()

        keys = pygame.key.get_pressed()



        if ultra_active:
            if hero_direction == "right":
                hero = hero_ultra_right
            else:
                hero = hero_ultra_left


        else:
            # Возвращаем обычного героя (в зависимости от направления)
            if keys[pygame.K_d]:
                hero = hero_img_right
            elif keys[pygame.K_a]:
                hero = hero_img_left

        # Вставить перед screeen.blit(hero, (hero_x, hero_y))


        # Фон и UI
        if portal_3_entered:
            screen.blit(bg_5, (bg_x, 0))
            screen.blit(bg_5, (bg_x + 1296, 0))
            screen.blit(bg_5, (bg_x - 1296, 0))
        elif portal_2_entered:
            screen.blit(bg_4, (bg_x, 0))
            screen.blit(bg_4, (bg_x + 1296, 0))
            screen.blit(bg_4, (bg_x - 1296, 0))
        elif portal_1_entered:
            screen.blit(bg_3, (bg_x, 0))
            screen.blit(bg_3, (bg_x + 1296, 0))
            screen.blit(bg_3, (bg_x - 1296, 0))
        elif portal_entered:
            screen.blit(bg_2, (bg_x, 0))
            screen.blit(bg_2, (bg_x + 1296, 0))
            screen.blit(bg_2, (bg_x - 1296, 0))
        else:
            screen.blit(bg, (bg_x, 0))
            screen.blit(bg, (bg_x + 1296, 0))
            screen.blit(bg, (bg_x - 1296, 0))

        screen.blit(labal_life, (100, 40))
        screen.blit(heart, (10, 10))
        screen.blit(killed_dinos, (220, 40))
        screen.blit(death, (150, 30))
        screen.blit(settings, (1200, 30))

        hero_rect = hero.get_rect(topleft=(hero_x, hero_y))
        screen.blit(hero, (hero_x, hero_y))

        # Отрисовка портала
        if portal_active:
            screen.blit(portal, portal_rect)
            if hero_rect.colliderect(portal_rect):
                portal_entered = True
                portal_active = False
                portal_rect.topleft = (-100, -100)  # убираем портал

        if portal_1_active:
            screen.blit(portal_1, portal_1_rect)
            if hero_rect.colliderect(portal_1_rect):
                portal_1_entered = True
                portal_1_active = False
                portal_1_rect.topleft = (-100, -100)

        if portal_2_active:
            screen.blit(portal_2, portal_2_rect)
            if hero_rect.colliderect(portal_2_rect):
                portal_2_entered = True
                portal_2_active = False
                portal_2_rect.topleft = (-100, -100)

        if portal_3_active:
            screen.blit(portal_3, portal_3_rect)
            if hero_rect.colliderect(portal_3_rect):
                portal_3_entered = True
                portal_3_active = False
                portal_3_rect.topleft = (-100, -100)


        # ШКАЛА СИЛЫ
        power_bar_x = 450
        power_bar_y = 20
        power_bar_width = 300
        power_bar_height = 25
        fill_width = int((power_value / max_power) * power_bar_width)

        # рамка
        pygame.draw.rect(screen, (255, 255, 255),
                         (power_bar_x - 2, power_bar_y - 2, power_bar_width + 4, power_bar_height + 4), 2)

        # заполнение
        pygame.draw.rect(screen, (255, 165, 0), (power_bar_x, power_bar_y, fill_width, power_bar_height))

        # текст: сколько осталось до 100
        power_remaining = max_power - power_value
        power_text = labal_font.render(f"{power_value} / 100", False, (255, 255, 255))
        screen.blit(power_text, (power_bar_x + power_bar_width + 10, power_bar_y - 3))



        # Бросок камня
        if keys[pygame.K_e] and len(stone_list) < max_stones:
            direction = hero_direction
            stone_rect = stone.get_rect(topleft=(hero_x + 20, hero_y + 10))
            stone_list.append({'rect': stone_rect, 'dir': direction})

        # Обработка камней
        for i in range(len(stone_list) - 1, -1, -1):
            stone_data = stone_list[i]
            rect = stone_data['rect']
            direction = stone_data['dir']

            # Движение
            if direction == "right":
                rect.x += stone_speed
                if rect.x > 1296:
                    stone_list.pop(i)
                    continue
            else:
                rect.x -= stone_speed
                if rect.x < 0:
                    stone_list.pop(i)
                    continue

            # Отрисовка
            screen.blit(stone, rect)

            # Столкновение с динозаврами
            for j in range(len(dino_list) - 1, -1, -1):
                dino_rect = dino_list[j]['rect']
                if rect.colliderect(dino_rect):
                    stone_list.pop(i)
                    dino_list.pop(j)
                    score += 1
                    if power_value < max_power:
                        power_value = min(max_power, power_value + 1)
                    break



        # Урон по воинам и вуду
        for i in range(len(stone_list) - 1, -1, -1):
            stone_data = stone_list[i]
            rect = stone_data['rect']

            # Воины
            for j in range(len(warrior_list) - 1, -1, -1):
                warrior = warrior_list[j]
                warrior_rect = warrior[0]
                if rect.colliderect(warrior_rect):
                    warrior[1] -= 1
                    stone_list.pop(i)
                    if warrior[1] <= 0:
                        warrior_list.pop(j)
                        score += 1
                    break

            # Вуду
            for j in range(len(voodoo_list) - 1, -1, -1):
                voodoo = voodoo_list[j]
                voodoo_rect = voodoo[0]
                if rect.colliderect(voodoo_rect):
                    voodoo[1] -= 1
                    stone_list.pop(i)
                    if voodoo[1] <= 0:
                        voodoo_list.pop(j)
                        score += 1
                    break

        for i in range(len(stone_list) - 1, -1, -1):
            stone_data = stone_list[i]
            rect = stone_data['rect']

            # снеговики
            for j in range(len(snowman_list) - 1, -1, -1):
                snowman = snowman_list[j]
                snowman_rect = snowman[0]
                if rect.colliderect(snowman_rect):
                    snowman[1] -= 1
                    stone_list.pop(i)
                    if snowman[1] <= 0:
                        snowman_list.pop(j)
                        score += 1
                    break

            # ети
            for j in range(len(yeti_list) - 1, -1, -1):
                yeti = yeti_list[j]
                yeti_rect = yeti[0]
                if rect.colliderect(yeti_rect):
                    yeti[1] -= 1
                    stone_list.pop(i)
                    if yeti[1] <= 0:
                        yeti_list.pop(j)
                        score += 1
                    break

            # жуки
            for k in range(len(bittle_list) - 1, -1, -1):
                bittle = bittle_list[k]
                bittle_rect = bittle[0]
                if rect.colliderect(bittle_rect):
                    bittle[1] -= 1
                    stone_list.pop(i)
                    if bittle[1] <= 0:
                        bittle_list.pop(k)
                        score += 1
                    break

        #    мумии
            for m in range(len(mummy_list) - 1, -1, -1):
                mummy = mummy_list[m]
                mummy_rect = mummy[0]
                if rect.colliderect(mummy_rect):
                    mummy[1] -= 1
                    stone_list.pop(i)
                    if mummy[1] <= 0:
                        mummy_list.pop(m)
                        score += 1
                    break

        for i in range(len(stone_list) - 1, -1, -1):
            stone_data = stone_list[i]
            rect = stone_data['rect']

            # рыцари
            for k in range(len(knight_list) - 1, -1, -1):
                knight = knight_list[k]
                knight_rect = knight[0]
                if rect.colliderect(knight_rect):
                    knight[1] -= 1
                    stone_list.pop(i)
                    if knight[1] <= 0:
                        knight_list.pop(k)
                        score += 1
                    break

                    # рыцари
            for r in range(len(rider_list) - 1, -1, -1):
                rider = rider_list[r]
                rider_rect = rider[0]
                if rect.colliderect(rider_rect):
                    rider[1] -= 1
                    stone_list.pop(i)
                    if rider[1] <= 0:
                        rider_list.pop(r)
                        score += 1
                    break


        # первый босс
        if score == 50 and not boss_active:
            boss_active = True
            boss_rect.topleft = (1296, 490)  # правая граница экрана

        if boss_active and hero_life > 0:
            screen.blit(Boss, boss_rect)
            boss_rect.x -= boss_speed

            max_health = 20
            health_bar_width = 200
            health_bar_height = 20
            health_ratio = boss_life / max_health
            bar_x = boss_rect.x + 50
            bar_y = boss_rect.y - 30

            pygame.draw.rect(screen, (0, 0, 0), (bar_x - 2, bar_y - 2, health_bar_width + 4, health_bar_height + 4))  # рамка
            pygame.draw.rect(screen, (200, 0, 0), (bar_x, bar_y, int(health_bar_width * health_ratio), health_bar_height))  # красная полоса


            if boss_rect.colliderect(hero_rect):
                hero_life -= 2


            for i in range(len(stone_list) - 1, -1, -1):
                stone_data = stone_list[i]
                rect = stone_data['rect']
                if rect.colliderect(boss_rect):
                    stone_list.pop(i)
                    boss_life -= 1
                    break

            if boss_life <= 0:
                boss_active = False

            if power_value < max_power:
                power_value = min(max_power, power_value + 33)

        # второй босс
        if score >= 100 and not boss_red_active:
            boss_red_active = True
            boss_red_rect.topleft = (1296, 500)

        if boss_red_active and hero_life > 0:
            screen.blit(Boss_red, boss_red_rect)
            boss_red_rect.x -= boss_red_speed

            max_health_red = 35
            health_bar_width_red = 200
            heath_bar_height_red = 20
            heath_ratio_red = boss_red_life / max_health_red
            bar_red_x = boss_red_rect.x + 50
            bar_red_y = boss_red_rect.y - 30

            pygame.draw.rect(screen, (0, 0, 0), (bar_red_x - 2, bar_red_y - 2, health_bar_width_red + 4, heath_bar_height_red + 4))  # рамка
            pygame.draw.rect(screen, (200, 0, 0), (bar_red_x, bar_red_y, int(health_bar_width_red * heath_ratio_red), heath_bar_height_red))

            if boss_red_rect.colliderect(hero_rect):
                if shield_active:
                    shield_active = False
                else:
                    hero_life -= 2


            for i in range(len(stone_list) - 1, -1, -1):
                stone_data = stone_list[i]
                rect = stone_data['rect']
                if rect.colliderect(boss_red_rect):
                    stone_list.pop(i)
                    boss_red_life -= 1
                    break

            if boss_red_life <= 0:
                boss_red_active = False

            if power_value < max_power:
                power_value = min(max_power, power_value + 33)

        #третий босс
        if score >= 150 and not boss_3_active:
            boss_3_active = True
            boss_3_rect.topleft = (1296, 525)  # правая граница экрана

        if boss_3_active and hero_life > 0:
            screen.blit(Boss_3, boss_3_rect)
            boss_3_rect.x -= boss_3_speed

            # Полоса здоровья
            max_health = 45
            health_bar_width = 200
            health_bar_height = 20
            health_ratio = boss_3_life / max_health
            bar_x = boss_3_rect.x + 50
            bar_y = boss_3_rect.y - 30

            pygame.draw.rect(screen, (0, 0, 0), (bar_x - 2, bar_y - 2, health_bar_width + 4, health_bar_height + 4))
            pygame.draw.rect(screen, (200, 0, 0), (bar_x, bar_y, int(health_bar_width * health_ratio), health_bar_height))

            # Столкновение героя с боссом
            if boss_3_rect.colliderect(hero_rect):
                if shield_active:
                    shield_active = False
                else:
                    hero_life -= 2

            # Попадания камней
            for i in range(len(stone_list) - 1, -1, -1):
                stone_data = stone_list[i]
                rect = stone_data['rect']
                if rect.colliderect(boss_3_rect):
                    stone_list.pop(i)
                    boss_3_life -= 1
                    break

            # Проверка смерти босса
            if boss_3_life <= 0:
                boss_3_active = False

            if power_value < max_power:
                power_value = min(max_power, power_value + 33)

        # четвёртый босс
        if score >= 200 and not boss_4_active:
            boss_4_active = True
            boss_4_rect.topleft = (1296, 530)

        if boss_4_active and hero_life > 0:
            # Анимация
            boss_4_anim_timer += 1
            if boss_4_anim_timer >= boss_4_anim_speed:
                boss_4_anim_index = (boss_4_anim_index + 1) % len(boss_4_frames)
                boss_4_anim_timer = 0
            current_boss_4_image = boss_4_frames[boss_4_anim_index]
            screen.blit(current_boss_4_image, boss_4_rect)

            boss_4_rect.x -= boss_4_speed

            # Полоса здоровья
            max_health = 60
            health_bar_width = 200
            health_bar_height = 20
            health_ratio = boss_4_life / max_health
            bar_x = boss_4_rect.x + 50
            bar_y = boss_4_rect.y - 30

            pygame.draw.rect(screen, (0, 0, 0), (bar_x - 2, bar_y - 2, health_bar_width + 4, health_bar_height + 4))
            pygame.draw.rect(screen, (200, 0, 0), (bar_x, bar_y, int(health_bar_width * health_ratio), health_bar_height))

            if boss_4_rect.colliderect(hero_rect):
                if shield_active:
                    shield_active = False
                else:
                    hero_life -= 2


            for i in range(len(stone_list) - 1, -1, -1):
                stone_data = stone_list[i]
                rect = stone_data['rect']
                if rect.colliderect(boss_4_rect):
                    stone_list.pop(i)
                    boss_4_life -= 1
                    break

            if boss_4_life <= 0:
                boss_4_active = False

            if power_value < max_power:
                power_value = min(max_power, power_value + 33)

    # Активация портала при 250 очках


        # Прыжок
        # Начало прыжка
        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
        else:
            if jump_count >= -10:
                movement = (jump_count ** 2) * 0.3 * jump_boost
                if jump_count > 0:
                    hero_y -= movement  # вверх
                else:
                    hero_y += movement  # вниз
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 10
                hero_y = ground_y - hero_height

        # Защита от выхода за верх экрана
        if hero_y < 0:
            hero_y = 0

        potion_red_timer +=1
        if potion_red_timer >= potion_red_spawn_delay and not potion_red_active:
            potion_x = ri(100, 1200)
            potion_y = 630
            potion_red_rect.topleft = (potion_x, potion_y)
            potion_red_active = True
            potion_red_timer = 0

        if potion_red_active:
            screen.blit(potion_red, potion_red_rect)
            if hero_rect.colliderect(potion_red_rect):
                if hero_life < 5:
                    hero_life += 1
                potion_red_active = False
                potion_red_rect.topleft = (-100, -100)

        potion_blue_timer += 1
        if potion_blue_timer >= potion_blue_spawn_delay and not potion_blue_active:
            potion_x = ri(100, 1200)
            potion_y = 630
            potion_blue_rect.topleft = (potion_x, potion_y)
            potion_blue_active = True
            potion_blue_timer = 0

        if potion_blue_active:
            screen.blit(potion_blue, potion_blue_rect)
            if hero_rect.colliderect(potion_blue_rect):
                shield_active = True
                shield_timer = 0
                potion_blue_active = False
                potion_blue_rect.topleft = (-100, -100)

        # Спавн зелёного зелья

        potion_green_timer += 1

        # Спавн зелёного зелья
        if potion_green_timer >= potion_green_spawn_delay and not potion_green_active:
            potion_x = ri(100, 1200)
            potion_y = 630
            potion_green_rect.topleft = (potion_x, potion_y)
            potion_green_active = True
            potion_green_timer = 0


        # Отрисовка и подбор зелёного зелья
        if potion_green_active:
            screen.blit(potion_green, potion_green_rect)
            if hero_rect.colliderect(potion_green_rect):
                potion_green_active = False
                potion_green_effect_active = True
                potion_green_effect_time = pygame.time.get_ticks()
                jump_boost = 1.8
                potion_green_rect.topleft = (-100, -100)

        # Обработка эффекта зелёного зелья (4 секунд)
        if potion_green_effect_active:
            if pygame.time.get_ticks() - potion_green_effect_time >= 1600:
                jump_boost = 1.0
                potion_green_effect_active = False

        if potion_green_effect_active:
            screen.blit(Jump_icon, (110, 110))

            if hero_rect.colliderect(potion_green_rect):
                jump_boost = 2.0
                potion_active = True
                potion_timer = pygame.time.get_ticks()  # текущий момент времени в мс
                potion_collected = True  # убираем зелье с экрана

        if score < 250:
            dino_timer += 1
            if dino_timer >= dino_spawn_delay:
                side = ri(0, 1)
                if side == 0:
                    dino_x = 0
                    direction = 'right'
                    img = dino_img_right
                else:
                    dino_x = 1296
                    direction = 'left'
                    img = dino_img_left

                dino_rect = img.get_rect(topleft=(dino_x, 640))
                dino_list.append({'rect': dino_rect, 'dir': direction, 'img': img})
                dino_timer = 0

        # Движение и отрисовка динозавров
        for dino_data in dino_list[:]:
            rect = dino_data['rect']
            direction = dino_data['dir']
            img = dino_data['img']

            screen.blit(img, rect)

            if direction == 'left':
                rect.x -= dino_speed
            else:
                rect.x += dino_speed

            if hero_rect.colliderect(rect):
                if shield_active:
                    shield_hits += 1
                    if shield_hits >= 5:
                        shield_active = False
                        shield_hits = 0
                else:
                    hero_life -= 1
                dino_list.remove(dino_data)

        if shield_active:
            shield_timer += 1
            screen.blit(shield_icon, (60, 100))
            if shield_timer >= shield_duration:
                shield_active = False
                shield_timer = 0

        if ultra_active:
            if pygame.time.get_ticks() - ultra_start_time >= 8000:
                ultra_active = False
                hero_life = min(hero_life, 5)

        if score >= 250 and not portal_active and not portal_entered:
            portal_active = True
            portal_rect.topleft = (1000, 550)  # координаты портала на экране

        # === Активация новых врагов при 250 очках ===
        if portal_entered and score < 450:
            dino_spawn_rate = 99999
            warrior_spawn = True
            voodoo_spawn = True
        else:
            warrior_spawn = False
            voodoo_spawn = False

        current_time = pygame.time.get_ticks() / 1000

        # === Спавн воинов ===
        if warrior_spawn and current_time - warrior_timer > warrior_spawn_rate:
            side = ri(0, 1)
            if side == 0:  # слева
                x = -warrior_img_left.get_width()
                direction = 'right'
                img = warrior_img_right
            else:  # справа
                x = 1300
                direction = 'left'
                img = warrior_img_left

            y = ground_y - warrior_img_left.get_height()
            rect = img.get_rect(topleft=(x, y))
            warrior_list.append([rect, 2, direction, img])  # rect, hp, dir, img
            warrior_timer = current_time

        # === Спавн вуду ===
        if voodoo_spawn and current_time - voodoo_timer > voodoo_spawn_rate:
            side = ri(0, 1)
            if side == 0:
                x = -voodoo_img_left.get_width()
                direction = 'right'
                img = voodoo_img_right
            else:
                x = 1300
                direction = 'left'
                img = voodoo_img_left

            y = ground_y - voodoo_img_left.get_height()
            rect = img.get_rect(topleft=(x, y))
            voodoo_list.append([rect, 3, direction, img])  # rect, hp, dir, img
            voodoo_timer = current_time

        # Движение воинов и вуду
        for warrior in warrior_list:
            if warrior[2] == 'left':
                warrior[0].x -= warrior_speed
            else:
                warrior[0].x += warrior_speed

        for voodoo in voodoo_list:
            if voodoo[2] == 'left':
                voodoo[0].x -= voodoo_speed
            else:
                voodoo[0].x += voodoo_speed

        # Отрисовка воинов с полоской HP
        for warrior in warrior_list:
            rect = warrior[0]
            hp = warrior[1]
            img = warrior[3]

            screen.blit(img, rect)

            bar_width = rect.width
            hp_ratio = hp / 2
            hp_bar_width = int(bar_width * hp_ratio)
            pygame.draw.rect(screen, (255, 0, 0), (rect.x, rect.y - 10, bar_width, 5))
            pygame.draw.rect(screen, (0, 255, 0), (rect.x, rect.y - 10, hp_bar_width, 5))

        # Отрисовка вуду

        for voodoo in voodoo_list:
            rect = voodoo[0]
            hp = voodoo[1]
            img = voodoo[3]

            screen.blit(img, rect)

            bar_width = rect.width
            hp_ratio = hp / 3
            hp_bar_width = int(bar_width * hp_ratio)
            pygame.draw.rect(screen, (255, 0, 0), (rect.x, rect.y - 10, bar_width, 5))
            pygame.draw.rect(screen, (0, 255, 0), (rect.x, rect.y - 10, hp_bar_width, 5))

        # Удаление вышедших за экран
        warrior_list = [w for w in warrior_list if -200 < w[0].x < 1400]
        voodoo_list = [v for v in voodoo_list if -200 < v[0].x < 1400]

        # Урон от воинов
        for warrior in warrior_list:
            if warrior[0].colliderect(hero_rect):
                if shield_active:
                    shield_hits += 1
                    if shield_hits >= 5:
                        shield_active = False
                        shield_hits = 0
                else:
                    hero_life -= 1
                warrior_list.remove(warrior)
                break

        # Урон от вуду
        for voodoo in voodoo_list:
            if voodoo[0].colliderect(hero_rect):
                if shield_active:
                    shield_hits += 1
                    if shield_hits >= 5:
                        shield_active = False
                        shield_hits = 0
                else:
                    hero_life -= 1
                voodoo_list.remove(voodoo)
                break


        # === БОСС 5 ===
        if score == 300 and not boss_5_active:
            boss_5_active = True
            boss_5_life = 60
            boss_5_rect.topleft = (1296, 455)

        if boss_5_active and hero_life > 0:
            screen.blit(boss_5, boss_5_rect)
            boss_5_rect.x -= boss_5_speed

            # Полоса здоровья
            max_health = 60
            health_bar_width = 200
            health_bar_height = 20
            health_ratio = boss_5_life / max_health
            bar_x = boss_5_rect.x + 50
            bar_y = boss_5_rect.y - 30

            pygame.draw.rect(screen, (0, 0, 0), (bar_x - 2, bar_y - 2, health_bar_width + 4, health_bar_height + 4))
            pygame.draw.rect(screen, (200, 0, 0), (bar_x, bar_y, int(health_bar_width * health_ratio), health_bar_height))

            if boss_5_rect.colliderect(hero_rect):
                if shield_active:
                    shield_active = False
                else:
                    hero_life -= 2

            for i in range(len(stone_list) - 1, -1, -1):
                stone_data = stone_list[i]
                rect = stone_data['rect']
                if rect.colliderect(boss_5_rect):
                    stone_list.pop(i)
                    boss_5_life -= 1
                    break

            if boss_5_life <= 0:
                boss_5_active = False

            if power_value < max_power:
                power_value = min(max_power, power_value + 33)

        # === БОСС 6: Шаман ===
        if score == 350 and not shaman_boss_active:
            shaman_boss_active = True
            shaman_boss_life = 35
            shaman_boss_rect.topleft = (1296, 430)
            fireballs.clear()

        if shaman_boss_active and hero_life > 0:
            screen.blit(shaman_boss, shaman_boss_rect)
            shaman_boss_rect.x -= shaman_boss_speed

            # Полоса HP
            max_health = 40
            health_bar_width = 200
            health_ratio = shaman_boss_life / max_health
            bar_x = shaman_boss_rect.x + 50
            bar_y = shaman_boss_rect.y - 30
            pygame.draw.rect(screen, (0, 0, 0), (bar_x - 2, bar_y - 2, health_bar_width + 4, 24))
            pygame.draw.rect(screen, (255, 50, 0), (bar_x, bar_y, int(health_bar_width * health_ratio), 20))

            # Столкновение с героем
            if shaman_boss_rect.colliderect(hero_rect):
                if shield_active:
                    shield_active = False
                else:
                    hero_life -= 2

            # Получение урона от камней
            for i in range(len(stone_list) - 1, -1, -1):
                stone_data = stone_list[i]
                rect = stone_data['rect']
                if rect.colliderect(shaman_boss_rect):
                    stone_list.pop(i)
                    shaman_boss_life -= 1
                    break

            # Стрельба огненными шарами
            fireball_timer += 1
            if fireball_timer >= fireball_delay:
                fireball_rect = fireball_img.get_rect(midleft=(shaman_boss_rect.x, shaman_boss_rect.centery))
                fireballs.append(fireball_rect)
                fireball_timer = 0

            # Обработка огненных шаров
            for fireball in fireballs[:]:
                fireball.x -= 8
                screen.blit(fireball_img, fireball)
                if fireball.colliderect(hero_rect):
                    if shield_active:
                        shield_active = False
                    else:
                        hero_life -= 1
                    fireballs.remove(fireball)
                elif fireball.x < -50:
                    fireballs.remove(fireball)

            # Смерть босса
            if shaman_boss_life <= 0:
                shaman_boss_active = False
                fireballs.clear()


        if score == 400 and not boss_7_active:
            boss_7_active = True
            boss_7_rect.topleft = (1296, 430)  # правая граница экрана
            boss_7_life = 75

        if boss_7_active and hero_life > 0:
            screen.blit(boss_7, boss_7_rect)
            boss_7_rect.x -= boss_7_speed

            max_health = 75
            health_bar_width = 200
            health_bar_height = 20
            health_ratio = boss_7_life / max_health
            bar_x = boss_7_rect.x + 50
            bar_y = boss_7_rect.y - 30

            pygame.draw.rect(screen, (0, 0, 0), (bar_x - 2, bar_y - 2, health_bar_width + 4, health_bar_height + 4))  # рамка
            pygame.draw.rect(screen, (200, 0, 0), (bar_x, bar_y, int(health_bar_width * health_ratio), health_bar_height))  # красная полоса


            if boss_7_rect.colliderect(hero_rect):
                hero_life -= 2


            for i in range(len(stone_list) - 1, -1, -1):
                stone_data = stone_list[i]
                rect = stone_data['rect']
                if rect.colliderect(boss_7_rect):
                    stone_list.pop(i)
                    boss_7_life -= 1
                    break

            if boss_7_life <= 0:
                boss_7_active = False

            if power_value < max_power:
                power_value = min(max_power, power_value + 33)

        if score >= 450 and not portal_1_active and not portal_1_entered:
            portal_1_active = True
            portal_1_rect.topleft = (1000, 550)  # координаты портала на экране

        if portal_1_entered  and score <= 650:
            dino_spawn_rate = 99999
            snowman_spawn = True
            yeti_spawn = True
        else:
            snowman_spawn = False
            yeti_spawn = False



        current_time = pygame.time.get_ticks() / 1000

        # === Спавн снеговиков ===
        if snowman_spawn and current_time - snowman_timer > snowman_spawn_rate:
            side = ri(0, 1)
            if side == 0:  # слева
                x = -snowman_img_left.get_width()
                direction = 'right'
                img = snowman_img_right
            else:  # справа
                x = 1300
                direction = 'left'
                img = snowman_img_left

            y = ground_y - snowman_img_left.get_height()
            rect = img.get_rect(topleft=(x, y))
            snowman_list.append([rect, 3, direction, img])  # rect, hp, dir, img
            snowman_timer = current_time

        # === Спавн ети ===
        if yeti_spawn and current_time - yeti_timer > yeti_spawn_rate:
            side = ri(0, 1)
            if side == 0:
                x = -yeti_img_left.get_width()
                direction = 'right'
                img = yeti_img_right
            else:
                x = 1300
                direction = 'left'
                img = yeti_img_left

            y = ground_y - yeti_img_left.get_height()
            rect = img.get_rect(topleft=(x, y))
            yeti_list.append([rect, 4, direction, img])  # rect, hp, dir, img
            yeti_timer = current_time

        # Движение снеговиков и ети
        for snowman in snowman_list:
            if snowman[2] == 'left':
                snowman[0].x -= snowman_speed
            else:
                snowman[0].x += snowman_speed

        for yeti in yeti_list:
            if yeti[2] == 'left':
                yeti[0].x -= yeti_speed
            else:
                yeti[0].x += yeti_speed

        # Отрисовка снеговиков с полоской HP
        for snowman in snowman_list:
            rect = snowman[0]
            hp = snowman[1]
            img = snowman[3]

            screen.blit(img, rect)

            bar_width = rect.width
            max_hp = 3
            hp_ratio = hp / max_hp
            hp_bar_width = int(bar_width * hp_ratio)
            pygame.draw.rect(screen, (255, 0, 0), (rect.x, rect.y - 10, bar_width, 5))
            pygame.draw.rect(screen, (0, 255, 0), (rect.x, rect.y - 10, hp_bar_width, 5))

        # Отрисовка ети

        for yeti in yeti_list:
            rect = yeti[0]
            hp = yeti[1]
            img = yeti[3]

            screen.blit(img, rect)

            bar_width = rect.width
            max_hp = 4
            hp_ratio = hp / max_hp
            hp_bar_width = int(bar_width * hp_ratio)
            pygame.draw.rect(screen, (255, 0, 0), (rect.x, rect.y - 10, bar_width, 5))
            pygame.draw.rect(screen, (0, 255, 0), (rect.x, rect.y - 10, hp_bar_width, 5))

        # Удаление вышедших за экран
        snowman_list = [s for s in snowman_list if -200 < s[0].x < 1400]
        yeti_list = [y for y in yeti_list if -200 < y[0].x < 1400]

        # Урон от снеговиков
        for snowman in snowman_list:
            if snowman[0].colliderect(hero_rect):
                if shield_active:
                    shield_hits += 1
                    if shield_hits >= 5:
                        shield_active = False
                        shield_hits = 0
                else:
                    hero_life -= 1
                snowman_list.remove(snowman)
                break

        # Урон от ети
        for yeti in yeti_list:
            if yeti[0].colliderect(hero_rect):
                if shield_active:
                    shield_hits += 1
                    if shield_hits >= 5:
                        shield_active = False
                        shield_hits = 0
                else:
                    hero_life -= 1
                yeti_list.remove(yeti)
                break

        if score == 500 and not boss_8_active:
            boss_8_active = True
            boss_8_rect.topleft = (1296, 490)  # правая граница экрана

        if boss_8_active and hero_life > 0:
            screen.blit(boss_8, boss_8_rect)
            boss_8_rect.x -= boss_8_speed

            max_health = 80
            health_bar_width = 200
            health_bar_height = 20
            health_ratio = boss_8_life / max_health
            bar_x = boss_8_rect.x + 50
            bar_y = boss_8_rect.y - 30

            pygame.draw.rect(screen, (0, 0, 0), (bar_x - 2, bar_y - 2, health_bar_width + 4, health_bar_height + 4))  # рамка
            pygame.draw.rect(screen, (200, 0, 0), (bar_x, bar_y, int(health_bar_width * health_ratio), health_bar_height))  # красная полоса


            if boss_8_rect.colliderect(hero_rect):
                hero_life -= 2


            for i in range(len(stone_list) - 1, -1, -1):
                stone_data = stone_list[i]
                rect = stone_data['rect']
                if rect.colliderect(boss_8_rect):
                    stone_list.pop(i)
                    boss_8_life -= 1
                    break

            if boss_8_life <= 0:
                boss_8_active = False

            if power_value < max_power:
                power_value = min(max_power, power_value + 33)

        if score == 550 and not boss_9_active:
            boss_9_active = True
            boss_9_life = 90
            boss_9_rect.topleft = (1296, 430)
            ice_chunks.clear()
        if boss_9_active and hero_life > 0:
            screen.blit(boss_9, boss_9_rect)
            boss_9_rect.x -= boss_9_speed

            # HP полоска
            max_health = 90
            health_bar_width = 200
            health_bar_height = 20
            health_ratio = boss_9_life / max_health
            bar_x = boss_9_rect.x + 50
            bar_y = boss_9_rect.y - 30
            pygame.draw.rect(screen, (0, 0, 0), (bar_x - 2, bar_y - 2, health_bar_width + 4, health_bar_height + 4))
            pygame.draw.rect(screen, (0, 200, 255),
                             (bar_x, bar_y, int(health_bar_width * health_ratio), health_bar_height))

            # Столкновение с героем
            if boss_9_rect.colliderect(hero_rect):
                if shield_active:
                    shield_active = False
                else:
                    hero_life -= 2

            # Урон от камней
            for i in range(len(stone_list) - 1, -1, -1):
                rect = stone_list[i]['rect']
                if rect.colliderect(boss_9_rect):
                    stone_list.pop(i)
                    boss_9_life -= 1
                    break

            # Смерть
            if boss_9_life <= 0:
                boss_9_active = False

            # === Бросание глыб ===
            ice_chunk_timer += 1
            if ice_chunk_timer >= ice_chunk_delay:
                ice_chunk_timer = 0
                chunk_x = boss_9_rect.centerx
                chunk_y = boss_9_rect.centery
                vx = -15  # горизонтальная скорость
                vy = -10  # начальная вертикальная
                ice_chunks.append({'x': chunk_x, 'y': chunk_y, 'vx': vx, 'vy': vy})

            gravity = 0.5

            for chunk in ice_chunks[:]:
                chunk['x'] += chunk['vx']
                chunk['vy'] += gravity
                chunk['y'] += chunk['vy']

                rect = ice_chunk_img.get_rect(center=(chunk['x'], chunk['y']))
                screen.blit(ice_chunk_img, rect)

                if rect.colliderect(hero_rect):
                    if shield_active:
                        shield_active = False
                    else:
                        hero_life -= 2
                    ice_chunks.remove(chunk)
                elif chunk['y'] > 800 or chunk['x'] < -50:
                    ice_chunks.remove(chunk)

        # === БОСС 10: королева ===
        if score == 600 and not boss_10_active:
            boss_10_active = True
            boss_10_life = 35
            boss_10_rect.topleft = (1296, 480)
            icicle.clear()

        if boss_10_active and hero_life > 0:
            screen.blit(boss_10, boss_10_rect)
            boss_10_rect.x -= boss_10_speed

            # Полоса HP
            max_health = 50
            health_bar_width = 200
            health_ratio = boss_10_life / max_health
            bar_x = boss_10_rect.x + 50
            bar_y = boss_10_rect.y - 30
            pygame.draw.rect(screen, (0, 0, 0), (bar_x - 2, bar_y - 2, health_bar_width + 4, 24))
            pygame.draw.rect(screen, (255, 50, 0), (bar_x, bar_y, int(health_bar_width * health_ratio), 20))

            # Столкновение с героем
            if boss_10_rect.colliderect(hero_rect):
                if shield_active:
                    shield_active = False
                else:
                    hero_life -= 2

            # Получение урона от камней
            for i in range(len(stone_list) - 1, -1, -1):
                stone_data = stone_list[i]
                rect = stone_data['rect']
                if rect.colliderect(boss_10_rect):
                    stone_list.pop(i)
                    boss_10_life -= 1
                    break

            # Стрельба огненными шарами
            icicle_timer += 1
            if icicle_timer >= icicle_delay:
                icicle_rect = icicle_img.get_rect(midleft=(boss_10_rect.x, boss_10_rect.centery))
                icicle_list.append(icicle_rect)
                icicle_timer = 0

            # Обработка огненных шаров
            for ic in icicle_list[:]:
                ic.x -= 8
                screen.blit(icicle_img, ic)
                if ic.colliderect(hero_rect):
                    if shield_active:
                        shield_active = False
                    else:
                        hero_life -= 1
                    icicle_list.remove(ic)
                elif ic.x < -50:
                    icicle_list.remove(ic)

            # Смерть босса
            if boss_10_life <= 0:
                boss_10_active = False
                icicle.clear()

        # === Активация портала пустынного измерения ===
        if score == 650 and not portal_2_active and not portal_2_entered and score <= 850:
            portal_2_active = True
            portal_2_rect.topleft = (1000, 550)  # координаты портала на экране

        if portal_2_entered:
            dino_spawn_rate = 99999
            bittle_spawn = True
            mummy_spawn = True
        else:
            bittle_spawn = False
            mummy_spawn = False

        current_time = pygame.time.get_ticks() / 1000

        # === Спавн жуков (bittle) ===
        if bittle_spawn and current_time - bittle_timer > bittle_spawn_rate:
            side = ri(0, 1)
            if side == 0:  # слева
                x = -bittle_img_left.get_width()
                direction = 'right'
                img = bittle_img_right
            else:  # справа
                x = 1300
                direction = 'left'
                img = bittle_img_left

            y = ground_y - bittle_img_left.get_height()
            rect = img.get_rect(topleft=(x, y))
            bittle_list.append([rect, 4, direction, img])  # rect, hp, dir, img
            bittle_timer = current_time

        # === Спавн мумий (mummy) ===
        if mummy_spawn and current_time - mummy_timer > mummy_spawn_rate:
            side = ri(0, 1)
            if side == 0:
                x = -mummy_img_left.get_width()
                direction = 'right'
                img = mummy_img_right
            else:
                x = 1300
                direction = 'left'
                img = mummy_img_left

            y = ground_y - mummy_img_left.get_height()
            rect = img.get_rect(topleft=(x, y))
            mummy_list.append([rect, 5, direction, img])  # rect, hp, dir, img
            mummy_timer = current_time

        # === Движение жуков и мумий ===
        for bittle in bittle_list:
            if bittle[2] == 'left':
                bittle[0].x -= bittle_speed
            else:
                bittle[0].x += bittle_speed

        for mummy in mummy_list:
            if mummy[2] == 'left':
                mummy[0].x -= mummy_speed
            else:
                mummy[0].x += mummy_speed

        # === Отрисовка жуков с HP полоской ===
        for bittle in bittle_list:
            rect = bittle[0]
            hp = bittle[1]
            img = bittle[3]

            screen.blit(img, rect)

            bar_width = rect.width
            max_hp = 4
            hp_ratio = hp / max_hp
            hp_bar_width = int(bar_width * hp_ratio)
            pygame.draw.rect(screen, (255, 0, 0), (rect.x, rect.y - 10, bar_width, 5))
            pygame.draw.rect(screen, (0, 255, 0), (rect.x, rect.y - 10, hp_bar_width, 5))

        # === Отрисовка мумий с HP полоской ===
        for mummy in mummy_list:
            rect = mummy[0]
            hp = mummy[1]
            img = mummy[3]

            screen.blit(img, rect)

            bar_width = rect.width
            max_hp = 5
            hp_ratio = hp / max_hp
            hp_bar_width = int(bar_width * hp_ratio)
            pygame.draw.rect(screen, (255, 0, 0), (rect.x, rect.y - 10, bar_width, 5))
            pygame.draw.rect(screen, (0, 255, 0), (rect.x, rect.y - 10, hp_bar_width, 5))

        # === Удаление вышедших за экран ===
        bittle_list = [b for b in bittle_list if -200 < b[0].x < 1400]
        mummy_list = [m for m in mummy_list if -200 < m[0].x < 1400]

        # === Урон от жуков ===
        for bittle in bittle_list:
            if bittle[0].colliderect(hero_rect):
                if shield_active:
                    shield_hits += 1
                    if shield_hits >= 5:
                        shield_active = False
                        shield_hits = 0
                else:
                    hero_life -= 1
                bittle_list.remove(bittle)
                break

        # === Урон от мумий ===
        for mummy in mummy_list:
            if mummy[0].colliderect(hero_rect):
                if shield_active:
                    shield_hits += 1
                    if shield_hits >= 5:
                        shield_active = False
                        shield_hits = 0
                else:
                    hero_life -= 1
                mummy_list.remove(mummy)
                break

        # === БОСС: Царь-Мумия ===
        if score == 700 and not mummy_king_active:
            mummy_king_active = True
            mummy_king_life = 60
            mummy_king_rect.topleft = (1296, 550)
            sand_hands.clear()

        if mummy_king_active and hero_life > 0:
            screen.blit(mummy_king_image, mummy_king_rect)

            # Движение к герою
            if mummy_king_rect.x > hero_rect.x:
                mummy_king_rect.x -= mummy_king_speed
            else:
                mummy_king_rect.x += mummy_king_speed

            # HP бар
            max_health = 60
            health_bar_width = 200
            health_ratio = mummy_king_life / max_health
            pygame.draw.rect(screen, (0, 0, 0), (mummy_king_rect.x + 40, mummy_king_rect.y - 20, health_bar_width, 10))
            pygame.draw.rect(screen, (255, 0, 0),
                             (mummy_king_rect.x + 40, mummy_king_rect.y - 20, int(health_bar_width * health_ratio), 10))

            # Столкновение с героем
            if mummy_king_rect.colliderect(hero_rect):
                if shield_active:
                    shield_active = False
                else:
                    hero_life -= 2

            # Стрельба: руки из песка
            sand_hand_timer += 1
            if sand_hand_timer >= sand_hand_delay:
                x = hero_rect.centerx
                hand_rect = sand_hand_image.get_rect(midbottom=(x, 680))  # рука вылазит из земли
                sand_hands.append(hand_rect)
                sand_hand_timer = 0

            for hand in sand_hands[:]:
                screen.blit(sand_hand_image, hand)
                if hand.colliderect(hero_rect):
                    if shield_active:
                        shield_active = False
                    else:
                        hero_life -= 1
                    sand_hands.remove(hand)



            # Получение урона от камней
            for i in range(len(stone_list) - 1, -1, -1):
                stone_data = stone_list[i]
                rect = stone_data['rect']
                if rect.colliderect(mummy_king_rect):
                    stone_list.pop(i)
                    mummy_king_life -= 1
                    break

            # Смерть
            if mummy_king_life <= 0:
                mummy_king_active = False
                sand_hands.clear()
                score += 0

        # Game Over
        if hero_life <= 0:
            screen.blit(bg_lose, (0, 0))
            screen.blit(labal_lose, (400, 400))

        if score == 750 and not boss_11_active:
            boss_11_active = True
            boss_11_life = 85
            boss_11_rect.topleft = (1296, 520)
            tornadoes.clear()
            djinn_burrow_timer = 0
            djinn_burrowed = False

        if boss_11_active and hero_life > 0:
            # движение к герою (если не зарытся)
            if not djinn_burrowed:
                screen.blit(sand_djinn, boss_11_rect)
                if boss_11_rect.x > hero_rect.x:
                    boss_11_rect.x -= boss_11_speed
                else:
                    boss_11_rect.x += boss_11_speed
            else:
                # «пустая» фаза под песком
                if pygame.time.get_ticks() - djinn_burrow_time > djinn_burrow_duration * 16:
                    djinn_burrowed = False
                    # выскакивает рядом с героем
                    boss_11_rect.midbottom = (max(60, min(1236, hero_rect.centerx + ri(-200, 200))), 700)

            # HP-бар
            max_health = 85
            health_bar_width = 200
            health_ratio = boss_11_life / max_health
            pygame.draw.rect(screen, (0, 0, 0), (boss_11_rect.x + 50, boss_11_rect.y - 30, health_bar_width, 20), 0)
            pygame.draw.rect(screen, (218, 165, 32),
                             (boss_11_rect.x + 50, boss_11_rect.y - 30, int(health_bar_width * health_ratio), 20), 0)

            # контактный урон
            if not djinn_burrowed and boss_11_rect.colliderect(hero_rect):
                if shield_active:
                    shield_active = False
                else:
                    hero_life -= 2

            # попадание камнем
            for i in range(len(stone_list) - 1, -1, -1):
                if stone_list[i]['rect'].colliderect(boss_11_rect) and not djinn_burrowed:
                    stone_list.pop(i)
                    boss_11_life -= 1
                    break

            # спавн торнадо
            tornado_timer += 1
            if tornado_timer >= tornado_delay and not djinn_burrowed:
                vx = -8 if boss_11_rect.centerx > hero_rect.centerx else 8
                vy = -6
                tornadoes.append({'x': boss_11_rect.centerx, 'y': boss_11_rect.centery - 20, 'vx': vx, 'vy': vy})
                tornado_timer = 0

            # движение торнадо (парабола + лёгкое «скольжение»)
            gravity = 0.4
            for t in tornadoes[:]:
                t['x'] += t['vx']
                t['vy'] += gravity
                t['y'] += t['vy']
                rect = tornado_img.get_rect(center=(t['x'], t['y']))
                screen.blit(tornado_img, rect)
                if rect.colliderect(hero_rect):
                    if shield_active:
                        shield_active = False
                    else:
                        hero_life -= 1
                        # лёгкий отбрасывающий импульс
                        hero_x += 25 if t['vx'] > 0 else -25
                    tornadoes.remove(t)
                elif t['x'] < -60 or t['x'] > 1360 or t['y'] > 820:
                    tornadoes.remove(t)

            # нырок под песок по КД
            djinn_burrow_timer += 1
            if djinn_burrow_timer >= djinn_burrow_cd and not djinn_burrowed:
                djinn_burrowed = True
                djinn_burrow_time = pygame.time.get_ticks()
                djinn_burrow_timer = 0

            # смерть
            if boss_11_life <= 0:
                boss_11_active = False
                tornadoes.clear()

        if score == 800 and not boss_12_active:
            boss_12_active = True
            boss_12_life = 130
            boss_12_rect.topleft = (1296, 425)
            venoms.clear()
            mini_scorpions.clear()
            phase2 = False
            boss_12_speed = 1.2

        if boss_12_active and hero_life > 0:
            screen.blit(scorpion_emperor, boss_12_rect)

            # фаза 2 включается при <=40% HP
            if not phase2 and boss_12_life <= 70:
                phase2 = True
                boss_12_speed = 1.6
                venom_delay = 50  # быстрее стреляет

            # движение к герою
            if boss_12_rect.x > hero_rect.x:
                boss_12_rect.x -= boss_12_speed
            else:
                boss_12_rect.x += boss_12_speed

            # HP-бар
            max_health = 130
            health_bar_width = 220
            health_ratio = boss_12_life / max_health
            pygame.draw.rect(screen, (0, 0, 0), (boss_12_rect.x + 40, boss_12_rect.y - 28, health_bar_width, 18), 0)
            pygame.draw.rect(screen, (34, 139, 34),
                             (boss_12_rect.x + 40, boss_12_rect.y - 28, int(health_bar_width * health_ratio), 18), 0)

            # контактный урон
            if boss_12_rect.colliderect(hero_rect):
                if shield_active:
                    shield_active = False
                else:
                    hero_life -= 2

            # попадание камнем
            for i in range(len(stone_list) - 1, -1, -1):
                if stone_list[i]['rect'].colliderect(boss_12_rect):
                    stone_list.pop(i)
                    boss_12_life -= 1
                    break

            # выстрел ядом (парабола)
            venom_timer += 1
            if venom_timer >= venom_delay:
                vx = -10 if boss_12_rect.centerx > hero_rect.centerx else 10
                vy = -7
                venoms.append({'x': boss_12_rect.centerx, 'y': boss_12_rect.centery - 15, 'vx': vx, 'vy': vy})
                venom_timer = 0

            gravity = 0.5
            for v in venoms[:]:
                v['x'] += v['vx']
                v['vy'] += gravity
                v['y'] += v['vy']
                rect = venom_img.get_rect(center=(v['x'], v['y']))
                screen.blit(venom_img, rect)
                if rect.colliderect(hero_rect):
                    if shield_active:
                        shield_active = False
                    else:
                        hero_life -= 1
                    venoms.remove(v)
                elif v['x'] < -60 or v['x'] > 1360 or v['y'] > 820:
                    venoms.remove(v)

            # призыв мини-скорпионов во 2-й фазе
            if phase2:
                summon_timer += 1
                if summon_timer >= summon_delay:
                    summon_timer = 0
                    side = ri(0, 1)
                    x = -mini_scorpion_img.get_width() if side == 0 else 1300
                    y = 710 - mini_scorpion_img.get_height()
                    dirc = 'right' if side == 0 else 'left'
                    rect = mini_scorpion_img.get_rect(topleft=(x, y))
                    mini_scorpions.append([rect, 2, dirc])  # rect, hp, dir

            # поведение мини-скорпионов
            mini_spd = 4
            for m in mini_scorpions[:]:
                if m[2] == 'left':
                    m[0].x -= mini_spd
                else:
                    m[0].x += mini_spd
                screen.blit(mini_scorpion_img, m[0])

                # урон герою
                if m[0].colliderect(hero_rect):
                    if shield_active:
                        shield_active = False
                    else:
                        hero_life -= 1
                    mini_scorpions.remove(m)
                    continue

                # попадание камнем
                hit = False
                for i in range(len(stone_list) - 1, -1, -1):
                    if stone_list[i]['rect'].colliderect(m[0]):
                        stone_list.pop(i)
                        m[1] -= 1
                        if m[1] <= 0:
                            mini_scorpions.remove(m)
                        hit = True
                        break
                if hit: continue

                # чистка за экраном
                if m[0].x < -200 or m[0].x > 1400:
                    mini_scorpions.remove(m)

            # смерть босса
            if boss_12_life <= 0:
                boss_12_active = False
                venoms.clear()
                mini_scorpions.clear()

        if score == 850 and not portal_3_active and not portal_3_entered:
            portal_3_active = True
            portal_3_rect.topleft = (1000, 550)  # координаты портала на экране

        if portal_3_entered and score <= 1050:
            knight_spawn = True
            rider_spawn = True
        else:
            knight_spawn = False
            rider_spawn = False



        current_time = pygame.time.get_ticks() / 1000

        # === Спавн снеговиков ===
        if knight_spawn and current_time - knight_timer > knight_spawn_rate:
            side = ri(0, 1)
            if side == 0:  # слева
                x = -knight_img_left.get_width()
                direction = 'right'
                img = knight_img_right
            else:  # справа
                x = 1300
                direction = 'left'
                img = knight_img_left

            y = ground_y - knight_img_left.get_height()
            rect = img.get_rect(topleft=(x, y))
            knight_list.append([rect, 5, direction, img])  # rect, hp, dir, img
            knight_timer = current_time

        # === Спавн ети ===
        if rider_spawn and current_time - rider_timer > rider_spawn_rate:
            side = ri(0, 1)
            if side == 0:
                x = -rider_img_left.get_width()
                direction = 'right'
                img = rider_img_right
            else:
                x = 1300
                direction = 'left'
                img = rider_img_left

            y = ground_y - rider_img_left.get_height()
            rect = img.get_rect(topleft=(x, y))
            rider_list.append([rect, 6, direction, img])  # rect, hp, dir, img
            rider_timer = current_time

        # Движение рыцарей и всадников
        for knight in knight_list:
            if knight[2] == 'left':
                knight[0].x -= knight_speed
            else:
                knight[0].x += knight_speed

        for rider in rider_list:
            if rider[2] == 'left':
                rider[0].x -= rider_speed
            else:
                rider[0].x += rider_speed

        # Отрисовка снеговиков с полоской HP
        for knight in knight_list:
            rect = knight[0]
            hp = knight[1]
            img = knight[3]

            screen.blit(img, rect)

            bar_width = rect.width
            max_hp = 5
            hp_ratio = hp / max_hp
            hp_bar_width = int(bar_width * hp_ratio)
            pygame.draw.rect(screen, (255, 0, 0), (rect.x, rect.y - 10, bar_width, 5))
            pygame.draw.rect(screen, (0, 255, 0), (rect.x, rect.y - 10, hp_bar_width, 5))

        # Отрисовка ети

        for rider in rider_list:
            rect = rider[0]
            hp = rider[1]
            img = rider[3]

            screen.blit(img, rect)

            bar_width = rect.width
            max_hp = 6
            hp_ratio = hp / max_hp
            hp_bar_width = int(bar_width * hp_ratio)
            pygame.draw.rect(screen, (255, 0, 0), (rect.x, rect.y - 10, bar_width, 5))
            pygame.draw.rect(screen, (0, 255, 0), (rect.x, rect.y - 10, hp_bar_width, 5))

        # Удаление вышедших за экран
        knight_list = [k for k in knight_list if -200 < k[0].x < 1400]
        rider_list = [r for r in rider_list if -200 < r[0].x < 1400]

        # Урон от снеговиков
        for rider in rider_list:
            if rider[0].colliderect(hero_rect):
                if shield_active:
                    shield_hits += 1
                    if shield_hits >= 5:
                        shield_active = False
                        shield_hits = 0
                else:
                    hero_life -= 1
                rider_list.remove(rider)
                break

        # Урон от ети
        for knight in knight_list:
            if knight[0].colliderect(hero_rect):
                if shield_active:
                    shield_hits += 1
                    if shield_hits >= 5:
                        shield_active = False
                        shield_hits = 0
                else:
                    hero_life -= 1
                knight_list.remove(knight)
                break

    if paused:
        pause_text = labal_font.render("PAUSE", True, (255, 255, 255))
        screen.blit(pause_text, (550, 350))
        pygame.display.update()
        continue  # чтобы не выполнять остальной код цикла

    pygame.display.update()
    if keys[pygame.K_d] and hero_x < 1240:
        hero_x += 10
        bg_x -= hero_speed - 2
        hero_direction = "right"
    elif keys[pygame.K_a] and hero_x > 20:
        hero_x -= 10
        bg_x += hero_speed - 2
        hero_direction = "left"

    time.tick(40)


