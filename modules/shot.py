import os

from modules.parseData import parseData

class Shot:
    def __init__(self,filePath):
        self.filePath = filePath
        self.fileName = os.path.basename
        [self.attachZ, self.attachSignal, self.detachZ, self.detachSignal] = parseData(self.filePath)