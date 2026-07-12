from PyQt6.QtWidgets import QFrame, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt


class StatCard(QFrame):

    def __init__(self, title, value, color="#0078D7"):
        super().__init__()

        self.setMinimumHeight(100)

        self.setStyleSheet(f"""
            QFrame {{
                background: white;
                border: 2px solid #DDDDDD;
                border-radius: 12px;
            }}
        """)

        layout = QVBoxLayout()

        self.title = QLabel(title)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setStyleSheet("""
            font-size:14px;
            color:#666666;
        """)

        self.value = QLabel(str(value))
        self.value.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.value.setStyleSheet(f"""
            font-size:30px;
            font-weight:bold;
            color:{color};
        """)

        layout.addStretch()
        layout.addWidget(self.title)
        layout.addWidget(self.value)
        layout.addStretch()

        self.setLayout(layout)

    def setValue(self, value):
        self.value.setText(str(value))