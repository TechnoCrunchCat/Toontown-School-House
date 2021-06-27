from panda3d.core import *
import SafeZoneLoader
import DLPlayground

class DLSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):

    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.playgroundClass = DLPlayground.DLPlayground
        self.musicFile = 'phase_8/audio/bgm/Donalds Dreamland - Playground.ogg'
        self.activityMusicFile = 'phase_8/audio/bgm/Donalds Dreamland - Interior.ogg'
        self.dnaFile = 'phase_8/dna/donalds_dreamland_sz.dna'
        self.safeZoneStorageDNAFile = 'phase_8/dna/storage_DL_sz.dna'
