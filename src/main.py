import os
from trim import trim_to_object
from PyQt6.QtWidgets import QFileDialog
from PIL import Image
from PyQt6.QtCore import pyqtSlot
from gui import QtWidgets, Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    """Docstring for MainWindow."""

    def __init__(self):
        """TODO: to be defined."""
        super().__init__()
        self.setupUi(self)

        # set path to directory from which script is run
        self.base_path = os.getcwd()
        self.input_path = self.base_path + "/input_folder"
        self.output_path = self.base_path + "/output_folder"

        self.input_path_line.setText(self.input_path)
        self.output_path_line.setText(self.output_path)

    @pyqtSlot()
    def on_input_btn_clicked(self):
        """When input button clicked open file dialog and set input path to
        folder selected.
        :returns: TODO

        """
        self.input_path = QFileDialog.getExistingDirectory(
            self, "Select Input Folder")
        self.input_path_line.setText(self.input_path)

    @pyqtSlot()
    def on_output_btn_clicked(self):
        """When output button clicked open file dialog and set output path to
        folder selected.
        :returns: TODO

        """
        self.output_path = QFileDialog.getExistingDirectory(
            self, "Select Output Folder")
        self.output_path_line.setText(self.output_path)

    @pyqtSlot()
    def on_trim_btn_clicked(self):
        """When run button clicked run trim on all images in input folder and
        save to output folder.
        :returns: TODO

        """
        self.input_path = self.input_path_line.text()
        self.output_path = self.output_path_line.text()

        images = [f for f in os.listdir(self.input_path) if
                  os.path.isfile(os.path.join(self.input_path, f))]

        for image in images:
            img = Image.open(self.input_path + "/" + image)
            trimmed_img = trim_to_object(img)
            trimmed_img.save(self.output_path + "/" + image)


def main():
    """TODO: Docstring for main.
    :returns: TODO

    """

    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
