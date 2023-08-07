from data_handler import DataHandler
from ctk_ui import UI

# RO Competency and Proficiency Tracking System
if __name__ == "__main__":
    try:
        ro_data = DataHandler()
        interface = UI("RO Competency and Proficiency Tracking System", 800, 850)
        interface.drop_down(list(filter(None, ro_data.ro_dataframe['RO Name'].tolist())), 'RO Name')
        interface.y += 30
        interface.drop_down(list(filter(None, ro_data.ro_dataframe['Category'].tolist())), 'Category')
        interface.y += 30
        interface.drop_down(list(filter(None, ro_data.ro_dataframe['Mentor'].tolist())), 'Mentor')
        interface.y += 70
        interface.drop_down([],"Start Time")
        interface.y += 30
        interface.drop_down([],"End Time")
        interface.y += 60
        interface.check_box(list(filter(None, ro_data.ro_dataframe['Functions'].tolist())))
        interface.y += 60
        interface.drop_down(list(filter(None, ro_data.ro_dataframe['Accident'].tolist())), 'Accident')
        interface.y += 60
        interface.text_box("Remark")
        interface.y += 100
        interface.submit_button()
        ro_data.update_online(interface.updated_data)

    except KeyboardInterrupt:
        pass