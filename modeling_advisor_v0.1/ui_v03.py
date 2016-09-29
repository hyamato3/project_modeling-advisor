'''
Created on 2016/09/18

@author: H.Yamato
'''
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

filepath = 'workflowImage.png'

class UI1:    
    def __init__(self):
        self.w = QWidget()
        self.w.setGeometry(500, 200, 450, 100)
        self.w.setWindowTitle('ui_01')
        
        grid = QGridLayout(self.w)
        
        self.groupBoxUse = QGroupBox("モデルの使用目的", self.w)
        layout1 = QGridLayout()
        
        btnUse1 = QRadioButton("pre - Rendering", self.w)
        btnUse1.clicked.connect(self.onClickedPre)
        layout1.addWidget(btnUse1, 1, 0)
        
        btnUse2 = QRadioButton("real time - Rendering", self.w)
        btnUse2.clicked.connect(self.onClickedReal)
        layout1.addWidget(btnUse2, 2, 0)
        
        self.groupBoxUse.setLayout(layout1)
        grid.addWidget(self.groupBoxUse)
        
        
        self.groupBoxPro = QGroupBox("制作物")
        layout2 = QGridLayout()
    
        btnPro1 = QRadioButton("Characters", self.w)
        layout2.addWidget(btnPro1, 1, 0)
        
        btnPro2 = QRadioButton("Props", self.w)
        layout2.addWidget(btnPro2, 2, 0)
        
        btnPro3 = QRadioButton("BGs", self.w)
        layout2.addWidget(btnPro3, 3, 0)
        
        self.groupBoxPro.setLayout(layout2)
        grid.addWidget(self.groupBoxPro)
        
        
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
        
        self.textbox = QLineEdit(self.w)
        msgStart = "条件を選択してください"
        self.textbox.setText(msgStart)
        grid.addWidget(self.textbox, 3, 0)
        
        buttonOK = QPushButton('OK', self.w)
        grid.addWidget(buttonOK, 3, 1)
        QObject.connect(buttonOK,SIGNAL('clicked()'),self.onClickedOK)

    def onClickedPre(self):
        msgPre = "pre-rendering : 事前にレンダリングされているものを使用する作品"
        self.textbox.setText(msgPre)

    def onClickedReal(self):
        msgReal = "realTime-rendering : 入力に応じてその都度レンダリングをかける作品"
        self.textbox.setText(msgReal)

    def show(self):
        self.w.show()

    def onClickedOK(self):
        self.second = UI2(self.w)
        self.second.show()

class UI2:
    def __init__(self,parent=None):
        self.w = QDialog(parent)
        self.w.setGeometry(500, 625, 350, 100)
        self.w.setWindowTitle('ui_02')
        
        grid = QGridLayout(self.w)
        
        self.groupBoxKnd = QGroupBox("制作物の種別", self.w)
        layout3 = QGridLayout()
        
        btnknd1 = QRadioButton("car", self.w)
        btnknd1.clicked.connect(self.onClickedCar)
        layout3.addWidget(btnknd1, 1, 0)
        
        btnknd2 = QRadioButton("book", self.w)
        layout3.addWidget(btnknd2, 1, 1)
        
        btnknd3 = QRadioButton("robot", self.w)
        layout3.addWidget(btnknd3, 2, 0)
        
        btnknd4 = QRadioButton("cup", self.w)
        layout3.addWidget(btnknd4, 2, 1)
        
        btnknd5 = QRadioButton("gun", self.w)
        layout3.addWidget(btnknd5, 3, 0)
        
        btnknd6 = QRadioButton("lope", self.w)
        layout3.addWidget(btnknd6, 3, 1)
        
        self.groupBoxKnd.setLayout(layout3)
        grid.addWidget(self.groupBoxKnd)
        
        
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
        
        
        self.textbox = QLineEdit(self.w)
        msgStart = "制作物の種類と作るパーツを選択してください"
        self.textbox.setText(msgStart)
        grid.addWidget(self.textbox, 3, 0)
                       
        button2 = QPushButton('GO!', self.w)
        grid.addWidget(button2, 4, 0)
        
    def onClickedCar(self):
        msgCar = "車を制作します"
        self.textbox.setText(msgCar)
    
    def show(self):
        self.w.exec_()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    ui1 = UI1()
    ui1.show()
    
#    workflow = workFlow()
#    workflow.show()
    
    sys.exit(app.exec_())