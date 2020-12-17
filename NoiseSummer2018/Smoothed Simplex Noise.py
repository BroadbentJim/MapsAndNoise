from opensimplex import OpenSimplex
import matplotlib.pyplot as plt
import numpy as np
import time

simplex = OpenSimplex()
width = 512
height = 1024
Map = np.zeros((width, height))

def sumOctave(num_iterations, x, y, persistence, scale, low, high):
    maxAmp = 0
    amp = 1
    freq = scale
    noise = 0

    #Successively smaller, high frequency terms
    for i in range(num_iterations):
        noise += simplex.noise2d(x * freq, y * freq) * amp
        maxAmp += amp
        amp *= persistence
        freq *= 2

    #Take the average value
    noise /= maxAmp

    #Normalise the result
    noise = noise * (high - low) / 2 + (high + low) / 2

    return noise

def main():
    scale = 0.007
    for x in range(width):
        print("Row Down:", x)
        for y in range(height):
            dx = sumOctave(16, x, y, .5, scale, 0, 255)
            dy = sumOctave(16, x+3, y+4, .5, scale, 0, 255)
            d2x = sumOctave(4, x+4*dx, y+4*dy, .5, scale, 0, 255)
            d2y = sumOctave(4, x+4*dx+4, y+4*dy+3, .5, scale, 0, 255)
            # noise = sumOctave(16, x, y + 4, .5, scale, 0, 255) #Warpless

            noise = sumOctave(16, x+2*d2x+4*dx, y+2*d2y+4*dy, .5, scale, 0, 255)
            Map[x][y] = noise + 7 * (dx + dy)

start = time.time()
main()
finish= time.time()
elapsed_time = finish-start
print("Time taken: ", elapsed_time)
plt.imshow(Map, cmap='gray')
plt.show()
