import random
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.paint_circle = False
        self.circle_button.clicked.connect(self.paint)

    def paint(self):
        self.paint_circle = True
        self.update()

    def paintEvent(self, event):
        if self.paint_circle:
            painter = QPainter()
            painter.begin(self)
            num = random.randint(20, 100)
            painter.setBrush(QColor(255, 255, 0))
            painter.drawEllipse(208 - num, 155 - num, num * 2, num * 2)
            painter.end()
        self.paint_circle = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())
