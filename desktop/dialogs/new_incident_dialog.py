from PyQt6.QtWidgets import (
    QDialog,
    QLabel,
    QLineEdit,
    QTextEdit,
    QPushButton,
    QComboBox,
    QFormLayout,
    QHBoxLayout,
    QVBoxLayout,
    QMessageBox,
)

from services.api_client import APIClient


class NewIncidentDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.api = APIClient()

        self.setWindowTitle("Create New Incident")
        self.setMinimumWidth(500)

        self.caller_name = QLineEdit()
        self.phone = QLineEdit()
        self.address = QLineEdit()

        self.incident_type = QComboBox()
        self.incident_type.addItems([
            "Medical",
            "Fire",
            "Motor Vehicle Accident",
            "Crime",
            "Rescue",
            "Other"
        ])

        self.priority = QComboBox()
        self.priority.addItems([
            "Low",
            "Medium",
            "High",
            "Critical"
        ])

        self.description = QTextEdit()

        form = QFormLayout()

        form.addRow("Caller Name:", self.caller_name)
        form.addRow("Phone:", self.phone)
        form.addRow("Incident Type:", self.incident_type)
        form.addRow("Priority:", self.priority)
        form.addRow("Address:", self.address)
        form.addRow("Description:", self.description)

        save_btn = QPushButton("Save")
        cancel_btn = QPushButton("Cancel")

        save_btn.clicked.connect(self.save_incident)
        cancel_btn.clicked.connect(self.reject)

        buttons = QHBoxLayout()
        buttons.addStretch()
        buttons.addWidget(save_btn)
        buttons.addWidget(cancel_btn)

        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addLayout(buttons)

        self.setLayout(layout)

    def save_incident(self):

        incident = {
            "caller_name": self.caller_name.text(),
            "caller_phone": self.phone.text(),
            "incident_type": self.incident_type.currentText(),
            "priority": self.priority.currentText(),
            "address": self.address.text(),
            "description": self.description.toPlainText(),
        }

        try:
            self.api.create_incident(incident)

            QMessageBox.information(
                self,
                "Success",
                "Incident created successfully."
            )

            self.accept()

        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                str(e)
            )