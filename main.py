from tkinter import *
import customtkinter
import pyautogui
from question import *
from otherWid import *

class Win:
	def __init__(self):
		self.WIDTH, self.HEIGHT = pyautogui.size()

		customtkinter.set_appearance_mode("dark")
		customtkinter.set_default_color_theme("dark-blue")

		self.root = customtkinter.CTk()
		self.root.geometry(f"{self.WIDTH}x{self.HEIGHT}")
		self.root.title('Quiz')

		self.clicked1 = False
		self.clicked2 = False

		self.widgets()

	def right_answer1(self):
		if self.clicked1 == False:
			self.question1.question.configure(bg_color = 'green', text = 'Right Answer')
			self.score.current_score += 1
			self.score.show_score.configure(text = self.score.current_score)
			self.clicked1 = True

	def wrong_answer1(self):
		if self.clicked1 == False:
			self.question1.question.configure(bg_color = 'red', text = 'Wrong Answer The Right Answer is option D')
			self.clicked1 = True


	def right_answer2(self):
		if self.clicked2 == False:
			self.question2.question.configure(bg_color = 'green', text = 'Right Answer')
			self.score.current_score += 1
			self.score.show_score.configure(text = self.score.current_score)
			self.clicked2 = True

	def wrong_answer2(self):
		if self.clicked2 == False:
			self.question2.question.configure(bg_color = 'red', text = 'Wrong Answer The Right Answer is option D')
			self.clicked2 = True


	def widgets(self):
		self.MainFrame = customtkinter.CTkFrame(
			master = self.root,
			width = self.WIDTH,
			height = self.HEIGHT,
			)
		self.MainFrame.place(x = 0, y = 0)

		self.question1 = Question1(self.MainFrame)
		self.question1.question.grid(row = 0, column = 0)

		self.question2 = Question2(self.MainFrame)
		self.question2.question.grid(row = 0, column = 0)

		self.score = Widgets(self.MainFrame)
		self.score.score.grid(row = 0, column = 0)
		self.score.show_score.grid(row = 0, column = 1)

		self.ans0_1 = self.question1.Answers('User Experience', self.wrong_answer1, 1, 0)
		self.ans0_2 = self.question1.Answers('Artificial Intelligence',self.wrong_answer1, 2, 0)
		self.ans0_3 = self.question1.Answers('Augmented Reality',self.wrong_answer1, 3, 0,)
		self.ans0_4 = self.question1.Answers('Graphical User Interface',self.right_answer1, 4, 0)


		self.ans1_1 = self.question2.Answers('A human understanding language', self.wrong_answer2, 1, 0)
		self.ans1_2 = self.question2.Answers('A foregin language', self.wrong_answer2, 2, 0)
		self.ans1_3 = self.question2.Answers('A computer understanding language', self.right_answer2, 3, 0,)
		self.ans1_4 = self.question2.Answers('A programming language', self.wrong_answer2, 4, 0)


win = Win()
win.root.mainloop()
