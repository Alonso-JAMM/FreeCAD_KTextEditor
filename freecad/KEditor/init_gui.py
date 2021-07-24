import os
import FreeCADGui as Gui


class keditor_workbench(Gui.Workbench):
    """
    class which gets initiated at starup of the gui
    """

    MenuText = "KEditor"
    ToolTip = "Embedded KTextEditor in FreeCAD"
    Icon = os.path.join(os.path.dirname(__file__), "resources", "Accessories-text-editor.svg")
    toolbox = [
        "OpenFile",
    ]

    def GetClassName(self):
        return "Gui::PythonWorkbench"

    def Initialize(self):
        """
        This function is called at the first activation of the workbench.
        here is the place to import all the commands
        """
        from .commands import OpenFile

        self.appendToolbar("KEditor", self.toolbox)
        self.appendMenu("KEditor", self.toolbox)

        Gui.addCommand("OpenFile", OpenFile())

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


Gui.addWorkbench(keditor_workbench())
