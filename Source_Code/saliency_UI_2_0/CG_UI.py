#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os
import random
class myGUI(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.picture_name = None
        self.mark_show_details = 0
        self.initUI()
        
        
    def initUI(self):      

        self.statusBar()
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(50, 50, 300, 25)


        # buttons
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.setToolTip('Quit From Program')
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(280, 150)

        self.rbtn = QPushButton('Start', self)
        self.rbtn.resize(self.rbtn.sizeHint())
        self.rbtn.move(160, 150)
        self.rbtn.clicked.connect(self.doAction)

        obtn = QPushButton('Open', self)
        obtn.clicked.connect(self.show_picture)
        obtn.setToolTip('Open File')
        obtn.resize(obtn.sizeHint())
        obtn.move(40, 150)

        self.timer = QBasicTimer()
        self.step = 0
        
        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('Saliency_Bar')
        self.show()
        
    # this timerEvent use (self, e), connect to the timer
    # When timer is active, call timerEvent() in the hidden layer
    def timerEvent(self, e):
        if (self.step >= 5) and (self.step < 15):
            self.statusBar().showMessage('Configuring ...')
        if (self.step >= 15) and (self.step < 80):
            self.statusBar().showMessage('Calculating, forwarding...')
        if (self.step >= 80) and (self.step < 90):
            self.statusBar().showMessage('Generating...')      
        if self.step >= 100:
            self.pbar.setValue(100)
            self.timer.stop()
            self.rbtn.setText('Results')
            self.statusBar().showMessage('Finished')
            self.mark_show_details = 1
            return

        self.step = int(self.step + random.uniform(0, 2))
        self.pbar.setValue(self.step)
        

    def doAction(self):
        if self.picture_name == None:
            self.statusBar().showMessage('No input')
            return
        if self.mark_show_details == 0:
            self.statusBar().showMessage('Loading ... ')
          
            if self.timer.isActive():
                self.timer.stop()
                self.rbtn.setText('Start')
            else:
                self.timer.start(100, self)
                self.rbtn.setText('Stop')
        else:
            try:
                newname = self.picture_name.split('/')[-1].split('.')[0].split('_')[0]
                #newname = 'saliency_data/present/'+ newname + '_final.png'
                newname = 'saliency_data/new_present/'+ newname + '_final.png'
                os.system('eog '+newname)
            except:
                self.statusBar().showMessage('Failed in Generating')
            self.rbtn.setText('Start')
            self.step = 0
            self.mark_show_details = 0

    def show_picture(self):

        pic_path = QFileDialog.getOpenFileName(self, 'Open file', 'saliency_data/picture')
        if pic_path[0]:
            self.picture_name = pic_path[0]
            try:
                print(self.picture_name)
                os.system('eog '+pic_path[0])
                self.statusBar().showMessage('New Picture is Ready')
            except:
                self.statusBar().showMessage('The path is not a picture path')
            
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = myGUI()
    sys.exit(app.exec_())
