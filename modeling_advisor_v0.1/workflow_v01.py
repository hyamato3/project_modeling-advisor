'''
Created on 2016/09/18

@author: H.Yamato
'''
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

filepath = 'workflow_car.tif'

def main():

    app = QApplication(sys.argv)

    view = QGraphicsView()
    scene = QGraphicsScene()
    
    #self.setWindowTitle('Workflow 制作物 "車"')
    
    pixmap = QPixmap(filepath)
    item = QGraphicsPixmapItem(pixmap)
    scene .addItem(item)
    view.setScene(scene)
    view.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()