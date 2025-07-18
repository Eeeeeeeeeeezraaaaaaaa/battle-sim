import os
from character import Hero, Enemy
from weapons import *


hero = Hero(name="goob", health=100)
hero.equip(iron_sword)
enemy = Enemy(name="10,000 chickens", health=100, weapon=gafelid)


while True:
    os.system("cls")

    hero.attack(enemy)
    enemy.attack(hero)

    hero.health_bar.draw()
    enemy.health_bar.draw()

    input()
