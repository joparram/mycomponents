#
# Copyright (C) 2015 by YOUR NAME HERE
#
#    This file is part of RoboComp
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

ROBOCOMP = ''
try:
	ROBOCOMP = os.environ['ROBOCOMP']
except:
	pass
if len(ROBOCOMP)<1:
	print 'ROBOCOMP environment variable not set! Exiting.'
	sys.exit()


preStr = "-I"+ROBOCOMP+"/interfaces/ --all "+ROBOCOMP+"/interfaces/"
Ice.loadSlice(preStr+"DifferentialRobot.ice")
from RoboCompDifferentialRobot import *
Ice.loadSlice(preStr+"Laser.ice")
from RoboCompLaser import *


from differentialrobotI import *

class SpecificWorker(GenericWorker):
	def __init__(self, proxy_map):
		super(SpecificWorker, self).__init__(proxy_map)
		self.timer.timeout.connect(self.compute)
		self.Period = 2000
		self.timer.start(self.Period)

	def setParams(self, params):
		#// 	try
		#// 	{
		#// 		RoboCompCommonBehavior::Parameter par = params.at("InnerModelPath");
		#// 		innermodel_path=par.value;
		#// 		innermodel = new InnerModel(innermodel_path);
		#// 	}
		#// 	catch(std::exception e) { qFatal("Error reading config params"); }
		return True

	@QtCore.Slot()
	def compute(self):
		print 'SpecificWorker.compute...'
		#// 	try
		#// 	{
		#// 		camera_proxy->getYImage(0,img, cState, bState);
		#// 		memcpy(image_gray.data, &img[0], m_width*m_height*sizeof(uchar));
		#// 		searchTags(image_gray);
		#// 	}
		#// 	catch(const Ice::Exception &e)
		#// 	{
		#// 		std::cout << "Error reading from Camera" << e << std::endl;
		#// 	}
		return True

	def correctOdometer(self, x, z, alpha):
		#
		# YOUR CODE HERE
		#
		pass

	def getBasePose(self):
		#
		# YOUR CODE HERE
		#
		x = int()
		z = int()
		alpha = float()
		return [x, z, alpha]
	def resetOdometer(self):
		#
		# YOUR CODE HERE
		#
		pass

	def setOdometer(self, state):
		#
		# YOUR CODE HERE
		#
		pass

	def getBaseState(self):
		#
		# YOUR CODE HERE
		#
		state = TBaseState()
		return state

	def setOdometerPose(self, x, z, alpha):
		#
		# YOUR CODE HERE
		#
		pass

	def stopBase(self):
		#
		# YOUR CODE HERE
		#
		pass

	def setSpeedBase(self, adv, rot):
		#
		# YOUR CODE HERE
		#
		pass





