from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def plot_kvader(ax, kvader):
    a, b, c = kvader.a, kvader.b, kvader.c
    x_pos, y_pos, z_pos = kvader.pozicija

    vertices = np.array([[x_pos-a/2, y_pos-b/2, z_pos-c/2],
                     [x_pos+a/2, y_pos-b/2, z_pos-c/2],
                     [x_pos+a/2, y_pos+b/2, z_pos-c/2],
                     [x_pos-a/2, y_pos+b/2, z_pos-c/2],
                     [x_pos-a/2, y_pos-b/2, z_pos+c/2],
                     [x_pos+a/2, y_pos-b/2, z_pos+c/2],
                     [x_pos+a/2, y_pos+b/2, z_pos+c/2],
                     [x_pos-a/2, y_pos+b/2, z_pos+c/2]])

    faces = [[vertices[0], vertices[1], vertices[2], vertices[3]],
            [vertices[4], vertices[5], vertices[6], vertices[7]],
            [vertices[0], vertices[1], vertices[5], vertices[4]],
            [vertices[2], vertices[3], vertices[7], vertices[6]],
            [vertices[0], vertices[3], vertices[7], vertices[4]],
            [vertices[1], vertices[2], vertices[6], vertices[5]]]

    ax.add_collection3d(Poly3DCollection(faces, edgecolor='b', linewidths=1, alpha=0.5))



def plot_valj(ax, valj, num_points=100):
    r, h = valj.r, valj.h
    x_pos, y_pos, z_pos = valj.pozicija

    z = np.linspace(z_pos-h/2, z_pos+h/2, num_points)
    theta = np.linspace(0, 2*np.pi, num_points)
    theta_grid, z_grid = np.meshgrid(theta, z)
    x_grid = r*np.cos(theta_grid) + x_pos
    y_grid = r*np.sin(theta_grid) + y_pos

    if valj.os == "x":
        ax.plot_surface(z_grid, x_grid, y_grid, alpha=0.5)
    elif valj.os == "y":    
        ax.plot_surface(y_grid, z_grid, x_grid, alpha=0.5)
    elif valj.os == "z":
        ax.plot_surface(x_grid, y_grid, z_grid, alpha=0.5)




def plot_tocka(ax, tocka):
    x = tocka.pozicija[0]
    y = tocka.pozicija[1]
    z = tocka.pozicija[2]
    ax.scatter(x, y, z, s=25, c='red')