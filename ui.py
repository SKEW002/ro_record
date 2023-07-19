import tkinter as tk
from tkinter import ttk
import datetime


class UI:
	def __init__(self):
		self.root = tk.Tk()
		self.window_size = (800, 900) #x,y
		self.root.geometry("800x900")
		self.root.title("RO Competency and Proficiency Tracking System")
		self.root.resizable(False, False)

		self.raw_data = {
			"RO Name":tk.StringVar(),
			"Category":tk.StringVar(),
			"Mentor": tk.StringVar(),
			"Accident":tk.StringVar(),
			"Date": datetime.datetime.now().strftime("%d/%m/%Y"),
			"Start Time":tk.IntVar(),
			"End Time": tk.IntVar(),
			"Duration":0,
			"Move Slowly":tk.BooleanVar(),
			"Path Selection":tk.BooleanVar(),
			"Re-Localization":tk.BooleanVar(),
			"Traffic Light Override":tk.BooleanVar(),
			"Move by Distance":tk.BooleanVar(),
			"Set Destination":tk.BooleanVar(),
			"Remark":tk.StringVar()
		}

		self.x = 0
		self.y = 50

		ttk.Label(self.root, text=self.raw_data["Date"], font=("Times New Roman", 17)).place(x = 400,y = 0)


	def update_data(self):
		try:		
			updated_data = {}
			for key, value in self.raw_data.items():
				if key == "Date":
					updated_data[key] = value

				elif key == "Duration": # save in mins
					updated_data[key] = self.raw_data["End Time"].get() // 100 * 60 - self.raw_data["Start Time"].get() // 100 * 60 + self.raw_data["End Time"].get() % 100 - self.raw_data["Start Time"].get() % 100
				
				else:
					updated_data[key] = value.get()
			print(updated_data)

			return updated_data

		except:
			return


	def drop_down(self, data_list, data_title, x=0, y=0):
		ttk.Label(self.root, text=data_title, font=("Times New Roman", 13)).place(x=x, y = self.y)
		drop = ttk.Combobox(self.root, width = 15, textvariable = self.raw_data[data_title], state="readonly")
		drop['values'] = data_list
		drop.place(x = x+200, y = self.y)
		drop.current()
		self.y += 30

	def text_box(self, data_title):
		if data_title == "Start Time":
			input_guide = "Enter start time (enter in 24hr format eg. time now is "+datetime.datetime.now().strftime ('%H%M')+") "

		elif data_title == "End Time":
			input_guide = "Enter end time (enter in 24hr format eg. time now is "+datetime.datetime.now().strftime ('%H%M')+") "

		elif data_title == "Remark":
			input_guide = "Remark: "

		ttk.Label(self.root, text=input_guide,font=("Times New Roman", 13)).place(x=0, y=self.y)
		self.y += 30
		entry_box = tk.Entry(self.root, textvariable=self.raw_data[data_title])
		entry_box.place(x=0, y=self.y) #width=380, height=100

		self.y += 30

	def check_box(self, data_list):
		ttk.Label(self.root, text ="Select functions that you attempted").place(x = 0,y = self.y)
		self.y += 30

		for i in data_list:
			button = tk.Checkbutton(self.root, text =i,takefocus = 0,variable=self.raw_data[i]).place(x = 0,y = self.y)
			self.y += 30

	def submit_button(self):
		button = tk.Button( self.root , text = "Submit" , command = self.update_data ).place(y=self.y)