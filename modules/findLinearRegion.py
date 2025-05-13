import numpy as np
import modules.parameters as p

def findLinearRegion(yData):
    # smooth the data
    ySmooth = np.convolve(yData, np.ones(p.window_size)/p.window_size, mode='same')

    gradient = np.gradient(ySmooth)
    curvature = np.gradient(gradient)

    flatStart, flatEnd, linStart, linEnd = len(gradient), len(gradient), None, len(gradient)

    isFlatEnd = False
    for i,(c,g) in reversed(list(enumerate(zip(curvature,gradient)))):
        if not isFlatEnd and p.gradient_threshold < g:
            isFlatEnd = True
            flatStart = linEnd = i
        if p.curvature_threshold < c:
            linStart = i
            break

    return  linStart, linEnd, flatStart, flatEnd