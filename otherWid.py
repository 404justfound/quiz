from tkinter import *
import customtkinter

class Widgets:
	def __init__(self, window):
		self.window = window
		self.text = 'Score: '
		self.current_score = 0
		
		self.Frame = customtkinter.CTkFrame(
			master = self.window
			)
		self.Frame.grid(row = 0, column = 1)

		self.score = customtkinter.CTkLabel(
			master = self.Frame,
			text = self.text,
		)

		self.show_score = customtkinter.CTkLabel(
			master = self.Frame,
			text = self.current_score,
		)