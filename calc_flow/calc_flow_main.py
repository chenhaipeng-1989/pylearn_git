from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QPushButton
from PyQt5.QtCore import Qt
import sys
# from PyQt5 import QtCore
from calcflow import Ui_MainWindow
from D1 import Ui_Dialog


# import traceback


class MyMainUi(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainUi, self).__init__(parent)
        self.setupUi(self)

    def calcVL(self):
        try:
            L = float(self.lineEdit_1.text())
            W = float(self.lineEdit_2.text())
            H = float(self.lineEdit_3.text())
            V = L * W * H
            self.lineEdit_4.setText(str(V / 1000))
        except Exception as e:
            QMessageBox.about(self, "About", "%s \n请输入数字" % e)

    def calcFlow(self):
        try:
            V = float(self.lineEdit_4.text())
            P = float(self.lineEdit_5.text())
            T = float(self.lineEdit_6.text())
            QL = V * P / (101.325 * T)
            self.labe_f1.setNum(QL)
            self.labe_f2.setNum(QL * 60)
        except ZeroDivisionError as e:
            QMessageBox.about(self, "About", "测试时间不能为0")
        except ValueError as e:
            QMessageBox.about(self, "About", "%s \n请输入数字" % e)
        except Exception as e:
            print(e)

    def tanchuangt(self):
        myWin2.show()


class MyMainUi2(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super(MyMainUi2, self).__init__(parent)
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)

    def accept(self):
        self.close()

    def reject(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainUi()
    myWin.show()
    myWin2 = MyMainUi2()
    sys.exit(app.exec_())

'''
import sys
if __name__ == '__main__':
   app = QtWidgets.QApplication(sys.argv)
   MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
   ui = Ui_MainWindow() # 创建PyQt设计的窗体对象
   ui.setupUi(MainWindow) # 调用PyQt窗体的方法对窗体对象进行初始化设置
   MainWindow.show() # 显示窗体
   sys.exit(app.exec_()) # 程序关闭时退出进程

'''
