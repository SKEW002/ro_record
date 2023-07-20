import gspread
import pandas as pd


class DataHandler:
	def __init__(self):
		self.__sa = gspread.service_account(filename="rorecord-a80647abebdc.json")
		self.__sh = self.__sa.open("RO Record")
		self.ro_data = self.__sh.worksheet("RO Data")
		self.ro_dataframe = pd.DataFrame(self.ro_data.get_all_records())


	def dataframe_tolist(self, dataframe):
		return [dataframe.columns.tolist()] + dataframe.values.tolist()


	def update_online(self,updated_data): # updated data in dict
		history_data = self.__sh.worksheet("Test")
		history_dataframe = pd.DataFrame(history_data.get_all_records())
		updated_dataframe = pd.DataFrame.from_dict(updated_data)

		history_dataframe = pd.concat([history_dataframe, updated_dataframe])
		history_data.update("A1", self.dataframe_tolist(history_dataframe))

		compiled_data = self.__sh.worksheet("Compiled Data")
		compiled_dataframe = pd.DataFrame(compiled_data.get_all_records())

		if compiled_dataframe.empty:
			updated_dataframe = updated_dataframe.filter(items=["RO Name","Duration","Move Slowly","Path Selection", "Re-Localization","Traffic Light Override", "Move by Distance", "Set Destination","Accident","Encountered Bug"])
			compiled_dataframe = pd.concat([compiled_dataframe, updated_dataframe])

		else:
			if updated_data["RO Name"] in compiled_dataframe["RO Name"].unique():
				index = compiled_dataframe.loc[compiled_dataframe["RO Name"] == updated_data["RO Name"]].index[0]
				compiled_dataframe.at[index, "Duration"] += updated_data["Duration"]
				compiled_dataframe.at[index, "Move Slowly"] += updated_data["Move Slowly"]
				compiled_dataframe.at[index, "Path Selection"] += updated_data["Path Selection"]
				compiled_dataframe.at[index, "Re-Localization"] += updated_data["Re-Localization"]
				compiled_dataframe.at[index, "Traffic Light Override"] += updated_data["Traffic Light Override"]
				compiled_dataframe.at[index, "Move by Distance"] += updated_data["Move by Distance"]
				compiled_dataframe.at[index, "Set Destination"] += updated_data["Set Destination"]
				compiled_dataframe.at[index, "Accident"] += updated_data["Accident"]

			else:
				updated_dataframe = updated_dataframe.filter(items=["RO Name","Duration","Move Slowly","Path Selection", "Re-Localization","Traffic Light Override", "Move by Distance", "Set Destination"])
				compiled_dataframe = pd.concat([compiled_dataframe, updated_dataframe])

		compiled_data.update("A1", self.dataframe_tolist(compiled_dataframe))


	def test_print(self):
		print(self.dataframe['RO Name'].tolist())


	def create_worksheet(self, title):
		worksheet = self.__sh.add_worksheet(title=title, rows=100, cols=20)