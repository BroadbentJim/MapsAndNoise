import numpy as np
from scipy.spatial import Voronoi,voronoi_plot_2d, Delaunay
import matplotlib.pyplot as plt

points = np.random.rand(1000,2)

points = np.append(points, [[-999,999], [-999,999], [999, -999], [999,999]], axis =0)

vor = Voronoi(points)

voronoi_plot_2d(vor, show_vertices=False, show_points=False)

for region in vor.regions:
    if not -1 in region:
        polygon = [vor.vertices[i] for i in region]
        plt.fill(*zip(*polygon))

plt.xlim([0,1])
plt.ylim([0,1])
plt.show()