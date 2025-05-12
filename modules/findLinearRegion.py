import numpy as np
import modules.parameters as p

def findLinearRegion(yData):
    # smooth the data
    ySmooth = np.convolve(yData, np.ones(p.window_size)/p.window_size, mode='valid')

    gradient = np.gradient(ySmooth)
    curvature = np.gradient(gradient)

    flatStart, flatEnd, linStart, linEnd = len(gradient), len(gradient), None, len(gradient)

    # iterate from back
    for i,(c,g) in enumerate(zip(np.flip(curvature), np.flip(gradient))):
        if g < p.gradient_threshold and i < 100:
            flatStart = flatStart - 1
            linEnd = flatStart
        if p.curvature_threshold < c:
            linStart = len(gradient) - i - 1
            break

    return  linStart, linEnd, flatStart, flatEnd