"""Objektum kezelő szkriptje"""

import python_kotelezo_program.sprite as sp
import python_kotelezo_program.npc as n


class ObjectHandler:
    """Objektum kezelőt reprezentáló osztály"""

    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'resources/sprites/npc'
        self.static_sprite_path = 'resources/sprites/static_sprites'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_positions = {}

        if self.game.levels_done == 0:
            # Spriteok
            add_sprite(sp.Sprite(game, pos=(6.25, 1.25)))
            add_sprite(sp.Sprite(game, pos=(6.25, 1.75)))
            add_sprite(sp.Sprite(game, pos=(6.25, 2.25)))
            add_sprite(sp.Sprite(game, pos=(6.25, 2.75)))
            add_sprite(sp.Sprite(game, pos=(11.25, 7.75)))
            add_sprite(sp.Sprite(game, pos=(11.75, 7.75)))
            add_sprite(sp.Sprite(game, pos=(12.25, 7.75)))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/table.png',
                                 pos=(8.25, 1.75), scale=1, shift=0.1))

            # NPCk
            add_npc(n.NPC(game, pos=(4.5, 4.5)))
            add_npc(n.NPC(game, pos=(9.5, 1.75)))
            add_npc(n.NPC(game, pos=(11.5, 3.5)))
            add_npc(n.NPC(game, pos=(13.5, 1.75)))

        elif self.game.levels_done == 1:
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/plant.png',
                                 pos=(2.75, 5.75), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/plant.png',
                                 pos=(4.25, 9.25), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/plant.png',
                                 pos=(9.75, 3.25), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/plant.png',
                                 pos=(8.25, 8.75), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/plant.png',
                                 pos=(14.75, 10.75), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/plant.png',
                                 pos=(14.75, 1.25), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/table.png',
                                 pos=(4.5, 7.5), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/table.png',
                                 pos=(11.25, 3.5), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/table.png',
                                 pos=(4.25, 1.5), scale=1, shift=0.1))

            add_npc(n.NPC(game, pos=(4.5, 4.5)))
            add_npc(n.NPC(game, pos=(2.5, 7.5)))
            add_npc(n.NPC(game, pos=(6.5, 8.5)))
            add_npc(n.NPC(game, pos=(4.5, 2.5)))
            add_npc(n.NPC(game, pos=(11.5, 4.5)))
            add_npc(n.NPC(game, pos=(12.5, 9.5)))

        elif self.game.levels_done == 2:
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/bones.png',
                                 pos=(2.75, 3.75), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/bones.png',
                                 pos=(2.75, 5.25), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/bones.png',
                                 pos=(1.25, 12.25), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/bones.png',
                                 pos=(1.25, 13), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/bones.png',
                                 pos=(1.25, 13.75), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/bones.png',
                                 pos=(5.25, 3.5), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, pos=(6.75, 9.75)))
            add_sprite(sp.Sprite(game, pos=(6.75, 9.25)))
            add_sprite(sp.Sprite(game, pos=(6.25, 9.75)))
            add_sprite(sp.Sprite(game, pos=(12.75, 11.75)))
            add_sprite(sp.Sprite(game, pos=(12.75, 8.75)))
            add_sprite(sp.Sprite(game, pos=(14.75, 1.25)))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/puddle.png',
                                 pos=(3.5, 1.5), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/puddle.png',
                                 pos=(4.5, 11.5), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/puddle.png',
                                 pos=(8.5, 12.5), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/puddle.png',
                                 pos=(11.5, 13.5), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/puddle.png',
                                 pos=(11.5, 7.5), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/puddle.png',
                                 pos=(14.5, 8.5), scale=1, shift=0.1))

            add_npc(n.NPC(game, pos=(4.5, 4.5)))
            add_npc(n.NPC(game, pos=(4.5, 6.5)))
            add_npc(n.NPC(game, pos=(4.5, 9.5)))
            add_npc(n.NPC(game, pos=(2.5, 12.5)))
            add_npc(n.NPC(game, pos=(8.5, 5.5)))
            add_npc(n.NPC(game, pos=(12.5, 13.5)))
            add_npc(n.NPC(game, pos=(14.5, 5.5)))
            add_npc(n.NPC(game, pos=(10.5, 1.75)))

        elif self.game.levels_done == 3:
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/table.png',
                                 pos=(2.5, 4.5), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/table.png',
                                 pos=(3.5, 5.5), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/table.png',
                                 pos=(1.5, 16.5), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/table.png',
                                 pos=(12.5, 4.5), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/vase.png',
                                 pos=(5.75, 3.25), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/vase.png',
                                 pos=(5.75, 6.75), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/vase.png',
                                 pos=(12.25, 7.75), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/vase.png',
                                 pos=(11.75, 8.25), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/vase.png',
                                 pos=(14.75, 16.75), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/vase.png',
                                 pos=(14.75, 16.25), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/plant.png',
                                 pos=(9.75, 5.25), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/plant.png',
                                 pos=(10.75, 6.25), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/plant.png',
                                 pos=(4.75, 9.25), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/plant.png',
                                 pos=(1.25, 10.75), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/plant.png',
                                 pos=(11.75, 14.75), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/plant.png',
                                 pos=(13.25, 8.75), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/sink.png',
                                 pos=(8.5, 8.5), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/sink.png',
                                 pos=(6.5, 14.75), scale=1, shift=0.1))

            add_npc(n.NPC(game, pos=(7.5, 2.5)))
            add_npc(n.NPC(game, pos=(14.5, 2.5)))
            add_npc(n.NPC(game, pos=(12.5, 3.5)))
            add_npc(n.NPC(game, pos=(14.5, 14.5)))
            add_npc(n.NPC(game, pos=(1.5, 15.5)))
            add_npc(n.NPC(game, pos=(5.5, 12.5)))
            add_npc(n.NPC(game, pos=(12.5, 9.5)))
            add_npc(n.NPC(game, pos=(6.5, 7.5)))
            add_npc(n.NPC(game, pos=(6.5, 8.5)))
            add_npc(n.NPC(game, pos=(4.5, 7.5)))
            add_npc(n.NPC(game, pos=(1.5, 4.5)))

        elif self.game.levels_done == 4:
            add_sprite(sp.Sprite(game, pos=(5.75, 1.25)))
            add_sprite(sp.Sprite(game, pos=(5.75, 1.75)))
            add_sprite(sp.Sprite(game, pos=(5.75, 2.25)))
            add_sprite(sp.Sprite(game, pos=(5.75, 2.75)))
            add_sprite(sp.Sprite(game, pos=(7.25, 3.75)))
            add_sprite(sp.Sprite(game, pos=(1.25, 11.25)))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/plant.png',
                                 pos=(1.25, 6.75), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/plant.png',
                                 pos=(8.75, 5.25), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/plant.png',
                                 pos=(11.75, 12.25), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/plant.png',
                                 pos=(7.25, 16.75), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/plant.png',
                                 pos=(1.25, 9.75), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/vase.png',
                                 pos=(1.75, 6.75), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/vase.png',
                                 pos=(2.25, 6.75), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/vase.png',
                                 pos=(12.75, 13.25), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/vase.png',
                                 pos=(12.75, 13.75), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/vase.png',
                                 pos=(1.25, 19.75), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/vase.png',
                                 pos=(1.75, 19.75), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/sink.png',
                                 pos=(8.75, 8.5), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/sink.png',
                                 pos=(5.25, 18.25), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/sink.png',
                                 pos=(7.25, 18.25), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/puddle.png',
                                 pos=(10.5, 9.5), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/puddle.png',
                                 pos=(11.5, 2.5), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/puddle.png',
                                 pos=(14.5, 1.5), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/puddle.png',
                                 pos=(13.5, 9.5), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/puddle.png',
                                 pos=(14.5, 13.5), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/bones.png',
                                 pos=(12.25, 6.25), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/bones.png',
                                 pos=(12.25, 7), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/bones.png',
                                 pos=(12.25, 7.75), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/bones.png',
                                 pos=(12.25, 8.5), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/bones.png',
                                 pos=(11.25, 16.5), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/table.png',
                                 pos=(10.5, 2.5), scale=1, shift=0.1))
            add_sprite(sp.Sprite(game, path='resources/sprites/static_sprites/table.png',
                                 pos=(3.5, 14.5), scale=1, shift=0.1))

            add_npc(n.NPC(game, pos=(4.5, 4.5)))
            add_npc(n.NPC(game, pos=(7.5, 8.5)))
            add_npc(n.NPC(game, pos=(10.5, 8.5)))
            add_npc(n.NPC(game, pos=(7.5, 1.75)))
            add_npc(n.NPC(game, pos=(9.5, 1.75)))
            add_npc(n.NPC(game, pos=(12.5, 1.75)))
            add_npc(n.NPC(game, pos=(14.5, 5.5)))
            add_npc(n.NPC(game, pos=(12.5, 16.5)))
            add_npc(n.NPC(game, pos=(12.5, 17.5)))
            add_npc(n.NPC(game, pos=(5.5, 16.5)))
            add_npc(n.NPC(game, pos=(1.5, 15.5)))
            add_npc(n.NPC(game, pos=(1.5, 13.5)))
            add_npc(n.NPC(game, pos=(5.5, 11.5)))
            add_npc(n.NPC(game, pos=(5.5, 8.5)))
            add_npc(n.NPC(game, pos=(1.5, 8.5)))

    def update(self):
        """Objektum kezelőt frissítő függvény"""

        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]

    def add_npc(self, npc):
        """Függvény, ami a paraméterként kapott
        npct hozzáadja az npc_listhez"""

        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        """Függvény, ami a paraméterként kapott
        spriteot hozzáadja a sprite_listhez"""

        self.sprite_list.append(sprite)
