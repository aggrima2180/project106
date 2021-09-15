import plotly.express as px
import csv

with open("roll number.csv") as csv_file:
    df=csv.DictReader(csv_file)
    fig=px.scatter(df,x="Roll No",y="Marks In Percentage",color="Days Present")
    fig.show()