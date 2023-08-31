import sys
import time
from pyorbital.orbital import Orbital, tlefile
from datetime import datetime
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class App(QWidget):
	def __init__(self):
		super().__init__()
		
		#Utworzenie zmiennych używanych w aplikacji:
		self.title = "Satelity meteorologiczne"
		self.width = 1910
		self.height = 900
		self.longitude = 0
		self.longitude1 = 0
		self.longitude2 = 0
		self.longitude3 = 0
		self.latitude = 0
		self.latitude1 = 0
		self.latitude2 = 0
		self.latitude3 = 0
		self.altitude = 0
		self.altitude1 = 0
		self.altitude2 = 0
		self.altitude3 = 0
		self.position = 0
		self.velocity = 0

		#Wywołanie funkcji:
		self.interfejs()
	
	def interfejs(self):

		#Ustawienie tytułu, położenia oraz wielości aplikacji:
		self.setWindowTitle(self.title)
		self.setGeometry(0, 0, self.width, self.height)

		#Dodanie pól wyboru satelitów do wyświetlenia:
		self.checkbox1 = QCheckBox('NOAA 15 (kolor czerwony)', self)
		self.checkbox2 = QCheckBox('NOAA 18 (kolor zielony)', self)
		self.checkbox3 = QCheckBox('NOAA 19 (kolor żółty)', self)		

		#Dodanie rozwijanej listy satelitów:
		combo = QComboBox(self)
		combo.addItem('NOAA 15')
		combo.addItem('NOAA 18')
		combo.addItem('NOAA 19')

		#Dodanie przycisków:
		button = QPushButton('Wyświetl', self)
		button1 = QPushButton('Zaktualizuj pliki TLE', self)
		
		#Utworzenie tabel z opisem oraz pustych do wypełnienia:
		#informacjami o satelitach
		wybor = QLabel("Wybór satelity:", self)
		info = QLabel("Informacje:", self)
		name = QLabel("Satelita: " , self)
		self.noaa = QLabel(self)
		wys = QLabel("Wysokość [km]: ", self)
		self.alti = QLabel(self)
		dlug = QLabel("Długość: ", self)
		self.long = QLabel(self)
		szer = QLabel("Szerokość: ", self)
		self.lati = QLabel(self)
		numer = QLabel("Numer orbity: ", self)
		self.orbnum = QLabel(self)
		azymut = QLabel("Azymut: ",self)
		self.azy = QLabel(self)
		elewacja = QLabel("Elewacja: ", self)
		self.elew = QLabel(self)
		self.tle = QLabel(self)

		#Ustawienie wywołania funkcji po zdarzeniu:
		combo.activated[str].connect(self.onChanged)
		button.clicked.connect(self.on_click)
		button1.clicked.connect(self.update_tle)
		
		#Ustawienie czcionek oraz położenia elementów:
		wybor.setFont(QFont('TimesNewRoman', 14))
		wybor.move(1620, 20)
		self.checkbox1.setFont(QFont('TimesNewRoman', 10))
		self.checkbox1.move(1620, 60)
		self.checkbox2.setFont(QFont('TimesNewRoman', 10))
		self.checkbox2.move(1620, 80)
		self.checkbox3.setFont(QFont('TimesNewRoman', 10))
		self.checkbox3.move(1620, 100)
		button.move(1620,130)
		info.setFont(QFont('TimesNewRoman', 14))
		info.move(1620, 180)
		combo.setFont(QFont('TimesNewRoman', 10))
		combo.move(1620, 210)
		name.setFont(QFont('TimesNewRoman', 10))
		name.move(1610, 250)
		self.noaa.setFont(QFont('TimesNewRoman', 10))
		self.noaa.move(1750, 250)
		wys.setFont(QFont('TimesNewRoman', 10))
		wys.move(1610, 280)
		self.alti.setFont(QFont('TimesNewRoman', 10))
		self.alti.move(1750,280)
		dlug.setFont(QFont('TimesNewRoman', 10))
		dlug.move(1610, 310)
		self.long.setFont(QFont('TimesNewRoman', 10))
		self.long.move(1750, 310)
		szer.setFont(QFont('TimesNewRoman', 10))
		szer.move(1610, 340)
		self.lati.setFont(QFont('TimesNewRoman', 10))
		self.lati.move(1750,340)
		numer.setFont(QFont('TimesNewRoman', 10))
		numer.move(1610,370)
		self.orbnum.setFont(QFont('TimesNewRoman', 10))
		self.orbnum.move(1750,370)
		azymut.setFont(QFont('TimesNewRoman', 10))
		azymut.move(1610,400)
		self.azy.setFont(QFont('TimesNewRoman', 10))
		self.azy.move(1750,400)
		elewacja.setFont(QFont('TimesNewRoman', 10))
		elewacja.move(1610,430)
		self.elew.setFont(QFont('TimesNewRoman', 10))
		self.elew.move(1750,430)
		button1.move(1620, 700)
		self.tle.setFont(QFont('TimesNewRoman', 10))
		self.tle.move(1620, 730)

		#Ułożenie elementów w siatce:
		widok = QGridLayout()


	def onChanged(self, text):

		#Ustawienie wyświetlanej nazwy satelity:
		self.noaa.setText(text)
		self.noaa.adjustSize()

		#Wyznaczenie aktualnego czasu:
		now = datetime.utcnow()

		#Wczytanie danych o wybranym satelicie:
		orb=Orbital(text,tle_file='/Users/Alicja/Desktop/tlefile.txt')

		# Uzyskanie długości, szerokości i wysokości satelity:
		self.longitude, self.latitude, self.altitude = orb.get_lonlatalt(now)

		#Uzyskanie numeru orbity
		self.orbnumber = orb.get_orbit_number(now)

		#Położenie miasta Poznań:
		self.x = 52.4082663
		self.y = 16.9335199
		self.h = 0.069

		#Uzyskanie azytmutu i elewacji względem miasta Poznań
		self.azimuth, self.elevation = orb.get_observer_look(now,self.y,self.x,self.h)
		
		#Ustawienie wyświetlania wczytanych danych:
		self.alti.setText(str(round(self.altitude,6)))
		self.lati.setText(str(round(self.latitude,6)))
		self.long.setText(str(round(self.longitude,6)))
		self.orbnum.setText(str(self.orbnumber))
		self.azy.setText(str(round(self.azimuth,6)))
		self.elew.setText(str(round(self.elevation,6)))

		#Ustawienie wielkości tabeli do wielkości elementu:
		self.alti.adjustSize()
		self.lati.adjustSize()
		self.long.adjustSize()
		self.orbnum.adjustSize()
		self.azy.adjustSize()
		self.elew.adjustSize()

		#Aktualizacja interfejsu:
		self.update()

	def on_click(self):

		#Pobranie aktualnego czasu
		now = datetime.utcnow()

		#Ustawienie wyświetlania zaznaczonych satelitów:
		if self.checkbox1.isChecked() == True:
			orb1=Orbital('NOAA 15', tle_file='/Users/Alicja/Desktop/tlefile.txt')
			self.longitude1, self.latitude1, self.altitude1 = orb1.get_lonlatalt(now)
		if self.checkbox2.isChecked() == True:
			orb2=Orbital('NOAA 18', tle_file='/Users/Alicja/Desktop/tlefile.txt')
			self.longitude2, self.latitude2, self.altitude2 = orb2.get_lonlatalt(now)
		if self.checkbox3.isChecked() == True:
			orb3=Orbital('NOAA 19', tle_file='/Users/Alicja/Desktop/tlefile.txt')
			self.longitude3, self.latitude3, self.altitude3 = orb3.get_lonlatalt(now)

	def update_tle(self):
		
		#Próba aktualizacji plików TLE
		try:
			tlefile.fetch('/Users/Alicja/Desktop/tlefile.txt')
			self.tle.setText('Plik TLE zaktualizowany')
			self.tle.adjustSize()
		except:
			self.tle.setText('Nie udało się pobrać plików TLE')
			self.tle.adjustSize()
		
	def paintEvent(self, event):

		#Ustawienie obrazu, na którym rysowane jest położenie satelity
		pixmap = QPixmap('map.png')
		painter = QPainter(self)
		painter.drawPixmap(0,0,1600,900, pixmap)

		#Rysowanie położenia wybranych satelitów:
		if self.checkbox1.isChecked() == True:
			pen1 = QPen(Qt.red, 10)
			painter.setPen(pen1)
			if(self.longitude1 != 0 and self.latitude1 != 0):
				painter.drawEllipse(780 + int(self.longitude1*4.27),
									440 - int(self.latitude1*4.67),10,10)
			
		if self.checkbox2.isChecked() == True:
			pen2 = QPen(Qt.green, 10)
			painter.setPen(pen2)
			if(self.longitude2 != 0 and self.latitude2 != 0):
				painter.drawEllipse(780 + int(self.longitude2*4.27),
									440 - int(self.latitude2*4.67),10,10)
			
		if self.checkbox3.isChecked() == True:
			pen3 = QPen(Qt.yellow, 10)
			painter.setPen(pen3)
			if(self.longitude3 != 0 and self.latitude3 != 0):
				painter.drawEllipse(780 + int(self.longitude3*4.27),
									440 - int(self.latitude3*4.67),10,10)
			
		self.update()


if __name__ == '__main__':

	#Uruchomienie aplikacji
	app = QApplication(sys.argv)
	okno = App()
	okno.show()
	sys.exit(app.exec_())
