import columnSectCheck_UI as csc
from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import comtypes.client

class ColumnSectionCheck(QtWidgets.QMainWindow):
    def __init__(self):
        super(ColumnSectionCheck, self).__init__()
        self.ui = csc.Ui_Form()
        self.ui.setupUi(self)

        self.ETABSObject = comtypes.client.GetActiveObject("CSI.ETABS.API.ETABSObject")
        self.SapModel = self.ETABSObject.SapModel
        self.ui.label_2.setPixmap(QtGui.QPixmap("columnsection.PNG"))
        self.ui.control_button.clicked.connect(self.check_columns)

    def check_columns(self):
        self.SapModel.SetModelIsLocked(False)
        self.SapModel.Analyze.RunAnalysis()

        self.column_numbers = int(self.ui.column_number.text())
        for i in range(1, self.column_numbers+1):
            self.ret1 = self.SapModel.Results.Setup.DeselectAllCasesAndCombosForOutput()
            self.ret2 = self.SapModel.Results.Setup.SetComboSelectedForOutput("1.4g+1.6q")
            self.ObjectElm = 0
            self.NumberResults = 0
            self.Obj = []
            self.ObjSta = []
            self.Elm = []
            self.ElmSta = []
            self.LoadCase = []
            self.StepType = []
            self.StepNum = []
            self.P = []
            self.V2 = []
            self.V3 = []
            self.T = []
            self.M2 = []
            self.M3 = []
            self.ret = self.SapModel.Results.FrameForce(f"{i}", self.ObjectElm, self.NumberResults, self.Obj, self.ObjSta, self.Elm, self.ElmSta, self.LoadCase,
                                              self.StepType, self.StepNum, self.P, self.V2, self.V3, self.T, self.M2, self.M3)
            self.zero_elements = [tuples[0] for tuples in self.ret[1:-1]]
            print("C" + self.zero_elements[0], "-->", abs(self.zero_elements[7] / 1000), "kN")

            self.ret3 = self.SapModel.PropMaterial.GetOConcrete("C35/45")
            self.fck = self.ret3[0]
            self.fcd = self.fck / 1.5

            self.ret3 = self.SapModel.FrameObj.GetSection(f"{i}")
            self.ret4 = self.SapModel.PropFrame.GetRectangle(f"{self.ret3[0]}")
            self.section_area = self.ret4[2] * self.ret4[3]
            self.capacity_load = (0.9 * self.fcd * self.section_area) / 1000
            print(self.capacity_load)
            self.result_text_capacity = f"{self.capacity_load}"
            self.ui.capacity_list.addItem(self.result_text_capacity)
            if abs(self.zero_elements[7] / 1000) <= self.capacity_load:
                print("Kesit Yeterli")
                self.result_text_check = "Kesit Yeterli"
                self.ui.check_list.addItem(self.result_text_check)
            else:
                print("Kesit Yetersiz")
                self.result_text_check = "Kesit Yetersiz"
                self.ui.check_list.addItem(self.result_text_check)

            # ListWidget add item start
            self.result_text_name = f"C{i}"
            self.ui.columns_name_list.addItem(self.result_text_name)
            self.result_text_loads = f"{round(abs(self.zero_elements[7] / 1000),3)}"
            self.ui.axial_load_list.addItem(self.result_text_loads)
            # ListWidget add item end


def app():
    app = QtWidgets.QApplication(sys.argv)
    window = ColumnSectionCheck()
    window.show()
    sys.exit(app.exec_())

app()
