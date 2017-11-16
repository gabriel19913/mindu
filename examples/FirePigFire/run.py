
import random
import mindu

mindu.screen.set_size((640, 400))
mindu.screen.set_title('Fire, Pig, Fire!')
mindu.screen.set_icon(mindu.Image('images/icon.png', True))
mindu.mouse.toggle_visible()



@mindu.keyboard.on_ding
def on_keyboard_ding(symbol):

    if symbol == 'escape':
        mindu.screen.toggle_full()



class Pig(object):

    def __init__(self, scene):
        self.scene = scene

        self.walking_left = mindu.Animation(
            directory = 'animations/pig-walking',
            redraw = 5)

        self.walking_right = self.walking_left.flip(True, False)

        self.aiming_left = mindu.Image(
            file = 'images/pig-aiming.png',
            midbottom = (mindu.screen.centerx, mindu.screen.bottom - 10))

        self.aiming_right = self.aiming_left.flip(True, False)
        self.aiming_up = mindu.Image('images/pig-aiming-up.png')

        self.explosion = mindu.Animation(
            directory = 'animations/pig-explosion',
            redraw = 2,
            repeat = False)

        self.sprite = self.aiming_left

        self.alive = True
        self.shooting = False
        self.walking = False
        self.aiming = 'left'
        self.side = 'left'
        self.speed = 3



    def update(self):
        if not self.alive:
            self.explosion.center = self.sprite.center
            self.explosion.draw()
            return

        space_busy = mindu.keyboard.busy('space')
        space_time = mindu.keyboard.time('space')
        up_busy = mindu.keyboard.busy('up')
        left_busy = mindu.keyboard.busy('left')
        right_busy = mindu.keyboard.busy('right')

        if space_busy:
            if space_time >= 1000:
                self.shooting = not random.randint(0, space_time // 1000)
            else: self.shooting = True

            self.walking = False

            if up_busy: self.aiming = 'up'

            elif right_busy and not left_busy:
                self.aiming = 'right'
                self.side = 'right'

            elif left_busy and not right_busy:
                self.aiming = 'left'
                self.side = 'left'

            else: self.aiming = self.side

        else:
            self.shooting = False

            if up_busy:
                self.aiming = 'up'
                self.walking = False

            elif right_busy and not left_busy:
                self.aiming = 'right'
                self.side = 'right'
                self.walking = True

            elif left_busy and not right_busy:
                self.aiming = 'left'
                self.side = 'left'
                self.walking = True

            else:
                self.aiming = self.side
                self.walking = False

        midbottom = self.sprite.midbottom

        if self.aiming == 'left':
            if self.walking: self.sprite = self.walking_left
            else: self.sprite = self.aiming_left

        elif self.aiming == 'right':
            if self.walking: self.sprite =  self.walking_right
            else: self.sprite = self.aiming_right

        else: self.sprite = self.aiming_up

        self.sprite.midbottom = midbottom
        self.sprite.set_osd(self.shooting)

        if self.walking:
            if self.aiming == 'left': self.sprite.move(-self.speed, 0)
            elif self.aiming == 'right': self.sprite.move(self.speed, 0)
            mindu.screen.grab(self.sprite)

        self.sprite.draw()



class Fire(object):

    def __init__(self, scene):
        self.scene = scene

        self.left = mindu.Animation(
            directory = 'animations/fire',
            osd = True,
            redraw = 3)

        self.right = self.left.flip(True, False)
        self.up = self.left.rotate(90.0)
        self.sprite = self.left



    def update(self):
        sound = self.scene.fire_channel.get_sound()

        if not self.scene.pig.shooting:
            if sound not in (None, self.scene.fire_echo_sound):
                self.scene.fire_channel.play(self.scene.fire_echo_sound)
            return

        if sound is not self.scene.fire_sound:
            self.scene.fire_channel.play(self.scene.fire_sound, -1)

        if self.scene.pig.aiming == 'up':
            self.sprite = self.up
            self.sprite.midbottom = self.scene.pig.sprite.midtop

        elif self.scene.pig.aiming == 'left':
            self.sprite = self.left
            self.sprite.midright = self.scene.pig.sprite.midleft

        else:
            self.sprite = self.right
            self.sprite.midleft = self.scene.pig.sprite.midright

        self.sprite.draw()



class Ship(object):

    def __init__(self, scene):
        scene.ship_reload_control -= 1
        if scene.ship_reload_control > 0: return
        scene.ship_reload_control = scene.ship_reload
        if random.randint(0, 5): return

        self.scene = scene
        self.sprite = self.scene.ship_sprite.copy()
        self.sparks_sprite = self.scene.sparks_sprite.copy()
        self.speed = 5
        self.life = 100
        self.altitude = 4
        self.bright = False
        self.scene.ships.append(self)



    def update(self):
        self.sprite.move(self.speed, 0)

        if not mindu.screen.collide(self.sprite):
            self.sprite.top = self.sprite.bottom + 10
            self.altitude -= 1

            if self.altitude == 0 and random.randint(0, 1):
                self.sprite.left = mindu.screen.right

            else: self.speed = -self.speed

        self.sprite.draw()

        if self.scene.pig.shooting:

            if self.scene.pig.aiming == 'up':
                if self.sprite.left <= self.scene.pig.sprite.centerx:
                    if self.scene.pig.sprite.centerx <= self.sprite.right:
                        self.bright = True
                        self.life -= 5

            elif self.scene.pig.aiming == 'left':
                if self.altitude == 0:
                    if self.sprite.right < self.scene.pig.sprite.left:
                        self.bright - True
                        self.life -= 5

            elif self.scene.pig.aiming == 'right':
                if self.altitude == 0:
                    if self.sprite.left > self.scene.pig.sprite.right:
                        self.bright = True
                        self.life -= 5

        if self.bright:
            self.sprite.toggle_osd()
            self.sprite.draw()
            self.sprite.toggle_osd()
            self.sparks_sprite.center = self.sprite.center
            self.sparks_sprite.draw()
            self.bright = False

        else: self.sprite.draw()

        if self.sprite.collide_point(self.scene.pig.sprite.center):
            self.scene.ships.remove(self)
            explosion = Explosion(self.scene)
            explosion.sprite.center = self.sprite.center
            self.scene.score += 1
            self.scene.score_sprite.set_text('Score: ' + str(self.scene.score))

        elif self.life > 0:

            if self.altitude > 2 and not random.randint(0, 100):
                bomb = Bomb(self.scene)
                bomb.sprite.midtop = self.sprite.midbottom

        else:
            self.scene.ships.remove(self)
            explosion = Explosion(self.scene)
            explosion.sprite.center = self.sprite.center
            self.scene.score += 1
            self.scene.score_sprite.set_text('Score: ' + str(self.scene.score))



class Explosion(object):

    def __init__(self, scene):
        self.scene = scene
        self.sprite = self.scene.explosion_sprite.copy()
        self.scene.explosions.append(self)
        self.scene.explosion_channel.play(self.scene.explosion_sound)



    def update(self):
        self.sprite.draw()

        if not self.sprite.running():
            self.scene.explosions.remove(self)

        if self.sprite.collide_point(self.scene.pig.sprite.center):
            self.scene.pig.alive = False




class Bomb(object):

    def __init__(self, scene):
        self.scene = scene
        self.sprite = self.scene.bomb_sprite.copy()
        self.scene.bombs.append(self)
        self.speed = 5



    def update(self):
        self.sprite.move(0, self.speed)

        if self.sprite.bottom < mindu.screen.bottom - 10:
            self.sprite.draw()

        else:
            self.scene.bombs.remove(self)
            explosion = Explosion(self.scene)
            explosion.sprite.center = self.sprite.center



@mindu.loop.on_iterate
class TitleScene(object):

    def __init__(self):
        self.music_channel = mindu.channels[0]
        self.effects_channel = mindu.channels[1]

        self.pig_ok_sound = mindu.Sound('sounds/pig-ok!.ogg')
        self.choir_sound = mindu.Sound('sounds/choir.ogg')
        self.music_sound = mindu.Sound('sounds/title-music.ogg')

        title_sprite = mindu.Label(
            text = 'Fire, Pig, Fire!',
            font = 'fonts/biting.ttf',
            size = 40,
            color = (1.0, 0.7, 0.7, 1.0),
            centerx = mindu.screen.centerx,
            top = mindu.screen.top + 20)

        logo_sprite = mindu.Image(
            file = 'images/logo.png',
            alpha = False,
            centerx = title_sprite.centerx,
            top = title_sprite.bottom + 20)

        message_sprite = mindu.Label(
            text = 'Press return to play',
            font = 'fonts/biting.ttf',
            size = 20,
            color = (1.0, 0.7, 0.7, 1.0),
            centerx = logo_sprite.centerx,
            top = logo_sprite.bottom + 20)

        self.sprites = (title_sprite, logo_sprite, message_sprite)

        self.music_channel.play(self.music_sound, -1, 0, 2000)
        self.effects_channel.play(self.choir_sound)

        mindu.screen.bright = 0.0
        mindu.loop.on_iterate(self.fadein)

    def fadein(self):
        for sprite in self.sprites: sprite.draw()
        mindu.screen.bright += 0.05
        if mindu.screen.bright == 1.0: mindu.loop.on_iterate(self.inside)

    def inside(self):
        for sprite in self.sprites: sprite.draw()
        if mindu.keyboard.get() == 'return':
            self.effects_channel.play(self.pig_ok_sound)
            self.music_channel.fadeout(2000)
            mindu.loop.on_iterate(self.fadeout)

    def fadeout(self):
        for sprite in self.sprites: sprite.draw()
        mindu.screen.bright -= 0.05
        if mindu.screen.bright == 0.0:
            if not self.music_channel.busy():
                if not self.effects_channel.busy():
                    mindu.loop.on_iterate(MainScene)



class MainScene(object):

    def __init__(self):
        self.music_channel = mindu.channels[0]
        self.explosion_channel = mindu.channels[1]
        self.fire_channel = mindu.channels[2]
        self.pig_channel = mindu.channels[3]

        self.music_sound = mindu.Sound('sounds/main-music.ogg')
        self.explosion_sound = mindu.Sound('sounds/explosion.ogg')
        self.fire_sound = mindu.Sound('sounds/fire.ogg')
        self.fire_echo_sound = mindu.Sound('sounds/fire-echo.ogg')
        self.pig_ok_sound = mindu.Sound('sounds/pig-ok!.ogg')
        self.pig_ah_sound = mindu.Sound('sounds/pig-ah!.ogg')

        self.background_sprite = mindu.Image(
            file = 'images/background.png',
            alpha = False)

        self.game_over_sprite = mindu.Label(
            text = 'Game over',
            font = 'fonts/biting.ttf',
            size = 40,
            color = (1.0, 0.0, 0.0, 1.0),
            centerx = mindu.screen.centerx,
            bottom = mindu.screen.centery - 10,
            osd = True)

        self.message_sprite = mindu.Label(
            text = 'Press return to continue',
            font = 'fonts/biting.ttf',
            size = 20,
            color = (1.0, 0.0, 0.0, 1.0),
            centerx = self.game_over_sprite.centerx,
            top = self.game_over_sprite.bottom + 20,
            osd = True)

        self.ship_sprite = mindu.Image(
            file = 'images/ship.png',
            right = mindu.screen.left,
            top = mindu.screen.top + 10)

        self.sparks_sprite = mindu.Animation(
            directory = 'animations/sparks',
            osd = True,
            redraw = 5,
            anchor = 'center')

        self.bomb_sprite = mindu.Image('images/bomb.png')

        self.explosion_sprite = mindu.Animation(
            directory = 'animations/explosion',
            osd = True,
            redraw = 2,
            repeat = False,
            anchor = 'center')

        self.score_sprite = mindu.Label(
            text = 'Score: 0',
            font = 'fonts/biting.ttf',
            size = 20,
            color = (1.0, 0.0, 0.0, 1.0),
            osd = True,
            left = mindu.screen.left + 10,
            bottom = mindu.screen.bottom - 10)

        self.ships = []
        self.bombs = []
        self.explosions = []

        self.ship_reload = 15
        self.ship_reload_control = self.ship_reload
        self.score = 0

        self.pig = Pig(self)
        self.fire = Fire(self)

        self.music_channel.play(self.music_sound, -1)
        mindu.loop.on_iterate(self.fadein)



    def fadein(self):
        self.background_sprite.draw()
        self.pig.sprite.draw()
        self.score_sprite.draw()
        mindu.screen.bright += 0.05
        if mindu.screen.bright == 1.0: mindu.loop.on_iterate(self.inside)

    def inside(self):
        Ship(self)

        self.background_sprite.draw()

        for ship in self.ships: ship.update()
        for bomb in self.bombs: bomb.update()
        for explosion in self.explosions: explosion.update()

        self.pig.update()
        self.fire.update()

        self.score_sprite.draw()

        mindu.screen.red -= 0.00005
        mindu.screen.green -= 0.00005

        if not self.pig.alive:
            self.fire_channel.stop()
            self.music_channel.fadeout(2000)
            self.pig_channel.play(self.pig_ah_sound)
            mindu.loop.on_iterate(self.zoomin)

    def zoomin(self):
        self.background_sprite.draw()
        self.pig.update()
        self.score_sprite.draw()

        mindu.screen.zoom += 0.05
        mindu.screen.zcenter = self.pig.sprite.center

        if mindu.screen.zoom == 1.0: mindu.loop.on_iterate(self.game_over)

    def game_over(self):
        self.background_sprite.draw()
        self.game_over_sprite.draw()
        self.message_sprite.draw()
        self.score_sprite.draw()
        if mindu.keyboard.get() == 'return':
            self.pig_channel.play(self.pig_ok_sound)
            self.screenshot = mindu.screen.get_last_frame()
            self.screenshot.draw()
            mindu.screen.red = 1.0
            mindu.screen.green = 1.0
            mindu.screen.zoom = 0.0
            mindu.loop.on_iterate(self.fadeout)

    def fadeout(self):
        self.screenshot.draw()
        mindu.screen.bright -= 0.05
        if mindu.screen.bright == 0.0:
            if not self.explosion_channel.busy():
                if not self.pig_channel.busy():
                    mindu.loop.on_iterate(TitleScene)



mindu.loop.start()



