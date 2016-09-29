'''
Created on 2016/09/18

@author: H.Yamato
'''
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def pushSlot(button_name):
    def func():
        print("%s is pushed." % button_name)
    return func

def firstGuiButtons():
    app = QApplication(sys.argv)
    self = QWidget()
    self.setGeometry(500, 200, 350, 100)
    #self.resize(400, 400)
    self.setWindowTitle('ui_01')
    
    grid = QGridLayout()
    
    self.groupBox1 = QGroupBox("モデルの使用目的")
    layout1 = QGridLayout()
    
    buttonA1 = QRadioButton("pre - Rendering")
    buttonA1.clicked.connect(pushSlot("preRendering"))
    layout1.addWidget(buttonA1, 1, 0)
    
    
    buttonA2 = QRadioButton("real time - Rendering")
    buttonA2.clicked.connect(pushSlot("realtimeRendering"))
    layout1.addWidget(buttonA2, 2, 0)
    
    self.bg1 = QButtonGroup()
    self.bg1.addButton(buttonA1)
    self.bg1.addButton(buttonA2)
    
    self.groupBox1.setLayout(layout1)
    grid.addWidget(self.groupBox1)
    
    self.groupBox2 = QGroupBox("制作物")
    layout2 = QGridLayout()
    
    buttonB1 = QRadioButton("Characters")
    buttonB1.clicked.connect(pushSlot("character"))
    layout2.addWidget(buttonB1, 1, 0)
    
    buttonB2 = QRadioButton("Props")
    buttonB2.clicked.connect(pushSlot("props"))
    layout2.addWidget(buttonB2, 2, 0)
    
    buttonB3 = QRadioButton("BGs")
    buttonB3.clicked.connect(pushSlot("BGs"))
    layout2.addWidget(buttonB3, 3, 0)
    
    self.bg2 = QButtonGroup()
    self.bg2.addButton(buttonB1)
    self.bg2.addButton(buttonB2)
    self.bg2.addButton(buttonB3)
    
    self.groupBox2.setLayout(layout2)
    grid.addWidget(self.groupBox2)
    
    self.text = QTextEdit(self)
    grid.addWidget(self.text)
    
    button1 = QPushButton("GO!")
    grid.addWidget(button1, 4, 0)
    
    self.setLayout(grid)
    self.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    firstGuiButtons() 