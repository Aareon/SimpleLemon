import sys

from PySide6.QtWidgets import QApplication

from src.main_window import MainWindow


def run():
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
import sys

from PySide6.QtWidgets import QApplication

from src.main_window import MainWindow


def run():
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
