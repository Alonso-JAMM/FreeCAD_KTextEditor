import os
import FreeCADGui as gui
from KEditorView import KEditorView


class keditor_workbench(gui.Workbench):
    """
    class which gets initiated at starup of the gui
    """

    MenuText = "KEditor"
    ToolTip = "Embedded KTextEditor in FreeCAD"
    toolbox = []

    def GetClassName(self):
        return "Gui::PythonWorkbench"

    def Initialize(self):
        """
        This function is called at the first activation of the workbench.
        here is the place to import all the commands
        """
        pass

    def Activated(self):
        '''
        code which should be computed when a user switch to this workbench
        '''
        pass

    def Deactivated(self):
        '''
        code which should be computed when this workbench is deactivated
        '''
        pass


gui.addWorkbench(keditor_workbench())
