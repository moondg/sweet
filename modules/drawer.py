from matplotlib.widgets import Slider

from modules.data import Data
import modules.parameters as p


class Drawer:
    def __init__(self,fig,ax):
        self.fig, self.ax = fig, ax
        slider_ax = self.fig.add_axes([0.35, 0.17, 0.45, 0.03])
        self.gt_slider = Slider(slider_ax, 'Gradient Thdsreshold', 0, 0.1, valinit=p.gradient_threshold)
        slider_ax = self.fig.add_axes([0.35, 0.12, 0.45, 0.03])
        self.ct_slider = Slider(slider_ax, 'Curvature Thdsreshold', 0, 1, valinit=p.curvature_threshold)
        slider_ax = self.fig.add_axes([0.35, 0.07, 0.45, 0.03])
        self.msr_slider = Slider(slider_ax, 'Minimum-Searching Range', 1, 100, valinit=p.minimum_search_range, valstep=1)
        slider_ax = self.fig.add_axes([0.35, 0.02, 0.45, 0.03])
        self.ws_slider = Slider(slider_ax, 'Moving Avg Window Size', 2, 20, valinit=p.window_size, valstep=1)
        self.gt_slider.on_changed(self.update_gt)
        self.ct_slider.on_changed(self.update_ct)
        self.msr_slider.on_changed(self.update_msr)
        self.ws_slider.on_changed(self.update_ws)


    def draw(self,data:Data):
        self.data = data
        self.ax.clear()
        self.ax.axvline(data.attachZ[data.linStart], color='r', linestyle='dashed')
        self.ax.axvline(data.attachZ[data.linEnd], color='b', linestyle='dashed')
        self.ax.scatter(data.attachZ,data.attachSignal,s=3,color='orange')
        self.ax.scatter(data.detachZ,data.detachSignal,s=3,color='g')
        self.ax.set_title(f'{data.fileName}')
        self.fig.canvas.draw_idle()

    def update_gt(self,val):
        p.gradient_threshold = val
        self.data.analyze()
        self.draw(self.data)

    def update_ct(self,val):
        p.curvature_threshold = val
        self.data.analyze()
        self.draw(self.data)

    def update_msr(self,val):
        p.minimum_search_range = val
        self.data.analyze()
        self.draw(self.data)

    def update_ws(self,val):
        p.window_size = val
        self.data.analyze()
        self.draw(self.data)