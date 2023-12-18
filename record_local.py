from data_handler import DataHandler
from ctk_ui import UI
import pandas as pd
import requests
import threading

def update_local_data(csv_path):
    ro_data = DataHandler()
    ro_data.ro_dataframe.to_csv(csv_path, index=False)

if __name__ == "__main__":
    csv_path = "secret_file/cache_data.csv"
    try:
        if(requests.get('https://google.com/')):
            ro_dataframe = pd.read_csv(csv_path)
            threading.Thread(target=update_local_data, args=(csv_path,)).start()
            interface = UI("RO Competency and Proficiency Tracking System", 800, 950)
            interface.drop_down(ro_dataframe["RO Name"].dropna(), "RO Name")
            interface.y += 30
            interface.drop_down(ro_dataframe["Category"].dropna(), "Category")
            interface.y += 30
            interface.drop_down(ro_dataframe["Mentor"].dropna(), "Mentor")
            interface.y += 30
            interface.drop_down(ro_dataframe["Version"].dropna(), "Version")
            interface.y += 70
            interface.drop_down([],"Start Time")
            interface.y += 30
            interface.drop_down([],"End Time")
            interface.y += 60
            interface.check_box(ro_dataframe["Functions"].dropna())
            interface.y += 30
            interface.drop_down(ro_dataframe["Accident"].dropna(), "Accident")
            interface.y += 50
            interface.drop_down(ro_dataframe["Disciplinary Issue or Safety Breach"].dropna(), "Disciplinary Issue or Safety Breach", x=150)
            interface.y += 70
            interface.text_box_vertical("Remark")
            interface.y += 60
            interface.submit_button()
            ro_data = DataHandler()
            ro_data.update_online_month(updated_data=interface.updated_data)
        else:
            print("No internet connection")

    except KeyboardInterrupt:
        pass
