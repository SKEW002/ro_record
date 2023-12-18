# RO Competency and Proficiency Tracking System

## Introduction: 
Develop a RO Competency and Proficiency Tracking System that enables the efficient monitoring, evaluation, and documentation of remote operators' skills and competencies. The system should provide real-time insights into operators' performance, facilitate skill development, and enhance overall operational efficiency.


## Requirements
1. Applicable to Win & Linux operation system
2. User-friendly
3. Can use any programming language
4. Having User Interface(s) which allows user to key in all info
5. Having User Interface(s) which allows user to query
6. All info should sync to the cloud database in real-time

## UI Elements:
1. RO Name: Drop-down list, Only allow to select one name. Whenever there's a new RO, Admin should register the name to the system first, and sync to this drop down list in real-time
2. Category:  Drop-down list, Only allow to select one name per time
   different categories: 1. PSA Trainee, 2. Venti Trainee, 3. PSA OJT, 4. Venti OJT, 5. PSA RO, 6. Venti RO
3. Mentor: Drop-down list, Only allow to select one name
   Data come from the same RO list, and add one more "NA", means no mentor for that session
4. Date: Automatically filled in, indicating the date of login, (e.g. 11/Jul/2023)
5. Start Time: datetime type, the format should be fixed  (e.g. 10/Jul/2023, 23:09)
6. End Time: datetime type, the format should be fixed (e.g. 11/Jul/2023, 07:09)
7. Duration: Automatically filled in, Duration = End Time - Start Time
8. Accident: Drop-down list, Only allow to select one (1. Yes, 2. No)
9. Remark: Big text box, allow user to key in any comment and observations


Start UI by running `python3 record_local.py`

![image](https://github.com/SKEW002/ro_record/assets/57441569/62ac89ee-c8aa-4be3-88ea-b772369c0ad7)

Clicking submit button will upload the data accordingly to Google Sheet
![image](https://github.com/SKEW002/ro_record/assets/57441569/3d9ec6f1-0ac6-47b2-b567-834109f75461)
