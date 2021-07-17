# Overview
This project uses shiboken2 to create python bindings of a QWidget containing
KTextEditor. The python bindings then can be packaged into a python package,
installed, and then loaded by FreeCAD.

# How to install
The python bindings and the python package can be build and installed by using
the setup file:

```
python setup.py install --user

```

The whole build system is really rough and may not work but it is a good initial
guess of how to create python bindings that can be loaded by FreeCAD.


# How to embed KTextEditor in FreeCAD
After installing the python package created above, then loading it in FreeCAD is
simple by using the following code:

```python
from PySide import QtGui
from Editor.KEditor import KEditorView


def getMainWindow():
    toplevel = QtGui.QApplication.topLevelWidgets()
    for i in toplevel:
        if i.metaObject().className() == "Gui::MainWindow":
            return i
    raise Exception("No main window found")


mw = getMainWindow()

mdi=mw.findChild(QtGui.QMdiArea)
sub=mdi.addSubWindow(KEditorView())
sub.show()
mw.update()
```

Then, it should create a new window with KTextEditor.

![](Resources/Embedded_KTextEditor.png)

# Limitations
Most of the code here is to build the python bindings and the python package so the
resulting editor doesn't have that many features.

1. Can't open and edit python/macro files yet. FreeCAD doesn't know about the
embedded editor and instead it uses the built-in editor to open and edit python/macro
files. So the embedded editor is not that useful yet.
2. The embedded editor is a bare bones KTextEditor which doesn't contain some neat
features like a python lsp client. Hopefully it could be added later.
