from PyQt5.Qt import *
import Change_window
class Change_button(QPushButton):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.clicked.connect(self.Open_change_window)
        self.Change_ = Change_window.Ui_Change()
    def Open_change_window(self):
        self.Change_.show()