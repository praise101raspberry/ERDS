from PyQt6.QtWidgets import (
    QWidget,
    QGridLayout,
    QLabel,
    QGroupBox,
    QVBoxLayout
)
from PyQt6.QtCore import Qt


class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(20, 20, 20, 20)

        # Dashboard Cards
        self.active_incidents = self.create_card("🚨 Active Incidents", 12)
        self.available_responders = self.create_card("🚑 Available Responders", 25)
        self.units_dispatched = self.create_card("🚓 Units Dispatched", 8)
        self.system_status = self.create_card("🟢 System Status", "Online")

        # Add cards to the grid
        layout.addWidget(self.active_incidents, 0, 0)
        layout.addWidget(self.available_responders, 0, 1)
        layout.addWidget(self.units_dispatched, 1, 0)
        layout.addWidget(self.system_status, 1, 1)

        self.setLayout(layout)

    def create_card(self, title, value):
        card = QGroupBox()

        card_layout = QVBoxLayout()

        title_label = QLabel(title)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("""
            font-size: 16px;
            font-weight: bold;
        """)

        value_label = QLabel(str(value))
        value_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        value_label.setStyleSheet("""
            font-size: 34px;
            font-weight: bold;
            color: #0078D7;
        """)

        card_layout.addWidget(title_label)
        card_layout.addStretch()
        card_layout.addWidget(value_label)
        card_layout.addStretch()

        card.setLayout(card_layout)

        card.setStyleSheet("""
            QGroupBox {
                background: white;
                border: 2px solid #CCCCCC;
                border-radius: 12px;
                padding: 15px;
            }
        """)

        return card