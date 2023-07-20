import tkinter as tk
from tkinter import ttk
import datetime


class UI:
	def __init__(self):
		self.root = tk.Tk()
		self.window_size = {"x":800, "y":900}
		self.root.geometry("{}x{}".format(self.window_size["x"], self.window_size["y"]))
		self.root.title("RO Competency and Proficiency Tracking System")
		self.root.resizable(False, False)

		self.updated_data = {}
		self.raw_data = {
			"RO Name":tk.StringVar(),
			"Category":tk.StringVar(),
			"Mentor": tk.StringVar(),
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
			"Accident":tk.StringVar(),
			"Remark":tk.StringVar()
		}

		self.x = 0  # initial position
		self.y = 50 # initial position

		ttk.Label(self.root, text=self.raw_data["Date"], font=("Times New Roman", 17)).place(x = self.window_size["x"] // 2, y = 0)


	def update_data(self):
		try:
			for key, value in self.raw_data.items():
				if key == "Date":
					self.updated_data[key] = value

				elif key == "Duration": # save in mins
					end_time_hrs = self.raw_data["End Time"].get() // 100
					start_time_hrs = self.raw_data["Start Time"].get() // 100
					end_time_mins = self.raw_data["End Time"].get() % 100
					start_time_mins = self.raw_data["Start Time"].get() % 100

					if (end_time_hrs > 23 or start_time_hrs > 23) or (end_time_mins > 59 or start_time_mins > 59):
						raise ValueError
					
					else:
						self.updated_data[key] = end_time_hrs * 60 - start_time_hrs * 60 + end_time_mins % 100 - start_time_mins % 100
				
				else:
					self.updated_data[key] = value.get()
			self.alert_exit_program()

		except (tk.TclError, ValueError):
			self.alert_input_err()
			return


	def alert_input_err(self):
		pop_up = tk.Tk()
		pop_up.wm_title("Warning")
		label = ttk.Label(pop_up, text="Please key in the time in correct format", font=("Times New Roman", 13))
		label.pack(side="top", fill="x", pady=10)
		button = ttk.Button(pop_up, text="close", command = pop_up.destroy)
		button.pack()
		pop_up.mainloop()

	def alert_exit_program(self):
		self.exit_pop_up = tk.Tk()
		self.exit_pop_up.wm_title("Exiting")
		label = ttk.Label(self.exit_pop_up, text="Submitted successfully", font=("Times New Roman", 13))
		label.pack(side="top", fill="x", pady=10)
		button = ttk.Button(self.exit_pop_up, text="Ok", command = self.destroy_all_windows)
		button.pack()
		self.exit_pop_up.mainloop()
	
	def destroy_all_windows(self):
		self.exit_pop_up.destroy()
		self.root.destroy()


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
		self.root.mainloop()