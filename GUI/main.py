import scripts
from PyQt5.QtWidgets import QApplication
import sys


parent_app = QApplication(sys.argv)
main_window = scripts.app.Ui_MainWindow()
main_window.show()
sys.exit(parent_app.exec_())
