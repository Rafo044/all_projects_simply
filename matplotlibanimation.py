import numpy as np
from matplotlib.animation import FuncAnimation
import geopandas as gpd
from IPython import display
import numpy as np

shapefile_path = '/data/World_Countries_Generalized.shp'
world = gpd.read_file(shapefile_path)
# create random color
def random_color():
    return np.random.rand(3,)

# Animation
def update(frame):
    world['color'] = [random_color() for _ in range(len(world))]
    ax.clear()
    world.plot(ax=ax, color=world['color'])
    ax.set_title('Dunya Xeritesi  {}'.format(frame))

# empty map
fig, ax = plt.subplots(figsize=(10, 6))

# FuncAnimation create
ani = FuncAnimation(fig, update, frames=range(10), interval=500)

# converting to an html5 video
video = ani.to_html5_video()
  
# embedding for the video
html = display.HTML(video)
  
# draw the animation
display.display(html)
plt.close()
