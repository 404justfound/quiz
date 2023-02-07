from tkinter import *
import customtkinter

class Question1:
	def __init__(self, window):
		self.Frame = customtkinter.CTkFrame(
			master = window,
			)
		self.Frame.grid(row = 1, column = 0)
		self.questions = 'What is the full form of GUI?'

		self.question = customtkinter.CTkLabel(
			master = self.Frame,
			height = 40,
			width = 900,
			text = self.questions
			)

	def Answers(self, text, command, row, column):
		self.text = text
		self.row = row
		self.column = column
		self.command = command

		self.Btn = customtkinter.CTkButton(
			master = self.Frame,
			text = self.text,
			height = 40,
			width = 900,
			command = self.command
			)
		self.Btn.grid(row = self.row, column = self.column, pady = 2)


class Question2:
	def __init__(self, window):
		self.Frame = customtkinter.CTkFrame(
			master = window,
			)
		self.Frame.grid(row = 2, column = 0, pady = 2)
		self.questions = 'What is Binary Language?'

		self.question = customtkinter.CTkLabel(
			master = self.Frame,
			height = 40,
			width = 900,
			text = self.questions
			)

	def Answers(self, text, command, row, column):
		self.text = text
		self.row = row
		self.column = column
		self.command = command

		self.Btn = customtkinter.CTkButton(
			master = self.Frame,
			text = self.text,
			height = 40,
			width = 900,
			command = self.command
			)
		self.Btn.grid(row = self.row, column = self.column, pady = 2)