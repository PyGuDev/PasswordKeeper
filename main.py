#-*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.properties import ObjectProperty
from kivy.config import Config
from kivy.uix.button import Button




#Config.set('graphics', 'width', '720')
#Config.set('graphics', 'height', '1280')

#root.manager.current = "main"
class LogScreen(Screen):
	pass		

class MainScreen(Screen):
	 pass

class RegistrScreen(Screen):
	pass

class Manager(ScreenManager):
	log_screen = ObjectProperty(None)
	main_screen = ObjectProperty(None)
	registr_screen = ObjectProperty(None)

class ScreensApp(App):

	def pass_r(self,text):
		self.is_suitable = False
		password_file = open("passw.txt", "r")
		if text == '':
			self.is_suitable = False
		else:
			for x in password_file.read().split('\n'):
				if x == text:
					self.is_suitable = True
					self.m.current = "main"
		#if password_file.read().split():
		#	print("yes")
		password_file.close()
		return self.is_suitable

	def add_account(self, name, lastname, passwd):
		account_file = open("account.txt", "a")
		password_file = open("passw.txt", "a")
		account_file.write(name+'\n')
		account_file.write(lastname+'\n')
		account_file.write(passwd+'\n')
		password_file.write(name+'\n')
		password_file.write(passwd+'\n')
		account_file.close()
		password_file.close()
		self.m.current = "log"

	def database_save(instance, text):
		db = open("db.txt", "w")
		db.write(text)
		db.close()

	def database_read(instance):
		db = open("db.txt", "r")
		return db.read()


	def build(self):
		self.m = Manager(transition=WipeTransition())
		return self.m


if __name__ == "__main__":
	ScreensApp().run()