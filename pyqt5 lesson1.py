import sys, os, time, uuid, hashlib, re
from PyQt5 import QtCore, QtGui, uic  
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QComboBox, QTextEdit 

winMain = uic.loadUiType("homeScreen.ui") [0]
win2 = uic.loadUiType("InfoOutput.ui") [0]

class HomeScreen(QtWidgets.QMainWindow, winMain): #imports the PyQT 'main window' functionality, winMain links to UI screens above

	def __init__(self, parent = None):
		QtWidgets.QMainWindow.__init__(self,parent) ##setting the screen up, defining where the buttons are linking to, and where text box information is being stored 
		self.setupUi(self)
		self.submitBtn.clicked.connect(self.submitInput)
		self.clearBtn.clicked.connect(self.clearForm)


	def submitInput(self):
		self.nameText = self.nameTxt.text()
		self.ageText = self.ageTxt.text()
		user1.name = self.nameText
		user1.age = self.ageText
		QtWidgets.QMessageBox.information(self,"Success", "Name and age recorded", QMessageBox.Yes)

		self.hide()
		self.newWindow = InfoOut()
		self.newWindow.show()


	def clearForm(self):
		user1.name = " "
		user1.age = " "
		self.nameTxt.clear()
		self.ageTxt.clear()

class InfoOut(QtWidgets.QMainWindow, win2): #imports the PyQT 'main window' functionality, winMain links to UI screens above

	def __init__(self, parent = None):
		QtWidgets.QMainWindow.__init__(self,parent) ##setting the screen up, defining where the buttons are linking to, and where text box information is being stored 
		self.setupUi(self)
		self.backBtn.clicked.connect(self.back)

		self.name = "Your name is: " + user1.name
		self.age = "Your age is: " + user1.age

		self.namelabel = self.nameLbl.setText(self.name)
		self.agelabel = self.ageLbl.setText(self.age)

		self.setImage()


	def setImage(self):

		pokeImages = ['evee.jpg', 'bulbasaur.png', 'mrMime.jpg', 'charmander.png', 'pika.jpg']
		num = random.randint(0, len(pokeImages)-1)
		self.imageLbl.setPixmap(QtGui.QPixmap("%s" %pokeImages[num]))


	def back(self):
		self.hide()
		self.newWindow = HomeScreen()
		self.newWindow.show()		

class User():
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def getDetails(self):
		pass
		#print (self.name, self.age)


user1 = User(" ", " ") #creates a customer object with no name or age 

app = QtWidgets.QApplication(sys.argv) #think of this as the 'main ()' section in procedural programming. Allows you to call the program into action 
winMain = HomeScreen()
winOut = InfoOut()

winMain.show()
app.exec_()
