import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import smtplib
import random

class Window(QMainWindow):
	"""docstring for Window"""
	def __init__(self):
		super (Window, self).__init__()
		self.setGeometry(200, 200, 300, 300)
		self.setWindowTitle("OTP Sender")
		self.initUI()
		self.setStyleSheet("""QMainWindow{
					background-color:rgb(37, 38, 48)
			}""")
		self.l1 = []
		self.l1.append(self.get_random())

		

	def sendEmail(self, to, content):
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.ehlo()
		server.starttls()
		server.login('parthsinghrajput12@gmail.com', 'Ironman@2006')
		server.sendmail('parthsinghrajput12@gmail.com', to, content)

		server.close()
		print('Email has been sent')

	def get_random(self):
		global a
		n = random.randint(1000, 9999)

		for i in range(1000, 9999):
			if i == n:
				a = i
		return a


	

	def initUI(self):
		self.input = QtWidgets.QLineEdit(self)
		self.input.setPlaceholderText('Email ID')
		self.input.setGeometry(50, 50,  200, 35)
		self.input.setStyleSheet("""QLineEdit{
					border: 2px solid rgb(97, 97, 97);
					color: rgb(97, 97, 97);
					background-color:rgb(37, 38, 48);
					border-radius:10px;
			}

			QLineEdit:hover{
							border-color:rgb(119, 0, 255)
							
							}
			QLineEdit:focus{
							border-color:rgb(119, 0, 255)
							
							}
			""")


		self.btn2 = QtWidgets.QPushButton(self)
		self.btn2.setText('Send')
		self.btn2.setGeometry(100, 100, 100, 30)
		self.btn2.setStyleSheet("""	QPushButton{
							background-color:rgb(119, 0, 255);
							border: 2px solid rgb(97, 97, 97);
							color: rgb(97, 97, 97);
							border-radius:10px;
			}

			QPushButton:hover{border-color:rgb(119, 0, 255);}
			""")
		self.btn2.clicked.connect(self.send)

		self.input2 = QtWidgets.QLineEdit(self)
		self.input2.setPlaceholderText('OTP')
		self.input2.setGeometry(50, 150,  200, 35)
		self.input2.setStyleSheet("""QLineEdit{
					border: 2px solid rgb(97, 97, 97);
					color: rgb(97, 97, 97);
					background-color:rgb(37, 38, 48);
					border-radius:10px;
			}

			QLineEdit:hover{
							border-color:rgb(119, 0, 255)
							
							}

			QLineEdit:focus{
							border-color:rgb(119, 0, 255)
							
							}

			""")




		self.btn = QtWidgets.QPushButton(self)
		self.btn.setText('Next')
		self.btn.setGeometry(100, 230, 100, 30)
		self.btn.setStyleSheet("""	QPushButton{
							background-color:rgb(119, 0, 255);
							border: 2px solid rgb(97, 97, 97);
							color: rgb(97, 97, 97);
							border-radius:10px;
			}

			QPushButton:hover{border-color:rgb(119, 0, 255);}
			""")
		self.btn.clicked.connect(self.check)

		self.label = QtWidgets.QLabel(self)
		self.label.move(120, 200)
		self.label.setStyleSheet("color:rgb(97, 97, 97)")
		self.label.setText('')

	def send(self):
		self.sendEmail(self.input.text(), 'Your OTP is ' + str(self.l1[0]))
	
	def check(self):
		try:
			if int(self.input2.text()) == self.l1[0]:
				self.label.setText("Valid OTP")
			else:
				self.label.setText('InValid OTP')

		except Exception as e:
			self.label.setText('InValid OTP')

def window():
	app = QApplication(sys.argv)
	win = Window()
	win.show()
	sys.exit(app.exec_())


window()
		

