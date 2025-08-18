import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from Interface.Interface import Ui_MainWindow
from utils.Generate import Generate
from utils.WriteFile import WriteFile


class MainWindow(QMainWindow):
    def GenerateButton(self,action:bool):
        self.ui.pushButton_2.setEnabled(action)
        self.ui.pushButton_3.setEnabled(action)
        self.ui.label.setEnabled(action)
        self.ui.label_2.setEnabled(action)
        self.ui.spinBox.setEnabled(action)
        self.ui.spinBox_2.setEnabled(action)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.fileName:tuple[str,str]
        self.GenerateButton(False)
        self.output:list[str]

    def start(self):
        QMessageBox.information(self,"Generation has started","Please wait...")
        self.GenerateButton(False)
        generator = Generate(self.ui.spinBox.value(),self.ui.spinBox_2.value(),self.fileName[0])
        self.output = generator()
        WriteFile(self.fileName[0])(self.output)
        QMessageBox.information(self,
            "Generation Complete",
            "The dictionary has been generated successfully.\nPlease check the directory of your .py file. There should be a txt file contains the same name.")
        self.close()

    def openFileSelectionDialog(self):
        self.fileName = (
            QFileDialog.getOpenFileName(self,self.tr("Open Python File"), "/", self.tr("Python Files (*.py)")))
        if self.fileName[0]:
            self.GenerateButton(True)
            self.ui.pushButton.setText(f"File Selected: {self.fileName[0]}")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())