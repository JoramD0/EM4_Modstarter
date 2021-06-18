import os
import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLabel, QVBoxLayout, QComboBox
from PyQt5 import QtGui

mainDir = os.path.dirname(os.path.realpath(__file__))
modDir = mainDir + "\Mods"
modFolders = [name for name in os.listdir(modDir) if os.path.isdir(os.path.join(modDir, name))]

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QtGui.QIcon("911.ico"))

        # Set the label before the ComboBox
        self.topLabel = QLabel("Select Emergency 4 mod:", self)

        # Define the combobox with items
        combobox = QComboBox(self)

        combobox.addItem("Select mod...")
        for x in modFolders:
            os.chdir(f"{modDir}/{x}")
            if os.path.exists("e4mod.info") and os.path.isfile("e4mod.info"):
                combobox.addItem(str(x))
            os.chdir(mainDir)

        # Set the label after the ComboBox
        self.button = QPushButton("", self)
        self.button.hide()
        self.button.adjustSize()
        self.button.clicked.connect(self.onClicked)

        # Define vartical layout box
        vLayout = QVBoxLayout()
        vLayout.addWidget(self.topLabel)
        vLayout.addWidget(combobox)
        vLayout.addWidget(self.button)

        # Call the custom method if any item is selected
        combobox.activated[str].connect(self.onSelected)

        # Set the configurations for the window
        self.setContentsMargins(20, 20, 20, 20)
        self.setLayout(vLayout)
        self.setWindowTitle("Emergency 4 Mod Launcher")

    # Custom function to read the value of the selected item
    def onSelected(self, txtVal):
        self.button.setText("Launch: " + txtVal)
        global selectedText
        if txtVal != "Select mod...":
            self.button.show()
            selectedText = txtVal
        else:
            self.button.hide()
            self.adjustSize()
            selectedText = txtVal

    def onClicked(self):
        formattedText = f'"{selectedText}"'
        formattedFolder = f'"{mainDir}"'
        subprocess.Popen(f'cmd /c "start /d {formattedFolder} em4.exe -game -mod {formattedText}"')
        self.close()

# Create app object and execute the app
app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
