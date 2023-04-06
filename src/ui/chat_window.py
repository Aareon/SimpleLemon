import sys
from typing import List
from PySide6.QtCore import SIGNAL
from PySide6.QtGui import QScreen
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QTreeWidget, QTreeWidgetItem, QWidget, QPushButton, QTextEdit, QLineEdit


class UserTreeItem(QTreeWidgetItem):
    """Custom QTreeWidgetItem with Widgets"""
    def __init__(self, parent, name):
        """parent (QTreeWidget) : Item's QTreeWidget parent.
        name   (str)         : Item's name. just an example."""

        super(UserTreeItem, self).__init__(parent)
        self.setText(0, name)

        ## Signals
        #self.treeWidget().connect(self.button, SIGNAL("clicked()"), self.buttonPressed)

    @property
    def name(self):
        '''
        Return name ( 1st column text )
        '''
        return self.text(0)

class ServerTreeItem(QTreeWidgetItem):
    """Custom QTreeWidgetItem with Widgets"""
    def __init__(self, parent, name):
        """parent (QTreeWidget) : Item's QTreeWidget parent.
        name   (str)         : Item's name. just an example."""

        super(ServerTreeItem, self).__init__(parent)
        self.setText(0, name)

        ## Signals
        #self.treeWidget().connect(self.button, SIGNAL("clicked()"), self.buttonPressed)

    @property
    def name(self):
        """Return name ( 1st column text )"""
        return self.text(0)


class ChatWindow(QWidget):
    def __init__(self, servers: List = None, users: List = None):
        super().__init__()
        self.servers = servers or []
        self.users = users or []
        self.setup()

    def setup(self):
        # set window size
        self.setGeometry(150, 150, 400, 350)
        # get size of screen for window placement
        screen_size = QScreen.availableGeometry(QApplication.primaryScreen())
        frmX = (screen_size.width() - self.width()) / 2
        frmY = (screen_size.height() - self.height()) / 2
        # move window to center of screen
        self.move(frmX, frmY)
        self.setWindowTitle("SimpleLemon -- Chat")

        hlayout = QHBoxLayout()
        self.server_tree = QTreeWidget()
        self.server_tree_headers = ("Server List",)
        self.server_tree.setColumnCount(len(self.server_tree_headers))
        self.server_tree.setHeaderLabels(self.server_tree_headers)
        # add servers to tree
        for s in self.servers:
            item = ServerTreeItem(self.server_tree, s)
        # set column width to fit content
        for col in range(self.server_tree.columnCount()):
            self.server_tree.resizeColumnToContents(col)

        hlayout.addWidget(self.server_tree)

        vlayout = QVBoxLayout()
        self.message_box = QTextEdit(readOnly=True, text="Aareon: this shit boo boo cuh\ndapper: stfu and get back to work monkey")
        vlayout.addWidget(self.message_box)

        hlayout1 = QHBoxLayout()
        self.input_box = QLineEdit(placeholderText="Enter message")
        hlayout1.addWidget(self.input_box)
        self.btn_send = QPushButton("Send")
        hlayout1.addWidget(self.btn_send)
        vlayout.addLayout(hlayout1)

        hlayout.addLayout(vlayout)
        self.user_tree = QTreeWidget()
        self.user_tree_headers = ("User List",)
        self.user_tree.setColumnCount(len(self.user_tree_headers))
        self.user_tree.setHeaderLabels(self.user_tree_headers)
        # add servers to tree
        for s in self.users:
            item = ServerTreeItem(self.user_tree, s)
        # set column width to fit content
        for col in range(self.user_tree.columnCount()):
            self.user_tree.resizeColumnToContents(col)
        hlayout.addWidget(self.user_tree)

        self.setLayout(hlayout)

if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    app = QApplication()
    w = ChatWindow(
        ["Freenode", "Discord", "Skype"],
        ["Aareon", "dapper", "pin", "SolarFlame"])
    w.show()
    sys.exit(app.exec_())
