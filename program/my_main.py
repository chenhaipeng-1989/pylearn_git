from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys
from PyQt5 import QtCore
from uiDemo1 import Ui_MainWindow


class MyMainUi(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainUi, self).__init__(parent)
        self.setupUi(self)
        self.treeWidget.itemClicked.connect(self.click_treeWidget)  # 点击 treeWidget 触发

    def click_pushButton_2(self):  # 点击 pushButton_2 触发
        self.textEdit_2.setText("click_pushButton_2")
        return

    def trigger_actHelp(self):  # 动作 actHelp 触发
        QMessageBox.about(self, "About", """数字图像处理工具箱 v1.0\nCopyright YouCans, XUPT 2021""")
        return

    def click_treeWidget(self, item, column):  # 点击 treeWidget 触发
        # item = self.treeWidget.currentItem()
        print('key = {}\tvalue = {}'.format(item.text(0), item.text(1)))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainUi()
    myWin.show()
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



