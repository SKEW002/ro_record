import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import dash_table as dt
from datetime import date


history_data = pd.read_csv('RO Record - 0723_History.csv')
history_data['Date'] = pd.to_datetime(history_data['Date'],dayfirst=True)
history_data['Year'] = history_data['Date'].dt.year
history_data['Month'] = history_data['Date'].dt.month_name()
history_data['Day'] = history_data['Date'].dt.day

app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])

app.layout = html.Div((
    html.Div([
        html.Div([
            html.Div([
                html.H3('RO Record', style = {'margin-bottom': '0px', 'color': 'black'}),
            ])
        ], className = "one third column", id = "title1"),



        html.Div([
            html.P('Start -> End date', className = 'fix_label', style = {'color': 'black'}),
            dcc.DatePickerRange(id='selected_date',
                                min_date_allowed=date(2023, 7, 5),
                                max_date_allowed=date(2024, 1, 1),
                                display_format='MMM Do, YY',
                                start_date_placeholder_text='MMM Do, YY',
                                start_date=date(2023, 7, 1),
                                end_date=date(2023, 8, 25)
                               ),

        ], className = "one-half column", id = "title2"),

        

        html.Div([
            html.P('RO Name', className = 'fix_label', style = {'color': 'black'}),
            dcc.Dropdown(id = 'selected_name', 
                         options = [{'label': i, 'value': i} for i in history_data['RO Name'].unique()],
                        )
        ], className = "one-third column", id = 'title3'),
        

        
        html.Div([
            html.P('Version', className = 'fix_label', style = {'color': 'black'}),
            dcc.RadioItems(id = 'selected_version',
                           labelStyle = {"display": "inline-block"},
                           value = 'Consumer',
                           options = [{'label': i, 'value': i} for i in history_data['Version'].unique()],
                           style = {'text-align': 'center', 'color': 'black'}, className = 'dcc_compon'),

        ], className = "one-third column", id = 'title4'),
    

    ], id = "header", className = "row flex-display", style = {"margin-bottom": "25px"}),


    html.Div((
        html.Div([
            dt.DataTable(id = 'my_datatable',
                         columns = [{'name': i, 'id': i} for i in
                                    history_data.loc[:, ['RO Name','Category', 'Mentor', 'Date',
                                                  'Start Time', 'End Time', 'Move Slowly',
                                                  'Path Selection', 'Re-Localization', 'Traffic Light Override',
                                                  'Move by Distance', 'Set Destination', 'Accident',
                                                  'Disciplinary Issue or Safety Breach','Remark']]],
                         sort_action = "native",
                         sort_mode = "multi",
                         virtualization = True,
                         style_cell = {'textAlign': 'left',
                                       'min-width': '100px',
                                       'backgroundColor': '#1f2c56',
                                       'color': '#FEFEFE',
                                       'border-bottom': '0.01rem solid #19AAE1',
                                       },
                         style_as_list_view = True,
                         style_header = {
                             'backgroundColor': '#1f2c56',
                             'fontWeight': 'bold',
                             'font': 'Lato, sans-serif',
                             'color': 'orange',
                             'border': '#1f2c56',
                         },
                         style_data = {'textOverflow': 'hidden', 'color': 'white'},
                         fixed_rows = {'headers': True},
                         )

        ], className = 'create_container2 three columns'),



    ), className = "row flex-display"),

), id= "mainContainer", style={"display": "flex", "flex-direction": "column"})


@app.callback(
    Output('my_datatable', 'data'),
    [Input('selected_date', 'start_date')],
    [Input('selected_date', 'end_date')],
    [Input('selected_version', 'value')],
    [Input('selected_name', 'value')])
def display_table(start_date, end_date, selected_version,selected_name):
    if start_date != None:
        start_date = pd.to_datetime(start_date)
#         history_data["Date"] = pd.to_datetime(history_data["Date"]).dt.date
        end_date = pd.to_datetime(end_date)

        data_table = history_data[(history_data['Version'] == selected_version) & 
                                  (history_data['RO Name'] == selected_name)&
                                 (history_data['Date'] >= start_date) & 
                                  (history_data['Date'] <= end_date)]
        return data_table.to_dict('records')




if __name__ == '__main__':
    app.run_server(debug=True)
