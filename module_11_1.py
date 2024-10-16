#import matplotlib
#from mpl_toolkits.mplot3d import Axes3D
#from matplotlib.tri import Triangulation
import matplotlib.pyplot as plt
import numpy


def makeData ():
    # Строим сетку в интервале от -10 до 10, имеющую 100 отсчетов по обеим координатам
    x = numpy.linspace (-10, 10, 100)
    y = numpy.linspace (-10, 10, 100)

    # Создаем двумерную матрицу-сетку
    xgrid, ygrid = numpy.meshgrid(x, y)

    # В узлах рассчитываем значение функции
    z = numpy.sin (xgrid) * numpy.sin (ygrid) / (xgrid * ygrid)
    return xgrid, ygrid, z


if __name__ == '__main__':
    x, y, z = makeData()
    fig = plt.figure()
    axes = fig.add_subplot(projection='3d')
    plt.title(r'$f_1(x)=\sin(x),\ f_2(x)=\cos(x),\ f_3(x)=-x$')
    # !!!
    axes.plot_surface(x, y, z)

    # плоский график


    fig, ax = plt.subplots()  # Create a figure containing a single Axes.
    ax.plot([1, 2, 3, 4], [1, 4, 2, 3])

    #ещё один
    sp = plt.subplot(224)
    plt.plot(x, x)
    sp.spines['left'].set_position('center')
    sp.spines['bottom'].set_position('center')
    plt.title(r'$x$')
    # полярные координаты
    # plt.subplot(111, polar=True)
    # phi = numpy.arange(0, 2 * numpy.pi, 0.01)
    # rho = 2 * phi
    # plt.plot(phi, rho, lw=2)
    # plt.show()
    plt.show()

    # формула

    mu, sigma = 100, 15
    #x = mu + sigma * numpy.random.randn(10000)
    # the histogram of the data
    #n, bins, patches = plt.hist(x, 50, density=True, facecolor='g', alpha=0.75)

    # plt.xlabel('Smarts')
    # plt.ylabel('Probability')
    # plt.title('Histogram of IQ')
    plt.text(60, .030, r'$\mu=100,\ \sigma=15$')
    plt.text(50, .033,
             r'$\varphi_{\mu,\sigma^2}(x) = \frac{1}{\sigma\sqrt{2\pi}} \,e^{ -\frac{(x- \mu)^2}{2\sigma^2}} = \frac{1}{\sigma} \varphi\left(\frac{x - \mu}{\sigma}\right),\quad x\in\mathbb{R}$',
             fontsize=20, color='red')
    plt.axis([40, 160, 0, 0.04])
    #plt.grid(True)
    plt.show()

    print(numpy.log(3) / numpy.log(2))



# def f(x, y):
#     return np.sin(np.sqrt(x ** 2 + y ** 2))
#
#
# x = np.linspace(-6, 6, 30)
# y = np.linspace(-6, 6, 30)
# X, Y = np.meshgrid(x, y)
# Z = f(X, Y)
#
# tri = Triangulation(X.ravel(), Y.ravel())
#
# fig = plt.figure(figsize=(10, 8))
# ax = fig.add_subplot(111, projection='3d')
#
# ax.plot_trisurf(tri, Z.ravel(), cmap='cool', edgecolor='none', alpha=0.8)
#
# ax.set_title('Surface Triangulation Plot of f(x, y) =\
#                 sin(sqrt(x^2 + y^2))', fontsize=14)
# ax.set_xlabel('x', fontsize=12)
# ax.set_ylabel('y', fontsize=12)
# ax.set_zlabel('z', fontsize=12)
#
# plt.show()
