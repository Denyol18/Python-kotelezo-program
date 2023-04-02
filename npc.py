"""NPCk scriptje"""

import math
from random import randint, random
import pygame as pg
import settings as s
import sprite as sp


class NPC(sp.AnimatedSprite):
    """NPCt reprezentáló osztály,
    ami az AnimatedSprite osztály gyerek osztálya"""

    def __init__(self, game, path='resources/sprites/'
                                  'npc/guard/0.png',
                 pos=(14.5, 7.5), scale=1, shift=0.1,
                 animation_time=180):

        super().__init__(game, path, pos, scale, shift, animation_time)
        self.attack_images = self.get_images(self.path + '/attack')
        self.death_images = self.get_images(self.path + '/death')
        self.idle_images = self.get_images(self.path + '/idle')
        self.pain_images = self.get_images(self.path + '/pain')
        self.walk_images = self.get_images(self.path + '/walk')

        self.attack_dist = randint(3, 6)
        self.speed = 0.02
        self.size = 10
        self.health = 100
        self.attack_damage = 10
        self.accuracy = 0.15
        self.alive = True
        self.pain = False
        self.ray_cast_value = False
        self.frame_counter = 0
        self.player_search_trigger = False

    def update(self):
        """NPCt frissítő függvény"""

        self.check_animation_time()
        self.get_sprite()
        self.run_logic()
        # self.draw_ray_cast()

    def run_logic(self):
        """NPC életciklusát megvalósító és figyelő függvény"""

        if self.alive:
            self.ray_cast_value = self.ray_cast_player_npc()
            self.check_hit_in_npc()

            if self.pain:
                self.animate_pain()

            elif self.ray_cast_value:
                self.player_search_trigger = True

                if self.dist < self.attack_dist:
                    self.animate(self.attack_images)
                    self.attack()
                else:
                    self.animate(self.walk_images)
                    self.movement()

            elif self.player_search_trigger:
                self.animate(self.walk_images)
                self.movement()

            else:
                self.animate(self.idle_images)
        else:
            self.animate_death()

    def ray_cast_player_npc(self):
        """Ray castinget megvalósító függvény
        játékos és NPC között"""

        if self.game.player.map_pos == self.map_pos:
            return True

        v_wall_dist, h_wall_dist = 0, 0
        v_player_dist, h_player_dist = 0, 0

        pos_x, pos_y = self.game.player.pos
        map_x, map_y = self.game.player.map_pos

        ray_angle = self.theta

        sin_a = math.sin(ray_angle)
        cos_a = math.cos(ray_angle)

        # Vízszintes irány

        hor_y, d_y = (map_y + 1, 1) if sin_a > 0 else (map_y - 1e-6, -1)
        hor_depth = (hor_y - pos_y) / sin_a
        hor_x = pos_x + hor_depth * cos_a

        delta_depth = d_y / sin_a
        d_x = delta_depth * cos_a

        for i in range(s.MAX_DEPTH):  # pylint: disable=unused-variable
            hor_tile = int(hor_x), int(hor_y)
            if hor_tile == self.map_pos:
                h_player_dist = hor_depth
                break
            if hor_tile in self.game.map.world_map:
                h_wall_dist = hor_depth
                break
            hor_x += d_x
            hor_y += d_y
            hor_depth += delta_depth

        # Függőleges irány

        vert_x, d_x = (map_x + 1, 1) if cos_a > 0 else (map_x - 1e-6, -1)
        vert_depth = (vert_x - pos_x) / cos_a
        vert_y = pos_y + vert_depth * sin_a

        delta_depth = d_x / cos_a
        d_y = delta_depth * sin_a

        for i in range(s.MAX_DEPTH):
            vert_tile = int(vert_x), int(vert_y)
            if vert_tile == self.map_pos:
                v_player_dist = vert_depth
                break
            if vert_tile in self.game.map.world_map:
                v_wall_dist = vert_depth
                break
            vert_x += d_x
            vert_y += d_y
            vert_depth += delta_depth

        player_dist = max(v_player_dist, h_player_dist)
        wall_dist = max(v_wall_dist, h_wall_dist)

        if 0 < player_dist < wall_dist or not wall_dist:
            return True
        return False

    def check_hit_in_npc(self):
        """NPCt való eltalálás vizsgáló függvény"""

        if self.ray_cast_value and self.game.player.shot:
            if s.HALF_WIDTH - self.sprite_half_width < self.screen_x \
                    < s.HALF_HEIGHT + self.sprite_half_width:
                self.game.sound.npc_pain.play()
                self.game.player.shot = False
                self.pain = True
                self.health -= self.game.weapon.damage
                self.check_health()

    def animate_pain(self):
        """NPC sérülését animáló függvény"""

        self.animate(self.pain_images)
        if self.animation_trigger:
            self.pain = False

    def check_health(self):
        """NPC életerejét vizsgáló függvény"""

        if self.health < 1:
            self.alive = False
            self.game.sound.npc_death.play()

    def animate_death(self):
        """NPC halálát animáló függvény"""

        if not self.alive:
            if self.animation_trigger and self.frame_counter \
                    < len(self.death_images) - 1:

                self.death_images.rotate(-1)
                self.image = self.death_images[0]
                self.frame_counter += 1

    def attack(self):
        """NPC támadás hangját lejátszó függvény"""

        if self.animation_trigger:
            self.game.sound.npc_shot.play()
            if random() < self.accuracy:
                self.game.player.get_damage(self.attack_damage)

    def movement(self):
        """NPC mozgását megvalósító függvény"""

        next_pos = self.game.pathfinding.get_path(self.map_pos,
                                                  self.game.player.map_pos)

        next_x, next_y = next_pos

        # Rajzolás debugging célból
        # pg.draw.rect(self.game.screen, 'pink',
        # (80 * next_x, 80 * next_y, 80, 80))

        if next_pos not in self.game.object_handler.npc_positions:
            angle = math.atan2(next_y + 0.5 - self.y, next_x + 0.5 - self.x)
            d_x = math.cos(angle) * self.speed
            d_y = math.sin(angle) * self.speed
            self.check_wall_collision(d_x, d_y)

    def check_wall_collision(self, inc_x, inc_y):
        """Fallal való ütközés detektáló és kezelő függvény"""

        if self.check_wall(int(self.x + inc_x * self.size), int(self.y)):
            self.x += inc_x
        if self.check_wall(int(self.x), int(self.y + inc_y * self.size)):
            self.y += inc_y

    def check_wall(self, x, y):  # pylint: disable=invalid-name
        """Falat detektáló függvény"""

        return (x, y) not in self.game.map.world_map

    @property
    def map_pos(self):
        """Függvény mely visszatér azzal a négyzettel,
        amelyiken az NPC éppen áll"""

        return int(self.x), int(self.y)

    def draw_ray_cast(self):
        """ray_cast_player_npc függvényt tesztelő
        függvény"""

        pg.draw.circle(self.game.screen, 'red', (80 * self.x, 80 * self.y), 15)
        if self.ray_cast_player_npc():
            pg.draw.line(self.game.screen, 'orange',
                         (80 * self.game.player.x, 80 * self.game.player.y),
                         (80 * self.x, 80 * self.y), 2)
