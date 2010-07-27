#!/usr/bin/python

import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class WindFarms(QFrame):
	def __init__(self, parent=None):
		QFrame.__init__(self, parent)
		
		self.setWindowTitle('Wind Farms')
		self.showMaximized()
	def paintEvent(self,event):
		painter=QPainter(self)
		painter.setRenderHint(QPainter.Antialiasing,True)
		painter.setRenderHint(QPainter.HighQualityAntialiasing,True)
		
		width=painter.window().width()
		height=painter.window().height()
		
		#draw sky
		#TODO: strech this
		skyGradient=QRadialGradient(width/2,height/2,width/2)
		skyGradient.setColorAt(0, QColor("#ffcc5f"))
		skyGradient.setColorAt(1, QColor("#e19b3e"))
		skyBrush=QBrush(skyGradient)
		painter.fillRect(painter.window(),skyBrush)
		
		
		
		areaPath=QPainterPath()
		areaPath.moveTo(0,height/3)
		
		painter.setPen(QColor("red"))
		array=[0.1,0.2,0.3,0.1,0.4,0.1]
		array=map(lambda x: (1-x)*height,array)
		
		step=width/(len(array)-1)
		for index,element in enumerate(array):
			
			destination=QPointF(step*index,element)
			mid1=QPointF(step*index-2*step/3,array[index-1])
			mid2=QPointF(step*index-step/3,element)
			painter.drawLine(mid1,mid2)
			painter.drawLine(mid2,destination)
			areaPath.cubicTo(mid1,mid2,destination)
			print destination
			print height
		
		areaPath.lineTo(width,height)
		areaPath.lineTo(0,height)
		painter.fillPath(areaPath,QBrush(QColor("black")))
		

app = QApplication(sys.argv)
wallpaper = WindFarms()
wallpaper.show()
sys.exit(app.exec_())