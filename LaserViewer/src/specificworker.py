#
# Copyright (C) 2015 by YOUR NAME HERE
#
# This file is part of RoboComp
#
#    RoboComp is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    RoboComp is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with RoboComp.  If not, see <http://www.gnu.org/licenses/>.
#

import sys, os, Ice

from PySide import *
from genericworker import *
from laserViewer import *

ROBOCOMP = ''
try:
    ROBOCOMP = os.environ['ROBOCOMP']
except:
    pass
if len(ROBOCOMP) < 1:
    print 'ROBOCOMP environment variable not set! Exiting.'
    sys.exit()

preStr = "-I" + ROBOCOMP + "/interfaces/ --all " + ROBOCOMP + "/interfaces/"
Ice.loadSlice(preStr + "Laser.ice")
from RoboCompLaser import *


class SpecificWorker(GenericWorker):
    def __init__(self, proxy_map):
        super(SpecificWorker, self).__init__(proxy_map)
        self.timer.timeout.connect(self.compute)
        self.Period = 2000
        self.timer.start(self.Period)
        self.app = QtGui.QApplication.instance()
        self.myapp = laserViewer()
        self.myapp.show()
        sys.exit(self.app.exec_())



    def setParams(self, params):

        return True

    @QtCore.Slot()
    def compute(self):

        ld = self.laser_proxy.getLaserData()
        tupl = lambda x: (i.dist, i.angle)
        V = [tupl(i) for i in ld]
        self.myapp.updateG(V)
        self.myapp.paintC()

        return True







