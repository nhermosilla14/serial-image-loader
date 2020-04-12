#!/usr/bin/env python

"""
Serial Image Loader GUI

Converts an image into 24 bit RGB and sends it through serial.
Written using PyQt5 and QtDesigner.

Nicolás Hermosilla Polanco - UTFSM 2018

Liberado para su uso, modificación y estudio bajo los términos de la GPLv3 
o superior.
"""
import serial
import sys
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets

"""
* Ui_MainWindow
*
* Clase principal que define el layout de la ventana del programa
* 
* Fue creada automáticamente mediante QtDesigner
*
"""
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(450, 500))
        MainWindow.setMaximumSize(QtCore.QSize(450, 500))
        MainWindow.setBaseSize(QtCore.QSize(450, 380))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 10, 381, 421))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.preview = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.preview.setMinimumSize(QtCore.QSize(128, 98))
        self.preview.setMaximumSize(QtCore.QSize(256, 196))
        self.preview.setBaseSize(QtCore.QSize(256, 196))
        self.preview.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.preview.setFrameShadow(QtWidgets.QFrame.Raised)
        self.preview.setScaledContents(True)
        self.preview.setAlignment(QtCore.Qt.AlignCenter)
        self.preview.setObjectName("preview")
        self.horizontalLayout_7.addWidget(self.preview)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.filenameEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.filenameEdit.setText("")
        self.filenameEdit.setObjectName("filenameEdit")
        self.horizontalLayout_5.addWidget(self.filenameEdit)
        self.selectFile = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.selectFile.setObjectName("selectFile")
        self.horizontalLayout_5.addWidget(self.selectFile)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.widthLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.widthLineEdit.setObjectName("widthLineEdit")
        self.horizontalLayout_3.addWidget(self.widthLineEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.heightLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.heightLineEdit.setObjectName("heightLineEdit")
        self.horizontalLayout_3.addWidget(self.heightLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.baudrateLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.baudrateLineEdit.setObjectName("baudrateLineEdit")
        self.horizontalLayout_6.addWidget(self.baudrateLineEdit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.portLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.portLineEdit.setObjectName("portLineEdit")
        self.horizontalLayout_6.addWidget(self.portLineEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout.addLayout(self.horizontalLayout_4)
        self.sendButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sendButton.setObjectName("sendButton")
        self.horizontalLayout.addWidget(self.sendButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 22))
        self.menubar.setObjectName("menubar")
        self.menuSession = QtWidgets.QMenu(self.menubar)
        self.menuSession.setObjectName("menuSession")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_terminal_window = QtWidgets.QAction(MainWindow)
        self.actionNew_terminal_window.setObjectName("actionNew_terminal_window")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionAbout_Serial_Image_Loader = QtWidgets.QAction(MainWindow)
        self.actionAbout_Serial_Image_Loader.setObjectName("actionAbout_Serial_Image_Loader")
        self.menuSession.addAction(self.actionExit)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout_Serial_Image_Loader)
        self.menubar.addAction(self.menuSession.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Serial Image Loader "))
        self.preview.setText(_translate("MainWindow", "Preview your image"))
        self.selectFile.setText(_translate("MainWindow", "Select File"))
        self.label_2.setText(_translate("MainWindow", "Width  "))
        self.widthLineEdit.setText(_translate("MainWindow", "512"))
        self.label.setText(_translate("MainWindow", "Height"))
        self.heightLineEdit.setText(_translate("MainWindow", "392"))
        self.label_4.setText(_translate("MainWindow", "Baudrate"))
        self.baudrateLineEdit.setText(_translate("MainWindow", "230400"))
        self.label_5.setText(_translate("MainWindow", "Port"))
        self.portLineEdit.setText(_translate("MainWindow", "/dev/ttyUSB0"))
        self.sendButton.setText(_translate("MainWindow", "Send"))
        self.menuSession.setTitle(_translate("MainWindow", "Session"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew_terminal_window.setText(_translate("MainWindow", "New terminal window..."))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation"))
        self.actionAbout_Serial_Image_Loader.setText(_translate("MainWindow", "About Serial Image Loader"))

"""
* SerialUI
*
* Clase que utiliza la interfaz diseñada arriba, para "armar" la ventana.
*
* Contiene los métodos:
*    __init__ : método llamado al instanciar la clase.
*
*    load_img : este método intenta abrir el archivo seleccionado
*    gráficamente (usando selectFile), convertirlo a RGB y redimensionarlo.
*    Si algo sale mal, captura la excepción generada y muestra el mensaje
*    de error.
*    
*    openSerialPort : este método intenta abrir el puerto serial escrito
*    en el cuadro de texto correspondiente, y despliega un mensaje de error
*    si algo sale mal.
*
*    sendImage : este método llama a los dos anteriores, y luego intenta
*    enviar el archivo dividido en 8 trozos (esto se usa exclusivamente
*    para poder actualizar el indicador de progreso). Si algo sale mal,
*    igualmente muestra un mensaje de error.
*
*    selectFile : este método permite seleccionar gráficamente el archivo
*    de imagen. Tiene incorporados filtros para evitar seleccionar archivos
*    incompatibles. Además, actualiza la vista previa de la imagen.
*
*
"""
class SerialUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(SerialUI, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.sendButton.clicked.connect(self.sendImage)
        self.ui.selectFile.clicked.connect(self.selectFile)
        self.ui.actionExit.triggered.connect(sys.exit)
        self.ui.progressBar.setValue(0)
        self.error_dialog = QtWidgets.QErrorMessage()
    
    def load_img(self):
        try:
            size = (int(self.ui.widthLineEdit.text()), int(self.ui.heightLineEdit.text()))
            self.image = Image.open(self.ui.filenameEdit.text())
            self.image = self.image.convert('RGB')
            self.image = self.image.resize(size)
        except:
            print("Error loading image file")
            self.error_dialog.showMessage('Unable to open image file. Either the file you selected is not a valid image, or you didn\'t pick any image at all.')

        
    def sendImage(self):
        try:
            self.openSerialPort()
            self.load_img()
        
            value = 0
            self.ui.progressBar.setMaximum(8)
            self.ui.progressBar.setMinimum(0)
            initial_data = [byte for pixel in self.image.getdata() for byte in pixel]
            initial_data_chunks = [initial_data[i*len(initial_data) // 8: (i+1)*len(initial_data) // 8] for i in range(8) ] 
            for init_data in initial_data_chunks:
                data = bytes(init_data)
                self.serial_port.write(data)
                value += 1
                self.ui.progressBar.setValue(value)
        except:
            print("Unable to send image.")

    def openSerialPort(self):
        self.serial_port = serial.Serial()
        self.serial_port.port = self.ui.portLineEdit.text() 
        self.serial_port.baudrate = int(self.ui.baudrateLineEdit.text())
        try:
            self.serial_port.open()
        except:
            print("Serial port error")
            self.error_dialog.showMessage('Unable to open serial port. Please check for typos or incorrect permissions.')



    def selectFile(self):
        self.ui.filenameEdit.setText(QtWidgets.QFileDialog.getOpenFileName(QtWidgets.QFileDialog(), "Choose an image...", ".", "Images (*.png *.jpg *.jpeg *.gif *.bmp)" )[0]) 
        image = QtGui.QImage(self.ui.filenameEdit.text())
        self.ui.preview.setPixmap(QtGui.QPixmap.fromImage(image))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = SerialUI()
    window.show()
    sys.exit(app.exec_())
