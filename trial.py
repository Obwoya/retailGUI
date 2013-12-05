import sys, random
from PyQt4 import QtGui, QtCore

# Robot Widget
class RobotLink(QtGui.QWidget):
    def __init__(self, parent, x, y, width, height, fill):
        super(RobotLink, self).__init__(parent)
        self._fill     = fill
        self._rotation = 0
        self.setGeometry(x, y, width, height)

    def paintEvent(self, e):
        painter = QtGui.QPainter()
        painter.begin(self)
        self.drawLink(painter)
        painter.end()

    def drawLink(self, painter):
        painter.setPen(QtGui.QColor(0, 0, 0))
        painter.setBrush(self._fill)
        painter.drawEllipse(0, 0, self.width(), self.height())

# Window
class Window(QtGui.QWidget):
    # Default Constructor, sets up the window GUI
    def __init__(self):
        super(Window, self).__init__()
        self.initUI()

    def initUI(self):
        self._link1 = RobotLink(self, 10, 10, 100, 50, QtCore.Qt.DiagCrossPattern)
        self._link2 = RobotLink(self, 100, 100, 50, 100, QtCore.Qt.Dense5Pattern)
        self._link3 = RobotLink(self, 150, 150, 50, 50, QtCore.Qt.Dense2Pattern)

        self.setGeometry(30, 300, 800, 600)
        self.setWindowTitle("CSCE 452 - PaintBot")

    def paintEvent(self, e):
        super(Window, self).paintEvent(e)
        painter = QtGui.QPainter()
        painter.begin(self)
        self.drawBoundingBoxes(painter)
        painter.end()

    # Draws the boxes that define the robots workspace and
    # the control panel
    def drawBoundingBoxes(self, painter):
        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor("#cccccc")
        painter.setPen(color)

        # Draw the robot workspace
        painter.setBrush(QtGui.QColor(255, 255, 255))
        painter.drawRect(10, 10, 500, 578)

        # Draw the control panel workspace
        painter.setBrush(QtGui.QColor(150, 150, 150))
        painter.drawRect(520, 10, 270, 578)

        # Draws the slider 'base'
        painter.setPen(QtGui.QColor(0, 0, 0))
        painter.drawLine(100, 570, 400, 570)

    def changeValue(self, value):
        self.wid.emit(QtCore.SIGNAL("updateRobot(int)"), value)
        self.wid.repaint()

# Setup the Window, and the Robot
app = QtGui.QApplication(sys.argv)
win = Window()
win.show()
app.exec_()