import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.special import sph_harm
from matplotlib import cm
import time


def Ylm(m, l, PHI, THETA):
    return sph_harm(m, l, PHI, THETA)


while True:
    l = - 99999.666
    while l < 0 or m < -l or m > l:
        if l != -99999.666:
            print('Error:Please check the quantum number.')
        l, m = map(int, input('l m = ').split())

    theta = np.linspace(0, np.pi, 180)
    phi = np.linspace(0, 2 * np.pi, 180)

    THETA, PHI = np.meshgrid(theta, phi)

    Y = Ylm(m, l, PHI, THETA)

    xyz = np.array([np.sin(THETA) * np.cos(PHI),
                    np.sin(THETA) * np.sin(PHI),
                    np.cos(THETA)])

    if m > 0:
        Y = np.sqrt(2) * Y.real
    elif m < 0:
        Y = np.sqrt(2) * Y.imag
    elif m == 0:
        Y = Y.real

    Wfn = np.abs(Y) * xyz
    # 这里只有加上绝对值才能使球谐函数的正负部分都显示出来，具体原因还在研究
    #  Wfn = Y * xyz
    Orb = Y ** 2 * xyz
    colormap = cm.ScalarMappable(cmap='rainbow')
    # 按照球谐函数的正负值进行染色

    fig = plt.figure(figsize=(16, 8))
    sp = fig.add_subplot(121, projection='3d')
    sp.set_title('Real Spherical Harmonic Function')
    sp.get_proj = lambda: np.dot(Axes3D.get_proj(sp), np.diag([0.75, 0.75, 1, 1]))
    sp.set_xlabel('X')
    sp.set_ylabel('Y')
    sp.set_zlabel('Z')
    plot = sp.plot_surface(
        Wfn[0], Wfn[1], Wfn[2], rstride=1, cstride=1, facecolors=colormap.to_rgba(Y.real),
        linewidth=0)
    # print(Wfn[0].max(), Wfn[1].max(), Wfn[2].max())
    l_1 = [Wfn[0].max(), Wfn[1].max(), Wfn[2].max()]
    max1 = max(l_1)
    sp.set_xlim(-max1 * 1.5, max1 * 1.5)
    sp.set_ylim(-max1 * 1.5, max1 * 1.5)
    sp.set_zlim(-max1 * 1.5, max1 * 1.5)

    spd = fig.add_subplot(122, projection='3d')
    spd.get_proj = lambda: np.dot(Axes3D.get_proj(spd), np.diag([0.75, 0.75, 1, 1]))
    # 原本的z方向坐标格子被稍微有点压扁了，用这一行代码可以让它正常。
    spd.set_title('Electron Cloud')
    spd.set_xlabel('X')
    spd.set_ylabel('Y')
    spd.set_zlabel('Z')
    plot = spd.plot_surface(Orb[0], Orb[1], Orb[2], rstride=1, cstride=1, facecolors=colormap.to_rgba(Y.real))
    l_2 = [Orb[0].max(), Orb[1].max(), Orb[2].max()]
    max2 = max(l_2)
    spd.set_xlim(-max2 * 1.5, max2 * 1.5)
    spd.set_ylim(-max2 * 1.5, max2 * 1.5)
    spd.set_zlim(-max2 * 1.5, max2 * 1.5)

    #  print(Orb[0].max(), Orb[1].max(), Orb[2].max())
    plt.show()

    print('Press Enter to exit or others to continue.')
    w = input()
    if w == '':
        break
    else:
        continue

print('exiting...')
time.sleep(1.2)
