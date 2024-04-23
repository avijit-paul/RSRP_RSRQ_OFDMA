import pandas as pd
import matplotlib.pyplot as plt


excel_doc = ' '

sheet = excel_doc[' ']

df = pd.read_excel(excel_doc,sheet)

x_axis = data["AF"]
y_axis_1 = data["Traffic"]
y_axis_2 = data["AFC"]

plt.plot(x_axis,y_axis_1, label="Traffic")
plt.plot(x_axis,y_axis_2, label="AFC")
plt.xlabel("AFC")
plt.ylabel("Traffic")

plt.legend()
plt.show()