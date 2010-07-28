import os, sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.phonon import *
from PyQt4 import uic
from PyKDE4.plasma import Plasma
from PyKDE4.plasmascript import Wallpaper
from PyKDE4.kdecore import *
from PyKDE4.kdeui import *

class WindFarms(Wallpaper):
	def __init__(self, parent, args = None):
		Wallpaper.__init__(self, parent)
		self.pixmap = None

	def init(self, config):
		print '### init',
		self.method = Plasma.Wallpaper.ResizeMethod(config.readEntry('method', Plasma.Wallpaper.ScaledResize).toInt()[0])
		self.color = QColor(config.readEntry("wallpapercolor", QColor(56, 111, 150)))
		self.size = self.boundingRect().size().toSize()
		self.image = self.package().filePath('images', 'concept.svg')
		print self.size, self.image
		self.render(self.image, self.size, self.method, self.color)
		self.test = QAction(i18n('Test'), self)
		self.setContextualActions([self.test])
		self.connect(self.test, SIGNAL('triggered(bool)'), self.play)

	def paint(self, painter, exposedRect):
		painter.setRenderHint(QPainter.Antialiasing,True)
		painter.setRenderHint(QPainter.HighQualityAntialiasing,True)
		
		width=painter.window().width()
		height=painter.window().height()
		
		#draw sky
		#TODO: strech this
		skyGradient=QRadialGradient(width/2,height/2,width/2)
		skyGradient.setColorAt(0, QColor("#ffcc5f"))
		skyGradient.setColorAt(1, QColor("#e19b3e"))
		#skyGradient.applyTo(QTransform().scale(1,0.1)) TODO, here
		skyBrush=QBrush(skyGradient)
		painter.fillRect(painter.window(),skyBrush)
		
		areaPath=QPainterPath()
		areaPath.moveTo(0,height/3)
		
		def yay(point):
			painter.setPen(QColor("blue"))
			painter.drawEllipse(point,10,10)
		
		howfar=0.3
		array=[0.1,0.2,0.3,0.1,0.4,0.1]
		step=width/(len(array)-1)
		points=[]
		
		for i,element in enumerate(array):
			if i!=0:
				points.insert(QPointF(step*i-howfar,array[i]*height))
			points.insert(QPointF(step*i,array[i]*height))
			if i!=len(array)-1:
				points.insert(QPointF(step*i+howfar,array[i]*height))
		
		print list(enumerate(array))
		array=map(lambda x: (1-x)*height,array)
		for index,element in enumerate(points):
			destination=QPointF(step*index,element)
			mid1=QPointF(step*index-2*step/3,array[index-1])
			mid2=QPointF(step*index-step/3,element)
			painter.drawLine(mid1,mid2)
			painter.drawLine(mid2,destination)
			areaPath.cubicTo(mid1,mid2,destination)
			yay(mid1)
			yay(mid2)
			yay(destination)
		
		areaPath.lineTo(width,height)
		areaPath.lineTo(0,height)
		painter.fillPath(areaPath,QBrush(QColor("black")))
		#if self.pixmap:
			#if painter.worldMatrix() == QMatrix():
				## draw the background untransformed when possible; (saves lots of per-pixel-math)
				#painter.resetTransform()

			## blit the background (saves all the per-pixel-products that blending does)
			#painter.setCompositionMode(QPainter.CompositionMode_Source)

			## for pixmaps we draw only the exposed part (untransformed since the
			## bitmapBackground already has the size of the viewport)
			#painter.drawPixmap(exposedRect, self.pixmap, exposedRect.translated(-self.boundingRect().topLeft()))

	def createConfigurationInterface(self, parent):
		self.currentColor = self.color
		widget = QWidget(parent)
		ui = uic.loadUi(self.package().filePath('ui', 'config.ui'), widget)
		ui.resizeCombo.setCurrentIndex(self.method)
		self.connect(ui.resizeCombo, SIGNAL('currentIndexChanged(int)'), self.resizeChanged)
		return widget

	def resizeChanged(self, index):
		self.method = index
		self.settingsChanged(True)
		self.render(self.image, self.size, self.method, self.color)

	def save(self, config):
		config.writeEntry('method', self.method)

	def mouseMoveEvent(self, event):
		pass

	def mousePressEvent(self, event):
		pass
	
	def mouseReleaseEvent(self, event):
		pass
	
	def wheelEvent(self, event):
		pass

	def renderCompleted(self, image):
		pass
		self.pixmap = QPixmap(image)
		self.update(self.boundingRect())

	def urlDropped(self, url):
		print '### urlDropped', url

	def play(self):
		print '### play'
		media = Phonon.MediaObject(self)
		output = Phonon.AudioOutput(self);
		Phonon.createPath(media, output)
		media.setCurrentSource(Phonon.MediaSource(\
				KStandardDirs.locate('sound', 'KDE-Sys-Log-In.ogg')))
		media.play()


def CreateWallpaper(parent):
	return WindFarms(parent)

