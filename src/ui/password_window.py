import string
from PySide6.QtCore import Qt
from PySide6.QtGui import QScreen
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QApplication,
    QPushButton,
)


class PasswordWindow(QWidget):
    """
    Justification for passphrases instead of passwords:
        - Easier to remember
        - Generally longer, so more secure
    """
    
    default_error = "Passphrase must be of length > 10 and consist of multiple words."

    def __init__(self):
        super().__init__()
        self.setup()

    def check_password_valid(self, *args):
        if self.passwd_field.text() != self.passwd_conf_field.text():
            self.error_label.setText("The fields do not match.")
            self.error_label.show()
            self.passwd_btn.setEnabled(False)
            return

        if len(self.passwd_field.text()) < 10 or not any(
            [s.isspace() for s in self.passwd_field.text()]
        ):
            self.error_label.setText(self.default_error)
            self.error_label.show()
            return

        self.error_label.hide()
        self.passwd_btn.setEnabled(True)

    def continue_introduction(self, *args):
        pass  # password is valid; go to next part of setup.

    def setup(self):
        self.setGeometry(300, 150, 200, 150)
        # get size of screen for window placement
        screen_size = QScreen.availableGeometry(QApplication.primaryScreen())
        frmX = (screen_size.width() - self.width()) / 2
        frmY = (screen_size.height() - self.height()) / 2
        # move window to center of screen
        self.move(frmX, frmY)
        self.setWindowTitle("SimpleLemon - Create new profile passphrase")
        # put this window above all others
        self.setWindowFlags(self.windowFlags() ^ Qt.WindowStaysOnTopHint)

        # window layout
        layout = QVBoxLayout()

        # Password area
        self.passwd_field = QLineEdit(
            self, placeholderText="Enter a passphrase", echoMode=QLineEdit.Password
        )
        layout.addWidget(self.passwd_field)

        self.passwd_conf_field = QLineEdit(
            self, placeholderText="Confirm passphrase", echoMode=QLineEdit.Password
        )
        layout.addWidget(self.passwd_conf_field)

        self.error_label = QLabel(self, text=self.default_error)
        self.error_label.resize(self.error_label.sizeHint())
        layout.addWidget(self.error_label)

        self.passwd_btn = QPushButton(self, text="Next", disabled=True)
        self.passwd_btn.resize(self.passwd_btn.sizeHint())
        self.passwd_btn.pressed.connect(self.continue_introduction())
        layout.addWidget(self.passwd_btn)

        # check password
        self.passwd_field.textChanged.connect(self.check_password_valid)
        self.passwd_conf_field.textChanged.connect(self.check_password_valid)
        self.error_label.hide()

        self.setLayout(layout)
