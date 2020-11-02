import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from test import ui_main_window
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = ui_main_window()
def print_BD():
    print('printBD')
    
def via (query):
    return (query.fetchall())
    
def new_data (fam,name,otc,strt,bldn,corp,app,tel):
    print('new_data')

def plus_fam(fam):
    print('plus_fam')

def check (a, data):
    print('check')
    
def plus_name(name):
    print('plus_name')
    
def plus_otc(otc):
    print('plus_otc')
    
def plus_strt(strt):
    print('plus_strt')
