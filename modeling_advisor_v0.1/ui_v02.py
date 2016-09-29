'''
Created on 2016/09/18

@author: H.Yamato
'''
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MainWindow:
        
    def __init__(self):
        self.w = QWidget()
        self.w.setGeometry(500, 200, 350, 100)
        self.w.setWindowTitle('ui_01')
        
        grid = QGridLayout(self.w)
        
        self.groupBox1 = QGroupBox("モデルの使用目的", self.w)
        layout1 = QGridLayout()
        
        buttonA1 = QRadioButton("pre - Rendering", self.w)
        layout1.addWidget(buttonA1, 1, 0)
        print("A")
        
        buttonA2 = QRadioButton("real time - Rendering", self.w)
        layout1.addWidget(buttonA2, 2, 0)
        
        self.groupBox1.setLayout(layout1)
        grid.addWidget(self.groupBox1)
        
        
        self.groupBox2 = QGroupBox("制作物")
        layout2 = QGridLayout()
    
        buttonB1 = QRadioButton("Characters", self.w)
        layout2.addWidget(buttonB1, 1, 0)
        
        buttonB2 = QRadioButton("Props", self.w)
        layout2.addWidget(buttonB2, 2, 0)
        
        buttonB3 = QRadioButton("BGs", self.w)
        layout2.addWidget(buttonB3, 3, 0)
        
        self.groupBox2.setLayout(layout2)
        grid.addWidget(self.groupBox2)
        
        
        self.groupBoxSoft = QGroupBox("使用可能なソフトウェア", self.w)
        layoutSoft = QGridLayout()
        
        btnSoft1 = QPushButton("Maya", self.w)
        btnSoft1.setCheckable(True)
        layoutSoft.addWidget(btnSoft1)
        
        
        btnSoft2 = QPushButton("Blender", self.w)
        btnSoft2.setCheckable(True)
        layoutSoft.addWidget(btnSoft2)
        
        btnSoft3 = QPushButton("Zbrush", self.w)
        btnSoft3.setCheckable(True)
        layoutSoft.addWidget(btnSoft3)
        
        self.groupBoxSoft.setLayout(layoutSoft)
        grid.addWidget(self.groupBoxSoft)
        
        
        text = QTextEdit(self.w)
        grid.addWidget(text, 4, 0)
        
        button1 = QPushButton('OK', self.w)
        grid.addWidget(button1, 4, 1)
        QObject.connect(button1,SIGNAL('clicked()'),self.onClicked)

        self.second = SecondWindow(self.w)

    def show(self):
        self.w.show()

    def onClicked(self):
        self.second.show()

class SecondWindow:
    def __init__(self,parent=None):
        self.w = QDialog(parent)
        self.w.setGeometry(500, 625, 350, 100)
        self.w.setWindowTitle('ui_02')
        
        grid = QGridLayout(self.w)
        
        self.groupBox3 = QGroupBox("制作物の種別", self.w)
        layout3 = QGridLayout()
        
        buttonC1 = QRadioButton("car", self.w)
        layout3.addWidget(buttonC1, 1, 0)
        
        buttonC2 = QRadioButton("book", self.w)
        layout3.addWidget(buttonC2, 1, 1)
        
        buttonC3 = QRadioButton("robot", self.w)
        layout3.addWidget(buttonC3, 2, 0)
        
        buttonC4 = QRadioButton("cup", self.w)
        layout3.addWidget(buttonC4, 2, 1)
        
        buttonC5 = QRadioButton("gun", self.w)
        layout3.addWidget(buttonC5, 3, 0)
        
        buttonC6 = QRadioButton("lope", self.w)
        layout3.addWidget(buttonC6, 3, 1)
        
        self.groupBox3.setLayout(layout3)
        grid.addWidget(self.groupBox3)
        
        
        self.groupBoxPart = QGroupBox("作る必要のあるパーツ", self.w)
        layoutPart = QGridLayout()
        
        btnPart1 = QPushButton("body", self.w)
        btnPart1.setCheckable(True)
        layoutPart.addWidget(btnPart1, 1, 0)
        
        btnPart2 = QPushButton("tire", self.w)
        btnPart2.setCheckable(True)
        layoutPart.addWidget(btnPart2, 1, 1)
        
        btnPart3 = QPushButton("tire", self.w)
        btnPart3.setCheckable(True)
        layoutPart.addWidget(btnPart3, 2, 0)
        
        btnPart4 = QPushButton("suspension", self.w)
        btnPart4.setCheckable(True)
        layoutPart.addWidget(btnPart4, 2, 1)
        
        btnPart5 = QPushButton("window", self.w)
        btnPart5.setCheckable(True)
        layoutPart.addWidget(btnPart5, 3, 0)
        
        btnPart6 = QPushButton("seat", self.w)
        btnPart6.setCheckable(True)
        layoutPart.addWidget(btnPart6, 3, 1)
        
        btnPart7 = QPushButton("light", self.w)
        btnPart7.setCheckable(True)
        layoutPart.addWidget(btnPart7, 4, 0)
        
        btnPart8 = QPushButton("muffler", self.w)
        btnPart8.setCheckable(True)
        layoutPart.addWidget(btnPart8, 4, 1)
        
        self.groupBoxPart.setLayout(layoutPart)
        grid.addWidget(self.groupBoxPart)
        
        
        text = QTextEdit(self.w)
        grid.addWidget(text, 3, 0)
                       
        button2 = QPushButton('GO!', self.w)
        grid.addWidget(button2, 4, 0)
        
        self.workflow = WorkflowWindow(self.w)
        
    def show(self):
        self.w.exec_()
        
    def onClicked(self):
        self.workflow.show()
        
class WorkflowWindow:
    def __init__(self,parent=None):
        self.w = QDialog(parent)
        self.w.setGeometry(500, 625, 350, 100)
        self.w.setWindowTitle('ui_02')
        
        grid = QGridLayout(self.w)
        
        self.groupBox3 = QGroupBox("制作物の種別", self.w)
        layout3 = QGridLayout()
        
        buttonC1 = QRadioButton("car", self.w)
        layout3.addWidget(buttonC1, 1, 0)
        
        buttonC2 = QRadioButton("book", self.w)
        layout3.addWidget(buttonC2, 1, 1)
        
        buttonC3 = QRadioButton("robot", self.w)
        layout3.addWidget(buttonC3, 2, 0)
        
        buttonC4 = QRadioButton("cup", self.w)
        layout3.addWidget(buttonC4, 2, 1)
        
        buttonC5 = QRadioButton("gun", self.w)
        layout3.addWidget(buttonC5, 3, 0)
        
        buttonC6 = QRadioButton("lope", self.w)
        layout3.addWidget(buttonC6, 3, 1)
        
        self.groupBox3.setLayout(layout3)
        grid.addWidget(self.groupBox3)
        
        
        self.groupBoxPart = QGroupBox("作る必要のあるパーツ", self.w)
        layoutPart = QGridLayout()
        
        btnPart1 = QPushButton("body", self.w)
        btnPart1.setCheckable(True)
        layoutPart.addWidget(btnPart1, 1, 0)
        
        btnPart2 = QPushButton("tire", self.w)
        btnPart2.setCheckable(True)
        layoutPart.addWidget(btnPart2, 1, 1)
        
        btnPart3 = QPushButton("tire", self.w)
        btnPart3.setCheckable(True)
        layoutPart.addWidget(btnPart3, 2, 0)
        
        btnPart4 = QPushButton("suspension", self.w)
        btnPart4.setCheckable(True)
        layoutPart.addWidget(btnPart4, 2, 1)
        
        btnPart5 = QPushButton("window", self.w)
        btnPart5.setCheckable(True)
        layoutPart.addWidget(btnPart5, 3, 0)
        
        btnPart6 = QPushButton("seat", self.w)
        btnPart6.setCheckable(True)
        layoutPart.addWidget(btnPart6, 3, 1)
        
        btnPart7 = QPushButton("light", self.w)
        btnPart7.setCheckable(True)
        layoutPart.addWidget(btnPart7, 4, 0)
        
        btnPart8 = QPushButton("muffler", self.w)
        btnPart8.setCheckable(True)
        layoutPart.addWidget(btnPart8, 4, 1)
        
        self.groupBoxPart.setLayout(layoutPart)
        grid.addWidget(self.groupBoxPart)
        
        
        text = QTextEdit(self.w)
        grid.addWidget(text, 3, 0)
                       
        button2 = QPushButton('GO!', self.w)
        grid.addWidget(button2, 4, 0)

    def show(self):
        self.w.exec_()

if __name__ == "__main__":

    app = QApplication(sys.argv)

    main = MainWindow()
    main.show()

    sys.exit(app.exec_())