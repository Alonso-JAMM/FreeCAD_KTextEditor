import os
from PySide import QtGui


def getMainWindow():
    """Returns the FreeCAD main window"""
    toplevel = QtGui.QApplication.topLevelWidgets()
    for i in toplevel:
        if i.metaObject().className() == "Gui::MainWindow":
            return i

    raise Exception("No main window found")


def getIconDir():
    """Returns the directory of the icon folder"""
    return os.path.join(os.path.dirname(__file__), "resources")


def getFileTypeIcon(fileName):
    """Returns an icon representing the type of the given filename. This
    function uses the extension of the filename in order to determine the type
    """
    extension = fileName.rsplit(".", 1)[1]
    pythonExtentions = ["py", "fcmacro"]
    if extension.lower() in pythonExtentions:
        return QtGui.QIcon(os.path.join(getIconDir(), "Applications-python.svg"))
    else:
        return QtGui.QIcon(os.path.join(getIconDir(), "TextDocument.svg"))
