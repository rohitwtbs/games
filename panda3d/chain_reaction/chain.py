from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import Point3, VBase4, Vec3
from panda3d.core import AmbientLight, DirectionalLight
from panda3d.core import CollisionTraverser, CollisionHandlerQueue
from panda3d.core import CollisionNode, CollisionSphere
from panda3d.core import LPoint3

class ChainReactionGame(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Disable the default camera trackball controls.
        self.disableMouse()

        # Load the environment model.
        self.environ = self.loader.loadModel("models/environment")
        self.environ.reparentTo(self.render)

        # Scale and position the model.
        self.environ.setScale(0.25, 0.25, 0.25)
        self.environ.setPos(-8, 42, 0)

        # Set up lighting.
        self.setupLighting()

        # Task to update the game
        self.taskMgr.add(self.update, "update")

        # Create a list to store spheres
        self.spheres = []

        # Add the initial sphere
        self.addSphere(Point3(0, 10, 0))

        # Setup collision detection
        self.cTrav = CollisionTraverser()
        self.cHandler = CollisionHandlerQueue()

        self.accept('mouse1', self.onMouseClick)

    def setupLighting(self):
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor(VBase4(0.3, 0.3, 0.3, 1))
        self.render.setLight(self.render.attachNewNode(ambientLight))

        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(Vec3(-5, -5, -5))
        directionalLight.setColor(VBase4(1, 1, 1, 1))
        self.render.setLight(self.render.attachNewNode(directionalLight))

    def addSphere(self, position):
        sphere = self.loader.loadModel("models/ball")
        sphere.reparentTo(self.render)
        sphere.setPos(position)
        sphere.setScale(0.5)
        self.spheres.append(sphere)

        # Add collision node to sphere
        cNode = CollisionNode('sphere')
        cNode.addSolid(CollisionSphere(0, 0, 0, 0.5))
        cNodePath = sphere.attachNewNode(cNode)
        self.cTrav.addCollider(cNodePath, self.cHandler)

    def onMouseClick(self):
        if self.mouseWatcherNode.hasMouse():
            mpos = self.mouseWatcherNode.getMouse()
            pos3d = Point3()
            nearPoint = Point3()
            farPoint = Point3()
            self.camLens.extrude(mpos, nearPoint, farPoint)

            if self.environ.getBounds().intersectsLine(pos3d, nearPoint, farPoint):
                pos3d = self.render.getRelativePoint(self.cam, nearPoint)
                self.addSphere(pos3d)

    def update(self, task):
        # Check for collisions
        self.cTrav.traverse(self.render)
        for entry in self.cHandler.entries:
            self.handleCollision(entry)

        return Task.cont

    def handleCollision(self, entry):
        sphere1 = entry.getFromNodePath().getParent()
        sphere2 = entry.getIntoNodePath().getParent()

        if sphere1 in self.spheres and sphere2 in self.spheres:
            self.spheres.remove(sphere1)
            sphere1.removeNode()
            self.spheres.remove(sphere2)
            sphere2.removeNode()
            self.createChainReaction(sphere1.getPos())

    def createChainReaction(self, position):
        # Create new spheres around the position of the collision
        offsets = [Point3(1, 0, 0), Point3(-1, 0, 0), Point3(0, 1, 0), Point3(0, -1, 0)]
        for offset in offsets:
            self.addSphere(position + offset)

game = ChainReactionGame()
game.run()
