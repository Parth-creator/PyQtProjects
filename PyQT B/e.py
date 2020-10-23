import smtplib
import random

def sendEmail(to, content):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.login('parthsinghrajput12@gmail.com', 'Ironman@2006')
	server.sendmail('parthsinghrajput12@gmail.com', to, content)

	server.close()
	print('Email has been sent')

def get_random():
	global a
	n = random.randint(1000, 9999)

	for i in range(1000, 9999):
		if i == n:
			a = i
	return a


l1 = []
l1.append(get_random())

sendEmail('parthsinghrajput12@gmail.com', 'You OTP ' + str(l1[0]))


while True:
	inpu = input('Enter OTP: ')
	try:
		if int(inpu) == l1[0]:
			print('Valid OTP')
			pass

		else:
			print('Invalid OTP')
			pass
	except:
		print('Invalid OTP')
		pass






