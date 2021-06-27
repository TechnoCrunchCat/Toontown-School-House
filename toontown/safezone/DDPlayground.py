from panda3d.core import *
import Playground
from direct.task.Task import Task
import random
from direct.fsm import ClassicFSM, State
from direct.actor import Actor
from toontown.toonbase import ToontownGlobals
from direct.directnotify import DirectNotifyGlobal
from toontown.hood import Place

class DDPlayground(Playground.Playground):
    notify = DirectNotifyGlobal.directNotify.newCategory('DDPlayground')

    def __init__(self, loader, parentFSM, doneEvent):
        Playground.Playground.__init__(self, loader, parentFSM, doneEvent)
        self.cameraSubmerged = -1
        self.toonSubmerged = -1
        self.activityFsm = ClassicFSM.ClassicFSM('Activity', [State.State('off', self.enterOff, self.exitOff, ['OnBoat']), State.State('OnBoat', self.enterOnBoat, self.exitOnBoat, ['off'])], 'off', 'off')
        self.activityFsm.enterInitialState()

    def load(self): # everything loads with this function bracket
        Playground.Playground.load(self)
        self.piano = loader.loadModel('phase_6/models/props/piano') # This lines loads our piano prop
        self.piano.reparentTo(render) # This line makes our piano prop a child node to the render
        self.piano.setPos(0, 0, 10) # This line sets the coordinates of our piano prop to 0x 0y and 10z

        self.piano.setHpr(250, 15, 10) #This line sets the roation of the pinao #firstvalue-leftandright,secondvalue-upanddown,thirdvalue-plane
        self.piano.setColorScale(1, 0, 0, 1) # This line sets the color of the piano #RGB+Transparency vaule

        self.apple = loader.loadModel('phase_4/models/minigames/apple')
        self.apple.reparentTo(self.piano) #This line makes our apple prop a child node of the piano prop #This means any child nodes of the pinao prop will also have the exact same attrutbutes as the parent node
        self.apple.setScale(5) # This line sets the scale of the apple

    def unload(self): # everything unloads with this function bracket, everything unloads when you leave
        self.piano.removeNode() # This line tells the game to ready the pinao child node to be unload when called to
        del self.piano # This tells the ready piano node to unload itself
        self.apple.removeNode()
        del self.apple

        del self.activityFsm
        Playground.Playground.unload(self)

    def enter(self, requestStatus):
        self.nextSeagullTime = 0
        taskMgr.add(self.__seagulls, 'dd-seagulls')
        self.loader.hood.setWhiteFog()
        Playground.Playground.enter(self, requestStatus)

    def exit(self):
        Playground.Playground.exit(self)
        taskMgr.remove('dd-check-toon-underwater')
        taskMgr.remove('dd-check-cam-underwater')
        taskMgr.remove('dd-seagulls')
        self.loader.hood.setNoFog()

    def enterStart(self):
        self.cameraSubmerged = 0
        self.toonSubmerged = 0
        taskMgr.add(self.__checkToonUnderwater, 'dd-check-toon-underwater')
        taskMgr.add(self.__checkCameraUnderwater, 'dd-check-cam-underwater')

    def enterDoorOut(self):
        taskMgr.remove('dd-check-toon-underwater')

    def exitDoorOut(self):
        pass

    def enterDoorIn(self, requestStatus):
        Playground.Playground.enterDoorIn(self, requestStatus)
        taskMgr.add(self.__checkToonUnderwater, 'dd-check-toon-underwater')

    def __checkCameraUnderwater(self, task):
        if camera.getZ(render) < 1.0:
            self.__submergeCamera()
        else:
            self.__emergeCamera()
        return Task.cont

    def __checkToonUnderwater(self, task):
        if base.localAvatar.getZ() < -2.3314585:
            self.__submergeToon()
        else:
            self.__emergeToon()
        return Task.cont

    def __submergeCamera(self):
        if self.cameraSubmerged == 1:
            return
        self.loader.hood.setUnderwaterFog()
        base.playSfx(self.loader.underwaterSound, looping=1, volume=0.8)
        self.loader.seagullSound.stop()
        taskMgr.remove('dd-seagulls')
        self.cameraSubmerged = 1
        self.walkStateData.setSwimSoundAudible(1)

    def __emergeCamera(self):
        if self.cameraSubmerged == 0:
            return
        self.loader.hood.setWhiteFog()
        self.loader.underwaterSound.stop()
        self.nextSeagullTime = random.random() * 8.0
        taskMgr.add(self.__seagulls, 'dd-seagulls')
        self.cameraSubmerged = 0
        self.walkStateData.setSwimSoundAudible(0)

    def __submergeToon(self):
        if self.toonSubmerged == 1:
            return
        base.playSfx(self.loader.submergeSound)
        if base.config.GetBool('disable-flying-glitch') == 0:
            self.fsm.request('walk')
        self.walkStateData.fsm.request('swimming', [self.loader.swimSound])
        pos = base.localAvatar.getPos(render)
        base.localAvatar.d_playSplashEffect(pos[0], pos[1], 1.675)
        self.toonSubmerged = 1

    def __emergeToon(self):
        if self.toonSubmerged == 0:
            return
        self.walkStateData.fsm.request('walking')
        self.toonSubmerged = 0

    def __seagulls(self, task):
        if task.time < self.nextSeagullTime:
            return Task.cont
        base.playSfx(self.loader.seagullSound)
        self.nextSeagullTime = task.time + random.random() * 4.0 + 8.0
        return Task.cont

    def enterTeleportIn(self, requestStatus):
        self.toonSubmerged = -1
        taskMgr.remove('dd-check-toon-underwater')
        Playground.Playground.enterTeleportIn(self, requestStatus)

    def teleportInDone(self):
        self.toonSubmerged = -1
        taskMgr.add(self.__checkToonUnderwater, 'dd-check-toon-underwater')
        Playground.Playground.teleportInDone(self)

    def enterOff(self):
        return None

    def exitOff(self):
        return None

    def enterOnBoat(self):
        base.localAvatar.b_setParent(ToontownGlobals.SPDonaldsBoat)
        base.playSfx(self.loader.waterSound, looping=1)

    def exitOnBoat(self):
        base.localAvatar.b_setParent(ToontownGlobals.SPRender)
        self.loader.waterSound.stop()
