# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
import StanfordDependencies
from nltk import Tree
from nltk.draw.util import CanvasFrame
from nltk.draw import TreeWidget
import nltk, sys, os
from nltk.tree import Tree
from nltk.parse import stanford

java_path = "/usr/lib/jvm/java-8-oracle" 
os.environ['JAVAHOME'] = java_path

os.environ['STANFORD_PARSER'] = '/home/sumit/stanford-parser-full-2015-04-20/stanford-parser.jar'
os.environ['STANFORD_MODELS'] = '/home/sumit/stanford-parser-full-2015-04-20/stanford-parser-3.5.2-models.jar'

parser = stanford.StanfordParser(model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz") 
prohibitedList=['(-RRB- -RRB-)', '(, ,)', '(. .)', '(-LRB- -LRB-)']


def tree_maker(line):

	
	tmp_lst=[] 
	tmp=line.rstrip("\n")		
	tmp_lst.append(tmp)		
	lst_tree = parser.raw_parse(tmp)	
	tree=Tree("", lst_tree)
	tmp=str(tree) 
	string_tree=tmp 
	tmp=tmp[1:-1] 
	tmp=tmp.strip()
	tree=Tree.fromstring(tmp)
	return string_tree
	

def analyser():
	sd = StanfordDependencies.get_instance(backend='subprocess')
	sent=sd.convert_tree(tree_maker('Hari was a great dancer.'))
	for token in sent:
		print (token)


class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.exitbutt = QtWidgets.QPushButton(Dialog)
        self.exitbutt.setGeometry(QtCore.QRect(290, 250, 98, 27))
        self.exitbutt.setObjectName("exitbutt")
        #QObject.connect(QtCore.QCoreApplication.instance().quit)
        self.exitbutt.clicked.connect(QtCore.QCoreApplication.instance().quit)

        self.analyse = QtWidgets.QPushButton(Dialog)
        self.analyse.setGeometry(QtCore.QRect(170, 250, 98, 27))
        self.analyse.setObjectName("analyse")

        self.InputTaker = QtWidgets.QTextEdit(Dialog)
        self.InputTaker.setGeometry(QtCore.QRect(10, 30, 381, 51))
        self.InputTaker.setObjectName("InputTaker")

        self.senLabel = QtWidgets.QLabel(Dialog)
        self.senLabel.setGeometry(QtCore.QRect(10, 10, 241, 17))
        self.senLabel.setObjectName("senLabel")
        self.tupList = QtWidgets.QLabel(Dialog)
        self.tupList.setGeometry(QtCore.QRect(10, 90, 271, 17))
        self.tupList.setObjectName("tupList")
        self.disp = QtWidgets.QTextBrowser(Dialog)
        self.disp.setGeometry(QtCore.QRect(10, 110, 381, 121))
        self.disp.setObjectName("disp")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Co-reference Resolution System"))
        self.exitbutt.setText(_translate("Dialog", "Exit"))
        self.analyse.setText(_translate("Dialog", "Analyse"))
        self.senLabel.setText(_translate("Dialog", "Enter the sentence here:"))
        self.tupList.setText(_translate("Dialog", "Co-referenced Tuples List:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

