import pandas as pd
import numpy as np

excel_file = ''
df = pd.read_excel(excel_file)

watt_values = df['']


def convert_to_dBm(watts):
    return 10*np.log10(watts * 1000)

dBm_values = convert_to_dBm(watt_values)

df['dBm'] = dBm_values

with pd.ExcelWriter(excel_file, engine = 'openpyxl', mode = 'a') as writer:
    df.to_excel(writer, excel_sheet = '')

print(excel_file)

