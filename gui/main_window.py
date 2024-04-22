from PyQt6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window properties
        self.setWindowTitle('Not-YNAB App')
        self.setGeometry(100, 100, 800, 600)

        # Add status bar
        self.statusBar().showMessage('Ready')

        # Display window
        self.show()
