"""Játékos scriptje"""

import sys
import math
import pygame as pg
import settings as s
import map as m


class Player:
    """Játékost reprezentáló osztály"""

    def __init__(self, game):
        self.game = game
        self.x, self.y = s.PLAYER_POS  # pylint: disable=invalid-name
        self.angle = s.PLAYER_ANGLE
        self.rel = 0
        self.shot = False
        self.health = s.PLAYER_MAX_HEALTH
        self.rel = 0
        self.health_recovery_delay = 1000
        self.time_prev = pg.time.get_ticks()
        self.diag_move_corr = 1 / math.sqrt(2)

    def update(self):
        """Játékos frissítő függvény"""

        self.movement()
        self.mouse_control()
        self.recover_health()
        self.check_level_done()

    def movement(self):
        """Játékos mozgásáért felelős függvény"""

        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        inc_x, inc_y = 0, 0
        speed = s.PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        num_keys_pressed = -1

        if keys[pg.K_w]:
            num_keys_pressed += 1
            inc_x += speed_cos
            inc_y += speed_sin

        if keys[pg.K_s]:
            num_keys_pressed += 1
            inc_x += -speed_cos
            inc_y += -speed_sin

        if keys[pg.K_a]:
            num_keys_pressed += 1
            inc_x += speed_sin
            inc_y += -speed_cos

        if keys[pg.K_d]:
            num_keys_pressed += 1
            inc_x += -speed_sin
            inc_y += speed_cos

        # Átlós mozgás javítása

        if num_keys_pressed:
            inc_x *= self.diag_move_corr
            inc_y *= self.diag_move_corr

        self.check_wall_collision(inc_x, inc_y)

        # if keys[pg.K_LEFT]:
        #    self.angle -= s.PLAYER_ROT_SPEED * self.game.delta_time

        # if keys[pg.K_RIGHT]:
        #    self.angle += s.PLAYER_ROT_SPEED * self.game.delta_time

        self.angle %= math.tau

    def check_wall_collision(self, inc_x, inc_y):
        """Fallal való ütközés detektáló és kezelő függvény"""

        scale = s.PLAYER_SIZE_SCALE / self.game.delta_time
        if self.check_wall(int(self.x + inc_x * scale), int(self.y)):
            self.x += inc_x
        if self.check_wall(int(self.x), int(self.y + inc_y * scale)):
            self.y += inc_y

    def check_wall(self, x, y):  # pylint: disable=invalid-name
        """Falat detektáló függvény"""

        return (x, y) not in self.game.map.world_map

    def mouse_control(self):
        """A játékos forgásáért felelős függvény"""

        m_x, m_y = pg.mouse.get_pos()
        if m_x < s.MOUSE_BORDER_LEFT or m_x > s.MOUSE_BORDER_RIGHT:
            pg.mouse.set_pos([s.HALF_WIDTH, s.HALF_HEIGHT])
        if m_y < s.MOUSE_BORDER_TOP or m_y > s.MOUSE_BORDER_BOTTOM:
            pg.mouse.set_pos([s.HALF_WIDTH, s.HALF_HEIGHT])
        self.rel = pg.mouse.get_rel()[0]
        self.rel = max(-s.MOUSE_MAX_REL, min(s.MOUSE_MAX_REL, self.rel))
        self.angle += self.rel * s.MOUSE_SENSITIVITY * self.game.delta_time

    def recover_health(self):
        """Játékos életerő visszanyerését megvalósító
        függvény"""

        if self.check_health_recovery_delay() and self.health \
                < s.PLAYER_MAX_HEALTH:
            self.health += 1

    def check_health_recovery_delay(self):
        """Játékos életerő visszanyerésének késleltetés
        figyelő függvénye"""

        time_now = pg.time.get_ticks()
        if time_now - self.time_prev > self.health_recovery_delay:
            self.time_prev = time_now
            return True
        return False

    def get_damage(self, damage):
        """Játékos sebződsését megvalósító függvény"""

        self.health -= damage
        self.game.object_renderer.player_damage()
        self.game.sound.player_pain.play()
        self.check_game_over()

    def check_game_over(self):
        """Játékos halálának, azaz a játék végét
         figyelő és azt újraindító függvény"""

        if self.health < 1:
            self.game.object_renderer.game_over()
            self.game.levels_done = 0
            pg.display.flip()
            pg.time.delay(1500)
            self.game.new_game(m.mini_map_1)

    def check_level_done(self):
        """Szint és/vagy játék teljesítését figyelő függvény"""

        if self.game.levels_done == -1:
            self.game.object_renderer.start()
            pg.display.flip()

            # Billentyű kezelő
            while True:
                event = pg.event.wait()
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    pg.display.flip()
                    self.game.levels_done = 0
                    self.game.new_game(m.mini_map_1)
                    break

        else:
            if self.game.npc_count == 0:
                self.game.object_renderer.level_done()
                self.game.levels_done += 1
                pg.display.flip()
                pg.time.delay(1500)

                if self.game.levels_done == 1:
                    self.game.new_game(m.mini_map_2)
                elif self.game.levels_done == 2:
                    self.game.new_game(m.mini_map_3)
                elif self.game.levels_done == 3:
                    self.game.new_game(m.mini_map_4)
                elif self.game.levels_done == 4:
                    self.game.new_game(m.mini_map_5)
                else:
                    self.game.object_renderer.game_done()
                    pg.display.flip()

                    # Billentyű kezelő
                    while True:
                        event = pg.event.wait()
                        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                            pg.quit()
                            sys.exit()
                        elif event.type == pg.KEYDOWN and event.key == pg.K_r:
                            pg.display.flip()
                            self.game.levels_done = 0
                            self.game.new_game(m.mini_map_1)
                            break

    def single_fire_event(self, event):
        """Játékos fegyverrel való lővését
        kezelő függvény"""

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and not self.shot and \
                    not self.game.weapon.reloading:
                self.game.sound.machine_gun.play()
                self.shot = True
                self.game.weapon.reloading = True

    def draw(self):
        """Játékost reprezentáló kör és iránymutató
        vonal rajzoló függvény debugging célból"""

        pg.draw.line(self.game.screen, 'blue', (self.x * 80, self.y * 80),
                     (self.x * 80 + s.WIDTH * math.cos(self.angle),
                      self.y * 80 + s.WIDTH * math.sin(self.angle)), 2)
        pg.draw.circle(self.game.screen, 'yellow',
                       (self.x * 80, self.y * 80), 15)

    @property
    def pos(self):
        """Játékos koordinátáival visszatérő függvény"""

        return self.x, self.y

    @property
    def map_pos(self):
        """Függvény mely visszatér azzal a négyzettel,
        amelyiken a játékos éppen áll"""

        return int(self.x), int(self.y)
