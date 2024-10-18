from PyQt5.Qt import *
import Signup_window
class Signup_label(QLabel):
    clicked = pyqtSignal()
    def __init__(self,parent):
        super().__init__(parent)
        self.clicked.connect(self.sign_up)
    def sign_up(self):
        self.sign_up_window = Signup_window.Signup_Dialog()
        self.sign_up_window.show()
    def mousePressEvent(self, QMouseEvent):
        self.clicked.emit()