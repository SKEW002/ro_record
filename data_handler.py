import gspread
import pandas as pd

class DataHandler:
	def __init__(self):
		self.__sa = gspread.service_account(filename="rorecord-a80647abebdc.json")
		self.__sh = self.__sa.open("RORecord")
		self.ro_data = self.__sh.worksheet("RO Data")
		self.ro_dataframe = pd.DataFrame(self.ro_data.get_all_records())

	def update_online(self, updated_data):
		updated_data_list = []
		history = self.__sh.worksheet("History")
		for _, value in updated_data.items():
			updated_data_list.append(value)

		#update_ro_dataframe = pd.DataFrame.from_dict(updated_data)

		#history.update( [update_ro_dataframe.columns.values.tolist()] + update_ro_dataframe.values.tolist())
		history.append_row(updated_data_list)

	def update_online_test(self,updated_data): # updated data in dict
		updated_data_list = []
		history = self.__sh.worksheet("Test")
		for _, value in updated_data.items():
			updated_data_list.append(value)

		#update_ro_dataframe = pd.DataFrame.from_dict(updated_data)

		#history.update( [update_ro_dataframe.columns.values.tolist()] + update_ro_dataframe.values.tolist())
		history.append_row(updated_data_list)

	def test_print(self):
		# print('Rows: ', wks.row_count)
		# print('Cols: ', wks.col_count)
		# print('Rows: ', wks.row_count)
		# print('Cols: ', wks.col_count)

		# print(wks.acell('A9').value)
		# print(wks.cell(3, 4).value)
		# print(wks.get('A7:E9'))

		# print(wks.get_all_records())
		
		print(self.dataframe['RO Name'].tolist())

		# print(wks.get_all_values())