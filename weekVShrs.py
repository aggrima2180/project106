import plotly.express as px
import csv

with open("week.csv") as csv_file:
    df=csv.DictReader(csv_file)
    fig=px.scatter(df,x="week",y="Coffee in ml",color="sleep in hours")
    fig.show()