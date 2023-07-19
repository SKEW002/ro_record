import gspread
import pandas as pd

class DataHandler:
	def __init__(self):
		sa = gspread.service_account(filename="rorecord-a80647abebdc.json")
		sh = sa.open("RORecord")
		self.wks = sh.worksheet("RO Data")
		self.dataframe = pd.DataFrame(self.wks.get_all_records())

	def update_online(self):
		# self.wks.update('A3', 'Anthony')
		# self.wks.update('D2:E3', [['Engineering', 'Tennis'], ['Business', 'Pottery']])
		# self.wks.update('F2', '=UPPER(E2)', raw=False)
		self.wks.update([self.dataframe.columns.values.tolist()] + self.dataframe.values.tolist())

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

		# wks.update('A3', 'Anthony')
		# wks.update('D2:E3', [['Engineering', 'Tennis'], ['Business', 'Pottery']])
		# wks.update('F2', '=UPPER(E2)', raw=False)
