import os
from KEditorView import KEditorView
from .features import getMainWindow, getIconDir, getFileTypeIcon
from PySide import QtGui
from PySide2.QtWidgets import QFileDialog


class OpenFile:
    def __init__(self):
        pass

    def IsActive(self):
        return True

    def Activated(self):
        # Open a file using KTextEditor
        (fileUrl, selFilter) = QFileDialog.getOpenFileUrl(None, "Open a File")
        editorView = KEditorView()
        editorView.openUrl(fileUrl)
        mw = getMainWindow()
        mdi = mw.findChild(QtGui.QMdiArea)
        sub = mdi.addSubWindow(editorView)
        sub.setWindowTitle(fileUrl.fileName())
        sub_icon = getFileTypeIcon(fileUrl.fileName())
        sub.setWindowIcon(sub_icon)
        sub.show()
        mw.update()

    def GetResources(self):
        return {'Pixmap': os.path.join(getIconDir(), "Document-open.svg"),
                'MenuText': "Open File",
                'ToolTip': "Open a File "
                }
