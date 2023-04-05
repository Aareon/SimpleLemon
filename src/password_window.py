import string
from PySide6.QtCore import Qt
from PySide6.QtGui import QScreen
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QApplication, QPushButton


class PasswordWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setup()

    def check_password_valid(self, *args):
        if self.passwd_conf_field.text() == self.passwd_field.text():
            if len(self.passwd_conf_field.text()) > 10:
                if any([s in self.passwd_conf_field.text() for s in string.punctuation]):
                    self.passwd_btn.setEnabled(True)
                    self.bad_pwd_label.hide()
                else:
                    self.bad_pwd_label.show()
            else:
                self.bad_pwd_label.show()
        else:
            self.passwd_btn.setEnabled(False)

    def setup(self):
        self.setGeometry(150, 150, 200, 150)
        # get size of screen for window placement
        screen_size = QScreen.availableGeometry(QApplication.primaryScreen())
        frmX = (screen_size.width() - self.width()) / 2
        frmY = (screen_size.height() - self.height()) / 2
        # move window to center of screen
        self.move(frmX, frmY)
        self.setWindowTitle("SimpleLemon -- Create new profile password")
        # put this window above all others
        self.setWindowFlags(self.windowFlags() ^ Qt.WindowStaysOnTopHint)

        # window layout
        layout = QVBoxLayout()

        # Password area
        label = QLabel(self, text="Create a secure password\nMust be of length >10 and must include special character(s)")
        label.resize(label.sizeHint())
        layout.addWidget(label)

        self.passwd_field = QLineEdit(self, placeholderText="Enter a password", echoMode=QLineEdit.Password)
        layout.addWidget(self.passwd_field)

        self.passwd_conf_field = QLineEdit(self, placeholderText="Confirm password", echoMode=QLineEdit.Password)
        layout.addWidget(self.passwd_conf_field)

        self.bad_pwd_label = QLabel(self, text="Password must contain special characters and be of length > 10")
        self.bad_pwd_label.resize(self.bad_pwd_label.sizeHint())
        layout.addWidget(self.bad_pwd_label)

        self.passwd_btn = QPushButton(self, text="Next", disabled=True)
        self.passwd_btn.resize(self.passwd_btn.sizeHint())
        layout.addWidget(self.passwd_btn)

        # check password
        self.passwd_field.textChanged.connect(self.check_password_valid)
        self.passwd_conf_field.textChanged.connect(self.check_password_valid)
        self.bad_pwd_label.hide()

        self.setLayout(layout)
