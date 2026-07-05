import sys

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QListWidget,
    QLabel,
    QHBoxLayout,
    QStatusBar,
    QStackedWidget,
)
from PyQt6.QtCore import Qt

from pages.dashboard import DashboardPage


class DispatcherWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ERDS Dispatcher Console")
        self.resize(1500, 900)

        self.create_menu()
        self.setup_ui()
        self.create_status_bar()

    def create_menu(self):
        menu = self.menuBar()

        menu.addMenu("File")
        menu.addMenu("View")
        menu.addMenu("Help")

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QHBoxLayout()

        # Navigation
        self.navigation = QListWidget()
        self.navigation.setFixedWidth(220)

        self.navigation.addItems([
            "Dashboard",
            "Incidents",
            "Dispatch",
            "Responders",
            "Vehicles",
            "Reports",
            "Settings"
        ])

        self.navigation.setCurrentRow(0)
        self.navigation.currentTextChanged.connect(self.change_page)

        # Stacked Pages
        self.pages = QStackedWidget()

        dashboard = DashboardPage()

        incidents = QLabel("🚨 Incidents Page")
        incidents.setAlignment(Qt.AlignmentFlag.AlignCenter)

        dispatch = QLabel("🚑 Dispatch Page")
        dispatch.setAlignment(Qt.AlignmentFlag.AlignCenter)

        responders = QLabel("👮 Responders Page")
        responders.setAlignment(Qt.AlignmentFlag.AlignCenter)

        vehicles = QLabel("🚒 Vehicles Page")
        vehicles.setAlignment(Qt.AlignmentFlag.AlignCenter)

        reports = QLabel("📊 Reports Page")
        reports.setAlignment(Qt.AlignmentFlag.AlignCenter)

        settings = QLabel("⚙️ Settings Page")
        settings.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.pages.addWidget(dashboard)
        self.pages.addWidget(incidents)
        self.pages.addWidget(dispatch)
        self.pages.addWidget(responders)
        self.pages.addWidget(vehicles)
        self.pages.addWidget(reports)
        self.pages.addWidget(settings)

        layout.addWidget(self.navigation)
        layout.addWidget(self.pages)

        central_widget.setLayout(layout)

    def change_page(self, page):
        pages = {
            "Dashboard": 0,
            "Incidents": 1,
            "Dispatch": 2,
            "Responders": 3,
            "Vehicles": 4,
            "Reports": 5,
            "Settings": 6,
        }

        self.pages.setCurrentIndex(pages[page])
        self.statusBar().showMessage(f"Current Page: {page}")

    def create_status_bar(self):
        status = QStatusBar()

        status.showMessage(
            "🟢 Backend: Connected | 🟢 Database: Connected | 👤 User: Guest"
        )

        self.setStatusBar(status)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = DispatcherWindow()
    window.show()

    sys.exit(app.exec())