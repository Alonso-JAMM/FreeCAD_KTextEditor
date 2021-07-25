import os
import FreeCAD
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


class OpenMacro:
    def __init__(self):
        pass

    def IsActive(self):
        return True

    def Activated(Self):
        parameter = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Macro")
        macroDir = parameter.GetString("MacroPath")
        fileDialog = QFileDialog()
        fileDialog.setDirectory(macroDir)
        (fileUrl, selFilter) = fileDialog.getOpenFileUrl(
            None,
            "Open a File")
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
        return {'Pixmap': os.path.join(getIconDir(), "MacroEditor.svg"),
                'MenuText': "Open Macro",
                'ToolTip': "Open a Macro File"
                }


class ConfigDialog:
    def __init__(self):
        pass

    def IsActive(self):
        return True

    def Activated(self):
        mw = getMainWindow()
        editorView = KEditorView()
        editorView.confidDialog(mw)

    def GetResources(self):
        return {'Pixmap': os.path.join(getIconDir(), "Preferences-general.svg"),
                'MenuText': "Configure",
                'ToolTip': "Configure KTextEditor"
                }
