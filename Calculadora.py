import sys
from PySide6.QtWidgets import (QApplication, QWidget, QFormLayout, QVBoxLayout, 
                               QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)

class CalculadoraBasica(QWidget):
    """
    Ventana principal de la calculadora gráfica.
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora Básica")

        layout_principal = QVBoxLayout()

        self.formulario = QFormLayout()

        self.num1_label = QLabel("Número 1: ")
        self.num1_input = QLineEdit()
        self.num1_input.setPlaceholderText("Ej. 10.5")

        self.num2_label = QLabel("Número 2: ")
        self.num2_input = QLineEdit()
        self.num2_input.setPlaceholderText("Ej. 2")

        self.formulario.addRow(self.num1_label, self.num1_input)
        self.formulario.addRow(self.num2_label, self.num2_input)

        layout_botones = QHBoxLayout()

        self.btn_suma = QPushButton("+ Sumar")
        self.btn_resta = QPushButton("- Restar")
        self.btn_multi = QPushButton("x Multiplicar")
        self.btn_div = QPushButton("/ Dividir")

        layout_botones.addWidget(self.btn_suma)
        layout_botones.addWidget(self.btn_resta)
        layout_botones.addWidget(self.btn_multi)
        layout_botones.addWidget(self.btn_div)

        self.resultado_label = QLabel("Resultado: ")
        self.resultado_label.setStyleSheet("font-weight: bold; font-size: 14px; margin-top: 10px;")

        self.btn_suma.clicked.connect(self.sumar)
        self.btn_resta.clicked.connect(self.restar)
        self.btn_multi.clicked.connect(self.multiplicar)
        self.btn_div.clicked.connect(self.dividir)

        layout_principal.addLayout(self.formulario)
        layout_principal.addLayout(layout_botones)
        layout_principal.addWidget(self.resultado_label)

        self.setLayout(layout_principal)

    def obtener_valores(self):
        try:
            num1 = float(self.num1_input.text().strip())
            num2 = float(self.num2_input.text().strip())
            return num1, num2
        except ValueError:
            QMessageBox.warning(self, "Error de entrada", "Por favor, introduce números válidos en ambos campos.")
            return None, None

    def sumar(self):
        num1, num2 = self.obtener_valores()
        if num1 is not None and num2 is not None:
            resultado = num1 + num2
            self.resultado_label.setText(f"Resultado: {resultado}")

    def restar(self):
        num1, num2 = self.obtener_valores()
        if num1 is not None and num2 is not None:
            resultado = num1 - num2
            self.resultado_label.setText(f"Resultado: {resultado}")

    def multiplicar(self):
        num1, num2 = self.obtener_valores()
        if num1 is not None and num2 is not None:
            resultado = num1 * num2
            self.resultado_label.setText(f"Resultado: {resultado}")

    def dividir(self):
        num1, num2 = self.obtener_valores()
        if num1 is not None and num2 is not None:
            if num2 == 0:
                QMessageBox.critical(self, "Error matemático", "No es posible dividir entre cero.")
            else:
                resultado = num1 / num2
                self.resultado_label.setText(f"Resultado: {resultado}")

if __name__ == "__main__":
    # Inicialización de la aplicación
    app = QApplication(sys.argv)

    # Crear la ventana
    ventana = CalculadoraBasica()
    ventana.show()

    # Ciclo de eventos de la aplicación
    sys.exit(app.exec())