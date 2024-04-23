import pandas as pd

excel_file = ''
working_sheet = ''

data = pd.read_excel(excel_file, working_sheet)

rsrp = data[' ']
rssi = data[' ']        # both should be in dBm(exccel contained 'mwatt' value)

rsrq = rsrp/rssi

data['rsrq'] = rsrq

data.in_excel(excel_file, working_sheet, index=False)