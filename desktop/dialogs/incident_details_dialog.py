from PyQt6.QtWidgets import (
    QDialog,
    QLabel,
    QFormLayout,
    QPushButton,
    QVBoxLayout,
)
from PyQt6.QtCore import Qt


class IncidentDetailsDialog(QDialog):

    def __init__(self, incident, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Incident Details")
        self.resize(500, 450)

        layout = QVBoxLayout()

        form = QFormLayout()

        form.addRow("Incident No:", QLabel(incident["incident_number"]))
        form.addRow("Caller:", QLabel(incident["caller_name"]))
        form.addRow("Phone:", QLabel(incident["caller_phone"]))
        form.addRow("Type:", QLabel(incident["incident_type"]))
        form.addRow("Priority:", QLabel(incident["priority"]))
        form.addRow("Status:", QLabel(incident["status"]))
        form.addRow("Address:", QLabel(incident["address"]))

        description = QLabel(incident["description"])
        description.setWordWrap(True)
        description.setAlignment(Qt.AlignmentFlag.AlignTop)

        form.addRow("Description:", description)

        layout.addLayout(form)

        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.accept)

        layout.addWidget(close_btn)

        self.setLayout(layout)