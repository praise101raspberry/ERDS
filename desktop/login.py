import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QVBoxLayout
)

from PyQt6.QtCore import Qt


class LoginWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("ERDS Login")
        self.resize(450, 300)

        layout = QVBoxLayout()

        title = QLabel("Emergency Response Dispatch System")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.username = QLineEdit()
        self.username.setPlaceholderText("Username")

        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        login_button = QPushButton("Login")

        layout.addWidget(title)
        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addWidget(login_button)

        self.setLayout(layout)


app = QApplication(sys.argv)

window = LoginWindow()
window.show()

sys.exit(app.exec())