
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from logic import generate_random_numbers, calculate_sum, calculate_avg, calculate_max, sort_numbers

class ListOperationApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("list_ui.ui", self)
        self.numbers = []

        # Başlangıçta toggle butonları ve combobox disable
        self.sumRadio.setEnabled(False)
        self.avgRadio.setEnabled(False)
        self.maxRadio.setEnabled(False)
        self.sortRadio.setEnabled(False)
        self.sortComboBox.setEnabled(False)

        self.generateButton.clicked.connect(self.generate_numbers)
        self.sumRadio.toggled.connect(self.perform_operation)
        self.avgRadio.toggled.connect(self.perform_operation)
        self.maxRadio.toggled.connect(self.perform_operation)
        self.sortRadio.toggled.connect(self.perform_operation)
        self.sortComboBox.currentIndexChanged.connect(self.perform_operation)

    def generate_numbers(self):
        self.numbers = generate_random_numbers()
        self.numbersTextEdit.setPlainText(", ".join(map(str, self.numbers)))
        self.statusLabel.setText("Numbers are generated")
        self.enable_operations()

    def enable_operations(self):
        self.sumRadio.setEnabled(True)
        self.avgRadio.setEnabled(True)
        self.maxRadio.setEnabled(True)
        self.sortRadio.setEnabled(True)
        self.sortComboBox.setEnabled(False)

    def perform_operation(self):
        if self.sumRadio.isChecked():
            result = calculate_sum(self.numbers)
            self.resultTextEdit.setPlainText(str(result))
            self.statusLabel.setText("Sum calculated")

        elif self.avgRadio.isChecked():
            result = calculate_avg(self.numbers)
            self.resultTextEdit.setPlainText(str(result))
            self.statusLabel.setText("Average calculated")

        elif self.maxRadio.isChecked():
            result = calculate_max(self.numbers)
            self.resultTextEdit.setPlainText(str(result))
            self.statusLabel.setText("Maximum calculated")

        elif self.sortRadio.isChecked():
            self.sortComboBox.setEnabled(True)
            if self.sortComboBox.currentText() == "Ascending":
                result = sort_numbers(self.numbers, ascending=True)
            else:
                result = sort_numbers(self.numbers, ascending=False)
            self.resultTextEdit.setPlainText(", ".join(map(str, result)))
            self.statusLabel.setText("Sorted")
