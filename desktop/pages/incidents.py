from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QHBoxLayout,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QLineEdit
)
from PyQt6.QtCore import Qt
from dialogs.incident_details_dialog import IncidentDetailsDialog

from services.api_client import APIClient
from dialogs.new_incident_dialog import NewIncidentDialog
from widgets.stat_card import StatCard

class IncidentsPage(QWidget):

    def __init__(self):
        super().__init__()

        self.api = APIClient()

        layout = QVBoxLayout()

        header = QHBoxLayout()

        title = QLabel("🚨 Incident Management")
        title.setStyleSheet("""
            font-size:22px;
            font-weight:bold;
        """)

        self.search = QLineEdit()
        self.search.setPlaceholderText("🔍 Search incidents...")

        new_btn = QPushButton("➕ New Incident")
        refresh_btn = QPushButton("🔄 Refresh")

        header.addWidget(title)
        header.addStretch()
        header.addWidget(self.search)
        header.addWidget(new_btn)
        header.addWidget(refresh_btn)

        layout.addLayout(header)

        stats_layout = QHBoxLayout()

        self.active_card = StatCard("Active", 0, "#E74C3C")
        self.critical_card = StatCard("Critical", 0, "#C0392B")
        self.new_card = StatCard("New", 0, "#27AE60")
        self.total_card = StatCard("Total", 0, "#2980B9")

        stats_layout.addWidget(self.active_card)
        stats_layout.addWidget(self.critical_card)
        stats_layout.addWidget(self.new_card)
        stats_layout.addWidget(self.total_card)

        layout.addLayout(stats_layout)

        self.table = QTableWidget()

        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self.table.setColumnCount(6)

        self.table.setHorizontalHeaderLabels([
            "Incident No",
            "Type",
            "Priority",
            "Status",
            "Caller",
            "Phone"
        ])

        self.table.setAlternatingRowColors(True)

        self.table.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )

        self.table.setSelectionMode(
            QTableWidget.SelectionMode.SingleSelection
        )

        self.table.setEditTriggers(
            QTableWidget.EditTrigger.NoEditTriggers
        )

        layout.addWidget(self.table)

        self.setLayout(layout)

        refresh_btn.clicked.connect(self.load_incidents)
        self.table.cellDoubleClicked.connect(self.open_incident)
        new_btn.clicked.connect(self.new_incident)
        self.search.textChanged.connect(self.filter_table)

        self.load_incidents()

    def open_incident(self, row, column):

        incident = self.incidents[row]

        dialog = IncidentDetailsDialog(
            incident,
            self
        )

        dialog.exec()

    def new_incident(self):

        dialog = NewIncidentDialog(self)

        if dialog.exec():
            self.load_incidents()

    def load_incidents(self):
        try:
            incidents = self.api.get_incidents()
            self.incidents = incidents

            self.table.setRowCount(len(incidents))

            for row, incident in enumerate(incidents):

                self.table.setItem(
                    row, 0,
                    QTableWidgetItem(incident["incident_number"])
                )

                self.table.setItem(
                    row, 1,
                    QTableWidgetItem(incident["incident_type"])
                )

                priority_item = QTableWidgetItem(incident["priority"])

                if incident["priority"] == "Critical":
                    priority_item.setBackground(Qt.GlobalColor.red)

                elif incident["priority"] == "High":
                    priority_item.setBackground(Qt.GlobalColor.darkYellow)

                elif incident["priority"] == "Medium":
                    priority_item.setBackground(Qt.GlobalColor.yellow)

                elif incident["priority"] == "Low":
                    priority_item.setBackground(Qt.GlobalColor.green)

                self.table.setItem(row, 2, priority_item)

                status_item = QTableWidgetItem(incident["status"])

                status = incident["status"]

                if status == "New":
                    status_item.setBackground(Qt.GlobalColor.green)

                elif status == "Assigned":
                    status_item.setBackground(Qt.GlobalColor.yellow)

                elif status == "En Route":
                    status_item.setBackground(Qt.GlobalColor.cyan)

                elif status == "On Scene":
                    status_item.setBackground(Qt.GlobalColor.blue)

                elif status == "Closed":
                    status_item.setBackground(Qt.GlobalColor.lightGray)

                self.table.setItem(row, 3, status_item)

                self.table.setItem(
                    row, 4,
                    QTableWidgetItem(incident["caller_name"])
                )

                self.table.setItem(
                    row, 5,
                    QTableWidgetItem(incident["caller_phone"])
                )

        except Exception as e:
            print("Failed to load incidents:", e)

        # Calculate statistics
        active = 0
        critical = 0
        new = 0

        for incident in incidents:

            if incident["status"] != "Closed":
                active += 1

            if incident["priority"] == "Critical":
                critical += 1

            if incident["status"] == "New":
                new += 1

        # Update cards
        self.active_card.setValue(active)
        self.critical_card.setValue(critical)
        self.new_card.setValue(new)
        self.total_card.setValue(len(incidents))

    def filter_table(self, text):

        text = text.lower()

        for row in range(self.table.rowCount()):

            show = False

            for column in range(self.table.columnCount()):

                item = self.table.item(row, column)

                if item and text in item.text().lower():
                    show = True
                    break

            self.table.setRowHidden(row, not show)