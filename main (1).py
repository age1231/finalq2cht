
import sys
from PyQt5.QtWidgets import QApplication
from app_logic import ListOperationApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ListOperationApp()
    window.show()
    sys.exit(app.exec_())
