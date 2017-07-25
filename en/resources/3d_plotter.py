from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from skimage import io, color

map_rgb = io.imread("../images/colour_map.png")
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x =50
y =50
z =50

a= 200
b= 50
c= 50

e=150
f=150
g=150

#single pixel from selfie
ax.scatter(x, y, z, c=[x/255,y/255,z/255], marker='o', s=1000)

# for row in map_rgb:
#     for pixel in row:
#         x, y, z = pixel
#         ax.scatter(x, y, z, c=[x/255,y/255,z/255], marker='o', s=100)
    
ax.scatter(a, b, c, c=[a/255,b/255,c/255], marker='o', s=1000)
ax.scatter(e, f, g, c=[e/255,f/255,g/255], marker='o', s=1000)
ax.set_xlim3d(0, 255)
ax.set_ylim3d(0, 255)
ax.set_zlim3d(0, 255)

ax.set_xlabel('RED', color='red')
ax.set_ylabel('GREEN', color = 'green')
ax.set_zlabel('BLUE', color= 'blue')

plt.show()

