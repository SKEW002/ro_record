import datetime
import customtkinter
from tkcalendar import Calendar

class UI:
	def __init__(self, title, width, height):
		customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
		customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
		self.root = customtkinter.CTk()
		self.window_size = {"x":width, "y":height}
		self.root.geometry("{}x{}".format(self.window_size["x"], self.window_size["y"]))
		# self.root.config(bg='#856ff8')
		self.root.title(title)
		self.root.resizable(False, False)

		self.updated_data = {}
		self.raw_data = {
			"RO Name":customtkinter.StringVar(),
			"Category":customtkinter.StringVar(),
			"Mentor": customtkinter.StringVar(),
			"Date": datetime.datetime.now().strftime("%d/%m/%Y"),
			"Start Time": None,
			"End Time": None,
			"Duration":0,
			"Move Slowly":customtkinter.BooleanVar(),
			"Path Selection":customtkinter.BooleanVar(),
			"Re-Localization":customtkinter.BooleanVar(),
			"Traffic Light Override":customtkinter.BooleanVar(),
			"Move by Distance":customtkinter.BooleanVar(),
			"Set Destination":customtkinter.BooleanVar(),
			"Accident":customtkinter.StringVar(),
			"Remark":customtkinter.StringVar(),
			"Day": datetime.datetime.now().strftime("%d")
		}

		self.hrs = [f"{number:02d}" for number in range(0,24)]
		self.mins = [f"{number:02d}" for number in range(0,60,5)]
		self.start_hrs = customtkinter.StringVar()
		self.start_mins = customtkinter.StringVar()
		self.end_hrs = customtkinter.StringVar()
		self.end_mins = customtkinter.StringVar()

		self.x = 30  # initial position
		self.y = 60 # initial position

		customtkinter.CTkLabel(self.root, text=self.raw_data["Date"], font=customtkinter.CTkFont(size=20, weight="bold")).place(x=self.window_size["x"] // 2, y=30, anchor="center")


	def update_data(self):
		try:
			self.raw_data["Start Time"] = self.start_hrs.get() + ":" + self.start_mins.get()
			self.raw_data["End Time"] = self.end_hrs.get() + ":" + self.end_mins.get()

			for key, value in self.raw_data.items():
				if key == "Date" or key == "Start Time" or key == "End Time" or key == "Day":
					self.updated_data[key] = [value]

				elif key == "Duration": # save in mins
					if len(self.raw_data["End Time"]) < 4 or len(self.raw_data["Start Time"]) < 4:
						raise ValueError("Do not leave blank at time input")

					end_time_hrs = int(self.raw_data["End Time"][:2])
					start_time_hrs = int(self.raw_data["Start Time"][:2])
					end_time_mins = int(self.raw_data["End Time"][3:])
					start_time_mins = int(self.raw_data["Start Time"][3:])
					self.updated_data[key] = (end_time_hrs * 60 + end_time_mins) - (start_time_hrs * 60 + start_time_mins)
					if self.updated_data[key] < 0:
						self.updated_data[key] += (24 * 60)
					self.updated_data[key] = [self.updated_data[key]]
					
				elif key == "Accident":
					self.updated_data[key] = [int(1 if value.get() == "Yes" else 0)]

				else:
					self.updated_data[key] = value.get()
					if(type(self.updated_data[key]) == bool):
						self.updated_data[key] = [int(self.updated_data[key])]
	
					else:
						if len(self.updated_data[key]) == 0 and key != "Remark":
							raise ValueError("Empty {}".format(key))

			self.alert_exit_program()

		except (ValueError, TypeError) as error:
			self.alert_input_err(error)
			return
		


	def alert_input_err(self, error):
		pop_up = customtkinter.CTk()
		pop_up.wm_title("Warning")
		label = customtkinter.CTkLabel(pop_up, text=error, font=customtkinter.CTkFont(size=13))
		label.pack(side="top", fill="x", pady=10)
		button = customtkinter.CTkButton(pop_up, text="close", command = pop_up.destroy)
		button.pack()
		pop_up.mainloop()


	def alert_exit_program(self):
		self.exit_pop_up = customtkinter.CTk()
		self.exit_pop_up.wm_title("Exiting")
		label = customtkinter.CTkLabel(self.exit_pop_up, text="Submitted successfully", font=customtkinter.CTkFont(size=13))
		label.pack(side="top", fill="x", pady=10)
		button = customtkinter.CTkButton(self.exit_pop_up, text="Ok", command = self.destroy_all_windows)
		button.pack()
		self.exit_pop_up.mainloop()
	

	def destroy_all_windows(self):
		self.exit_pop_up.destroy()
		self.root.destroy()


	def drop_down(self, data_list, data_title, x=0, y=0): # add date
		if data_title == "Start Time":
			customtkinter.CTkLabel(self.root, text="hrs", font=customtkinter.CTkFont(size=15)).place(x=self.x+230+10, y = self.y)
			customtkinter.CTkLabel(self.root, text="mins", font=customtkinter.CTkFont(size=15)).place(x=self.x+310+10, y = self.y)
			self.y += 30
			customtkinter.CTkLabel(self.root, text=data_title+" (24hr format)", font=customtkinter.CTkFont(size=15)).place(x=self.x, y=self.y)
			drop_start_hrs = customtkinter.CTkComboBox(self.root, width = 70, variable = self.start_hrs, state="readonly", values=self.hrs)
			drop_start_mins = customtkinter.CTkComboBox(self.root, width = 70, variable = self.start_mins, state="readonly",values=self.mins)

			drop_start_hrs.place(x=self.x+230, y=self.y)

			drop_start_mins.place(x=self.x+310, y=self.y)

		elif data_title == "End Time":
			customtkinter.CTkLabel(self.root, text=data_title + " (24hr format)", font=customtkinter.CTkFont(size=15)).place(x=self.x, y=self.y)
			drop_end_hrs = customtkinter.CTkComboBox(self.root, width = 70, variable = self.end_hrs, state="readonly", values=self.hrs)
			drop_end_mins = customtkinter.CTkComboBox(self.root, width = 70, variable = self.end_mins, state="readonly", values=self.mins)

			drop_end_hrs.place(x=self.x+230, y=self.y)

			drop_end_mins.place(x=self.x+310, y=self.y)

		else:
			customtkinter.CTkLabel(self.root, text=data_title, font=customtkinter.CTkFont(size=15)).place(x=self.x, y = self.y)
			drop = customtkinter.CTkComboBox(master=self.root, width = 180, variable = self.raw_data[data_title], values=data_list, state="readonly",hover=True)
			drop.place(x=self.x+100, y=self.y)



	def text_box(self, data_title):
		# if data_title == "Start Time":
		# 	input_guide = "Enter start time (enter in 24hr format eg. time now is "+datetime.datetime.now().strftime ('%H%M')+") "

		# elif data_title == "End Time":
		# 	input_guide = "Enter end time (enter in 24hr format eg. time now is "+datetime.datetime.now().strftime ('%H%M')+") "

		customtkinter.CTkLabel(self.root, text=data_title+": ",font=customtkinter.CTkFont(size=20)).place(x=self.window_size["x"] // 2, y=self.y, anchor="center")
		self.y += 60
		entry_box = customtkinter.CTkEntry(self.root, textvariable=self.raw_data[data_title],width=380, height=70)
		entry_box.place(x=self.window_size["x"] // 2, y=self.y, anchor="center")


	def check_box(self, data_list):
		customtkinter.CTkLabel(self.root, text ="Select functions that you attempted",font=customtkinter.CTkFont(size=18)).place(x=self.x ,y = self.y)
		self.y += 30

		for i in data_list:
			button = customtkinter.CTkCheckBox(self.root, text=i,variable=self.raw_data[i],checkbox_width=18,checkbox_height=18).place(x=self.x,y = self.y)
			self.y += 30


	def submit_button(self):
		button = customtkinter.CTkButton(self.root , text="Submit", command=self.update_data).place(x=self.window_size["x"] // 2, y=self.y, anchor="center")
		self.root.mainloop()



# start date title
	def calendar(self):
		self.y += 50
		self.start_date_title = customtkinter.CTkLabel(self.root, text="Select Start Date", font=customtkinter.CTkFont(size=18))
		self.start_date_title.place(x=self.window_size["x"]//6 * 2, y=self.y, anchor="center")

		self.end_date_title = customtkinter.CTkLabel(self.root, text="Select End Date",font=customtkinter.CTkFont(size=18))
		self.end_date_title.place(x=self.window_size["x"]//6 * 4, y=self.y, anchor="center")

		self.y += 100

		self.start_cal = Calendar(self.root, selectmode='day',showweeknumbers=False, cursor="hand2", date_pattern= 'y-mm-dd',borderwidth=0, bordercolor='white')
		self.start_cal.place(x=self.window_size["x"]//6*2, y=self.y, anchor="center")

		self.end_cal = Calendar(self.root, selectmode='day', showweeknumbers=False, cursor="hand2", date_pattern= 'y-mm-dd', borderwidth=0, bordercolor='white')
		self.end_cal.place(x=self.window_size["x"]//6 * 4, y=self.y, anchor="center")

		self.y += 120
		# # date confirm button
		self.confirm_date = customtkinter.CTkButton(self.root, text="Confirm Dates",  hover=True, command=self.test_cal)
		self.confirm_date.place(x=self.window_size["x"]//2, y=self.y, anchor="center")
		print(self.start_cal.get_date)
		self.proceed_overall_graph = customtkinter.CTkButton(self.root)

	def test_cal(self):
		print(self.start_cal.get_date(), self.end_cal.get_date())
