import numpy as np
import os

from modules.shot import Shot
from modules.findLinearRegion import findLinearRegion
import modules.parameters as p

class Data:
    def __init__(self,filePath):
        self.shot = Shot(filePath)
        self.filePath = filePath
        self.fileName = os.path.basename(filePath)
        self.attachZ = self.shot.attachZ
        self.attachSignal = self.shot.attachSignal
        self.detachZ = self.shot.detachZ
        self.detachSignal = self.shot.detachSignal
        self.analyze()

    def analyze(self):
        self.linStart, self.linEnd, self.flatStart, self.flatEnd = findLinearRegion(self.attachSignal)
        if self.linStart == None: self.linStart = 0
        else:
            minSearchStart = max(0,self.linStart - p.minimum_search_range)
            minSearchEnd = self.linStart + p.minimum_search_range
            self.linStart = minSearchStart + np.argmin(self.attachSignal[minSearchStart:minSearchEnd])
        if self.linEnd == None: self.linEnd = -1
        self.slope = (self.attachSignal[self.linEnd-5]-self.attachSignal[self.linEnd-5-p.minimum_search_range])/(self.attachZ[self.linEnd-5]-self.attachZ[self.linEnd-5-p.minimum_search_range])
        self.force = self.detachSignal[self.linStart]-self.attachSignal[self.linStart]