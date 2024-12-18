import pygame
import random
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Retro RPG")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 0)

font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 72)  # Większa czcionka dla napisu "Level Up!"

clock = pygame.time.Clock()
FPS = 360

player_img = pygame.image.load("dkes3tl4.bmp")
player_img = pygame.transform.scale(player_img, (150, 150))

enemy_img = pygame.image.load(("z6f5oheh.bmp")  )
enemy_img = pygame.transform.scale(enemy_img, (150, 150))


class Button:
    def __init__(self, x, y, w, h, text, color, hover_color, action=None):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.action = action

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(surface, self.hover_color, self.rect)
        else:
            pygame.draw.rect(surface, self.color, self.rect)

        text_surface = font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, event):
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                if self.action:
                    self.action()


class Player:
    def __init__(self):
        self.name = "Hero"
        self.level = 1
        self.hp = 1000
        self.max_hp = 1000
        self.mana = 50
        self.max_mana = 50
        self.gold = 50
        self.exp = 0
        self.skill_points = 0
        self.inventory = []
        self.equipped = {"weapon": 1, "armor": None, "amulet": None}
        self.skills = {"Power Strike": False, "Fireball": False}
        self.level_up_message_timer = 0  # Timer do wyświetlania napisu Level Up!

    def level_up(self):
        self.level += 1
        self.max_hp += 20
        self.hp = self.max_hp
        self.max_mana += 10
        self.mana = self.max_mana
        self.level_up_message_timer = FPS * 2  # Wyświetlaj "Level Up!" przez 2 sekundy
        print(f"{self.name} leveled up to {self.level}!")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"Added to inventory: {item['name']}!")

    def equip(self, item):
        self.equipped[item['type']] = item
        print(f"Equipped: {item['name']}")

    def heal(self):
        heal_cost = 20
        if self.gold >= heal_cost and self.hp < self.max_hp:
            self.gold -= heal_cost
            self.hp = self.max_hp
            print("Player healed!")

    def take_damage(self, amount):
        self.hp -= amount
        print(f"{self.name} took {amount} damage!")
        if self.hp <= 0:
            self.hp = 0
            print("Game Over!")
            return True  # Zwracamy True, gdy gra powinna się zakończyć
        return False  # Jeśli HP jest większe niż 0, gra trwa


class Enemy:
    def __init__(self, name, level, hp, damage, boss=False):
        self.name = name
        self.level = level
        self.hp = hp
        self.max_hp = hp
        self.damage = damage
        self.is_boss = boss


def generate_enemies(player):
    enemy_types = ["Goblin", "Orc", "Skeleton", "Demon"]
    enemies = []
    for _ in range(random.randint(1, 3)):
        name = random.choice(enemy_types)
        level = random.randint(player.level, player.level + 2)
        hp = level * 30
        damage = level * 5
        enemies.append(Enemy(name, level, hp, damage))

    if random.random() < 0.2:
        boss_name = random.choice(["Dragon", "Lich", "Titan"])
        boss = Enemy(boss_name, player.level + 5, player.level * 100, player.level * 10, boss=True)
        enemies.append(boss)
    return enemies


def battle():
    global current_enemies
    current_enemies = generate_enemies(player)
    print("Enemies have appeared!")


def shop():
    global in_shop
    in_shop = True


def buy_item(item):
    if player.gold >= item['cost']:
        player.gold -= item['cost']
        player.add_item(item)
        print(f"Bought {item['name']}!")
    else:
        print("Not enough gold!")


def buy_skill(skill_name):
    if player.skill_points >= 1:  # Wymagaj 1 punktu umiejętności do zakupu
        player.skill_points -= 1
        player.skills[skill_name] = True
        print(f"Unlocked skill: {skill_name}!")
    else:
        print("Not enough skill points!")


def attack():
    global current_enemies
    if current_enemies:
        damage = random.randint(10, 20) + (player.level * 2)
        target = random.choice(current_enemies)
        target.hp -= damage
        print(f"Dealt {damage} damage to {target.name}!")
        if target.hp <= 0:
            print(f"{target.name} defeated!")
            gold_reward = random.randint(20, 50)
            exp_reward = random.randint(15, 40)
            skill_points_reward = 1 if random.random() < 0.35 else 0
            player.gold += gold_reward
            player.exp += exp_reward
            player.skill_points += skill_points_reward
            print(f"Earned {gold_reward} gold, {exp_reward} XP, and {skill_points_reward} skill points!")
            current_enemies.remove(target)
            if player.exp >= player.level * 50:
                player.level_up()
        else:
            if player.take_damage(target.damage):  # Sprawdzamy, czy gra się kończy
                game_over()


def open_skill_tree():
    global in_skill_tree
    in_skill_tree = True


def toggle_inventory():
    global in_inventory
    in_inventory = not in_inventory


def close_windows():
    global in_shop, in_skill_tree, in_inventory
    in_shop = False
    in_skill_tree = False
    in_inventory = False


def game_over():
    game_over_text = font.render("GAME OVER", True, RED)
    text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(game_over_text, text_rect)
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()


player = Player()
current_enemies = []
shop_items = [
    {"name": "Health Potion", "cost": 20, "type": "consumable"},
    {"name": "Iron Sword", "cost": 100, "type": "weapon"},
    {"name": "Leather Armor", "cost": 150, "type": "armor"},
    {"name": "Magic Amulet", "cost": 200, "type": "amulet"}
]
in_shop = False
in_skill_tree = False
in_inventory = False
shop_buttons = []
skill_tree_buttons = []

def update_skill_tree_buttons():
    global skill_tree_buttons
    skill_tree_buttons = []
    skill_list = list(player.skills.keys())
    for idx, skill in enumerate(skill_list):
        if not player.skills[skill]:
            button = Button(
                600, 200 + idx * 50, 100, 30, "Unlock", GREEN, (0, 200, 0), 
                lambda s=skill: buy_skill(s)
            )
            skill_tree_buttons.append((skill, button))

fight_button = Button(50, 550, 200, 50, "Fight", RED, (200, 0, 0), battle)
shop_button = Button(300, 550, 200, 50, "Shop", BLUE, (0, 0, 200), shop)
attack_button = Button(550, 550, 200, 50, "Attack", GREEN, (0, 200, 0), attack)
skill_tree_button = Button(800, 550, 150, 50, "Skill Tree", YELLOW, (200, 200, 0), open_skill_tree)

running = True
while running:
    screen.fill(BLACK)

    hp_text = font.render(f"HP: {player.hp}/{player.max_hp}", True, GREEN)
    mana_text = font.render(f"Mana: {player.mana}/{player.max_mana}", True, BLUE)
    gold_text = font.render(f"Gold: {player.gold}", True, YELLOW)
    level_text = font.render(f"Level: {player.level}", True, WHITE)
    skill_points_text = font.render(f"Skill Points: {player.skill_points}", True, RED)

    # Wyświetl poziom gracza
    level_rect = level_text.get_rect(center=(SCREEN_WIDTH // 2, 10))
    screen.blit(level_text, level_rect)

    screen.blit(hp_text, (10, 10))
    screen.blit(mana_text, (10, 50))
    screen.blit(gold_text, (10, 90))
    screen.blit(skill_points_text, (10, 130))

    if current_enemies:
        for idx, enemy in enumerate(current_enemies):
            enemy_text = font.render(f"{enemy.name} HP: {enemy.hp}/{enemy.max_hp}", True, RED)
            screen.blit(enemy_text, (300, 150 + idx * 50))

    fight_button.draw(screen)
    shop_button.draw(screen)
    attack_button.draw(screen)
    skill_tree_button.draw(screen)

    if in_inventory:
        pygame.draw.rect(screen, GRAY, (150, 150, 700, 400))
        inventory_title = font.render("Inventory", True, WHITE)
        screen.blit(inventory_title, (450, 170))
        for idx, item in enumerate(player.inventory):
            item_text = font.render(item['name'], True, WHITE)
            screen.blit(item_text, (200, 200 + idx * 30))

    if in_shop:
        pygame.draw.rect(screen, GRAY, (150, 150, 700, 400))
        shop_title = font.render("Shop", True, WHITE)
        screen.blit(shop_title, (450, 170))
        
        if not shop_buttons:  # Generowanie przycisków tylko raz
            for idx, item in enumerate(shop_items):
                buy_button = Button(
                    600, 200 + idx * 30, 100, 30, "Buy", GREEN, (0, 200, 0),
                    lambda i=item: buy_item(i)
                )
                shop_buttons.append(buy_button)
        
        for idx, item in enumerate(shop_items):
            item_text = font.render(f"{item['name']} - {item['cost']} Gold", True, WHITE)
            screen.blit(item_text, (200, 200 + idx * 30))
            shop_buttons[idx].draw(screen)

        exit_text = font.render("Press ESC to exit shop", True, WHITE)
        screen.blit(exit_text, (300, 500))

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN and event.key == K_ESCAPE and in_shop:
            in_shop = False
            shop_buttons.clear()
        if event.type == KEYDOWN and event.key == K_ESCAPE and in_skill_tree:
            in_skill_tree = False
            shop_buttons.clear()

        if event.type == MOUSEBUTTONDOWN:
            fight_button.is_clicked(event)
            shop_button.is_clicked(event)
            attack_button.is_clicked(event)
            skill_tree_button.is_clicked(event)
            if in_shop:
                for button in shop_buttons:
                    button.is_clicked(event)
    
    if in_skill_tree:
        pygame.draw.rect(screen, GRAY, (150, 150, 700, 400))
        skill_tree_title = font.render("Skill Tree", True, WHITE)
        screen.blit(skill_tree_title, (450, 170))
        skill_list = list(player.skills.keys())
        for idx, skill in enumerate(skill_list):
            skill_text = font.render(skill, True, WHITE)
            screen.blit(skill_text, (200, 200 + idx * 30))
            if not player.skills[skill]:
                buy_button = Button(600, 200 + idx * 30, 100, 30, "Unlock", GREEN, (0, 200, 0), lambda s=skill: buy_skill(s))
                buy_button.draw(screen)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        for button in [fight_button, shop_button, skill_tree_button]:
            button.is_clicked(event)
        if in_shop or in_skill_tree:
            for _, button in skill_tree_buttons:
                button.is_clicked(event)

    if in_skill_tree:
        pygame.draw.rect(screen, GRAY, (150, 150, 700, 400))
        skill_tree_title = font.render("Skill Tree", True, WHITE)
        screen.blit(skill_tree_title, (450, 170))
        skill_list = list(player.skills.keys())
        for idx, skill in enumerate(skill_list):
            skill_text = font.render(skill, True, WHITE)
            screen.blit(skill_text, (200, 200 + idx * 30))
            if not player.skills[skill]:
                buy_button = Button(600, 200 + idx * 30, 100, 30, "Unlock", GREEN, (0, 200, 0), lambda s=skill: buy_skill(s))
                buy_button.draw(screen)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        for button in [fight_button, shop_button, skill_tree_button]:
            button.is_clicked(event)
        if in_shop or in_skill_tree:
            for _, button in skill_tree_buttons:
                button.is_clicked(event)

    # Wyświetl "Level Up!" na środku ekranu, jeśli timer > 0
    if player.level_up_message_timer > 0:
        level_up_text = big_font.render("LEVEL UP!", True, YELLOW)
        level_up_rect = level_up_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 350))
        screen.blit(level_up_text, level_up_rect)
        player.level_up_message_timer -= 1

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_i:
                toggle_inventory()
            if event.key == K_ESCAPE:
                close_windows()

        fight_button.is_clicked(event)
        shop_button.is_clicked(event)
        attack_button.is_clicked(event)
        skill_tree_button.is_clicked(event)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()