from PyQt5.Qt import *
import Add_window
class Add_weapon_button(QPushButton):
    def __init__(self,parent):
        super().__init__(parent)
        self.AddWeapon = Add_window.Add_Dialog()
        self.clicked.connect(self.open_add_window)
    def open_add_window(self):
        self.parent().parent().deleteLater()
        self.AddWeapon.show()
