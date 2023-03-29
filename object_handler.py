"""Objektum kezelő szkriptje"""

import sprite as sp


class ObjectHandler:
    """Objektum kezelőt reprezentáló osztály"""

    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.static_sprites = 'resources/sprites/static_sprites'
        add_sprite = self.add_sprite

        add_sprite(sp.Sprite(game))
        add_sprite(sp.Sprite(game, pos=(1.8, 1.8)))
        add_sprite(sp.Sprite(game, pos=(9.8, 5.5)))

    def update(self):
        """Objektum kezelőt frissítő függvény"""

        [sprite.update() for sprite in self.sprite_list]

    def add_sprite(self, sprite):
        """Függvény, ami a paraméterként kapott
        spriteot hozzáadja a sprite_listhez"""

        self.sprite_list.append(sprite)
