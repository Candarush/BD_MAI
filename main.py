import sys
import os
import func
from PyQt5 import QtCore, QtGui, QtWidgets
from test import ui_main_window
from test_1 import ui_dialog_window
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = ui_main_window()
Dialog = QtWidgets.QDialog()
di = ui_dialog_window()
ui.setupUi(MainWindow)
MainWindow.show()

def transp():
    fam = ui.textEdit.toPlainText()
    name = ui.textEdit_2.toPlainText()
    otc = ui.textEdit_3.toPlainText()
    strt = ui.textEdit_6.toPlainText()
    bldn = ui.textEdit_5.toPlainText()
    corp = ui.textEdit_4.toPlainText()
    app = ui.textEdit_7.toPlainText()
    tel = ui.textEdit_8.toPlainText()
    func.new_data(fam,name,otc,strt,bldn,corp,app,tel)
    ui.textEdit.clear()
    ui.textEdit_2.clear()
    ui.textEdit_3.clear()
    ui.textEdit_4.clear()
    ui.textEdit_5.clear()
    ui.textEdit_6.clear()
    ui.textEdit_7.clear()
    ui.textEdit_8.clear()
    
def view_BD():
    print('viewBD')
    
def hi():
    print ("Hi")
ui.pushButton_2.clicked.connect( func.print_BD )
ui.pushButton.clicked.connect( transp )
ui.pushButton_3.clicked.connect( view_BD)
sys.exit(app.exec_())
