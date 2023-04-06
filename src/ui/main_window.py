from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QScreen
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QMainWindow, QApplication, QWidget, QPushButton, QLabel, QFrame

from src.ui.password_window import PasswordWindow

SRC_PATH = Path(__file__).parent.parent
ROOT_PATH = SRC_PATH.parent
RES_PATH = ROOT_PATH / "res"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.passwd_window = PasswordWindow()
        self.setup()

    def continue_button_pressed(self):
        self.hide()
        self.passwd_window.show()

    def next_page_pressed(self):
        if self.curr_page < len(self.pages):
            self.curr_page += 1
            self.btn_page_back.setEnabled(True)
        if self.curr_page == len(self.pages)-1:
            self.btn_page_fwd.setEnabled(False)
        self.wisdom_label.setText(self.pages[self.curr_page])

    def back_page_pressed(self):
        if self.curr_page > 0:
            self.curr_page -= 1
            self.btn_page_back.setEnabled(True)
        if self.curr_page > 0 and self.curr_page < len(self.pages):
            self.btn_page_fwd.setEnabled(True)
        if self.curr_page == 0:
            self.btn_page_back.setEnabled(False)
        self.wisdom_label.setText(self.pages[self.curr_page])

    def setup(self):
        # set window size
        self.setGeometry(150, 150, 400, 350)
        # get size of screen for window placement
        screen_size = QScreen.availableGeometry(QApplication.primaryScreen())
        frmX = (screen_size.width() - self.width()) / 2
        frmY = (screen_size.height() - self.height()) / 2
        # move window to center of screen
        self.move(frmX, frmY)
        self.setWindowTitle("SimpleLemon -- Getting Started")

        # load wisdom.txt and make pages
        self.curr_page = 0
        with open(RES_PATH / "wisdom.txt") as f:
            self.pages = f.read().split("%20%")

        # Layout
        layout = QVBoxLayout()
        # words of wisdoom
        self.wisdom_label = QLabel(self)
        self.wisdom_label.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.wisdom_label.setText(self.pages[0])
        self.wisdom_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        layout.addWidget(self.wisdom_label)

        h_layout = QHBoxLayout()
        self.btn_page_back = QPushButton("<", self)
        self.btn_page_back.clicked.connect(self.back_page_pressed)
        self.btn_page_fwd = QPushButton(">", self)
        self.btn_page_fwd.clicked.connect(self.next_page_pressed)
        h_layout.addWidget(self.btn_page_back)
        h_layout.addWidget(self.btn_page_fwd)
        layout.addLayout(h_layout)

        # next button
        btn_continue = QPushButton("Continue", self)
        btn_continue.clicked.connect(self.continue_button_pressed)
        btn_continue.resize(btn_continue.sizeHint())
        layout.addWidget(btn_continue)

        # page control
        if self.curr_page == 0:
            self.btn_page_back.setEnabled(False)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.show()