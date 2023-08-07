from data_handler import DataHandler
from ctk_ui import UI

# RO Competency and Proficiency Tracking System
if __name__ == "__main__":
    try:
        ro_data = DataHandler()
        interface = UI("Data Extract", 800, 850)
        interface.drop_down(list(filter(None, ro_data.ro_dataframe['RO Name'].tolist())), 'RO Name')
        interface.y += 30
        interface.drop_down(list(filter(None, ro_data.ro_dataframe['Version'].tolist())), 'Version')
        interface.y += 30
        interface.calendar()
        ro_data.show_data(interface.raw_data)

    except KeyboardInterrupt:
        pass