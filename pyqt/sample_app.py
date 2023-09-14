import sys
import typing
from functools import partial
from PyQt6 import QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QAction, QKeySequence
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QMenu, QToolBar, QStyle, QSpinBox)

class Window(QMainWindow):
    
    def __init__(self, parent = None):

        super().__init__(parent)

        self.setWindowTitle("Pyhton Menu's and Toolbars")
        self.resize(400,200)
        self.centralWidget = QLabel("central widget")
        self.centralWidget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.setCentralWidget(self.centralWidget)

        self._createActions()
        self._createMenuBar()
        self._createToolBars()
        self._connectActions()
        self._createStatusBar()

    def _createMenuBar(self):

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        
        file_pixmapi = QStyle.StandardPixmap.SP_DirHomeIcon
        file_icon = self.style().standardIcon(file_pixmapi)
        fileMenu = menubar.addMenu(QIcon(file_icon), " &file")

        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        self.openRecentMenu = fileMenu.addMenu("Open Recent")
        fileMenu.addAction(self.saveAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAction)
        
        edit_pixmapi = QStyle.StandardPixmap.SP_FileDialogContentsView
        edit_icon = self.style().standardIcon(edit_pixmapi)
        editMenu = menubar.addMenu(QIcon(edit_icon)," &edit")

        editMenu.addAction(self.copyAction)
        editMenu.addAction(self.pasteAction)
        editMenu.addAction(self.cutAction)
        editMenu.addSeparator()
        findMenu = editMenu.addMenu(" find and replace")

        find_px = QStyle.StandardPixmap.SP_FileDialogContentsView
        find_icon = self.style().standardIcon(find_px)
        findMenu.addAction(QIcon(find_icon), " find...")

        replace_px = QStyle.StandardPixmap.SP_BrowserReload
        replace_icon = self.style().standardIcon(replace_px)
        findMenu.addAction(QIcon(replace_icon), " replace...")
        
        help_pixmapi = QStyle.StandardPixmap.SP_FileDialogInfoView
        help_icon = self.style().standardIcon(help_pixmapi)
        helpMenu = menubar.addMenu(QIcon(help_icon), " &help")

        helpMenu.addAction(self.helpContentAction)
        helpMenu.addAction(self.aboutAction)

    def _createToolBars(self):

        fileToolBar = self.addToolBar(" file")
        fileToolBar.addAction(self.newAction)
        fileToolBar.addAction(self.openAction)
        fileToolBar.addAction(self.saveAction)

        editToolBar = QToolBar(" &edit", self)
        self.addToolBar(Qt.ToolBarArea.RightToolBarArea,editToolBar)
        editToolBar.addAction(self.copyAction)
        editToolBar.addAction(self.pasteAction)
        editToolBar.addAction(self.cutAction)


        helpToolBar = QToolBar(" &help", self)
        self.addToolBar(Qt.ToolBarArea.LeftToolBarArea, helpToolBar)
        
        self.fontSizeSpinBox = QSpinBox()
        self.fontSizeSpinBox.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        editToolBar.addWidget(self.fontSizeSpinBox)

    def _createStatusBar(self):
        self.statusBar = self.statusBar()
        self.statusBar.showMessage("Ready", 3000)

    def _createActions(self):

        new_px = QStyle.StandardPixmap.SP_FileDialogNewFolder
        new_icon = self.style().standardIcon(new_px)
        self.newAction = QAction(QIcon(new_icon), " &new", self) 
        newTip = "Create a New File"
        self.newAction.setStatusTip(newTip)

        open_px = QStyle.StandardPixmap.SP_DialogOpenButton
        open_icon = self.style().standardIcon(open_px)
        self.openAction = QAction(QIcon(open_icon), " &open... ", self)
        openTip = "Open File"
        self.openAction.setStatusTip(openTip)

        save_px = QStyle.StandardPixmap.SP_DialogSaveButton
        save_icon = self.style().standardIcon(save_px)
        self.saveAction = QAction(QIcon(save_icon), " &save", self)
        saveTip = "Save File"
        self.saveAction.setStatusTip(saveTip)

        exit_px = QStyle.StandardPixmap.SP_DialogCloseButton
        exit_icon = self.style().standardIcon(exit_px)
        self.exitAction = QAction(QIcon(exit_icon), " &exit", self)
        exitTip = "Exit"
        self.exitAction.setStatusTip(exitTip)

        self.newAction.setShortcut("Ctrl+N")
        self.openAction.setShortcut("Ctrl+O")
        self.saveAction.setShortcut("Ctrl+S")
        self.exitAction.setShortcut("Ctrl+Q")

        self.copyAction = QAction(" &copy", self)
        self.pasteAction = QAction(" &paste", self)
        self.cutAction = QAction(" &c&ut", self)

        self.copyAction.setShortcut(QKeySequence.StandardKey.Copy)
        self.pasteAction.setShortcut(QKeySequence.StandardKey.Paste)
        self.cutAction.setShortcut(QKeySequence.StandardKey.Cut)


        help_px = QStyle.StandardPixmap.SP_MessageBoxQuestion
        help_icon = self.style().standardIcon(help_px)
        self.helpContentAction = QAction(QIcon(help_icon), " &help content", self)

        about_px = QStyle.StandardPixmap.SP_MessageBoxInformation
        about_icon = self.style().standardIcon(about_px)
        self.aboutAction = QAction(QIcon(about_icon), " &about", self)

    def contextMenuEvent(self, event) :
        self.menubar = QMenu(self.centralWidget)

        self.menubar.addAction(self.newAction)
        self.menubar.addAction(self.openAction)
        self.menubar.addAction(self.saveAction)

        seperator = QAction(self)
        seperator.setSeparator(True)
        self.menubar.addAction(seperator)

        self.menubar.addAction(self.copyAction)
        self.menubar.addAction(self.pasteAction)
        self.menubar.addAction(self.cutAction)

        self.menubar.exec(event.globalPos())


    def newFile(self):
        self.centralWidget.setText("<b>File >  New</b> clicked.")

    def openFile(self):
        self.centralWidget.setText("<b>File >  Open</b> clicked.")

    def saveFile(self):
        self.centralWidget.setText("<b>File >  Save</b> clicked.")
    
    def copyContent(self):
        self.centralWidget.setText("<b>Edit > Copy</b> clicked.")

    def pasteContent(self):
        self.centralWidget.setText("<b>Edit > Paste</b> clicked.")

    def cutContent(self):
        self.centralWidget.setText("<b>Edit > Cut</b> clicked.")

    def helpContent(self):
        self.centralWidget.setText("<b>Help > Help Content</b> clicked.")

    def about(self):
        self.centralWidget.setText("<b>Help > About</b> clicked.")
    
    def openRecentFile(self, filenName):
        self.centralWidget.setText(f"<b>{filenName}</b> opened.")

    def _connectActions(self):
        self.newAction.triggered.connect(self.newFile)
        self.openAction.triggered.connect(self.openFile)
        self.saveAction.triggered.connect(self.saveFile)
        self.copyAction.triggered.connect(self.copyContent)
        self.pasteAction.triggered.connect(self.pasteContent)
        self.cutAction.triggered.connect(self.cutContent)
        self.helpContentAction.triggered.connect(self.helpContent)
        self.aboutAction.triggered.connect(self.about)
        self.exitAction.triggered.connect(self.close )
        self.openRecentMenu.aboutToShow.connect(self.populateOpenRecent)

    def populateOpenRecent(self):
        
        self.openRecentMenu.clear()
        actions = []
        fileNames = [f"File-{n}" for n in range(5)]
        for fileName in fileNames:
            action = QAction(fileName, self)
            action.triggered.connect(partial(self.openRecentFile, fileName))
            actions.append(action)

        self.openRecentMenu.addActions(actions)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = Window()
    win.show()

    sys.exit(app.exec())

