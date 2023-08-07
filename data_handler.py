import gspread
import pandas as pd
import datetime
import matplotlib.pyplot as plt


class DataHandler:
	def __init__(self):
		self.__sa = gspread.service_account(filename="rorecord-a80647abebdc.json")
		self.__sh = self.__sa.open("RO Record")
		self.__ro_data = self.__sh.worksheet("RO Data")
		self.ro_dataframe = pd.DataFrame(self.__ro_data.get_all_records())


	def dataframe_tolist(self, dataframe):
		return [dataframe.columns.tolist()] + dataframe.values.tolist()


	def update_online_month(self,function, updated_data): # updated data in dict
		if function == "ro_record":
			title = datetime.datetime.now().strftime("%m%y"+"_History")
			try:
				history_data = self.__sh.worksheet(title)
			except gspread.exceptions.WorksheetNotFound:
				self.create_worksheet(title)
				history_data = self.__sh.worksheet(title)

			# title = "Test History"
			# history_data = self.__sh.worksheet(title)
			history_dataframe = pd.DataFrame(history_data.get_all_records())
			updated_dataframe = pd.DataFrame.from_dict(updated_data)

			history_dataframe = pd.concat([history_dataframe, updated_dataframe])
			history_data.update("A1", self.dataframe_tolist(history_dataframe))

			compiled_data = self.__sh.worksheet("Test Compiled Data")
			compiled_dataframe = pd.DataFrame(compiled_data.get_all_records())
			compiled_dataframe_columns = list(compiled_dataframe.columns)
			if compiled_dataframe.empty:
				compiled_dataframe_columns = compiled_data.row_values(1)
				compiled_dataframe = updated_dataframe.filter(items=compiled_dataframe_columns)
				#compiled_dataframe = pd.concat([compiled_dataframe, updated_dataframe])

			else:
				if updated_data["RO Name"] in compiled_dataframe["RO Name"].unique():
					index = compiled_dataframe.loc[compiled_dataframe["RO Name"] == updated_data["RO Name"]].index[0]
					for column_name in compiled_dataframe_columns:
						print(updated_data[column_name])
						if column_name == "RO Name":
							continue
						
						elif column_name == "Date":
							compiled_dataframe.at[index, column_name] = updated_data[column_name][0]

						else:
							compiled_dataframe.at[index, column_name] += updated_data[column_name]

				else:
					updated_dataframe = updated_dataframe.filter(items=compiled_dataframe_columns)
					compiled_dataframe = pd.concat([compiled_dataframe, updated_dataframe])

			compiled_data.update("A1", self.dataframe_tolist(compiled_dataframe))

		elif function == "bug_ticket":
			try:
				bug_data = self.__sh.worksheet(title)
			except gspread.exceptions.WorksheetNotFound:
				self.create_worksheet(title)
				bug_data = self.__sh.worksheet(title)

			history_data.update("A1", self.dataframe_tolist(history_dataframe))

	def update_online_version(self,function, updated_data):
		if function == "ro_record":
			title = updated_data["Version"]+"_History"
			try:
				history_data = self.__sh.worksheet(title)
			except gspread.exceptions.WorksheetNotFound:
				self.create_worksheet(title)
				history_data = self.__sh.worksheet(title)

			# title = "Test History"
			# history_data = self.__sh.worksheet(title)
			history_dataframe = pd.DataFrame(history_data.get_all_records())
			updated_dataframe = pd.DataFrame.from_dict(updated_data)

			history_dataframe = pd.concat([history_dataframe, updated_dataframe])
			history_data.update("A1", self.dataframe_tolist(history_dataframe))

			title = updated_data["Version"]+"_Compiled"
			try:
				compiled_data = self.__sh.worksheet(title)
			except gspread.exceptions.WorksheetNotFound:
				self.create_worksheet(title)
				compiled_data = self.__sh.worksheet(title)

			compiled_dataframe = pd.DataFrame(compiled_data.get_all_records())
			compiled_dataframe_columns = list(compiled_dataframe.columns)
			if compiled_dataframe.empty:
				compiled_dataframe_columns = compiled_data.row_values(1)
				compiled_dataframe = updated_dataframe.filter(items=compiled_dataframe_columns)
				#compiled_dataframe = pd.concat([compiled_dataframe, updated_dataframe])

			else:
				if updated_data["RO Name"] in compiled_dataframe["RO Name"].unique():
					index = compiled_dataframe.loc[compiled_dataframe["RO Name"] == updated_data["RO Name"]].index[0]
					for column_name in compiled_dataframe_columns:
						print(updated_data[column_name])
						if column_name == "RO Name":
							continue
						
						elif column_name == "Date":
							compiled_dataframe.at[index, column_name] = updated_data[column_name][0]

						else:
							compiled_dataframe.at[index, column_name] += updated_data[column_name]

				else:
					updated_dataframe = updated_dataframe.filter(items=compiled_dataframe_columns)
					compiled_dataframe = pd.concat([compiled_dataframe, updated_dataframe])

			compiled_data.update("A1", self.dataframe_tolist(compiled_dataframe))

		elif function == "bug_ticket":
			try:
				bug_data = self.__sh.worksheet(title)
			except gspread.exceptions.WorksheetNotFound:
				self.create_worksheet(title)
				bug_data = self.__sh.worksheet(title)

			history_data.update("A1", self.dataframe_tolist(history_dataframe))



	def show_data(self, ro_data):
		compiled_data = self.__sh.worksheet("0823_History")
		compiled_dataframe = pd.DataFrame(compiled_data.get_all_records())
		index = compiled_dataframe.loc[compiled_dataframe["RO Name"] == ro_data["RO Name"]].index[0]
		print(compiled_dataframe.loc[compiled_dataframe["RO Name"] == ro_data["RO Name"]])

		table_data = compiled_dataframe.loc[compiled_dataframe["RO Name"] == ro_data["RO Name"]].drop(columns="RO Name")

		fig = plt.figure()
		ax = fig.subplots()

		ax.text(0, 0.05, ro_data["RO Name"], style='italic', bbox={'facecolor': 'green', 'alpha': 0.5, 'pad': 10})

		ax.axis('off')
		ax.axis('tight')
		table = ax.table(cellText=table_data.values, colLabels=table_data.columns, loc='center')
		table.auto_set_font_size(False)
		table.set_fontsize(8)
		plt.show()

		print(compiled_dataframe.at[index, "Duration"])


	def create_worksheet(self, title): # todo: start writing into new worksheet every start of the month
		worksheet = self.__sh.add_worksheet(title=title, rows=100, cols=20)
