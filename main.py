import sys
from PyQt6.QtWidgets import QApplication
from gui.main_window import MainWindow


def main():
    # Create application object
    app = QApplication(sys.argv)

    # Create main window
    win = MainWindow()

    # Start app's event loop
    sys.exit(app.exec())


if __name__ == '__main__':
    main()