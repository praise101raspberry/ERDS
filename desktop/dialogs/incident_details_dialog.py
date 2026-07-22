from PyQt6.QtWidgets import (
    QDialog,
    QLabel,
    QFormLayout,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QComboBox,
    QTextEdit,
    QMessageBox,
)

from PyQt6.QtCore import Qt
from services.api_client import APIClient

class IncidentDetailsDialog(QDialog):

    def __init__(self, incident, parent=None):
        super().__init__(parent)

        self.incident = incident
        self.api = APIClient()

        self.setWindowTitle("Incident Details")
        self.resize(550, 500)

        layout = QVBoxLayout()

        # ------------------------
        # Form Layout
        # ------------------------

        form = QFormLayout()

        # Read-only fields
        form.addRow(
            "Incident No:",
            QLabel(incident["incident_number"])
        )

        form.addRow(
            "Incident Type:",
            QLabel(incident["incident_type"])
        )

        # Editable fields

        self.caller_name = QLineEdit(
            incident["caller_name"]
        )

        form.addRow(
            "Caller:",
            self.caller_name
        )

        self.phone = QLineEdit(
            incident["caller_phone"]
        )

        form.addRow(
            "Phone:",
            self.phone
        )

        self.priority = QComboBox()

        self.priority.addItems([
            "Low",
            "Medium",
            "High",
            "Critical"
        ])

        self.priority.setCurrentText(
            incident["priority"]
        )

        form.addRow(
            "Priority:",
            self.priority
        )

        self.status = QComboBox()

        self.status.addItems([
            "New",
            "Assigned",
            "En Route",
            "On Scene",
            "Closed"
        ])

        self.status.setCurrentText(
            incident["status"]
        )

        form.addRow(
            "Status:",
            self.status
        )

        self.address = QLineEdit(
            incident["address"]
        )

        form.addRow(
            "Address:",
            self.address
        )

        self.description = QTextEdit()

        self.description.setPlainText(
            incident["description"]
        )

        self.description.setMinimumHeight(120)

        form.addRow(
            "Description:",
            self.description
        )

        layout.addLayout(form)

        # ------------------------
        # Buttons
        # ------------------------

        buttons = QHBoxLayout()

        buttons.addStretch()

        save_btn = QPushButton("💾 Save")
        close_btn = QPushButton("Close")

        buttons.addWidget(save_btn)
        buttons.addWidget(close_btn)

        layout.addLayout(buttons)

        save_btn.clicked.connect(self.save_changes)
        close_btn.clicked.connect(self.reject)

        self.setLayout(layout)

    # -----------------------------------
    # Save (temporary)
    # -----------------------------------

    def save_changes(self):

        data = {
            "caller_name": self.caller_name.text(),
            "caller_phone": self.phone.text(),
            "priority": self.priority.currentText(),
            "status": self.status.currentText(),
            "address": self.address.text(),
            "description": self.description.toPlainText()
        }

        try:

            updated_incident = self.api.update_incident(
                self.incident["id"],
                data
            )

            QMessageBox.information(
                self,
                "Success",
                "Incident updated successfully."
            )

            self.accept()

        except Exception as e:

            QMessageBox.critical(
                self,
                "Update Failed",
                str(e)
            )