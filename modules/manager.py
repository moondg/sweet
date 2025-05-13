import matplotlib
import matplotlib.pyplot as plt
import os

from modules.data import Data
from modules.findData import findData
from modules.drawer import Drawer
from modules.saveData import save

class Manager():
    def __init__(self,dir:str):
        self.dir = dir
        self.filePaths = findData(dir)
        self.datas = [Data(filePath) for filePath in self.filePaths]
        self.idx = 0

    def setPlot(self):
        matplotlib.use('webagg')
        self.fig, self.ax = plt.subplots()
        self.drawer = Drawer(self.fig,self.ax)
        plt.subplots_adjust(bottom=0.25)
        self.fig.canvas.mpl_connect('scroll_event', self.onScroll)
        self.fig.suptitle(self.dir)
        self.show()
        plt.show()

    def check(self):
        print("Your first few files are")
        for i in range(5): print(f"\t{self.datas[i].fileName}")
        print("\t...\nCheck before analyze!")

    def analyze(self):
        for data in self.datas: data.analyze()

    def show(self):
        self.drawer.draw(self.datas[self.idx])

    def save(self):
        if not os.listdir(os.getcwd()).__contains__('analysis'):
            os.mkdir(os.path.join(os.getcwd(),'analysis'))
        save(datas=self.datas,nameAs=self.dir)

    def isNextAvailable(self) -> bool: return self.idx < len(self.datas) - 1
    def isPrevAvailable(self) -> bool: return 0 < self.idx

    def showNext(self):
        self.idx = self.idx + 1
        self.show()

    def showPrev(self):
        self.idx = self.idx - 1
        self.show()

    def onScroll(self,event):
        if event.button == 'up':
            if self.isPrevAvailable():
                self.showPrev()
        elif event.button == 'down':
            if self.isNextAvailable():
                self.showNext()
            else:
                plt.close()
                self.save()
