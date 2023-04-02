"""Fegyver scriptje"""

import sprite as sp
import settings as s


class Weapon(sp.AnimatedSprite):
    """Fegyvert reprezentáló osztály,
    ami az AnimatedSprite osztály gyerek osztálya"""

    def __init__(self, game, path='resources/sprites/'
                                  'weapon/0.png', scale=10,
                 animation_time=90):
        super().__init__(game=game, path=path, scale=scale,
                         animation_time=animation_time)

        self.images = sp.deque(
            [sp.pg.transform.smoothscale(img, (self.image.get_width() * scale,
                                         self.image.get_height() * scale))
             for img in self.images])

        self.weapon_pos = (s.HALF_WIDTH - self.images[0].get_width() // 2,
                           s.HEIGHT - self.images[0].get_height())
        self.reloading = False
        self.num_images = len(self.images)
        self.frame_counter = 0
        self.damage = 20

    def update(self):
        """Fegyvert frissítő függvény"""

        self.check_animation_time()
        self.animate_shot()

    def animate_shot(self):
        """Fegyver lövést animáló függvény"""

        if self.reloading:
            self.game.player.shot = False
            if self.animation_trigger:
                self.images.rotate(-1)
                self.image = self.images[0]
                self.frame_counter += 1
                if self.frame_counter == self.num_images:
                    self.reloading = False
                    self.frame_counter = 0

    def draw(self):
        """Fegyvert megrajzoló függvény"""

        self.game.screen.blit(self.images[0], self.weapon_pos)
