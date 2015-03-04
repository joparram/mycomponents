from laserViewerUI import *
from PySide import QtGui, QtCore
import threading
import sys
import math

__author__ = 'jose'


class laserViewer(QtGui.QDialog, threading.Thread):
    def __init__(self, parent=None):
        threading.Thread.__init__(self)
        # variables
        self.maxSize = 10
        self.scale = 4
        self.threshold = 1000
        self.VPoints = [2500, 3000, 3000, 800, 2300, 3000, 1000]
        self.lock = threading.Lock()
        # 1 metro = scaleY * scale
        self.scaleY = 20
        self.scaleX = 40
        #gui
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Dialog_main()
        self.ui.setupUi(self)
        #self.scene=QGraphicsScene(QtCore.QRect(0, 0, 800, 350))
        self.WIDTH1 = QtCore.QRect(self.ui.graphicsView.geometry()).getCoords()[2] - \
                      QtCore.QRect(self.ui.graphicsView.geometry()).getCoords()[0] - 10
        self.HEIGHT1 = QtCore.QRect(self.ui.graphicsView.geometry()).getCoords()[3] - \
                       QtCore.QRect(self.ui.graphicsView.geometry()).getCoords()[1] - 10
        self.WIDTH2 = QtCore.QRect(self.ui.graphicsView_screen.geometry()).getCoords()[2] - \
                      QtCore.QRect(self.ui.graphicsView_screen.geometry()).getCoords()[0] - 10
        self.HEIGHT2 = QtCore.QRect(self.ui.graphicsView_screen.geometry()).getCoords()[3] - \
                       QtCore.QRect(self.ui.graphicsView_screen.geometry()).getCoords()[1] - 10
        self.scene = QtGui.QGraphicsScene(QtCore.QRect(0, 0, self.WIDTH1, self.HEIGHT1))
        self.scene_screen = QtGui.QGraphicsScene(QtCore.QRect(0, 0, self.WIDTH2, self.HEIGHT2))
        self.ui.graphicsView.setScene(self.scene)
        self.ui.graphicsView_screen.setScene(self.scene_screen)
        self.drawCoordinateSystem()

    def drawCoordinateSystem(self):
        i = self.HEIGHT1 - self.scale * 5
        j = 10
        k = self.maxSize
        while i > 0:
            if j < 1:
                j = 10
                k = self.maxSize
            self.scene.addLine(0, i, k, i)
            k = self.maxSize / 2
            i -= self.scale
            j -= 1
        i = self.scale * 5 - 2
        j = 10
        k = self.maxSize
        while i < self.WIDTH1:
            if j < 1:
                j = 10
                k = self.maxSize
            self.scene.addLine(i, self.HEIGHT1 - k, i, self.HEIGHT1)
            k = self.maxSize / 2
            i += self.scale
            j -= 1

    def paintG(self):
        if len(self.VPoints) > 0:
            self.lock.acquire()
            getY = lambda x: self.HEIGHT2 - (x * self.scaleY * self.scale * 0.001)
            getX = lambda x: x * self.scale * 2
            self.scene_screen.clear()
            poly = QtGui.QPolygon(0)
            self.scene_screen.addLine(0, getY(self.threshold), self.WIDTH2, getY(self.threshold))
            for i in range(len(self.VPoints)):
                Y = getY(self.VPoints[i][0])
                if Y < 0:
                    Y = 0
                X = getX(i)
                poly.push_back(QtCore.QPoint(X, Y))

            path = QtGui.QPainterPath()
            path.addPolygon(poly)
            self.scene_screen.addPath(path)
            self.VPoints = []
            self.lock.release()

    def paintC(self):
        if len(self.VPoints) > 0:
            self.lock.acquire()
            getY = lambda x: self.HEIGHT2 - (x * self.scaleY * self.scale * 0.001) #entrada milimetros
            getX = lambda x: x * self.scale * self.scaleX * 0.001
            self.scene_screen.clear()
            poly = QtGui.QPolygon(0)
            for i in range(len(self.VPoints)):
                angle = self.VPoints[i][1]
                dist = self.VPoints[i][0]
                Y = getY(dist) * math.cos(angle)
                X = getX(dist) * math.sin(angle) + (self.WIDTH2/2)
                if Y < 0:
                    Y = 0
                Rect = QtGui.QGraphicsRectItem(X, Y, 2, 2)
                Rect.setBrush(QtGui.QBrush(QtGui.qRed(QtGui.qRgb(8888, 8, 8))))
                self.scene_screen.addItem(Rect)
                poly.push_back(QtCore.QPoint(X, Y))
            path = QtGui.QPainterPath()
            path.addPolygon(poly)
            self.scene_screen.addPath(path)
            self.VPoints = []
            self.lock.release()


    def updateG(self, VPoints):
        self.lock.acquire()
        self.VPoints = VPoints
        self.lock.release()

    def run(self, instance):
        pass


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    V = [(2499.761962890625, 1.5), (2506.220703125, 1.4700000286102295), (2514.98193359375, 1.440000057220459),
         (2526.086181640625, 1.409999966621399), (2539.58447265625, 1.3799999952316284),
         (2555.539794921875, 1.350000023841858),
         (2574.028076171875, 1.3200000524520874), (2595.138427734375, 1.2899999618530273),
         (2618.97412109375, 1.2599999904632568),
         (2645.65478515625, 1.2300000190734863), (2675.31689453125, 1.2000000476837158),
         (2708.11669921875, 1.1699999570846558),
         (2744.230712890625, 1.1399999856948853), (2783.8603515625, 1.1100000143051147),
         (2827.232666015625, 1.0800000429153442),
         (2874.60595703125, 1.0499999523162842), (2926.272216796875, 1.0199999809265137),
         (2982.562744140625, 0.9900000095367432),
         (1743.618408203125, 0.9600000381469727), (1672.7052001953125, 0.9300000071525574),
         (1608.7259521484375, 0.9000000357627869),
         (1550.8046875, 0.8700000047683716), (1498.2108154296875, 0.8400000333786011),
         (1518.734619140625, 0.8100000023841858),
         (1564.1009521484375, 0.7800000309944153), (1613.758056640625, 0.75), (1668.221923828125, 0.7200000286102295),
         (1728.1002197265625, 0.6899999976158142), (3156.3603515625, 0.6600000262260437),
         (3085.90966796875, 0.6299999952316284),
         (3021.1953125, 0.6000000238418579), (2961.749755859375, 0.5699999928474426),
         (2907.164306640625, 0.5400000214576721),
         (2857.0791015625, 0.5100000500679016), (2812.868408203125, 0.48000001907348633),
         (2769.179931640625, 0.45000001788139343),
         (2730.840087890625, 0.42000001668930054), (2697.5625, 0.39000001549720764),
         (2664.289306640625, 0.36000001430511475),
         (2635.717041015625, 0.33000001311302185), (2610.0751953125, 0.30000001192092896),
         (2587.233154296875, 0.27000004053115845),
         (823.6062622070312, 0.24000002443790436), (817.9700317382812, 0.21000002324581146),
         (813.1372680664062, 0.18000003695487976),
         (809.0851440429688, 0.15000003576278687), (805.7947387695312, 0.12000003457069397),
         (803.2509765625, 0.09000003337860107),
         (801.4421997070312, 0.06000003218650818), (800.3601684570312, 0.030000032857060432),
         (800.0, 3.3527612686157227e-08),
         (800.3601684570312, -0.02999996580183506), (801.4421997070312, -0.059999965131282806),
         (803.2509765625, -0.0899999663233757),
         (805.7947387695312, -0.119999960064888), (809.0851440429688, -0.1499999612569809),
         (813.1372680664062, -0.1799999624490738),
         (817.9700317382812, -0.2099999636411667), (823.606201171875, -0.23999996483325958),
         (2587.233154296875, -0.2699999511241913),
         (2610.074951171875, -0.2999999523162842), (2635.717041015625, -0.3299999535083771),
         (2664.289306640625, -0.35999995470046997), (2695.940673828125, -0.38999995589256287),
         (2730.840087890625, -0.41999995708465576), (2769.1796875, -0.44999995827674866),
         (2811.17724609375, -0.47999995946884155), (2857.078857421875, -0.5099999308586121),
         (2907.1640625, -0.5399999618530273), (2961.749755859375, -0.5699999332427979),
         (3021.195068359375, -0.5999999642372131), (3085.90966796875, -0.6299999356269836),
         (3156.35986328125, -0.6599999666213989), (1728.1002197265625, -0.6899999380111694),
         (1668.22216796875, -0.7199999690055847), (1613.758056640625, -0.7499999403953552),
         (1564.1009521484375, -0.7799999713897705), (1518.734619140625, -0.809999942779541),
         (1498.2108154296875, -0.8399999737739563), (1550.8046875, -0.8699999451637268),
         (1608.725830078125, -0.8999999761581421), (1672.7049560546875, -0.9299999475479126),
         (1743.6181640625, -0.9599999189376831), (2982.56298828125, -0.9899999499320984),
         (2926.272216796875, -1.0199999809265137), (2874.60595703125, -1.0499999523162842),
         (2827.23291015625, -1.0799999237060547), (2783.8603515625, -1.1099998950958252),
         (2744.230712890625, -1.1399999856948853), (2708.11669921875, -1.1699999570846558),
         (2675.31689453125, -1.1999999284744263), (2645.65478515625, -1.2299998998641968),
         (2618.97412109375, -1.2599999904632568), (2595.138427734375, -1.2899999618530273),
         (2574.028076171875, -1.3199999332427979), (2555.5400390625, -1.3499999046325684),
         (2539.58447265625, -1.3799998760223389), (2526.086181640625, -1.409999966621399),
         (2514.982177734375, -1.4399999380111694), (2506.220703125, -1.46999990940094)]
    C = [(2499.761962890625, 1.5), (2506.220703125, 1.4700000286102295), (2514.98193359375, 1.440000057220459),
         (2526.086181640625, 1.409999966621399), (2539.58447265625, 1.3799999952316284)]
    myapp = laserViewer()
    myapp.updateG(V)
    myapp.paintC()
    myapp.show()
    sys.exit(app.exec_())



