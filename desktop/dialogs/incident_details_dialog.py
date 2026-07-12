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
)

from PyQt6.QtCore import Qt


class IncidentDetailsDialog(QDialog):

    def __init__(self, incident, parent=None):
        super().__init__(parent)

        self.incident = incident

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

        print("===== Incident Updated =====")

        print(
            "Caller:",
            self.caller_name.text()
        )

        print(
            "Phone:",
            self.phone.text()
        )

        print(
            "Priority:",
            self.priority.currentText()
        )

        print(
            "Status:",
            self.status.currentText()
        )

        print(
            "Address:",
            self.address.text()
        )

        print(
            "Description:",
            self.description.toPlainText()
        )

        print("============================")

        self.accept()