## Solving poisson equation in 2D
## May 2020.

# importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# variables and discritization parameters
nt=400
nx=101
ny=101

dx=2/(nx-1)
dy=2/(ny-1)

x = np.linspace(0, 2, nx)
y = np.linspace(0, 2, ny)

#initial state of u=0 everywhere
u=np.zeros((ny,nx))
un=np.zeros((ny,nx))
uf=np.zeros((nt,nx,ny))

# The source term of poisson equation

b=np.zeros((nx,ny))
b[int(0.4 / dy):int(0.6 / dy + 1),int(0.4 / dx):int(0.6 / dx + 1)]=200
b[int(1.4 / dy):int(1.6 / dy + 1),int(1.4 / dx):int(1.6 / dx + 1)]=-200



###(ploting Source term)
fig = plt.figure(figsize=(11, 7), dpi=100)
ax = fig.gca(projection='3d')
X, Y = np.meshgrid(x, y)
ax.plot_surface(X, Y, b[:], cmap=cm.jet)
plt.title('U')
plt.xlabel('X')
plt.ylabel('Y');
fig.savefig('b.png', bbox_inches='tight')

    # loop for u
for n in range(nt):
    un=u.copy()
    for i in range(1,nx-1):
        for j in range(1,ny-1):
            u[i,j]=((un[i,j-1]+un[i,j+1])*(dx**2) + (un[i-1,j]+un[i+1,j])*(dy**2) - b[i,j]*(dx**2) * (dy**2))/(2*(dx**2 + dy**2))

    # # boundary conditions  u = 0 at x= 0, 2 and y= 0, 1
    u[:, 0] = 0
    u[:, -1] = 0
    u[0, :] = 0
    u[-1, :] =0

    # plotting U field as a Surface

fig = plt.figure(figsize=(11, 7), dpi=100)
ax = fig.gca(projection='3d')
X, Y = np.meshgrid(x, y)
ax.plot_surface(X, Y, u, cmap=cm.jet)
fig.savefig('U.png', bbox_inches='tight')