import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class MainWindow(QWidget):
  def __init__(self):
    QWidget.__init__(self)
    self.initUI()

  def initUI(self):
    self.setGeometry(100,50,800,800)

    oImage = QImage("saliency.jpg")
    sImage = oImage.scaled(QSize(800,800))                   # resize Image to widgets size
    palette = QPalette()
    palette.setBrush(10, QBrush(sImage))                     # 10 = Windowrole
    self.setPalette(palette)

    # buttons

    self.rbtn = QPushButton('Let\'s Begin', self)
    self.rbtn.setStyleSheet("background-color: SkyBlue")
    #self.rbtn.setStyleSheet("opacity: 0.5, filter: alpha(opacity=50)")
    self.rbtn.setToolTip('Begin the adventure')
    self.rbtn.resize(100,50)
    self.rbtn.move(340, 650)
    self.rbtn.clicked.connect(self.mybegin)

    self.show()
  def mybegin(self):
    os.system('python CG_UI.py')


if __name__ == '__main__':
    
  app = QApplication(sys.argv)
  ex = MainWindow()
  sys.exit(app.exec_())