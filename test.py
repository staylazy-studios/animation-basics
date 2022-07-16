from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from panda3d.core import PointLight

import simplepbr

class Scene(ShowBase):
    def __init__(self):
        super().__init__()
        self.pipeline = simplepbr.init()

        self.actor = Actor("animation.glb")
        self.actor.reparentTo(self.render)

        self.actor.loop("jumpscare")

        plight = PointLight("plight")
        plnp = self.render.attachNewNode(plight)
        plnp.setPos(0, -5, 5)
        self.render.setLight(plnp)

game = Scene()
game.run()