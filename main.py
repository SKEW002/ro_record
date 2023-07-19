from data_handler import DataHandler
from ui import UI


if __name__ == "__main__":
    try:
        ro_data = DataHandler()
        interface = UI()

        interface.drop_down(ro_data.dataframe['RO Name'].tolist(), 'RO Name')
        interface.drop_down(ro_data.dataframe['Category'].tolist(), 'Category')
        interface.drop_down(ro_data.dataframe['Mentor'].tolist(), 'Mentor')
        interface.y += 30
        interface.text_box("Start Time")
        interface.text_box("End Time")
        interface.text_box("Remark")
        interface.y += 30
        interface.check_box(ro_data.dataframe['Functions'].tolist())
        interface.y += 30
        interface.drop_down(ro_data.dataframe['Accident'].tolist(), 'Accident')
        interface.y += 30
        interface.submit_button()
        interface.root.mainloop()

    except KeyboardInterrupt:
        interface.update_data()