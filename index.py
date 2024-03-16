
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from os import path
from PyQt5.uic import  loadUiType  # here  import libarary  for incloud design file
import urllib.request
#------------------------------------------------------------------
FROM_CLASS,_ = loadUiType(path.join(path.dirname(__file__),"main.ui"))  # here inclouad file
#------------------------------------------------------------------
class Mainapp(FROM_CLASS,QMainWindow ):
    def __init__(self,parent=None):
        super(Mainapp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_Ui()
        self.Handel_Buttons()

    def Handel_Ui(self):
        self.setFixedSize(589,286)
        self.setWindowTitle('PyDownloader')
        self.setWindowIcon(QIcon('icon.png'))


    def Handel_Buttons(self):
        self.pushButton_2.clicked.connect(self.Downlad)
        self.pushButton.clicked.connect(self.Handel_Browse)

    def Handel_Browse(self):
        file_name = self.lineEdit.text()
        spil = file_name.split("/")
        name = spil[-1].replace("%20"," ")

        save_place = QFileDialog.getSaveFileName(self,caption="Save As" ,directory=f"./{name}",filter="All Files (*.*)")

        self.lineEdit_2.setText(save_place[0])
        # print(type(save_place[0]))


    def Handel_Progress(self,blocknum, blocksize, totalsize):

        read = blocknum * blocksize

        if totalsize > 0 :
            percent = read * 100 / totalsize
            self.progressBar.setValue(int(percent))
            QApplication.processEvents()

    def Downlad(self):
        # url   - save location - progress
        url = self.lineEdit.text()
        save_location = self.lineEdit_2.text()
        try:
            urllib.request.urlretrieve(url, save_location, self.Handel_Progress)
        except Exception:
            QMessageBox.warning(self, "Download Error ", "The Download Faild !")
            return

        QMessageBox.information(self,"Download Compleate " , "The Download Finshed")
        self.progressBar.setValue(0)
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
# -----------------------------------------------------------
def main():
    app = QApplication(sys.argv)
    window = Mainapp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()


