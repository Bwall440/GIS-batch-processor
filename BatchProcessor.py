"""
This program is designed to function with 'Processor.py' and requires both files to function. 

this program will take the input values chosen the user and use them to batch process raster and vector
files without having to run each file individually through the process. Information on how to use the code
can be found in the readme file. 
"""

from PyQt5 import QtCore, QtWidgets, QtGui
import sys, os
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
import subprocess

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Batch Processor")
        MainWindow.resize(400, 450)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 30, 321, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        #Input Folder and line edit
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.selectInputFolder)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        
        #Spacer
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        
        #Output folder and line edit
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(self.selectOutputFolder)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        
        #Spacer
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        
        #Select file type and combo box
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        
        #Spacer
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        
        #Output projection and combo
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.comboBox_2 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout.addWidget(self.comboBox_2)
        
        
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 350, 321, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        #Run button
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_4.clicked.connect(self.RunProgram)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1118, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #extra stuff
        self.error_dialog = QtWidgets.QErrorMessage() 
        



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Input Folder"))
        self.pushButton.setText(_translate("MainWindow", "Select Input Folder"))
        self.label_2.setText(_translate("MainWindow", "Output Folder"))
        self.pushButton_2.setText(_translate("MainWindow", "Select Output Folder"))
        self.label_3.setText(_translate("MainWindow", "File Type"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Select File Type"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Raster"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Vector"))
        self.label_4.setText(_translate("MainWindow", "Output Projection"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "WGS_1984_UTM_10N"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "NAD_1983_UTM_Zone_10N"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Proj 3"))
        self.pushButton_4.setText(_translate("MainWindow", "Start Batch Processing"))
##########################################################################################
        """
        These functions are button functions attached to the push buttons. these will allow
        the user to open up a folder browser when clicked. the folder extention will then be
        put into the line edit box associated with the button.
        """
    def selectInputFolder(self, MainWindow):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        Filename = QFileDialog.getExistingDirectory()
        self.lineEdit.setText(Filename)
    
    def selectOutputFolder(self, MainWindow):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        Filename = QFileDialog.getExistingDirectory()
        self.lineEdit_2.setText(Filename)
#########################################################################################        

    def RunProgram(self, MainWindow):
        """
        this will start the process using the inputs from the GUI options. variables will be
        taken from the inputs and then verified. Depending on the file type selected, the function
        will then direct the process down the desired path.
        """
        InputPath = self.lineEdit.text()
        OutputPath = self.lineEdit_2.text()
        FileType = self.comboBox.currentText()
        OutputRaster = self.comboBox_2.currentText()
        
        #Debug/test
        print("Input Folder: "+InputPath)
        print("Output Folder "+OutputPath)
        print("File Type: "+FileType)
        print("Output Raster: "+OutputRaster)
        
        
        if (FileType in ('Raster', 'Vector')):
            print ("File Type Selected!")
            #This IF statement will direct towards raster processing
            #send to raster file verifier (makes sure all files are raster in input folder)
            
            # edit the path below to go to your script file saved from above
            ScriptPath="C:\\Users\\bew171\\Desktop\\TechDemo_Final\\Processor.py"
            
            # path to the version of python we want to launch
            PythonPath="C:\\Program Files\\ArcGIS\\Pro\\bin\\Python\\envs\\arcgispro-py3\\python.exe";
            
            # parameters for the random distribution
            InputPathToArc = InputPath+"\\"
            OutputPathToArc = OutputPath+"\\"
            FileTypeToArc = FileType
            OutputRasterToArc = OutputRaster
            
            # Command line
            TheCommand=PythonPath+" "+ScriptPath+" "+str(InputPathToArc)+" "+str(OutputPathToArc)+" "+str(FileTypeToArc)+" "+format(OutputRasterToArc)
            
            # subprocess call to put up the histogram
            subprocess.call(TheCommand)            
            
            #Vector file deletion workaround. 
            ################
            #this will delete the vector files in the input folder if the process completed.
            DeleteList = os.listdir(InputPath)
            
            for TheFile in DeleteList:
                TheFileName, TheFileExtension = os.path.splitext(TheFile)
                DeleteFilePath=InputPath+"/"+TheFileName+TheFileExtension
                if FileType == "Vector":
                    
                    if (TheFileExtension in (".cpg",".dbf",".prj",".sbn",".sbx",".shx")):
                        os.remove(DeleteFilePath)
                    
                        
            ################
            TheMessageBox=QMessageBox()
            TheMessageBox.setText("Processing Comlete!")
            TheMessageBox.exec()
            
            print("Reprojection Complete")
        elif (FileType=='Vector'):
            #Not used but afraid to delete
            print("Vector Path!")
        else:
            #This will not let you continue unless you select a file type.
            print("you need to select a file type")
            self.error_dialog.showMessage('You need to select a file type')

    
            
            
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

