from data_handler import DataHandler
from ui import UI


if __name__ == "__main__":
    try:
        ro_data = DataHandler()
        interface = UI()

        interface.drop_down(list(filter(None, ro_data.ro_dataframe['RO Name'].tolist())), 'RO Name')
        interface.drop_down(list(filter(None, ro_data.ro_dataframe['Category'].tolist())), 'Category')
        interface.drop_down(list(filter(None, ro_data.ro_dataframe['Mentor'].tolist())), 'Mentor')
        interface.y += 30
        interface.text_box("Start Time")
        interface.text_box("End Time")
        interface.text_box("Remark")
        interface.y += 30
        interface.check_box(list(filter(None, ro_data.ro_dataframe['Functions'].tolist())))
        interface.y += 30
        interface.drop_down(list(filter(None, ro_data.ro_dataframe['Accident'].tolist())), 'Accident')
        interface.y += 30
        interface.submit_button()
        ro_data.update_online_test(interface.updated_data)

    except KeyboardInterrupt:
        pass