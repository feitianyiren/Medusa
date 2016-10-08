from src.LoadResources import *
from src.Player import *
from src.Sprite import *
from src.Key import *
from src.BarUI import *

class HUD:
    def __init__(self, player):
        self.player = player

        self.life_spr = Sprite(ImageEnum.HUD_LIFE)
        self.energy_spr = Sprite(ImageEnum.HUD_ENERGY)

        self.life_spr.set_location((32, 0))
        self.energy_spr.set_location((32, 32))

        self.life_bar = BarUI((64,2),(238,36,38),28,3)
        self.energy_bar = BarUI((64,34),(107,205,104),28,3)

        self.blink_spr = Sprite(ImageEnum.CAN_BLINK)
        self.no_blink_spr = Sprite(ImageEnum.NO_BLINK)

        self.key_spr = []
        for i in range(KeyEnum.NUM.value):
            self.key_spr.append(Sprite(KeySprites[i]))

    def draw(self, screen):
        self.life_spr.draw(screen, (0, 0))
        self.energy_spr.draw(screen,(0,0))

        self.life_bar.draw(screen, (0,0))
        self.energy_bar.draw(screen, (0,0))

        life_val = gFonts[0].render(str(self.player.health.health), True, (255,255,255))
        energy_val = gFonts[0].render(str(self.player.energy), True, (255, 255, 255))
        screen.blit(life_val, (0,5,32,32))
        screen.blit(energy_val,(0,37,32,32))

        for i in range(KeyEnum.NUM.value):
            self.key_spr[i].set_location((500, 0))

        for j in range(KeyEnum.NUM.value):
            for i in range(self.player.keys[j]):
                self.key_spr[j].draw(screen, (0, 0))
                for k in range(KeyEnum.NUM.value):
                    self.key_spr[k].move((32, 0))

        is_cooling_down = self.player.blink_component.state == BlinkState.COOLING_DOWN
        if is_cooling_down:
            self.no_blink_spr.set_location((screen.get_width() - 32, 0))
            self.no_blink_spr.draw(screen, (0, 0))
        elif not is_cooling_down:
            self.blink_spr.set_location((screen.get_width() - 32, 0))
            self.blink_spr.draw(screen, (0, 0))

    def update(self, deltatime):
        self.life_bar.update(self.player.health.health)
        self.energy_bar.update(self.player.energy)

