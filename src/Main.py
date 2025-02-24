import sys
from PyQt5 import QtWidgets
from MainWindow import Ui_MainWindow  # Import the auto-generated MainWindow UI
from ExactnessPage import Ui_Form as ExactnessPage  # Import the Exactness Page UI
from HomogeneityPage import Ui_Form as HomogeneityPage  # Import the Homogeneity Page UI
from checks import check_exactness, check_homogeneity  # Import the logic from checks.py


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Differential Equation Analyzer")
        self.setGeometry(200, 200, 800, 600)

        # Set up the UI from the generated MainWindow UI file
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect buttons to their respective actions
        self.ui.checkExactness.clicked.connect(self.openExactnessPage)
        self.ui.checkHomogeneity.clicked.connect(self.openHomogeneityPage)
        self.ui.exitProgram.clicked.connect(self.close)

    def openExactnessPage(self):
        self.window = ExactnessPage()
        self.window.show()
        self.close()

    def openHomogeneityPage(self):
        self.window = HomogeneityPage()
        self.window.show()
        self.close()


class ExactnessPage(QtWidgets.QWidget, ExactnessPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Connect the "Check Exactness" button to the function
        self.checkForExactness.clicked.connect(self.checkExactness)
        self.backToMenu.clicked.connect(self.backToMain)

    def checkExactness(self):
        m_expr = self.mXYInput.text()  # Get input for M(x, y)
        n_expr = self.nXYInput.text()  # Get input for N(x, y)

        result = check_exactness(m_expr, n_expr)  # Call the check_exactness function from checks.py
        self.resultText.setText(result)  # Display the result

    def backToMain(self):
        self.window = MainWindow()
        self.window.show()
        self.close()


class HomogeneityPage(QtWidgets.QWidget, HomogeneityPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Connect the "Check Homogeneity" button to the function
        self.checkForHomogeneity.clicked.connect(self.checkHomogeneity)
        self.backToMenu.clicked.connect(self.backToMain)

    def checkHomogeneity(self):
        m_expr = self.mXYInput.text()  # Get input for M(x, y)
        n_expr = self.nXYInput.text()  # Get input for N(x, y)

        result = check_homogeneity(m_expr, n_expr)  # Call the check_homogeneity function from checks.py
        self.resultText.setText(result)  # Display the result

    def backToMain(self):
        self.window = MainWindow()
        self.window.show()
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())