import os,sys
from PyQt4 import QtGui
app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()
window.setGeometry(30, 30, 400, 200)
pic = QtGui.QLabel(window)
pic.setGeometry(50, 50, 400, 100)
#use full ABSOLUTE path to the image, not relative
myPixmap = QtGui.QPixmap(_fromUtf8('image.jpg'))
myScaledPixmap = myPixmap.scaled(self.label.size(), Qt.KeepAspectRatio)
self.label.setPixmap(myScaledPixmap)
window.show()
sys.exit(app.exec_())