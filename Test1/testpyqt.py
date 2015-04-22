import os
import sys
import math


#from PyQt5.QtCore import QEvent
#from PyQt5.QtGui import (QGuiApplication, QMatrix4x4, QOpenGLContext,
        #QOpenGLShader, QOpenGLShaderProgram, QSurfaceFormat, QWindow, QTabWidget, QWidget)
import PyQt5.QtGui
import PyQt5.QtCore
import PyQt5.QtWidgets
from PyQt5.Qsci import QsciScintilla, QsciLexerPython, QsciLexerCPP
import PyQt5.Qsci

from PyQt5.QtGui import QFont, QColor, QFont

##from PyQt5.QtCore import QEvent, pyqtSignal, QPoint, QSize, Qt

#from PyQt5.QtGui import QGuiApplication, QMatrix4x4, QOpenGLContext,QOpenGLShader, QOpenGLShaderProgram, QSurfaceFormat, QWindow 

#from PyQt5.QtWidgets import QMenuBar, QTabWidget, QWidget, QApplication,  QVBoxLayout, QMessageBox 
  
#from PyQt5.QtOpenGL import QGLWidget

#class Window(QWindow):
##    parentWindows = None
    #def __init__(self, parent=None):
      #print("Create Window")
      #super(Window,self).__init__(parent)
      
    #def close(self):
      #self.parentapplication.close()
    
    #def add(self, parentW=None):
      #self.parentWindows.addWindow(self)
      
class GLSLEditor(QsciScintilla):
  def __init__(self):
    super(GLSLEditor, self).__init__()
    lexer = QsciLexerCPP()
    lexer.setColor(QColor("blue"), 1) 
    self.setMarginLineNumbers(1, True)
    self.setMarginWidth(1, "-----")
    self.setMarginsBackgroundColor(QColor("green"))
    self.setCaretLineVisible(True)
    self.setCaretLineBackgroundColor(QColor("#ffe4e4"))
    self.setLexer(lexer)
    self.show()
    
    
class TabbedWindow(PyQt5.QtWidgets.QMainWindow):
  def __init__(self, Parent=None):
    super(TabbedWindow, self).__init__(Parent)
    self.setGeometry(0, 0, 640, 480)
    self.setWindowTitle("Shader Editor")
    self.setupUI()
    #self.center()
  

  
  def setupUI(self):
    menu_bar = PyQt5.QtWidgets.QMenuBar()
    file = menu_bar.addMenu("&File")
    help = menu_bar.addMenu("&Help")
    build = menu_bar.addMenu("&Build")
    exit = menu_bar.addMenu("&Exit")    
    tabs = PyQt5.QtWidgets.QTabWidget()
    centerwidget = PyQt5.QtWidgets.QWidget()
    vshadertab = PyQt5.QtWidgets.QWidget()
    fshadertab = PyQt5.QtWidgets.QWidget()
    vshadertab_layout = PyQt5.QtWidgets.QVBoxLayout(vshadertab)
    fshadertab_layout = PyQt5.QtWidgets.QVBoxLayout(fshadertab)
    fshadereditor = GLSLEditor() # PyQt5.QtWidgets.QTextEdit()
    vshadereditor = GLSLEditor() # PyQt5.QtWidgets.QTextEdit()
    fshadertab_layout.addWidget(fshadereditor)
    vshadertab_layout.addWidget(vshadereditor)
    tabs.addTab(vshadertab, "Vertex Shader")
    tabs.addTab(fshadertab, "Fragment Shader")
    vbox = PyQt5.QtWidgets.QVBoxLayout()
    vbox.addWidget(menu_bar)
    vbox.addWidget(tabs)
    centerwidget.setLayout(vbox)
    self.setCentralWidget(centerwidget)
    pass
 
    #tabs = QTabWidget()
    #tab1 = QWidget()
    #tab2 = QWidget()
    
    #p1_vertical = QVBoxLayout(tab1)
    #p2_vertical = QVBoxLayout(tab2)
    
    #tabs.addTab(tab1, "Vertex Shader")
    #tabs.addTab(tab2, "Fragment Shader")
    
    #vbox = QVBoxLayout()
    #vbox.addWidget(menu_bar)
    #vbox.addWidget(tabs)
    #self.setLayout(vbox)
    #pass
    
    #def center(self):
      ##screen = QDesktopWidget().screenGeometry()
      ##size = self.geometry()
      ##self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
      #pass      


#class Windows(object):
  #def __init__(self):
    #self.WindowsList = None
    #self.Viewer = Window()
    #self.Viewer.resize(640, 480) 
    #self.Viewer.show()
    #self.Viewer.add(self)
    #self.Editor = Window()
    #self.Editor.resize(640, 480)
    #self.Editor.show()
  #@staticmethod
  #def addWindow(self, Window):
     #if self.WindowsList is None:
       #self.WindowsList = Window
  
  #def quit(self):
    #pass
    
if __name__=='__main__':
  app = PyQt5.QtWidgets.QApplication(sys.argv)
  window = TabbedWindow()
  #window.setupUI()
  window.show()
  sys.exit(app.exec_())
  
    
